from abc import ABCMeta, abstractmethod
import re
from random import choice


class StrategieBancuri(metaclass=ABCMeta):
    def __init__(self):
        text = open("Bancuri.txt", 'r').read()
        self._dictionar = {"*": [], "**": [], "***": []}
        self._dictionar["*"] += re.findall("(?<!\*{2})(?<!\*{3})(?<=\*)[^\*]+", text)
        self._dictionar["**"] += re.findall("(?<!\*{3})(?<=\*{2})[^\*]+", text)
        self._dictionar["***"] += re.findall("(?<=\*{3})[^\*]+", text)

    @abstractmethod
    def get_banc(self):
        pass


class StrategieBancuri1Stea(StrategieBancuri):
    def __init__(self):
        super().__init__()

    def get_banc(self):
        return choice(self._dictionar["*"])


class StrategieBancuri2Stele(StrategieBancuri):
    def __init__(self):
        super().__init__()

    def get_banc(self):
        return choice(self._dictionar["**"])


class StrategieBancuri3Stele(StrategieBancuri):
    def __init__(self):
        super().__init__()

    def get_banc(self):
        return choice(self._dictionar["***"])


class Student:
    def __init__(self, name):
        self.__name = name
        self.__dict_reaction_to_banc_strategy = {}
        self.__dict_reaction_to_banc_strategy["Buna"] = StrategieBancuri1Stea()
        self.__dict_reaction_to_banc_strategy["Foarte buna"] = StrategieBancuri2Stele()
        self.__dict_reaction_to_banc_strategy["Cea mai buna"] = StrategieBancuri3Stele()
        self.__possible_reactions = ["Buna", "Foarte buna", "Cea mai buna"]

    def get_reaction(self):
        reaction = choice(self.__possible_reactions)
        print(f"Studentul {self.__name} are reacția: \"{reaction}\".")
        return reaction

    def say_banc_to(self, other):
        reaction = other.get_reaction()
        print(f"Studentul {self.__name} a primit reacția \"{reaction}\" și spune următorul banc:")
        print(self.__dict_reaction_to_banc_strategy[reaction].get_banc())


if __name__ == '__main__':
    s1 = Student("alex")
    s2 = Student("gigi")
    s1.say_banc_to(s2)
    s2.say_banc_to(s1)
