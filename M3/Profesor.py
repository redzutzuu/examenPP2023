class Profesor:
    def __init__(self, asistent):
        self.__asistent=asistent

    def respond_if_passed(self, grade):
        return grade>=4.5

    def ask_if_attending(self, i):
        if(self.__asistent.ask_if_attending(i)):
            print("Creating one more exam subject...")
