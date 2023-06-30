import java.io.File

fun main() {
    val file = File("text.txt") // Numele fișierului text
    val text = file.readText() // Citirea conținutului fișierului într-un șir de caractere

    val cuvinte = text.split("\\s+".toRegex()) // Împărțirea textului în cuvinte

    val rezultat = cuvinte
        .filter { it.length >= 4 } // Filtrarea cuvintelor cu minim 4 caractere
        .map { it.substring(it.length / 2 - 1, it.length / 2 + 1) } // Extrage două caractere din mijlocul cuvântului
        .toList() // Convertirea rezultatului într-o listă

    println("Caracterele extrase din cuvinte:")
    rezultat.forEach { println(it) }
}
