package HashMapProcessor

class Min(private val file:String): HashMapProcessor() {
    override fun get_runnable_object(): Runnable {
        class temp:Runnable{
            override fun run() {
                print_min(file)
            }
        }
        return temp()
    }
}