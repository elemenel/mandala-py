#  my_splash_screen.py conntains file manipulation scripts associated with master_mandala_maker.py
#         by LeonRHatton

import turtle
import time
import My_template as t
import my_angles as a
import PIL.ImageGrab

# from PIL import Image #module for converting python output to image
import numpy as np
import cv2

# import pyautogui
import pyscreenshot
import datetime as datetime
import sys
import os
import audio_clips as au
import shutil
import Timer as tm
import FileScripts_feb as f
import My_logger as Lg


turtle.colormode(255)


def splash_screen():
    turtle.colormode(255)
    turtle.bgcolor(30, 0, 10)
    t.my_pen.penup()
    t.my_pen.setposition(-950, 200)
    t.my_pen.color(255, 255, 150)
    t.my_pen.pendown()
    t.my_pen.write(
        (f"Presenting {t.folder_name}"),
        font=("Verdana", 16, "bold italic"),
        align="left",
    )
    t.my_pen.penup()
    t.my_pen.setposition(-800, 100)
    t.my_pen.pendown()
    t.my_pen.write(
        (f"created and produced by LeonRHatton; {tm.my_date}"),
        move="False",
        font=("Verdana", 14, "italic"),
        align="left",
    )
    s_image = PIL.ImageGrab.grab()
    #     s_image = pyautogui.screenshot()
    s_image = cv2.cvtColor(np.array(s_image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(
        f"/home/sels/Pictures/SplashScreens/{t.my_project}_splash.jpeg", s_image
    )
    Lg.logger.info(
        f"Splash Screen for {t.my_project} has been saved to SplashScreen folder"
    )
    time.sleep(6)
    t.my_pen.reset()


def title_screen():
    #     turtle.colormode(255)
    t.my_pen.penup()
    turtle.bgcolor(50, 50, 10)
    t.my_pen.setposition(-850, 0)
    t.my_pen.color(255, 255, 255)
    t.my_pen.pendown()
    t.my_pen.write(
        f"{t.project_title}", move="False", font=("Verdana", 12, "bold italic")
    )
    t.my_pen.penup()
    t.my_pen.setposition(-650, -100)
    t.my_pen.pendown()
    t.my_pen.write(
        "created by LeonRHatton;  " + tm.my_date, font=("Verdana", 10, "italic")
    )
    image = PIL.ImageGrab.grab()
    #     image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(f"{t.project_title}.jpeg", image)
    time.sleep(9)
    t.my_pen.reset()


def watermark():
    #         turtle.colormode(255)
    t.my_pen.penup()
    t.my_pen.setpos(-950, -500)
    t.my_pen.color(10, 20, 30)
    t.my_pen.shape("blank")
    t.my_pen.pendown()
    t.my_pen.write(
        f"{t.project_title} by leonrhatton"
    )  # t.my_str + au.my_track, font = ("Garamond", 12 , "italic"))


def end_screen():
    turtle.colormode(255)
    t.my_pen.penup()
    turtle.bgcolor(10, 10, 50)
    #     t.my_pen.setposition(-200, 0)
    t.my_pen.color(255, 255, 199)
    t.my_pen.pendown()
    t.my_pen.write(
        "End of the Show.",
        move="False",
        font=("Garamond ", 40, "bold italic"),
        align="center",
    )
    t.my_pen.penup()
    t.my_pen.setposition(-500, -400)
    t.my_pen.pendown()
    t.my_pen.write(
        "Credits: Graphics by LeonRHatton, Music by Winston W. Rhodes and others,      "
        + tm.my_date,
        font=("Garamond ", 20, "italic"),
    )
    #     image = pyautogui.screenshot()
    image = PIL.ImageGrab.grab()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("End of Show" + "_" + "999" + ".png", image)
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
        t.my_pen.write(t.my_str, font=("Garamond ", 14, "bold italic"))
        t.my_pen.penup()
        t.my_pen.setposition(-200, -450)
        t.my_pen.pendown()
        t.my_pen.write(
            "by LeonRHatton,    " + tm.my_date, font=("Garamond ", 10, "italic")
        )
        save_thumb()
        time.sleep(5)
    t.my_pen.reset()
