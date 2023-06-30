package HashMapProcessor

import java.lang.IllegalArgumentException

class HashMapProcessorFactory {
    fun create(type:String, file:String):HashMapProcessor{
        when(type){
            "Max"->return Max(file)
            "Min"->return Min(file)
            "NrApar"->return NrApar(file)
            "EliminDup"->return EliminDup(file)
            else->throw IllegalArgumentException("Tipul $type este invalid!")
        }
    }
}