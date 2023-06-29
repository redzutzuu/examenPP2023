import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*
import kotlinx.coroutines.flow.*
import java.io.File

data class Word(val value: String, var isCorrect: Boolean = true)

fun extractWords(text: String): List<Word> {
    return text.split("\\s+".toRegex())
        .map { Word(it) }
}

fun checkSpelling(words: List<Word>, dictionary: Set<String>) {
    for (word in words) {
        if (!dictionary.contains(word.value.toLowerCase())) {
            word.isCorrect = false
        }
    }
}

class CorrectionObserver(private val channel: ConflatedBroadcastChannel<Int>) {
    suspend fun askForCorrection(index: Int): Int {
        channel.send(index)
        return channel.asFlow().first()
    }
}

class CorrectionMemento(private val words: List<Word>) {
    fun restore() {
        words.forEach { it.isCorrect = true }
    }
}

fun main() = runBlocking {
    val filePath = "input.txt"
    val text = async(Dispatchers.IO) {
        File(filePath).readText()
    }.await()

    val words = extractWords(text)
    val dictionary = setOf("corect", "forma", "cuvinte")

    val checkJob = async(Dispatchers.Default) {
        checkSpelling(words, dictionary)
    }

    val correctionChannel = ConflatedBroadcastChannel<Int>()
    val observer = CorrectionObserver(correctionChannel)

    val misspelledWords = words.asFlow()
        .filter { !it.isCorrect }
        .map { it.value }

    val misspelledWordsWithCorrection = misspelledWords.transform { word ->
        val index = correctionChannel.asFlow().firstOrNull()
        val shouldCorrect = index?.let { observer.askForCorrection(it) } ?: false
        emit(if (shouldCorrect as Boolean) "****" else word)
    }

    val transformedWords = words.asFlow()
        .map { if (it.isCorrect) it.value else "****" }

    val finalWordsFlow = merge(transformedWords, misspelledWordsWithCorrection)
        .withIndex()
        .map { (index, word) -> "${index + 1}. $word" }

    finalWordsFlow.collect { println(it) }

    val memento = CorrectionMemento(words)
}
