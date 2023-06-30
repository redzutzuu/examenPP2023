package HashMapProcessor

class Max(private val file:String): HashMapProcessor() {
    override fun get_runnable_object(): Runnable {
        class temp:Runnable{
            override fun run() {
                print_max(file)
            }
        }
        return temp()
    }
}