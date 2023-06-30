import java.util.concurrent.atomic.AtomicInteger

class Barrier(private val numThreads: Int) {
    private val counter = AtomicInteger(0)
    private val lock = Object()

    fun await() {
        synchronized(lock) {
            counter.incrementAndGet()
            if (counter.get() == numThreads) {
                lock.notifyAll()
            } else {
                while (counter.get() < numThreads) {
                    try {
                        lock.wait()
                    } catch (e: InterruptedException) {
                        e.printStackTrace()
                    }
                }
            }
        }
    }
}

fun main() {
    val numThreads = 4
    val barrier = Barrier(numThreads)

    val threads = List(numThreads) {
        Thread {
            println("Thread ${Thread.currentThread().id} before barrier")
            barrier.await()
            println("Thread ${Thread.currentThread().id} after barrier")
        }
    }

    threads.forEach(Thread::start)
    threads.forEach(Thread::join)
}
