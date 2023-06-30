import java.io.File

class TreeNode<T>(var value: T) {
    var left: TreeNode<T>? = null
    var right: TreeNode<T>? = null
}

class WordTree {
    val root: TreeNode<String> = TreeNode("")

    fun buildTree(words: List<String>, constraint: (String) -> Boolean) {
        for (word in words) {
            if (constraint(word)) {
                insertWord(root, word)
            }
        }
    }

    private fun insertWord(node: TreeNode<String>, word: String) {
        var current = node
        for (char in word) {
            if (char.isLetter()) {
                val childNode = findChildNode(current, char)
                if (childNode != null) {
                    current = childNode
                } else {
                    val newChild = TreeNode(char.toString())
                    if (char.isLowerCase()) {
                        current.left = newChild
                    } else {
                        current.right = newChild
                    }
                    current = newChild
                }
            }
        }
        current.value = word
    }

    private fun findChildNode(node: TreeNode<String>, char: Char): TreeNode<String>? {
        return if (char.isLowerCase()) {
            node.left
        } else {
            node.right
        }
    }

    fun traverseInOrder(node: TreeNode<String>?, action: (String) -> Unit) {
        if (node == null) return
        traverseInOrder(node.left, action)
        action(node.value)
        traverseInOrder(node.right, action)
    }

    fun traversePreOrder(node: TreeNode<String>?, action: (String) -> Unit) {
        if (node == null) return
        action(node.value)
        traversePreOrder(node.left, action)
        traversePreOrder(node.right, action)
    }

    fun traversePostOrder(node: TreeNode<String>?, action: (String) -> Unit) {
        if (node == null) return
        traversePostOrder(node.left, action)
        traversePostOrder(node.right, action)
        action(node.value)
    }
}

fun main() {

    val workingDir = System.getProperty("user.dir")
    println("Directorul de lucru curent: $workingDir")

    val fileName = "input.txt" // Numele fișierului de intrare
    val words = mutableListOf<String>()

    // Citirea cuvintelor din fișierul de intrare
    File(fileName).forEachLine { line ->
        val wordList = line.split(" ")
        words.addAll(wordList)
    }

    // Crearea și construirea arborelui binar cu constrângerea specificată
    val wordTree = WordTree()
    wordTree.buildTree(words) { word ->
        word.length % 2 == 0
    }

    // Afișarea porțiunilor arborelui utilizând metoda traverseInOrder()
    println("Traversare în ordine:")
    wordTree.traverseInOrder(wordTree.root) { word ->
        println(word)
    }

    // Actualizarea valorii unui nod în arbore
    wordTree.root.left?.value = "new value"

    // Afișarea porțiunilor arborelui după actualizare
    println("Traversare în preordine:")
    wordTree.traversePreOrder(wordTree.root) { word ->
        println(word)
    }

    println("Traversare în postordine:")
    wordTree.traversePostOrder(wordTree.root) { word ->
        println(word)
    }
}
