import turtle

# Definirea prototipului de carucior
class CarPrototype:
    def __init__(self, color):
        self.color = color

    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.penup()

def main():
    # Crearea prototipului de carucior
    car_prototype = CarPrototype("red")

    # Clonarea si desenarea mai multor carucioare
    car1 = car_prototype
    car1.draw(-100, 0)

    car2 = car_prototype
    car2.draw(0, 0)

    car3 = car_prototype
    car3.draw(100, 0)

    # Menținerea desenului vizibil până la închiderea ferestrei
    turtle.done()

if __name__ == "__main__":
    main()
