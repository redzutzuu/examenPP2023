def gestionare_lista_asteptare(func):
    def wrapper(self, numar_camera):
        func(self, numar_camera)
        self.rezerva_din_lista_de_asteptare()
    return wrapper

class Camera:
    def __init__(self, numar):
        self.numar = numar
        self.rezervat = False

    def rezerva(self):
        if not self.rezervat:
            self.rezervat = True
            return True
        else:
            return False

    def elibereaza(self):
        if self.rezervat:
            self.rezervat = False
            return True
        else:
            return False

class Hotel:
    def __init__(self, nr_camere):
        self.camere = [Camera(i) for i in range(1, nr_camere + 1)]
        self.lista_de_asteptare = []

    @gestionare_lista_asteptare
    def rezerva_camera(self, numar_camera):
        if self.camere[numar_camera - 1].rezerva():
            print(f"Camera {numar_camera} a fost rezervata.")
        else:
            print(f"Camera {numar_camera} este deja rezervata.")
            self.lista_de_asteptare.append(numar_camera)

    @gestionare_lista_asteptare
    def elibereaza_camera(self, numar_camera):
        if self.camere[numar_camera - 1].elibereaza():
            print(f"Camera {numar_camera} a fost eliberata.")
        else:
            print(f"Camera {numar_camera} nu este rezervata.")

    def rezerva_din_lista_de_asteptare(self):
        for numar_camera in self.lista_de_asteptare:
            if self.camere[numar_camera - 1].rezerva():
                print(f"Camera {numar_camera} a fost rezervata de pe lista de asteptare.")
                self.lista_de_asteptare.remove(numar_camera)
                break

def main():
    hotel = Hotel(3)
    hotel.rezerva_camera(1)
    hotel.rezerva_camera(2)
    hotel.rezerva_camera(3)
    hotel.rezerva_camera(1)  # Camera 1 este deja rezervata, deci va fi adaugata la lista de asteptare
    hotel.elibereaza_camera(1)  # Camera 1 va fi rezervata din nou imediat de pe lista de asteptare

if __name__ == "__main__":
    main()
