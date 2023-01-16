''' A Color Hue Tester for Turtle by Leon Hatton

This is a simple module to test color hues in the Python Turtle Module.
It uses colormode RGB (255 hues), and is totally independent and cross-platform enabled.
Result is output to a file.
'''
import turtle
import time
import pyautogui
import numpy as np
import cv2




# Create local variable of turtle

global my_hue
my_hue = turtle.Turtle()
my_hue.shape('blank')

# Future: set up error handling here

#Future save the result to file
my_path = '/media/elemen/Inland SSD1/Images/ColorHueTests/'
def save_image():
    my_region = 715, 290, 505, 505
    s_image = pyautogui.screenshot(region = my_region)
    s_image = cv2.cvtColor(np.array(s_image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(my_path + 'RGB:  ' + str(R) + ',' + str(G) + ',' + str(B) + ' '  + 'composite hues' +'.png', s_image)
   


# Set up Screen
my_screen = turtle.Turtle()
my_screen.screen.setup(500, 500)
my_screen.screen.screensize(100, 100)
my_screen.screen.title('Color Hue Tester')

#Set up User Interface
r = turtle.numinput('Red', 'Enter number value for Red Hue:', str(122))   #Default is 122
g = turtle.numinput('Green', 'Enter number value for Green Hue:', str(133))  # Default is 133
b = turtle.numinput('Blue', 'Enter number value for Blue Hue:', str(215))  #Default is 215

R = int(r)
G = int(g)
B = int(b)

turtle.colormode(255)

turtle.color(R, G, B)
           


#Create Polygon of the color
turtle.setpos(0,25)
turtle.shapesize(8)
turtle.shape('square')

#Create Frame
my_hue.penup()
my_hue.setposition(-75, -75)
my_hue.pendown()
my_hue.write(str('R:                 G:                  B:  '), font = ('Garamond', 10, 'bold'))

my_hue.penup()
my_hue.setposition(-80, -90)
my_hue.pendown()
my_hue.write(str(R), font = ('Garamond', 10, 'bold'))

my_hue.penup()
my_hue.setpos(-15, -90)
my_hue.pendown()
my_hue.write(str(G), font = ('Garamond', 10, 'bold'))

my_hue.penup()
my_hue.setpos(55, -90)
my_hue.pendown()
my_hue.write(str(B), font = ('Garamond', 10, 'bold'))


my_hue.penup()
my_hue.setpos(-240, 130)
my_hue.pendown()
my_hue.write('This is the composite hue for colors ' + str(R) +', ' + str(G) + ', ' + 'and ' + str(B) + '.', font = ('Garamond', 13, 'bold italic'))

# Save screen to file
save_image()
#Pause
time.sleep(9)
#Exit on mouse click
turtle.exitonclick()