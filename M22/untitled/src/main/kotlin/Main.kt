import HashMapProcessor.HashMapProcessorFactory
import java.io.File

fun main() {
    val map = HashMap<String, String>()
    File("hash_map.txt").useLines { lines ->
        lines.map { it.split("->") }.forEach { pair ->
            if (pair.size == 2) {
                val (key, filePath) = pair
                map[key.trim()] = filePath.trim()
            }
        }
    }

    val fact = HashMapProcessorFactory()
    val runnables = map.map { (key, value) ->
        fact.create(key, value).get_runnable_object()
    }
    val threads = runnables.map { Thread(it) }
    threads.forEach { it.start() }
    threads.forEach { it.join() }
}
