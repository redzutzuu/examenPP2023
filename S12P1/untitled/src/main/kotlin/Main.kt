fun main() {
    val collection = generateRandomCollection(100)
    val result = calculateSumOfSquares(collection)
    println("Suma patratelor elementelor din colectie: $result")
}

fun generateRandomCollection(size: Int): List<Int> {
    val collection = mutableListOf<Int>()
    repeat(size) {
        val randomNumber = (0..100).random() * 2 // Generare numar par aleatoriu
        collection.add(randomNumber)
    }
    return collection
}

fun calculateSumOfSquares(collection: List<Int>): Int {
    var sum = 0
    for (element in collection) {
        val square = element * element
        sum += square
    }
    return sum
}
