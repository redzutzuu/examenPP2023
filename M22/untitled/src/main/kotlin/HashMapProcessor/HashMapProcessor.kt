package HashMapProcessor

import java.io.File

abstract class HashMapProcessor
{
    fun print_max(file:String){
        val max = File(file).readText().split(',').map { it.toInt() }.maxOrNull()
        println("Max din $file : $max")
    }

    fun print_min(file:String){
        val min = File(file).readText().split(',').map { it.toInt() }.minOrNull()
        println("Min din $file : $min")
    }

    fun print_nr_apar(file:String){
        val numbers=File(file).readText().split(',')
        val distinct_numbers=numbers.distinct()
        val list_of_pairs=distinct_numbers.map { distinct->Pair(distinct,numbers.count { distinct==it }) }
        println("Numarul aparitiilor fiecarui numar din $file : $list_of_pairs")
    }

    fun print_elimin_dup(file:String){
        val distincts=File(file).readText().split(',').distinct()
        println("Lista numere fara duplicate din $file : $distincts")
    }

    abstract fun get_runnable_object():Runnable
}