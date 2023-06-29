import kotlinx.coroutines.*
import kotlin.random.Random

// Mesajul primit
data class AlertMessage(val message: String, val alertLevel: Int)

// Interfața pentru tratamentul mesajelor
interface MessageHandler {
    fun setNext(handler: MessageHandler)
    fun handle(message: AlertMessage)
}

// Handler pentru comunicări
class CommunicationsHandler : MessageHandler {
    private var nextHandler: MessageHandler? = null

    override fun setNext(handler: MessageHandler) {
        nextHandler = handler
    }

    override fun handle(message: AlertMessage) {
        if (message.alertLevel == 5) {
            println("Communications: ${message.message}")
        } else {
            nextHandler?.handle(message)
        }
    }
}

// Handler pentru poliție
class PoliceHandler : MessageHandler {
    private var nextHandler: MessageHandler? = null

    override fun setNext(handler: MessageHandler) {
        nextHandler = handler
    }

    override fun handle(message: AlertMessage) {
        if (message.alertLevel == 4) {
            println("Police: ${message.message}")
        } else {
            nextHandler?.handle(message)
        }
    }
}

// Handler pentru SRI
class SRIHandler : MessageHandler {
    private var nextHandler: MessageHandler? = null

    override fun setNext(handler: MessageHandler) {
        nextHandler = handler
    }

    override fun handle(message: AlertMessage) {
        if (message.alertLevel == 3) {
            println("SRI: ${message.message}")
        } else {
            nextHandler?.handle(message)
        }
    }
}

// Handler pentru SIE
class SIEHandler : MessageHandler {
    private var nextHandler: MessageHandler? = null

    override fun setNext(handler: MessageHandler) {
        nextHandler = handler
    }

    override fun handle(message: AlertMessage) {
        if (message.alertLevel == 2) {
            println("SIE: ${message.message}")
        } else {
            nextHandler?.handle(message)
        }
    }
}

// Handler pentru CSAT
class CSATHandler : MessageHandler {
    private var nextHandler: MessageHandler? = null

    override fun setNext(handler: MessageHandler) {
        nextHandler = handler
    }

    override fun handle(message: AlertMessage) {
        if (message.alertLevel == 1) {
            println("CSAT: ${message.message}")
        } else {
            nextHandler?.handle(message)
        }
    }
}

// Handler pentru NATO
class NATOHandler : MessageHandler {
    private var nextHandler: MessageHandler? = null

    override fun setNext(handler: MessageHandler) {
        nextHandler = handler
    }

    override fun handle(message: AlertMessage) {
        if (message.alertLevel == 0) {
            println("NATO: ${message.message}")
        } else {
            nextHandler?.handle(message)
        }
    }
}

// Interfața pentru comandă
interface Command {
    fun execute()
}

// Comanda pentru afișarea mesajului
class PrintMessageCommand(private val message: String) : Command {
    override fun execute() {
        println(message)
    }
}

// Funcție pentru generarea și trimiterea mesajelor
suspend fun generateAndSendAlerts() {
    val levels = listOf(0, 1, 2, 3, 4, 5)
    val messages = listOf(
        "Message 1",
        "Message 2",
        "Message 3",
        "Message 4",
        "Message 5"
    )

    repeat(10) {
        val level = levels.random()
        val message = messages.random()

        val alertMessage = AlertMessage(message, level)
        sendMessage(alertMessage)

        delay(1000)
    }
}

// Funcție pentru trimiterea mesajului către handler-ul potrivit
suspend fun sendMessage(message: AlertMessage) {
    val communicationsHandler = CommunicationsHandler()
    val policeHandler = PoliceHandler()
    val sriHandler = SRIHandler()
    val sieHandler = SIEHandler()
    val csatHandler = CSATHandler()
    val natoHandler = NATOHandler()

    communicationsHandler.setNext(policeHandler)
    policeHandler.setNext(sriHandler)
    sriHandler.setNext(sieHandler)
    sieHandler.setNext(csatHandler)
    csatHandler.setNext(natoHandler)

    communicationsHandler.handle(message)
}

// Funcția principală
fun main() = runBlocking<Unit> {
    // Pornirea corutinelor pentru generarea și tratarea mesajelor
    val alertsJob = launch { generateAndSendAlerts() }

    // Comenzile pentru afișarea mesajelor
    val printCommand1 = PrintMessageCommand("Print Command 1")
    val printCommand2 = PrintMessageCommand("Print Command 2")
    val printCommand3 = PrintMessageCommand("Print Command 3")
    val printCommand4 = PrintMessageCommand("Print Command 4")

    // Execuția comenzilor
    printCommand1.execute()
    printCommand2.execute()
    printCommand3.execute()
    printCommand4.execute()

    // Așteptarea încheierii corutinei de generare a mesajelor
    alertsJob.join()
}
