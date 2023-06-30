class Camera:
    def __init__(self, numar_camera, disponibila=True):
        self.numar_camera = numar_camera
        self.disponibila = disponibila

    def rezerva(self):
        if self.disponibila:
            print(f"Camera {self.numar_camera} a fost rezervată.")
            self.disponibila = False
        else:
            print(f"Camera {self.numar_camera} nu este disponibilă.")

    def elibereaza(self):
        if not self.disponibila:
            print(f"Camera {self.numar_camera} a fost eliberată.")
            self.disponibila = True
        else:
            print(f"Camera {self.numar_camera} este deja disponibilă.")


class Hotel:
    def __init__(self):
        self.camere = {}
        self.lista_asteptare = []

    def adauga_camera(self, camera):
        self.camere[camera.numar_camera] = camera

    def rezerva_camera(self, numar_camera):
        if numar_camera in self.camere:
            camera = self.camere[numar_camera]
            camera.rezerva()
        else:
            print(f"Camera {numar_camera} nu există în hotel.")

    def elibereaza_camera(self, numar_camera):
        if numar_camera in self.camere:
            camera = self.camere[numar_camera]
            camera.elibereaza()
        else:
            print(f"Camera {numar_camera} nu există în hotel.")

    def adauga_in_lista_asteptare(self, nume_client):
        self.lista_asteptare.append(nume_client)

    def afiseaza_lista_asteptare(self):
        print("Lista de așteptare:")
        for i, nume_client in enumerate(self.lista_asteptare, start=1):
            print(f"{i}. {nume_client}")

    def tratare_lista_asteptare(self):
        if len(self.lista_asteptare) > 0:
            nume_client = self.lista_asteptare.pop(0)
            print(f"Se rezervă o cameră pentru clientul {nume_client}.")
            # Implementați logica de rezervare a unei camere pentru clientul de pe lista de așteptare
            # Poate fi utilizată metoda rezerva_camera() cu un număr de cameră disponibil
        else:
            print("Nu există clienți în lista de așteptare.")


def main():
    hotel = Hotel()

    camera1 = Camera(101)
    camera2 = Camera(102)
    camera3 = Camera(103)

    hotel.adauga_camera(camera1)
    hotel.adauga_camera(camera2)
    hotel.adauga_camera(camera3)

    hotel.rezerva_camera(101)
    hotel.rezerva_camera(102)
    hotel.rezerva_camera(101)

    hotel.afiseaza_lista_asteptare()
    hotel.adauga_in_lista_asteptare("John Smith")
    hotel.adauga_in_lista_asteptare("Jane Doe")
    hotel.afiseaza_lista_asteptare()

    hotel.tratare_lista_asteptare()

    hotel.elibereaza_camera(102)
    hotel.elibereaza_camera(102)

    hotel.tratare_lista_asteptare()


if __name__ == "__main__":
    main()
