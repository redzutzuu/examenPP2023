class Laborator(val nume: String, val capacitate: Int) {
    val echipamente: MutableList<Echipament> = mutableListOf()

    fun adaugaEchipament(echipament: Echipament) {
        echipamente.add(echipament)
    }

    fun stergeEchipament(echipament: Echipament) {
        echipamente.remove(echipament)
    }

    fun afiseazaEchipamente() {
        println("Echipamentele din laboratorul $nume:")
        for (echipament in echipamente) {
            println(echipament)
        }
    }
}

abstract class Echipament(val nume: String) {
    abstract fun utilizeaza()
    override fun toString(): String {
        return "Echipament: $nume"
    }
}

class Calculator(nume: String) : Echipament(nume) {
    override fun utilizeaza() {
        println("Calculatorul $nume este utilizat.")
    }
}

class Microscop(nume: String) : Echipament(nume) {
    override fun utilizeaza() {
        println("Microscopul $nume este utilizat.")
    }
}

fun main() {
    val laborator = Laborator("Laborator de Biologie", 20)

    val calculator1 = Calculator("Calculator1")
    val calculator2 = Calculator("Calculator2")
    val microscop1 = Microscop("Microscop1")

    laborator.adaugaEchipament(calculator1)
    laborator.adaugaEchipament(calculator2)
    laborator.adaugaEchipament(microscop1)

    laborator.afiseazaEchipamente()

    calculator1.utilizeaza()
    microscop1.utilizeaza()

    laborator.stergeEchipament(calculator2)

    laborator.afiseazaEchipamente()
}
