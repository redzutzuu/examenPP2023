package BoomBox

import kotlinx.coroutines.channels.Channel

class Volume(ch:Channel<Boolean>):Component(ch){
    override fun do_task() {
        println("Volume is ${0.until(101).random()}.")
    }
}