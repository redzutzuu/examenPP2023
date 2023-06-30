import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.async
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.Deferred
import kotlin.coroutines.CoroutineContext
import kotlin.coroutines.EmptyCoroutineContext
import kotlin.coroutines.coroutineContext

// Interfață pentru operațiile de bază
interface Operation {
    fun performOperation(a: Int, b: Int): Int
}

// Clasă de bază pentru actori
abstract class Actor : Operation {
    abstract val name: String
}

// Subclasă pentru adunare
class AdditionActor : Actor() {
    override val name: String = "Addition"

    override fun performOperation(a: Int, b: Int): Int {
        return a + b
    }
}

// Subclasă pentru scădere
class SubtractionActor : Actor() {
    override val name: String = "Subtraction"

    override fun performOperation(a: Int, b: Int): Int {
        return a - b
    }
}

// Subclasă pentru înmulțire
class MultiplicationActor : Actor() {
    override val name: String = "Multiplication"

    override fun performOperation(a: Int, b: Int): Int {
        return a * b
    }
}

// Subclasă pentru împărțire
class DivisionActor : Actor() {
    override val name: String = "Division"

    override fun performOperation(a: Int, b: Int): Int {
        return a / b
    }
}

fun main() = runBlocking {
    // Crearea hashmap-ului
    val hashMap = HashMap<String, Actor>()
    hashMap["addition"] = AdditionActor()
    hashMap["subtraction"] = SubtractionActor()
    hashMap["multiplication"] = MultiplicationActor()
    hashMap["division"] = DivisionActor()

    // Realizarea operațiilor în fire de execuție separate
    val result = performOperationsAsync(hashMap, 5, 3)

    // Așteptarea finalizării execuției tuturor firelor de execuție
    result.await()
}

// Funcție pentru realizarea operațiilor în fire de execuție separate
suspend fun performOperationsAsync(hashMap: HashMap<String, Actor>, a: Int, b: Int): Deferred<Unit> = GlobalScope.async {
    // Iterarea prin fiecare pereche cheie-valoare din hashmap
    for ((key, actor) in hashMap) {
        // Executarea operației în fiecare actor într-un nou fir de execuție
        launchActor(actor, a, b)
    }
}

// Funcție pentru lansarea unui actor într-un nou fir de execuție
suspend fun launchActor(actor: Actor, a: Int, b: Int) {
    val result = actor.performOperation(a, b)
    println("${actor.name}: $result")
}
