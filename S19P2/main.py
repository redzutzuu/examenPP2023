class Camera:
    def __init__(self, numar, pret):
        self.numar = numar
        self.pret = pret
        self.consum_bar = 0

    def adauga_consum_bar(self, valoare):
        self.consum_bar += valoare


class ServiciuConsumBar:
    @staticmethod
    def tratare_plata(func):
        def wrapper(rezervare, *args, **kwargs):
            consum_bar = float(input("Introduceți valoarea consumului din bar: "))
            rezervare.camera.adauga_consum_bar(consum_bar)
            return func(rezervare, *args, **kwargs)
        return wrapper


class Rezervare:
    def __init__(self, camera):
        self.camera = camera

    @ServiciuConsumBar.tratare_plata
    def genereaza_nota_plata(self):
        total = self.camera.pret + self.camera.consum_bar
        print(f"Notă de plată pentru camera {self.camera.numar}:")
        print(f" - Preț camera: {self.camera.pret} lei/noapte")
        print(f" - Consum bar: {self.camera.consum_bar} lei")
        print(f" - Total: {total} lei")


# Exemplu de utilizare
def main():
    camera1 = Camera(1, 100)
    rezervare = Rezervare(camera1)
    rezervare.genereaza_nota_plata()


if __name__ == "__main__":
    main()
