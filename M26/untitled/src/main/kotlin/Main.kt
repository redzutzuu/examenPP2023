import kotlinx.coroutines.async
import kotlinx.coroutines.runBlocking
import java.io.File


fun main()= runBlocking{
    val text= File("input.txt").readText()
    val task=async{
        text.split(' ')
            .asSequence()
            .filter { it.length>=4 }
            .map { listOf(it[it.length/2-1],it[it.length/2]).joinToString("") }
            .joinToString("")
    }
    val rez=task.await()
    println("Rezultat: $rez")
}