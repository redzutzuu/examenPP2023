package chain

import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

class ManagerHandler(var right: Handler? = null, var left: Handler? = null, var vertical: Handler? = null): Handler {
    override suspend fun handleRequest(forwardDirection: String, messageToBeProcessed: String):Unit= runBlocking {
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
                    3->
                    {
                        println("Sunt Manager si prelucrez mesajul:\"$mes\"...")
                        delay(800)
                        launch {
                            if(vertical!=null)
                                vertical?.handleRequest("vertical","$prio:Mesajul \"$mes\" a fost prelucrat de catre Manager.")
                            else
                                left?.handleRequest("left","$prio:Mesajul \"$mes\" a fost prelucrat de catre Manager.")

                        }
                    }
                    else->launch{ right?.handleRequest("right",messageToBeProcessed) }
                }
            }
            "vertical"->launch{
                println("Sunt Manager si transmit mai departe rezultatul unei prelucrari: \"${mes}\"")
                if(vertical!=null)
                    vertical?.handleRequest("vertical",messageToBeProcessed)
                else
                    left?.handleRequest("left",messageToBeProcessed)
            }
            "left"->launch{
                println("Sunt Manager si transmit mai departe rezultatul unei prelucrari: \"${mes}\"")
                left?.handleRequest("left",messageToBeProcessed)
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