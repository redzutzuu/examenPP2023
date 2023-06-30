import turtle


class Forma:
    def deseneaza(self):
        pass


class Patrat(Forma):
    def __init__(self, latura):
        self.latura = latura

    def deseneaza(self):
        turtle.forward(self.latura)
        turtle.right(90)
        turtle.forward(self.latura)
        turtle.right(90)
        turtle.forward(self.latura)
        turtle.right(90)
        turtle.forward(self.latura)
        turtle.right(90)


class Dreptunghi(Forma):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def deseneaza(self):
        turtle.forward(self.lungime)
        turtle.right(90)
        turtle.forward(self.latime)
        turtle.right(90)
        turtle.forward(self.lungime)
        turtle.right(90)
        turtle.forward(self.latime)
        turtle.right(90)


class Cerc(Forma):
    def __init__(self, raza):
        self.raza = raza

    def deseneaza(self):
        turtle.circle(self.raza)


class FabricaForme:
    def creeaza_forma(self):
        pass


class FabricaPatrat(FabricaForme):
    def creeaza_forma(self, latura):
        return Patrat(latura)


class FabricaDreptunghi(FabricaForme):
    def creeaza_forma(self, lungime, latime):
        return Dreptunghi(lungime, latime)


class FabricaCerc(FabricaForme):
    def creeaza_forma(self, raza):
        return Cerc(raza)


def main():
    turtle.speed(2)

    fabrica_patrat = FabricaPatrat()
    forma_patrat = fabrica_patrat.creeaza_forma(100)
    forma_patrat.deseneaza()

    fabrica_dreptunghi = FabricaDreptunghi()
    forma_dreptunghi = fabrica_dreptunghi.creeaza_forma(150, 80)
    forma_dreptunghi.deseneaza()

    fabrica_cerc = FabricaCerc()
    forma_cerc = fabrica_cerc.creeaza_forma(50)
    forma_cerc.deseneaza()

    turtle.done()


if __name__ == "__main__":
    main()
