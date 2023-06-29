package BoomBox

import kotlinx.coroutines.channels.Channel

class BatteryStatus(ch:Channel<Boolean>):Component(ch){
    override fun do_task() {
        println("Battery status is ${0.until(101).random()}%.")
    }
}