import java.math.BigInteger
import java.util.concurrent.ConcurrentHashMap

class FibonacciCalculator {
    private val memoizationMap = ConcurrentHashMap<Int, BigInteger>()

    fun calculate(n: Int): BigInteger {
        return memoizationMap.computeIfAbsent(n) {
            when (n) {
                0 -> BigInteger.ZERO
                1 -> BigInteger.ONE
                else -> calculate(n - 1).add(calculate(n - 2))
            }
        }
    }
}

fun main() {
    val fibonacciCalculator = FibonacciCalculator()

    val n = 10
    for (i in 0..n) {
        val fibonacciNumber = fibonacciCalculator.calculate(i)
        println("F($i) = $fibonacciNumber")
    }
}
