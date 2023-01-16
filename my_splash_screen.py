#  my_splash_screen.py conntains file manipulation scripts associated with master_mandala_maker.py
#         by LeonRHatton

import turtle
import time
import My_template as t
import my_angles as a
# from PIL import Image #module for converting python output to image
import numpy as np
import cv2
import pyautogui
import pyscreenshot
import datetime as datetime
import sys
import os
import audio_clips as au
import shutil
import Timer as tm
import FileScripts as f

turtle.colormode(255)


def splash_screen():
    turtle.colormode(255)
    turtle.bgcolor(10, 15, 15)
    t.my_pen.penup()
    t.my_pen.setposition(-750, 0)
    t.my_pen.color(255, 255, 199)
    t.my_pen.pendown()
    t.my_pen.write( t.my_str, move = 'False', font = ("Garamond ", 18, "bold italic"))
    t.my_pen.penup()
    t.my_pen.setposition(-300, -150)
    t.my_pen.pendown()
    t.my_pen.write(" created by LeonRHatton, music credits by Winston Rhodes and others   " \
                   + tm.my_date, move = 'False', font = ("Garamond ", 14 , "italic"), align = 'center')
    s_image = pyautogui.screenshot()
    s_image = cv2.cvtColor(np.array(s_image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(t.my_str + '_splash' +'.jpeg', s_image)
    time.sleep(4)
    t.my_pen.reset()
    
    
    

def title_screen():
    turtle.colormode(255)
    t.my_pen.penup()
    turtle.bgcolor(0, 0, 0)
    t.my_pen.setposition(-850, 0)
    t.my_pen.color(255, 255, 255)
    t.my_pen.pendown()
    t.my_pen.write( t.my_title, move = 'False', font = ("Garamond ", 16, "bold italic"))
    t.my_pen.penup()
    t.my_pen.setposition(-450, -150)
    t.my_pen.pendown()
    t.my_pen.write("created by LeonRHatton, music credits to Winston Rhodes and others   " \
                   + tm.my_date, font = ("Garamond ", 14 , "italic"))
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(t.my_str + '_title' + '.jpeg', image)
    time.sleep(12)
    t.my_pen.reset()
    
    

def watermark():
        turtle.colormode(255)
        t.my_pen.penup()
        t.my_pen.setpos( -950, -500)
        t.my_pen.color(10, 20, 30)
        t.my_pen.shape("blank")
        t.my_pen.pendown()
        t.my_pen.write( t.my_str + au.my_track, font = ("Garamond", 12 , "italic"))
    



def end_screen():
    turtle.colormode(255)
    t.my_pen.penup()
    turtle.bgcolor(10, 10, 50)
#     t.my_pen.setposition(-200, 0)
    t.my_pen.color(255, 255, 199)
    t.my_pen.pendown()
    t.my_pen.write('End of the Show.', move = 'False', font = ("Garamond ", 40, "bold italic"), align = 'center')
    t.my_pen.penup()
    t.my_pen.setposition(-500, -400)
    t.my_pen.pendown()
    t.my_pen.write('Credits: Graphics by LeonRHatton, Music by Winston W. Rhodes and others,      '   \
                   + tm.my_date, font = ("Garamond ", 20 , "italic"))
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite('End of Show' + '_' + '999' +'.png', image)
    time.sleep(3)
    t.my_pen.reset()


def save_titles():
    for splash in range(9):
        turtle.colormode(255)
        t.my_pen.penup()
        turtle.bgcolor(100, 10, 10)
        t.my_pen.setposition(-450, -350)
        t.my_pen.color(255, 255, 199)
        t.my_pen.pendown()
        t.my_pen.write( t.my_str, font = ("Garamond ", 14, "bold italic"))
        t.my_pen.penup()
        t.my_pen.setposition(-200, -450)
        t.my_pen.pendown()
        t.my_pen.write("by LeonRHatton,    " + tm.my_date, font = ("Garamond ", 10 , "italic"))
        save_thumb()
        time.sleep(5)
    t.my_pen.reset()


def save_screenshot():
     # take screenshot using pyautogui
    image = pyautogui.screenshot()

    # since the pyautogui takes as a
    # PIL(pillow) and in RGB we need to
    # convert it to numpy array and BGR
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)

    # writing it to the disk using opencv
    cv2.imwrite(t.my_str, image)

def take_screenshot():
    # To capture the screen
    image = pyscreenshot.grab()

    # To display the captured screenshot
    image.show()

    # To save the screenshot
    image.save("LeonRHatton.png")
