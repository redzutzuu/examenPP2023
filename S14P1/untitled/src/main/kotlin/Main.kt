// Definirea clasei enum pentru tipurile de obiecte din sală
enum class ObjectType {
    TABLE,
    CHAIR,
    PROJECTOR,
    WHITEBOARD
}

// Definirea clasei pentru obiectele din sală
data class ClassroomObject(val objectType: ObjectType, val id: Int)

// Definirea clasei pentru sala de curs
class Classroom {
    private val objects = mutableListOf<ClassroomObject>()

    // Adăugarea unui obiect nou în sală
    fun addObject(objectType: ObjectType) {
        val id = objects.size + 1
        val classroomObject = ClassroomObject(objectType, id)
        objects.add(classroomObject)
        println("Obiectul ${objectType.name} cu ID-ul $id a fost adăugat în sală.")
    }

    // Listarea obiectelor din sală
    fun listObjects() {
        if (objects.isEmpty()) {
            println("Nu există obiecte în sală.")
        } else {
            println("Obiectele din sală sunt:")
            objects.forEach { println("${it.objectType.name} - ID ${it.id}") }
        }
    }

    // Înlăturarea unui obiect din sală
    fun removeObject(id: Int) {
        val index = objects.indexOfFirst { it.id == id }
        if (index != -1) {
            val objectType = objects[index].objectType
            objects.removeAt(index)
            println("Obiectul ${objectType.name} cu ID-ul $id a fost înlăturat din sală.")
        } else {
            println("Obiectul cu ID-ul $id nu există în sală.")
        }
    }
}

fun main() {
    val classroom = Classroom()

    classroom.addObject(ObjectType.TABLE)
    classroom.addObject(ObjectType.CHAIR)
    classroom.addObject(ObjectType.PROJECTOR)
    classroom.listObjects()

    classroom.removeObject(2)
    classroom.listObjects()
    classroom.removeObject(4)
}
