fun main() {
    val A = generateSequence(1) { it + 1 }
        .map { n -> (8 * n - 18).toDouble() / (2 * n - 9) }
        .take(100)
        .toList()

    val B = generateSequence(1) { it + 1 }
        .map { n -> (9 * n * n - 48 * n + 16).toDouble() / (3 * n - 8) }
        .take(100)
        .toList()

    val result = HashMap<Double, Double>()

    A.flatMap { a ->
        B.map { b -> Pair(a, b) }
    }.filter { (a, b) -> a >= b }
        .toSet()
        .forEach { (a, b) -> result[a] = b }

    println("Rezultat:")
    result.forEach { (a, b) ->
        println("($a, $b)")
    }
}
