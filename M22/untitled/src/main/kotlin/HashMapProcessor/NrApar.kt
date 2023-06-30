package HashMapProcessor

class NrApar(private val file:String): HashMapProcessor() {
    override fun get_runnable_object(): Runnable {
        class temp:Runnable{
            override fun run() {
                print_nr_apar(file)
            }
        }
        return temp()
    }
}