# CODE FOR ROTATING HEXES_07132020
import turtle
import random

turtle.bgcolor("black")
turtle.hideturtle()

myPen = turtle.Turtle()
myPen.hideturtle()


def pick_color():
    colors = [
        "blue",
        "brown",
        "red",
        "yellow",
        "green",
        "orange",
        "turquoise",
        "pink",
        "goldenrod",
        "olive",
        "lime green",
        "navy",
        "indigo",
        "medium purple",
    ]
    random.shuffle(colors)
    return colors[0]


le = turtle.Turtle()
le.shape("triangle")
le.color(pick_color())
le.shapesize(35)
le.left(60)
le.pensize(5)

te = turtle.Turtle()
te.shape("triangle")
te.color(pick_color())
te.shapesize(35)
te.pensize(5)

be = turtle.Turtle()
be.shape("triangle")
be.color(pick_color())
be.shapesize(30)
be.right(120)
be.pensize(5)

de = turtle.Turtle()
de.shape("triangle")
de.color(pick_color())
de.shapesize(30)
de.pensize(5)
de.right(60)


def rotateMe():
    for i in range(50):
        le.left(i + 144)
        te.left(i + 144)
        be.right(i + 144)
        de.right(i + 144)


rotateMe()

myPen.penup()
myPen.setposition(-75, -390)
myPen.color("grey")
myPen.write("Mandala _Rotating Hexes // DesignnsByLe //", font=("Arial ", 16, "bold"))
turtle.getscreen().getcanvas().postscript(file="Mandala_Rotating Hexes_07172020")
turtle.done()
