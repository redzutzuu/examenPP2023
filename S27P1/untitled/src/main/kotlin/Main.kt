fun main() {
    val colectieA = generateColecțieA()
    val colectieB = generateColecțieB()

    val rezultat = colectieA.union(colectieB).intersect(colectieB.intersect(colectieA))

    val hashMap = mutableMapOf<String, Double>()
    rezultat.forEachIndexed { index, numar ->
        hashMap["Numar$index"] = numar
    }

    println("Rezultatul operațiilor (A reuniune B) intersecție (B intersecție A):")
    hashMap.forEach { (cheie, valoare) ->
        println("$cheie -> $valoare")
    }
}

fun generateColecțieA(): List<Double> {
    val colectie = mutableListOf<Double>()
    for (n in 1..100) {
        val x = (8 * n - 18) / (2 * n - 9).toDouble()
        colectie.add(x)
    }
    return colectie
}

fun generateColecțieB(): List<Double> {
    val colectie = mutableListOf<Double>()
    for (n in 1..100) {
        val x = (9 * n * n - 48 * n + 16) / (3 * n - 8).toDouble()
        colectie.add(x)
    }
    return colectie
}
