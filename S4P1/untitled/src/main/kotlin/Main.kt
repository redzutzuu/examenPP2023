fun main() {
    val setA = setOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    val setB = setOf(11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

    val cartesianProduct = setA.flatMap { a ->
        setB.map { b -> Pair(a, b) }
    }

    val result = cartesianProduct.flatMap { (a, b) ->
        setB.union(setA).flatMap { c ->
            setB.map { d -> Quadruple(a, b, c, d) }
        }
    }.associate { (a, b, c, d) ->
        "$a-$b-$c-$d" to (a + b + c + d)
    }

    println(result)
}

data class Quadruple(val a: Int, val b: Int, val c: Int, val d: Int)
