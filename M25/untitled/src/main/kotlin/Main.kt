import kotlinx.coroutines.runBlocking
import java.util.concurrent.locks.ReentrantLock


fun main()= runBlocking{
    val files=listOf("file1.csv","file2.csv","file3.csv","file4.csv")
    val output_file="OUTPUT.txt"
    val adapter=Adapter(ReentrantLock(),files,output_file)
    adapter.write()
}