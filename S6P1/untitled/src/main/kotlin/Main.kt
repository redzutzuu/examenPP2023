fun main() {
    val setA = setOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    val setB = setOf(11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

    val cartesianProductAxB = setA.flatMap { a ->
        setB.map { b -> Pair(a, b) }
    }

    val cartesianProductBxB = setB.flatMap { b1 ->
        setB.map { b2 -> Pair(b1, b2) }
    }

    val result = cartesianProductAxB.union(cartesianProductBxB).associate { pair ->
        pair.toString() to pair
    }

    result.forEach { (key, value) ->
        println("$key -> $value")
    }
}
