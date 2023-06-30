from abc import ABCMeta, abstractmethod

class MamiferImplementation(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def preferred_food(self):
        pass


class Mamifer:
    def __init__(self, implementation):
        self._implementation = implementation

    def speak(self):
        self._implementation.speak()

    def preferred_food(self):
        self._implementation.preferred_food()


class Femeie(MamiferImplementation):
    def speak(self):
        print("Vorbeste cu voce de femeie.")

    def preferred_food(self):
        print("Caviar")


class Barbat(MamiferImplementation):
    def speak(self):
        print("Vorbeste cu voce de barbat.")

    def preferred_food(self):
        print("Mici")


class Caine(MamiferImplementation):
    def speak(self):
        print("Ham ham.")

    def preferred_food(self):
        print("Carne")


class Pisica(MamiferImplementation):
    def speak(self):
        print("Miau miau.")

    def preferred_food(self):
        print("Peste")


if __name__ == '__main__':
    caine = Mamifer(Caine())
    pisica = Mamifer(Pisica())
    femeie = Mamifer(Femeie())
    barbat = Mamifer(Barbat())
    mamifere = [caine, pisica, femeie, barbat]
    for mamifer in mamifere:
        mamifer.speak()
        mamifer.preferred_food()
