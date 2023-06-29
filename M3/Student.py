class Student:
    def __init__(self, name, asistent):
        self.__name = name
        self.__grade = 0
        self.__asistent = asistent
        self.__passed = False
        self.__attending=False

    def do_exam(self, grade):
        self.__grade = grade

    def ask_if_passed(self):
        self.__passed = self.__asistent.ask_if_passed(self.__grade)

    def respond_if_attending(self):
        return self.__attending

    # def set_passed(self, passed):
    #     self.__passed=passed
