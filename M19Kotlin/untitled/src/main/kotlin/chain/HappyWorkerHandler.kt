package chain

import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

class HappyWorkerHandler(var right: Handler? = null, var left: Handler? = null, var vertical: Handler? = null): Handler {
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
                    4->
                    {
                        println("Sunt HappyWorker si prelucrez mesajul:\"$mes\"...")
                        delay(10_000)
                        launch{
                            if(vertical!=null)
                                vertical?.handleRequest("vertical","$prio:Mesajul \"$mes\" a fost prelucrat de catre HappyWorker.")
                            else
                                left?.handleRequest("left","$prio:Mesajul \"$mes\" a fost prelucrat de catre HappyWorker.")
                        }
                    }
                    else->launch{
                        println("Sunt HappyWorker si nu am putut procesa mesajul \"$mes\"")
                        if(vertical!=null)
                            vertical?.handleRequest("vertical","$prio:Mesajul nu a putut fi procesat")
                        else
                            left?.handleRequest("left","$prio:Mesajul nu a putut fi procesat")
                    }
                }
            }
            "vertical"->launch{
                println("Sunt HappyWorker si transmit mai departe rezultatul unei prelucrari: \"${mes}\"")
                if(vertical!=null)
                    vertical?.handleRequest("vertical",messageToBeProcessed)
                else
                    left?.handleRequest("left",messageToBeProcessed)
            }
            "left"->launch{
                println("Sunt HappyWorker si transmit mai departe rezultatul unei prelucrari: \"${mes}\"")
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