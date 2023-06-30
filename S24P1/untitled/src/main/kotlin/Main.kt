class Obiect(val nume: String, val cod: String) {
    override fun toString(): String {
        return "$nume ($cod)"
    }
}

class SalaLaborator {
    private val obiecte = mutableListOf<Obiect>()

    fun adaugaObiect(nume: String, cod: String) {
        val obiect = Obiect(nume, cod)
        obiecte.add(obiect)
        println("Obiectul $obiect a fost adăugat în sală.")
    }

    fun afiseazaObiecte() {
        if (obiecte.isEmpty()) {
            println("Sala de laborator este goală.")
        } else {
            println("Obiectele din sala de laborator:")
            for (obiect in obiecte) {
                println(obiect)
            }
        }
    }

    fun stergeObiect(cod: String) {
        val obiect = obiecte.find { it.cod == cod }
        if (obiect != null) {
            obiecte.remove(obiect)
            println("Obiectul $obiect a fost eliminat din sală.")
        } else {
            println("Obiectul cu codul $cod nu există în sală.")
        }
    }

    fun numaraObiecte(): Int {
        return obiecte.size
    }
}

fun main() {
    val sala = SalaLaborator()

    sala.afiseazaObiecte()

    sala.adaugaObiect("Microscop", "MC123")
    sala.adaugaObiect("Calculator", "CL456")
    sala.adaugaObiect("Osciloscop", "OS789")

    sala.afiseazaObiecte()

    sala.stergeObiect("CL456")

    sala.afiseazaObiecte()

    val numarObiecte = sala.numaraObiecte()
    println("Numărul de obiecte din sală: $numarObiecte")
}
