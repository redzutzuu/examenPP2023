import kotlin.random.Random

fun main() {
    val A = generateRandomSet(15)
    val B = generateRandomSet(15)

    val result = A.flatMap { a ->
        B.map { b -> Pair(a, b) }
    }

    result.forEach { pair ->
        println(pair)
    }
}

fun generateRandomSet(size: Int): Set<Int> {
    return (1..size).map { Random.nextInt(1, 100) }.toSet()
}
