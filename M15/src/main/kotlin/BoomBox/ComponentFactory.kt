package BoomBox

import kotlinx.coroutines.channels.Channel
import java.lang.IllegalArgumentException

class ComponentFactory {
    fun create(type:String, ch: Channel<Boolean>):Component{
        when(type){
            "BatteryStatus" ->return BatteryStatus(ch)
            "FastForward"   ->return FastForward(ch)
            "Play"          ->return Play(ch)
            "Radio"         ->return Radio(ch)
            "Record"        ->return Record(ch)
            "Rewind"        ->return Rewind(ch)
            "Volume"        ->return Volume(ch)
            else->throw IllegalArgumentException("Invalid component type")
        }
    }
}