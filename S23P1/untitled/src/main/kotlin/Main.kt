fun main() {
    val A = setOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    val B = setOf(11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)

    val result = mutableMapOf<Pair<Int, Int>, Int>()

    val intersection = A.intersect(B)
    val union = A.union(B)

    for (a in union) {
        for (b in intersection) {
            result[a to b] = a * b
        }
    }

    println("Rezultatul este:")
    for ((pair, value) in result) {
        println("$pair -> $value")
    }
}
