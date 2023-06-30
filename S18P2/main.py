# Clasa Student
class Student:
    def __init__(self, name):
        self.name = name
        self.state = "Fericit"

    def change_state(self, new_state):
        self.state = new_state
        print(f"Studentul {self.name} a trecut în starea {self.state}")


# Clasa de bază Command
class Command:
    def execute(self):
        pass


# Clasa derivată ChangeStateCommand
class ChangeStateCommand(Command):
    def __init__(self, student, new_state):
        self.student = student
        self.new_state = new_state

    def execute(self):
        self.student.change_state(self.new_state)


# Clasa Professor care are capacitatea de a emite comenzi
class Professor:
    def __init__(self):
        self.command_history = []

    def send_command(self, command):
        self.command_history.append(command)
        command.execute()


# Funcția main
def main():
    # Crearea obiectelor
    student = Student("John")
    professor = Professor()

    # Crearea comenzilor și trimiterea lor de către profesor
    command1 = ChangeStateCommand(student, "Disperat")
    command2 = ChangeStateCommand(student, "Fericit")

    professor.send_command(command1)  # Schimbă starea studentului în "Disperat"
    professor.send_command(command2)  # Schimbă starea studentului în "Fericit"


# Apelul funcției main
if __name__ == "__main__":
    main()
