package BoomBox

import kotlinx.coroutines.channels.Channel

class FastForward(ch:Channel<Boolean>):Component(ch){
    override fun do_task() {
        println("FastForwarding...")
    }
}