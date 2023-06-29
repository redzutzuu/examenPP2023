package BoomBox

import kotlinx.coroutines.channels.Channel

abstract class Component(private val ch: Channel<Boolean>) {
    suspend fun run()
    {
        //println("APEL")
        while(ch.receive())
            do_task()
    }

    abstract fun do_task()
}