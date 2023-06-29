package BoomBox

import kotlinx.coroutines.Job
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import java.io.BufferedReader
import java.io.InputStreamReader

class BoomBoxFacade {
    private val componentTypes=listOf("BatteryStatus", "FastForward", "Play", "Radio", "Record", "Rewind", "Volume")
    private val ch_list= mutableListOf<Channel<Boolean>>().apply { repeat(componentTypes.size) { this.add(Channel()) } }
    private val componentToChannel=componentTypes.zip(ch_list).toMap()
    public val components:List<Component>
    //private lateinit var tasks:List<Job>
    init{
        val factory=ComponentFactory()
        components=ch_list.mapIndexed { index, channel -> factory.create(componentTypes[index], channel) }
    }

    //suspend fun tasks_init()= coroutineScope {
    //    components.map { launch { it.run() } }
    //}

    suspend fun menu():Boolean{
        val br=BufferedReader(InputStreamReader(System.`in`))
        println("Optiuni:")
        componentTypes.forEach { println("\"$it\" pentru $it") }
        println("Orice altceva pentru iesire")
        print("Raspunsul dumneavoastra: ")
        val opt=br.readLine()
        println()
        if(opt !in componentToChannel.keys){
            ch_list.forEach { it.send(false) }
            println("Pa pa...")
            //tasks.forEach { it.join() }
            return false
        }
        else
        {
            componentToChannel[opt]?.send(true)
        }
        return true
    }
}