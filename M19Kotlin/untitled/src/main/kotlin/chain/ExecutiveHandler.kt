package chain

import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

class ExecutiveHandler(var right: Handler? = null, var left: Handler? = null, var vertical: Handler? = null): Handler {
    override suspend fun handleRequest(forwardDirection: String, messageToBeProcessed: String): Unit = runBlocking {
        val prioRegex = Regex("^[0-9](?=:)")
        val mesRegex = Regex("(?<=:).+")
        val prio = prioRegex.find(messageToBeProcessed)!!.value.toInt()
        val mes = mesRegex.find(messageToBeProcessed)!!.value
        when (forwardDirection) {
            "right" -> {
                when (prio) {
                    2 -> {
                        println("Sunt Executive si prelucrez mesajul:\"$mes\"...")
                        delay(500)
                        launch {
                            if (vertical != null)
                                vertical?.handleRequest(
                                    "vertical",
                                    "$prio:Mesajul a fost prelucrat de catre Executive."
                                )
                            else
                                left?.handleRequest("left", "$prio:Mesajul a fost prelucrat de catre Executive.")
                        }
                    }
                    else -> launch { right?.handleRequest("right", messageToBeProcessed) }
                }
            }
            "vertical" -> {
                println("Sunt Executive si transmit mai departe rezultatul unei prelucrari: \"${mes}\"")
                if (vertical != null)
                    vertical?.handleRequest("vertical", messageToBeProcessed)
                else
                    left?.handleRequest("left", messageToBeProcessed)
            }
            "left" -> {
                println("Sunt Executive si transmit mai departe rezultatul unei prelucrari: \"${mes}\"")
                launch { left?.handleRequest("left", messageToBeProcessed) }
            }
        }
    }
    override fun SetRight(right:Handler?)
    {
        this.right=right
    }
    override fun SetLeft(left:Handler?)
    {
        this.left=left
    }
    override fun SetVertical(vertical:Handler?)
    {
        this.vertical=vertical
    }
}