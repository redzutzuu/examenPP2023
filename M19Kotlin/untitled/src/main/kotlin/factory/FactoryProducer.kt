package factory

class FactoryProducer {
    fun getFactory(choice: String): AbstractFactory {
        when(choice)
        {
            "Elite"->return EliteFactory()
            else->return HappyWorkerFactory()
        }
    }
}