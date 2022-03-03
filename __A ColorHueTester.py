import turtle
import time
import os

#My 255 Color tester chart

# Create local variable of turtle
global le
le = turtle.Turtle()
global myPen
myPen = turtle.Turtle()
myPen.shape('blank')

#global my_Str


#Save the result to file
def Make_File():
    pass
def save_to_ps():
    turtle.getscreen().getcanvas().postscript(file = my_Str)  

# Set up Screen
turtle.screensize(100, 100)


r = turtle.numinput('Red', 'Enter number value for Red Hue:', str(122))


g = turtle.numinput('Green', 'Enter number value for Green Hue:', str(133))

b = turtle.numinput('Blue', 'Enter number value for Blue Hue:', str(215))

R = int(r)
G = int(g)
B = int(b)

turtle.colormode(255)

turtle.color(R, G, B)
           


#Create Polygon of the color
turtle.setpos(0,25)
turtle.shapesize(8)
turtle.shape('square')

myPen.penup()
myPen.setposition(-55, -75)
myPen.pendown()
myPen.write(str('R:          G:            B:  '), font = ('Arial', 10, 'bold'))
myPen.penup()
myPen.setposition(-55, -100)
myPen.pendown()
myPen.write(str(R), font = ('Arial', 10, 'bold'))
myPen.penup()
myPen.setpos(0, -100)
myPen.pendown()
myPen.write(str(G), font = ('Arial', 10, 'bold'))
myPen.penup()
myPen.setpos(60, -100)
myPen.pendown()
myPen.write(str(B), font = ('Arial', 10, 'bold'))
            
time.sleep(6)
#save_to_ps()

