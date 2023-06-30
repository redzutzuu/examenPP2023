import turtle

def deseneaza_triunghi(pen):
    pen.penup()
    pen.goto(-100, -100)
    pen.pendown()
    pen.fillcolor("yellow")
    pen.begin_fill()
    for _ in range(3):
        pen.forward(200)
        pen.left(120)
    pen.end_fill()

def deseneaza_cerc(pen):
    pen.penup()
    pen.goto(100, 0)
    pen.pendown()
    pen.fillcolor("red")
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()

def deseneaza_dreptunghi(pen):
    pen.penup()
    pen.goto(-100, 100)
    pen.pendown()
    pen.fillcolor("blue")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(200)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
    pen.end_fill()

def main():
    # Inițializare
    window = turtle.Screen()
    window.title("Desenare forme geometrice")
    window.bgcolor("white")

    # Crearea unui obiect turtle pentru desenare
    pen = turtle.Turtle()

    deseneaza_triunghi(pen)
    deseneaza_cerc(pen)
    deseneaza_dreptunghi(pen)

    # Ascunderea obiectului turtle
    pen.hideturtle()

    # Închiderea ferestrei la clic
    window.exitonclick()

if __name__ == "__main__":
    main()


# +-------------------------------+
# |           Program             |
# +-------------------------------+
# | - main()                      |
# +-------------------------------+
#
#           / | \
#            |
#            |
#     +--------------+
#     |   Turtle     |
#     +--------------+
#     | - pen        |
#     +--------------+
#     | + __init__() |
#     | + penup()    |
#     | + pendown()  |
#     | + goto()     |
#     | + forward()  |
#     | + circle()   |
#     | + fillcolor()|
#     | + begin_fill()|
#     | + end_fill() |
#     | + hideturtle()|
#     +--------------+
#
#           / | \
#            |
#            |
#     +------------------+
#     |  deseneaza_triunghi() |
#     +------------------+
#     | - pen            |
#     +------------------+
#     | + deseneaza_triunghi() |
#     +------------------+
#
#           / | \
#            |
#            |
#     +------------------+
#     |  deseneaza_cerc() |
#     +------------------+
#     | - pen            |
#     +------------------+
#     | + deseneaza_cerc() |
#     +------------------+
#
#           / | \
#            |
#            |
#     +---------------------+
#     |  deseneaza_dreptunghi() |
#     +---------------------+
#     | - pen               |
#     +---------------------+
#     | + deseneaza_dreptunghi() |
#     +---------------------+