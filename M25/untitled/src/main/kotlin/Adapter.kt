import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import java.util.concurrent.locks.ReentrantLock

class Adapter(lock:ReentrantLock, files:List<String>, output_file:String):ConcurrentFileWriter(lock) {
    private val readers_and_writers=files.map { ReaderAndWriter(it,output_file) }
    override suspend fun write()= coroutineScope {
        val tasks=readers_and_writers.map { launch { lock.lock();it.write(it.read());lock.unlock() } }
        tasks.forEach { it.join() }
    }
}