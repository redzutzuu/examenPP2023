// Clasele abstracte pentru Student, Profesor și Secretar
abstract class Student {
    abstract fun displayInfo()
}

abstract class Profesor {
    abstract fun displayInfo()
}

abstract class Secretar {
    abstract fun displayInfo()
}

// Obiectele specifice asociate cu Profesor
class ProfesorPrincipal : Profesor() {
    override fun displayInfo() {
        println("Profesor Principal")
    }
}

class Conferentiar : Profesor() {
    override fun displayInfo() {
        println("Conferentiar")
    }
}

class SefLucrari : Profesor() {
    override fun displayInfo() {
        println("Sef Lucrari")
    }
}

class Asistent : Profesor() {
    override fun displayInfo() {
        println("Asistent")
    }
}

// Obiectele specifice asociate cu Student
class Integralist : Student() {
    override fun displayInfo() {
        println("Integralist")
    }
}

class Restantier : Student() {
    override fun displayInfo() {
        println("Restantier")
    }
}

class Repetent : Student() {
    override fun displayInfo() {
        println("Repetent")
    }
}

// Obiectele specifice asociate cu Secretar
class SecretarSef : Secretar() {
    override fun displayInfo() {
        println("Secretar Sef")
    }
}

class Secretar1 : Secretar() {
    override fun displayInfo() {
        println("Secretar 1")
    }
}

class Secretar2 : Secretar() {
    override fun displayInfo() {
        println("Secretar 2")
    }
}

// Fabrica abstractă pentru crearea de obiecte Student, Profesor și Secretar
abstract class FabricaAbstracta {
    abstract fun createStudent(): Student
    abstract fun createProfesor(): Profesor
    abstract fun createSecretar(): Secretar
}

// Implementarea fabricii abstracte
class FabricaConcreta : FabricaAbstracta() {
    override fun createStudent(): Student {
        // Returnează un obiect Student specific
        return Integralist()
    }

    override fun createProfesor(): Profesor {
        // Returnează un obiect Profesor specific
        return ProfesorPrincipal()
    }

    override fun createSecretar(): Secretar {
        // Returnează un obiect Secretar specific
        return SecretarSef()
    }
}

// Exemplu de utilizare a fabricii abstracte
fun main() {
    // Crearea fabricii concrete
    val fabrica: FabricaAbstracta = FabricaConcreta()

    // Crearea unui obiect Student
    val student: Student = fabrica.createStudent()
    student.displayInfo()

    // Crearea unui obiect Profesor
    val profesor: Profesor = fabrica.createProfesor()
    profesor.displayInfo()

    // Crearea unui obiect Secretar
    val secretar: Secretar = fabrica.createSecretar()
    secretar.displayInfo()
}
