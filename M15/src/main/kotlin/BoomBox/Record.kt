package BoomBox

import kotlinx.coroutines.channels.Channel

class Record(ch:Channel<Boolean>):Component(ch){
    override fun do_task() {
        println("Recording...")
    }
}