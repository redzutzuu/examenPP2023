import java.io.File
import java.io.FileWriter

class ReaderAndWriter(private val file:String, private val output_file:String) {
    fun read():String{
        return File(file).readText()
    }
    fun write(output: String){
        val fw=FileWriter(output_file,true)
        fw.write(output)
        fw.close()
    }
}