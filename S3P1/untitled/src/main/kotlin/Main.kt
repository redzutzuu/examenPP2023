import java.io.File
import java.io.PrintWriter

// Adaptor pentru a converti diverse tipuri de date în șiruri de caractere
interface Adapter<T> {
    fun convertToString(item: T): String
}

// Adaptor pentru tipurile de date simple (Int, String, Boolean)
object SimpleTypeAdapter : Adapter<Any> {
    override fun convertToString(item: Any): String {
        return item.toString()
    }
}

// Adaptor pentru colecții de tipul List<T>
class ListTypeAdapter<T>(private val itemAdapter: Adapter<T>) : Adapter<List<T>> {
    override fun convertToString(item: List<T>): String {
        val stringBuilder = StringBuilder()
        for (element in item) {
            val convertedElement = itemAdapter.convertToString(element)
            stringBuilder.append(convertedElement).append("\n")
        }
        return stringBuilder.toString()
    }
}

// Funcție generică pentru a scrie un obiect într-un fișier
fun <T> writeObjectToFile(obj: T, fileName: String, adapter: Adapter<T>) {
    val stringRepresentation = adapter.convertToString(obj)
    val file = File(fileName)
    PrintWriter(file).use { writer ->
        writer.write(stringRepresentation)
    }
}

fun main() {
    // Exemple de utilizare

    // Scriere unui număr întreg în fișier
    val number = 42
    writeObjectToFile(number, "number.txt", SimpleTypeAdapter)

    // Scriere unui șir de caractere în fișier
    val text = "Hello, world!"
    writeObjectToFile(text, "text.txt", SimpleTypeAdapter)

    // Scriere unei liste de șiruri de caractere în fișier
    val list = listOf("apple", "banana", "orange")
    val listAdapter = ListTypeAdapter(SimpleTypeAdapter)
    writeObjectToFile(list, "list.txt", listAdapter)
}
