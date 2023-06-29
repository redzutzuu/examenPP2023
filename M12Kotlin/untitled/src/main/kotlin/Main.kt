import java.util.Random

abstract class StudentState(protected val student: Student) {
    abstract fun updateState()
    abstract fun showState(): String
}

class FericitState(student: Student) : StudentState(student) {
    private val okStates = listOf("Fericit", "Bucuros", "Vesel")

    override fun updateState() {
        if (!okStates.contains(student.getCurrentState())) {
            student.toggleGeneralState()
        }
    }

    override fun showState(): String {
        return "Fericit"
    }
}

class NefericitState(student: Student) : StudentState(student) {
    private val okStates = listOf("Nefericit", "Disperat", "Suparat")

    override fun updateState() {
        if (!okStates.contains(student.getCurrentState())) {
            student.toggleGeneralState()
        }
    }

    override fun showState(): String {
        return "Nefericit"
    }
}

class Student(private val name: String) {
    private var currentState = "Fericit"
    private val generalStates = listOf(FericitState(this), NefericitState(this))
    private var generalState = generalStates[0]
    private val random = Random()

    fun getCurrentState(): String {
        return currentState
    }

    fun toggleGeneralState() {
        generalState = if (generalState == generalStates[0]) generalStates[1] else generalStates[0]
    }

    fun actNice(colega: Colega) {
        currentState = colega.actOn("Nice")
        updateGeneralState()
    }

    fun actBad(colega: Colega) {
        currentState = colega.actOn("Bad")
        updateGeneralState()
    }

    private fun updateGeneralState() {
        generalState.updateState()
    }

    fun printState() {
        println("Studentul $name este $currentState, în general fiind ${generalState.showState()}.")
    }
}

class Colega(private val name: String) {
    private val fericitStates = listOf("Fericit", "Bucuros", "Vesel")
    private val nefericitStates = listOf("Nefericit", "Disperat", "Suparat")

    fun actOn(actionType: String): String {
        val selected = if (actionType == "Nice") {
            fericitStates.random()
        } else if (actionType == "Bad") {
            nefericitStates.random()
        } else {
            throw IllegalArgumentException("Acțiune incorectă!")
        }
        println("Colega $name a făcut un coleg $selected.")
        return selected
    }
}

fun main() {
    val s1 = Student("Florin")
    val c1 = Colega("Andreea")
    s1.actBad(c1)
    s1.printState()
    s1.actNice(c1)
    s1.printState()
}
