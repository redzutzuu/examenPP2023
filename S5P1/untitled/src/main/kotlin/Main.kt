fun main() {
    val setA = setOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3)
    val setB = setOf(11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2, 3, 4)

    val cartesianProductAxB = setA.flatMap { a ->
        setB.map { b -> Pair(a, b) }
    }

    val cartesianProductBxA = setB.flatMap { b ->
        setA.map { a -> Pair(b, a) }
    }

    val result = cartesianProductAxB.filter { pair ->
        cartesianProductBxA.contains(pair)
    }.associate { pair ->
        pair.toString() to pair
    }

    println(result)
}
