package BoomBox

import kotlinx.coroutines.channels.Channel

class Radio(ch:Channel<Boolean>):Component(ch){
    override fun do_task() {
        println("Switching to radio...")
    }
}