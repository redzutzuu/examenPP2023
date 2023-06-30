import java.util.concurrent.locks.ReentrantLock

// Clasa de bază
open class OperationProcessor {
    open fun processOperation(a: Int, b: Int) {}
}

// Subclasă pentru adunare
class AdditionProcessor(private val resultHolder: ResultHolder) : OperationProcessor() {
    private val lock = ReentrantLock()

    override fun processOperation(a: Int, b: Int) {
        lock.lock()
        try {
            val result = a + b
            resultHolder.addResult("Adunare: $a + $b = $result")
        } finally {
            lock.unlock()
        }
    }
}

// Subclasă pentru scădere
class SubtractionProcessor(private val resultHolder: ResultHolder) : OperationProcessor() {
    private val lock = ReentrantLock()

    override fun processOperation(a: Int, b: Int) {
        lock.lock()
        try {
            val result = a - b
            resultHolder.addResult("Scădere: $a - $b = $result")
        } finally {
            lock.unlock()
        }
    }
}

// Subclasă pentru înmulțire
class MultiplicationProcessor(private val resultHolder: ResultHolder) : OperationProcessor() {
    private val lock = ReentrantLock()

    override fun processOperation(a: Int, b: Int) {
        lock.lock()
        try {
            val result = a * b
            resultHolder.addResult("Înmulțire: $a * $b = $result")
        } finally {
            lock.unlock()
        }
    }
}

// Subclasă pentru împărțire
class DivisionProcessor(private val resultHolder: ResultHolder) : OperationProcessor() {
    private val lock = ReentrantLock()

    override fun processOperation(a: Int, b: Int) {
        lock.lock()
        try {
            if (b != 0) {
                val result = a / b
                resultHolder.addResult("Împărțire: $a / $b = $result")
            } else {
                resultHolder.addResult("Împărțire: Nu se poate efectua împărțirea la zero.")
            }
        } finally {
            lock.unlock()
        }
    }
}

// Clasa pentru stocarea rezultatelor
class ResultHolder {
    private val lock = ReentrantLock()
    private val results = mutableListOf<String>()

    fun addResult(result: String) {
        lock.lock()
        try {
            results.add(result)
        } finally {
            lock.unlock()
        }
    }

    fun printResults() {
        lock.lock()
        try {
            println("Rezultate:")
            for (result in results) {
                println(result)
            }
        } finally {
            lock.unlock()
        }
    }
}

fun main() {
    val resultHolder = ResultHolder()

    val additionProcessor = AdditionProcessor(resultHolder)
    val subtractionProcessor = SubtractionProcessor(resultHolder)
    val multiplicationProcessor = MultiplicationProcessor(resultHolder)
    val divisionProcessor = DivisionProcessor(resultHolder)

    val a = 10
    val b = 5

    // Procesarea operațiilor în fire separate
    Thread { additionProcessor.processOperation(a, b) }.start()
    Thread { subtractionProcessor.processOperation(a, b) }.start()
    Thread { multiplicationProcessor.processOperation(a, b) }.start()
    Thread { divisionProcessor.processOperation(a, b) }.start()

    // Așteptăm ca toate firele să se termine înainte de a afișa rezultatele
    Thread.sleep(1000)

    // Afișarea rezultatelor
    resultHolder.printResults()
}
