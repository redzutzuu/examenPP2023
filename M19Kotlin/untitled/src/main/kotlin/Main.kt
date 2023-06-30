import chain.CEOHandler
import factory.FactoryProducer
import kotlinx.coroutines.runBlocking

fun main(args: Array<String>)= runBlocking {
    // se creeaza 1xFactoryProducer, 1xEliteFactory, 1xHappyWorkerFactory
    //...
    val factoryProducer=FactoryProducer()
    val eliteFactory=factoryProducer.getFactory("Elite")
    val happyWorkerFactory=factoryProducer.getFactory("HappyWorker")

    // crearea instantelor (prin intermediul celor 2 fabrici):
    // 2xCEOHandler, 2xExecutiveHandler, 2xManagerHandler, 2xHappyWorkerHandler
    //...
    val ceo1=eliteFactory.getHandler("CEO")
    val ceo2=eliteFactory.getHandler("CEO")

    val ex1=eliteFactory.getHandler("Executive")
    val ex2=eliteFactory.getHandler("Executive")

    val man1=eliteFactory.getHandler("Manager")
    val man2=eliteFactory.getHandler("Manager")

    val work1=happyWorkerFactory.getHandler("HappyWorker")
    val work2=happyWorkerFactory.getHandler("HappyWorker")

    // se construieste lantul (se verifica intai diagrama de obiecte si se realizeaza legaturile)
    //...
    ceo1.SetRight(ex1)

    ex1.SetVertical(ex2)
    ex1.SetRight(man1)

    man1.SetRight(work1)
    man1.SetVertical(man2)

    work1.SetVertical(work2)

    ceo2.SetVertical(ceo1)

    ex2.SetLeft(ceo2)
    ex2.SetRight(man2)

    man2.SetLeft(ex2)
    man2.SetRight(work2)

    work2.SetLeft(man2)

    // se executa lantul utilizand atat mesaje de prioritate diferita, cat si directii diferite in lant
    //...

    println("-".repeat(100))
    ceo1.handleRequest("right","4:Request")
    println("-".repeat(100))
    man2.handleRequest("right", "3:Alt Request")
    println("-".repeat(100))
    work1.handleRequest("right","9:Request eronat")
    println("-".repeat(100))

    //Formele "Request - Mesaj" si "Response - Mesaj" nu vad sa contina prioritate, am folosit formatul de cerere vechi
}