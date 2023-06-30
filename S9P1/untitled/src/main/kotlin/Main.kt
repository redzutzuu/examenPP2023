import java.io.File
import java.time.LocalDateTime

interface PriceRecalculationObserver {
    fun update(user: String, operation: String, rate: Double)
}

class PriceRecalculator {
    private val observers: MutableList<PriceRecalculationObserver> = mutableListOf()
    private val rates: MutableMap<String, Double> = mutableMapOf()

    fun attach(observer: PriceRecalculationObserver) {
        observers.add(observer)
    }

    fun detach(observer: PriceRecalculationObserver) {
        observers.remove(observer)
    }

    fun addRate(user: String, password: String, rate: Double) {
        if (validateUser(user, password)) {
            rates[user] = rate
            notifyObservers(user, "added", rate)
        }
    }

    fun updateRate(user: String, password: String, rate: Double) {
        if (validateUser(user, password) && user in rates) {
            rates[user] = rate
            notifyObservers(user, "updated", rate)
        }
    }

    private fun validateUser(user: String, password: String): Boolean {
        // Simulated user and password validation
        return true
    }

    private fun notifyObservers(user: String, operation: String, rate: Double) {
        for (observer in observers) {
            observer.update(user, operation, rate)
        }
    }
}

class LoggingObserver : PriceRecalculationObserver {
    private val logFile = File("price_log.txt")

    init {
        if (!logFile.exists()) {
            logFile.createNewFile()
        }
    }

    override fun update(user: String, operation: String, rate: Double) {
        val logEntry = "$user - $operation: Rate $rate changed at ${LocalDateTime.now()}\n"
        logFile.appendText(logEntry)
    }
}

fun main() {
    val priceRecalculator = PriceRecalculator()
    val loggingObserver = LoggingObserver()
    priceRecalculator.attach(loggingObserver)

    priceRecalculator.addRate("john", "password", 0.1)
    priceRecalculator.updateRate("john", "password", 0.2)

    // Afisarea continutului fisierului de jurnal
    val logFile = File("price_log.txt")
    val logContent = logFile.readText()
    println("Jurnal:")
    println(logContent)
}
