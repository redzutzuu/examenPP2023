import kotlinx.coroutines.async
import kotlinx.coroutines.runBlocking
import java.io.File

fun <T,R>List<T>.ap(fab:List<(T)->R>):List<R> = fab.flatMap { this.map(it) }


fun main()= runBlocking {
    val numbers= File("text.txt").readText().split(' ').map{ it.toInt() }
    val functii=listOf<(Int)->Int>({i->i/3},{i->i*5})
    val task=async{ numbers.ap(functii) }
    val newNumbers=task.await()
    println(newNumbers)
}

// Asta se face cu Maven si adaug dependenta in fisierul pom.xml
//         <dependency>
//            <groupId>org.jetbrains.kotlinx</groupId>
//            <artifactId>kotlinx-coroutines-android</artifactId>
//            <version>1.5.2</version>
//        </dependency>