from abc import ABCMeta, abstractmethod
from random import choice


class StudentState(metaclass=ABCMeta):
    def __init__(self, student):
        self._student = student

    @abstractmethod
    def update_state(self):
        pass

    @abstractmethod
    def show_state(self):
        pass


class FericitState(StudentState):
    def __init__(self, student):
        super().__init__(student)
        self.__ok_states = ["Fericit", "Bucuros", "Vesel"]

    def update_state(self):
        if self._student.get_current_state() not in self.__ok_states:
            self._student.toggle_general_state()

    def show_state(self):
        return "Fericit"


class NefericitState(StudentState):
    def __init__(self, student):
        super().__init__(student)
        self.__ok_states = ["Nefericit", "Disperat", "Suparat"]

    def update_state(self):
        if self._student.get_current_state() not in self.__ok_states:
            self._student.toggle_general_state()

    def show_state(self):
        return "Nefericit"


class Student:
    def __init__(self, name):
        self.__name = name
        self.__current_state = "Fericit"
        self.__general_states = [FericitState(self), NefericitState(self)]
        self.__general_state = self.__general_states[0]
        self.__nice_action = lambda colega: colega.act_on("Nice")
        self.__bad_action = lambda colega: colega.act_on("Bad")

    def get_current_state(self):
        return self.__current_state

    def toggle_general_state(self):
        if self.__general_state == self.__general_states[0]:
            self.__general_state = self.__general_states[1]
        else:
            self.__general_state = self.__general_states[0]

    def act_nice(self, colega):
        self.__current_state = self.__nice_action(colega)
        self.__update_general_state()

    def act_bad(self, colega):
        self.__current_state = self.__bad_action(colega)
        self.__update_general_state()

    def __update_general_state(self):
        self.__general_state.update_state()

    def print_state(self):
        print(
            f"Studentul {self.__name} este {self.__current_state}, în general fiind {self.__general_state.show_state()}.")


class Colega:
    def __init__(self, name):
        self.__name = name
        self.__fericit_states = ["Fericit", "Bucuros", "Vesel"]
        self.__nefericit_states = ["Nefericit", "Disperat", "Suparat"]

    def act_on(self, action_type):
        if action_type == "Nice":
            selected = choice(self.__fericit_states)
        elif action_type == "Bad":
            selected = choice(self.__nefericit_states)
        else:
            raise Exception("Acțiune incorectă!")
        print(f"Colega {self.__name} a făcut un coleg {selected}.")
        return selected


if __name__ == '__main__':
    s1 = Student("Florin")
    c1 = Colega("Andreea")
    s1.act_bad(c1)
    s1.print_state()
    s1.act_nice(c1)
    s1.print_state()
