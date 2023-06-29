import BoomBox.BoomBoxFacade
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

fun main()= runBlocking{
    val facade=BoomBoxFacade()
    facade.components.forEach { launch { it.run() } }
    while(facade.menu()){}
}