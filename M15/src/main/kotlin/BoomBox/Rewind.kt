package BoomBox

import kotlinx.coroutines.channels.Channel

class Rewind(ch:Channel<Boolean>):Component(ch){
    override fun do_task() {
        println("Rewinding...")
    }
}