from datetime import datetime

# Clasa pentru obiectul de recalculare a prețului
class RecalcularePret:
    def __init__(self):
        self.pret = 0
        self.observers = []

    def adauga_observer(self, observer):
        self.observers.append(observer)

    def elimina_observer(self, observer):
        self.observers.remove(observer)

    def set_pret(self, pret_nou):
        self.pret = pret_nou
        self.notifica_observers()

    def notifica_observers(self):
        for observer in self.observers:
            observer.update(self.pret)


# Clasa pentru obiectul Observer
class LoggerObserver:
    def update(self, pret):
        username = input("Introduceți numele de utilizator: ")
        password = input("Introduceți parola: ")

        # Verificare autentificare
        if self.verifica_autentificare(username, password):
            self.log(pret, username)

    def verifica_autentificare(self, username, password):
        # Verificare utilizator și parolă (implementarea depinde de cerințele tale)
        if username == "admin" and password == "adminpass":
            print("Autentificare reusita.")
            return True
        else:
            print("Autentificare eșuată.")
            return False

    def log(self, pret, username):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        modificare = f"Modificare de preț: {pret}"
        log_entry = f"{timestamp} - User: {username}, {modificare}\n"

        with open("log.txt", "a") as file:
            file.write(log_entry)


# Crearea obiectului de recalculare a prețului și adăugarea observatorului
recalculare_pret = RecalcularePret()
logger_observer = LoggerObserver()
recalculare_pret.adauga_observer(logger_observer)

# Exemplu de setare a unui nou preț
noul_pret = float(input("Introduceți noul preț: "))
recalculare_pret.set_pret(noul_pret)
