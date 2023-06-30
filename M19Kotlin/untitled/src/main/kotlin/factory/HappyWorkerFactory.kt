package factory

import chain.HappyWorkerHandler
import chain.Handler

class HappyWorkerFactory: AbstractFactory() {
    override fun getHandler(handler: String): Handler {
        when(handler)
        {
            "HappyWorker"->return HappyWorkerHandler()
            else->return HappyWorkerHandler()
        }
    }

}