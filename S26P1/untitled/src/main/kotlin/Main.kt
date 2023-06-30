fun main() {
    val hashMap = hashMapOf(
        1 to 5,
        2 to 10,
        3 to 15,
        4 to 20,
        5 to 25
    )

    val rezultat = hashMap.mapValues { (_, value) ->
        val rezultatFunctie = 3 * value - 1
        rezultatFunctie.toString()
    }

    println("Rezultatul aplicării functorului peste HashMap:")
    rezultat.forEach { (key, value) ->
        println("$key -> $value")
    }
}
