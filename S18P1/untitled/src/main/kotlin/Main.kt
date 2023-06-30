interface Printer {
    fun print(obj: Any?)
}

class SimplePrinter : Printer {
    override fun print(obj: Any?) {
        println(obj)
    }
}

class CollectionPrinter(private val printer: Printer) : Printer {
    override fun print(obj: Any?) {
        if (obj is Collection<*>) {
            for (item in obj) {
                printer.print(item)
            }
        } else {
            printer.print(obj)
        }
    }
}

fun main() {
    val printer: Printer = CollectionPrinter(SimplePrinter())

    // Example usage
    printer.print(10)  // Prints: 10
    printer.print("Hello")  // Prints: Hello
    printer.print(listOf(1, 2, 3, 4, 5))  // Prints: 1 2 3 4 5
    printer.print(setOf("apple", "banana", "orange"))  // Prints: apple banana orange
}
