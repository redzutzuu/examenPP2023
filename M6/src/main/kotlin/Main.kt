sealed class TipSimplu<out T>{
    object None:TipSimplu<Nothing>(){
        override fun toString()="Cu None"
    }
    data class Some<out T>(val value:T):TipSimplu<T>()
    companion object
}


fun <T>TipSimplu<T>.toInt():Int=when(this){
    TipSimplu.None->-1
    is TipSimplu.Some->(0..1).random()
}

fun TipSimplu<Int>.map(transform:(TipSimplu<Int>)->Int):TipSimplu<Int>{
    return TipSimplu.Some<Int>(transform(this))
}

fun main()
{
    println(TipSimplu.None.map(TipSimplu<Int>::toInt))
    println(TipSimplu.Some(3).map(TipSimplu<Int>::toInt))
    println(TipSimplu.Some(5).map(TipSimplu<Int>::toInt))
}