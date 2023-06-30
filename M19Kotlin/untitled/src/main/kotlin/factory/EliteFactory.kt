package factory

import chain.CEOHandler
import chain.ExecutiveHandler
import chain.Handler
import chain.ManagerHandler

class EliteFactory: AbstractFactory() {
    override fun getHandler(handler: String): Handler
    {
        when(handler)
        {
            "CEO"->return CEOHandler()
            "Executive"->return ExecutiveHandler()
            //"Manager"->return ManagerHandler()
            else->return ManagerHandler()
        }
    }
}