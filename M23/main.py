class Originator:
    def __init__(self, l):
        self.__state = l

    def set_state(self, l):
        self.__state = l

    def get_state(self):
        return self.__state

    def save_state_to_memento(self):
        return Memento(self.__state)

    def restore_state_from_memento(self, memento):
        self.__state = memento.get_state()


class Memento:
    def __init__(self, state):
        self.__state = state

    def get_state(self):
        return self.__state


class Caretaker:
    def __init__(self):
        self.__states = []

    def add(self, state):
        self.__states.append(state)

    def get(self):
        rez = self.__states[-1]
        self.__states.remove(self.__states[-1])
        return rez


if __name__ == '__main__':
    numbers = open("file1.csv", 'r').read().split(',')
    numbers = [int(x) for x in numbers]

    f1 = lambda x: (x % 2 == 0 and x + 1) or x
    f2 = lambda x: 3 * x * x - 2 * x + 1
    f3 = lambda x: x + x + 1
    functions = [f1, f2, f3]

    caretaker = Caretaker()
    originator = Originator(numbers)

    print(f"Lista originala: {numbers}")
    for i, f in enumerate(functions, 1):
        caretaker.add(originator.save_state_to_memento())
        originator.set_state([f(x) for x in originator.get_state()])
        print(f"Lista dupa aplicarea functiei f{i}: {originator.get_state()}")
        restore = input("Doriti restaurarea starii anterioare a listei? 1-Da Altceva-Nu\nRaspunsul dumneavoastra: ")
        if restore == "Da":
            originator.restore_state_from_memento(caretaker.get())
    print(f"Lista finala: {originator.get_state()}")
