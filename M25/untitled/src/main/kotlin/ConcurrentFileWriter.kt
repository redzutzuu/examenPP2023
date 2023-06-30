import java.util.concurrent.locks.ReentrantLock

abstract class ConcurrentFileWriter(protected val lock:ReentrantLock) {
    abstract suspend fun write()
}