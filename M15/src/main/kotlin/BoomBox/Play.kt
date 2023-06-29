package BoomBox

import kotlinx.coroutines.channels.Channel

class Play(ch:Channel<Boolean>):Component(ch){
    override fun do_task() {
        println("Playing...")
    }
}