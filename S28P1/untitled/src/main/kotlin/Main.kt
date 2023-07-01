import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

sealed class Message
data class PerformOperation(val value: Int) : Message()
data class Result(val result: Int) : Message()

abstract class Actor(val channel: Channel<Message>, private val supervisor: CompletableJob) {
    abstract fun operation(value: Int): Int

    fun launch() = GlobalScope.launch(supervisor) {
        for (message in channel) {
            when (message) {
                is PerformOperation -> {
                    val result = operation(message.value)
                    channel.send(Result(result))
                }
                is Result -> {
                    // Nimic de făcut aici
                }
            }
        }
    }
}

class AdderActor(channel: Channel<Message>, supervisor: CompletableJob) : Actor(channel, supervisor) {
    override fun operation(value: Int) = value + 10
}

class SubtractorActor(channel: Channel<Message>, supervisor: CompletableJob) : Actor(channel, supervisor) {
    override fun operation(value: Int) = value - 10
}

class MultiplierActor(channel: Channel<Message>, supervisor: CompletableJob) : Actor(channel, supervisor) {
    override fun operation(value: Int) = value * 10
}

class DividerActor(channel: Channel<Message>, supervisor: CompletableJob) : Actor(channel, supervisor) {
    override fun operation(value: Int) = value / 10
}

fun main() = runBlocking {
    val supervisor = SupervisorJob()
    val hashMap: HashMap<String, Pair<Actor, Int>> = hashMapOf(
        "adder" to Pair(AdderActor(Channel<Message>(), supervisor), 5),
        "subtractor" to Pair(SubtractorActor(Channel<Message>(), supervisor), 15),
        "multiplier" to Pair(MultiplierActor(Channel<Message>(), supervisor), 2),
        "divider" to Pair(DividerActor(Channel<Message>(), supervisor), 100)
    )

    hashMap.values.forEach { (actor, value) ->
        actor.launch()
        actor.channel.send(PerformOperation(value))
    }

    delay(1000L) // Dați un pic de timp pentru ca toate operațiunile să fie efectuate

    // Acum citiți rezultatele
    hashMap.values.forEach { (actor, _) ->
        GlobalScope.launch {
            for (message in actor.channel) {
                when (message) {
                    is Result -> println("Result: ${message.result}")
                    is PerformOperation -> {
                        // Nimic de făcut aici
                    }
                }
            }
        }
    }
}
