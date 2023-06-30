class Student:
    def __init__(self, name):
        self.name = name
        self.state = "fericit"

    def change_state(self, new_state):
        self.state = new_state
        print(f"Starea studentului {self.name} a fost schimbata in {self.state}.")


class Command:
    def execute(self):
        pass


class ChangeStateCommand(Command):
    def __init__(self, student, new_state):
        self.student = student
        self.new_state = new_state

    def execute(self):
        self.student.change_state(self.new_state)


class Colleague:
    def __init__(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()


def main():
    student = Student("John")

    while True:
        print("\n--- Meniu ---")
        print("1. Schimba starea studentului la fericit")
        print("2. Schimba starea studentului la disperat")
        print("3. Schimba starea studentului la plictisit")
        print("0. Iesire")

        option = input("Alege o optiune: ")

        if option == "1":
            command = ChangeStateCommand(student, "fericit")
            colleague = Colleague(command)
            colleague.execute_command()
        elif option == "2":
            command = ChangeStateCommand(student, "disperat")
            colleague = Colleague(command)
            colleague.execute_command()
        elif option == "3":
            command = ChangeStateCommand(student, "plictisit")
            colleague = Colleague(command)
            colleague.execute_command()
        elif option == "0":
            print("Programul s-a incheiat.")
            break
        else:
            print("Optiune invalida. Te rog sa alegi din nou.")


if __name__ == "__main__":
    main()
