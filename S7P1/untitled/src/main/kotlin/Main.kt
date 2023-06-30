open class Person(val name: String) {
    open fun eat(food: Any) {
        println("$name nu poate manca $food")
    }

    open fun drink(beverage: Any) {
        println("$name nu poate bea $beverage")
    }

    open fun dance(with: String) {
        println("$name nu poate dansa cu $with")
    }
}

class Ion : Person("Ion") {
    override fun eat(food: Any) {
        println("Ion mananca $food")
    }

    override fun drink(beverage: Any) {
        println("Ion bea $beverage")
    }

    override fun dance(with: String) {
        println("Ion danseaza cu $with")
    }
}

class Vasile : Person("Vasile") {
    override fun eat(food: Any) {
        println("Vasile mananca $food")
    }

    override fun drink(beverage: Any) {
        println("Vasile bea $beverage")
    }

    override fun dance(with: String) {
        println("Vasile danseaza cu $with")
    }
}

class Alex : Person("Alex") {
    override fun eat(food: Any) {
        println("Alex mananca $food")
    }

    override fun drink(beverage: Any) {
        println("Alex bea $beverage")
    }

    override fun dance(with: String) {
        println("Alex danseaza cu $with")
    }
}

fun main() {
    val ion = Ion()
    val vasile = Vasile()
    val alex = Alex()

    // Exemplu de intrebari
    println("Cu cine poate dansa Vasile?")
    vasile.dance("femei")

    println("Ce pot manca barbatii?")
    ion.eat("mere")
    vasile.eat("pere")
    alex.eat("prajituri brune")

    println("Ce pot manca femeile?")
    ion.eat("mere") // Ion este un bărbat, deci nu poate răspunde acestei întrebări
    vasile.eat("pere") // Vasile este un bărbat, deci nu poate răspunde acestei întrebări
    alex.eat("prajituri brune")
}
