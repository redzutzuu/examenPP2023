from abc import ABCMeta, abstractmethod

class Mediator(metaclass=ABCMeta):
    def __init__(self):
        self._profesor=None
        self._studenti=None

    @abstractmethod
    def ask_if_passed(self, grade):
        pass

    @abstractmethod
    def ask_if_attending(self, i):
        pass

    def set_studenti(self,studenti):
        self._studenti=studenti

    def set_profesor(self,profesor):
        self._profesor=profesor

class Asistent(Mediator):
    def __init__(self):
        super().__init__()

    def ask_if_passed(self,grade):
        return super()._profesor.respond_if_passed(grade)

    def ask_if_attending(self,i):
        return super()._studenti[i].respond_if_attending()
