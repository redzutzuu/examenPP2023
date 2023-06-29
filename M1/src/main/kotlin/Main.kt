import kotlin.math.sqrt

fun <T: Number> T.isPrime(): Boolean{
    val num = this.toDouble()
    if (num < 2){
        return false;
    }
    val sqrtNum = sqrt(num).toInt()
    for (i in 2..sqrtNum){
        if(num % i == 0.0){
            return false
        }
    }
    return true
}

fun main(){
    val number1 = 7
    println(number1.isPrime())

    val number2 = 20L
    println(number2.isPrime())

    val number3 = 13.0f
    println(number3.isPrime())
}