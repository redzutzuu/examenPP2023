class Operatie(val numar: Int, val operator: String)

object FactoryOperatii {
    fun genereazaOperatii(numarElemente: Int): List<Operatie> {
        val operatii = mutableListOf<Operatie>()

        // Generăm operațiile de tip sumă cu 5
        for (i in 1..numarElemente) {
            val rezultat = i + 5
            operatii.add(Operatie(i, "+ 5 = $rezultat"))
        }

        // Generăm operațiile de tip înmulțire cu 7
        for (i in 1..numarElemente) {
            val rezultat = i * 7
            operatii.add(Operatie(i, "* 7 = $rezultat"))
        }

        return operatii
    }
}

fun main() {
    val numarElemente = 10
    val operatii = FactoryOperatii.genereazaOperatii(numarElemente)

    println("Operatii generate:")
    for (operatie in operatii) {
        println("${operatie.numar} ${operatie.operator}")
    }
}
