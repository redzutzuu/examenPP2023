package chain

import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

class CEOHandler: Handler {
    var right: Handler? = null
    var vertical: Handler? = null
    override suspend fun handleRequest(forwardDirection: String, messageToBeProcessed: String):Unit=runBlocking{
        val prioRegex=Regex("^[0-9](?=:)")
        val mesRegex=Regex("(?<=:).+")
        val prio=prioRegex.find(messageToBeProcessed)!!.value.toInt()
        val mes=mesRegex.find(messageToBeProcessed)!!.value
        when(forwardDirection)
        {
            "right"->
            {
                when(prio)
                {
                    1->
                    {
                        println("Sunt CEO si prelucrez mesajul:\"$mes\"...")
                        delay(200)
                        launch{ vertical?.handleRequest("vertical","$prio:Mesajul a fost prelucrat de catre CEO.") }
                    }
                    else->launch{
                        right?.handleRequest("right",messageToBeProcessed)
                    }
                }
            }
            "vertical", "left"->
            {
                    if (vertical != null)
                    {
                        println("Sunt CEO si transmit mai departe rezultatul unei prelucrari: \"${mes}\"")
                        launch{ vertical?.handleRequest("vertical", messageToBeProcessed) }
                    }
                    else
                        println("Sunt CEO si am primit rezultatul unei prelucrari: \"${mes}\"")
                }
        }
    }


    override fun SetRight(right:Handler?)
    {
        this.right=right
    }
    override fun SetLeft(left:Handler?){}
    override fun SetVertical(vertical:Handler?)
    {
        this.vertical=vertical
    }
}