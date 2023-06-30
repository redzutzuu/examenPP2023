package HashMapProcessor

class EliminDup(private val file:String): HashMapProcessor() {
    override fun get_runnable_object(): Runnable {
        class temp:Runnable{
            override fun run() {
                print_elimin_dup(file)
            }
        }
        return temp()
    }
}