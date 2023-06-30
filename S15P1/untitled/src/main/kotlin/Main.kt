fun main() {
    val A = (1..100).toSet()

    val count = A.toList().combinations(4).count { 1 in it }

    println("Numărul de submulțimi cu patru elemente care conțin 1: $count")
}

fun <T> List<T>.combinations(length: Int): List<List<T>> {
    if (length == 0) return listOf(emptyList())
    if (length == size) return listOf(this)

    val result = mutableListOf<List<T>>()

    for (i in 0..size - length) {
        val element = this[i]
        val remaining = subList(i + 1, size).combinations(length - 1)
        for (comb in remaining) {
            val combination = mutableListOf(element)
            combination.addAll(comb)
            result.add(combination)
        }
    }

    return result
}
