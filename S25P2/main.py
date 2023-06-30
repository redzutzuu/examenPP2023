class Mediator:
    def __init__(self):
        self.furnici = []

    def adauga_furnica(self, furnica):
        self.furnici.append(furnica)

    def trimite_mesaj(self, expeditor, destinatar, mesaj):
        if destinatar in self.furnici:
            destinatar.primeste_mesaj(expeditor, mesaj)
        else:
            print(f"Destinatarul {destinatar} nu este înregistrat în mediator.")

class Furnica:
    def __init__(self, nume):
        self.nume = nume
        self.mediator = None

    def inregistreaza_mediator(self, mediator):
        self.mediator = mediator

    def trimite_mesaj(self, destinatar, mesaj):
        self.mediator.trimite_mesaj(self, destinatar, mesaj)

    def primeste_mesaj(self, expeditor, mesaj):
        print(f"Furnica {self.nume} a primit un mesaj de la furnica {expeditor.nume}: {mesaj}")


def main():
    mediator = Mediator()

    furnica1 = Furnica("Furnica 1")
    furnica2 = Furnica("Furnica 2")
    furnica3 = Furnica("Furnica 3")

    mediator.adauga_furnica(furnica1)
    mediator.adauga_furnica(furnica2)
    mediator.adauga_furnica(furnica3)

    furnica1.inregistreaza_mediator(mediator)
    furnica2.inregistreaza_mediator(mediator)
    furnica3.inregistreaza_mediator(mediator)

    furnica1.trimite_mesaj(furnica2, "Mâncare")
    furnica2.trimite_mesaj(furnica1, "Drum bun")
    furnica3.trimite_mesaj(furnica1, "Pericol")
    furnica3.trimite_mesaj(furnica2, "Ajutor")


if __name__ == "__main__":
    main()
