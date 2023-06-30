import kotlinx.coroutines.async
import kotlinx.coroutines.runBlocking
import java.io.File

fun create_collections(files:List<String>):List<List<Int>>{
    return files.map { File(it).readText().split(',').map { str->str.toInt() } }
}

fun get_list_of_pairs(X:List<Int>, Y:List<Int>):List<Pair<Int,Int>>{
    return X.flatMap { x->Y.filter { y->x*y==(x+y*3) }.map { y->Pair(x,y) } }
}

fun main()= runBlocking{
    println(System.getProperty("user.dir"))
    val files=listOf("file1.csv", "file2.csv")
    val rez1=async { create_collections(files) }
    val X=rez1.await()[0]
    val Y=rez1.await()[1]
    println("X:${X}\nY:${Y}")
    val rez2=async { get_list_of_pairs(X,Y) }
    val list_of_pairs=rez2.await()
    println("Perechi (x,y) care satisfac x*y==x+y*3: ${list_of_pairs}")
}