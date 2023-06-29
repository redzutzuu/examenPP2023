import kotlinx.coroutines.*
import kotlinx.coroutines.channels.Channel
import java.io.File

suspend fun main() {
    val words = readWordsFromFile("words.txt")

    val channel1 = Channel<String>(Channel.CONFLATED)
    val channel2 = Channel<String>(Channel.CONFLATED)
    val channel3 = Channel<String>(Channel.CONFLATED)

    val job1 = GlobalScope.launch {
        for (word in channel1) {
            println("Proces1 - Cuvant primit: $word")
        }
    }

    val job2 = GlobalScope.launch {
        for (word in channel2) {
            println("Proces2 - Cuvant primit: $word")
        }
    }

    val job3 = GlobalScope.launch {
        for (word in channel3) {
            println("Proces3 - Cuvant primit: $word")
        }
    }

    val channels = listOf(channel1, channel2, channel3)

    for (index in words.indices) {
        val word = words[index]
        val currentChannel = channels[index % channels.size]
        currentChannel.send(word)
    }

    job1.cancel()
    job2.cancel()
    job3.cancel()

    delay(100) // Așteaptă un scurt timp pentru a permite afișarea rezultatelor
    println(System.getProperty("user.dir"))

}

suspend fun readWordsFromFile(filename: String): List<String> = withContext(Dispatchers.IO) {
    val file = File(filename)
    if (file.exists()) {
        file.readLines()
    } else {
        emptyList()
    }
}
