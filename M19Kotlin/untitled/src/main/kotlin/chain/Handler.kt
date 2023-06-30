package chain


interface Handler {
    suspend fun handleRequest(forwardDirection: String, messageToBeProcessed: String)
    fun SetRight(right:Handler?)
    fun SetLeft(left:Handler?)
    fun SetVertical(vertical:Handler?)
}