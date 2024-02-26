"""
Copyright(c) 2024  Leon Hatton
# email: elementalsystems1@gmail.com
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.
"""

# I# +++++++++++MODULE  Bountiful Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''2/10/2024: Located at lines 7367 - 7851. Take-off from the popular courage mandala. first attempt at introducing
a working undo() function, to hopefully create a reversed animation at runtime. It would be good to reverse it and run another reverse
at the end. But we shall see how the code will progress...
2/11/2024: After several attempts to adjust the existing code, I have decided to create a "Simple MandalaMaker" that would
contain all code in a single module. It may well run faster. I also want to build in flexibility and run-time options.
'''
# Import modules
import turtle
import time
import sys
import os
import psutil
import shutil
import gc
from timeit import default_timer as timer
import random
import math
import numpy as np  # Processes the video
import cv2  # For screenshots
from select import select
import datetime
import logging
import My_logger as Lg
import subprocess as sp
from PIL import Image  # module for converting python output to image
import PIL.ImageGrab
import pyscreenshot
import datetime as datetime
# from shutil import copytree
import pathlib
# from pathlib import Path
import moviepy.editor as mp
from natsort import humansorted as hs
import glob
import imageio
from moviepy.editor import AudioFileClip, ImageClip, VideoFileClip, CompositeAudioClip
import pydub
from turtle import Screen as sc
from functools import lru_cache
from pathlib import Path
from moviepy.video.io.VideoFileClip import VideoFileClip
from dirsync import sync











# Set Environment
# Set up Logger
def startup_script():  # Starts module clock, sets up turtle functions, starts log file
    global module_start_time, count_limit, start, end, start_time
    Lg.logger.info(
        "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    )
    Lg.logger.info(
        "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    )
    # Start time
    module_start_time = timer()
    start_time = datetime.datetime.now()
    Lg.logger.info(
        f"StartupScript:{my_script}:Setting up module environment @ {start_time}"
    )
    t.my_venv()
    make_p_turtles()
    initialize_random_hue_pens()
    gc.enable()
    t.set_up_my_pen()
    Lg.logger.info(
        f"{my_script}:Starting to delete screenshots of {my_script} @ {Tm.this_time}...."
    )  # Thumbs are not necesssary after the video is created from them
#     f.clear_thumbs()  # Deletes all screenshot pngs
    count_limit = int(765)


#     start = f'{Tm.datetime.datetime.fromtimestamp(datetime)}'
#     end = f'{Tm.datetime.datetime.fromtimestamp(datetime)}'
# startup_script()

my_mandala_pics_path = "/home/sels/Pictures/Mandalas/Flower of Life Pics/"
my_pic_name = "Animated Flower Of Life"
Lg.my_project = my_pic_name
Lg.logger.info(f"Starting {Lg.my_project}")










# Select Angle
def get_my_multiples():
    global my_multiples, my_multiples_number, max_value, my_multiples_key
    my_multiples_number = 3278
    my_multiples_key = my_multiples_number * 4
    max_value = my_multiples_number * 3
    my_multiples = [
        my_number
        for my_number in np.arange(
            int(my_multiples_number), my_multiples_key, max_value
        )
        if my_multiples_number % (180) != 0 
    ] + [400, 1000, 1600, 2200]
# get_my_multiples()


# Automated Angle Generator using numpy.arange module; produces a list of angles based on custom algorithms.
#
def pick_angles():
    global i_angle_auto, i_angle_float
    get_my_multiples()
    angle_min = float(my_multiples_number)  # 51.42857
    angle_max = max_value
    key = my_multiples_key  # Dividing angle_min by 2 and using that as a key results in a harmonic angle family; also multiply by 3 or 5

    i_angle_float = [
            angle  for angle in np.arange(float(angle_min), float(angle_max), float(key))
            if angle % (180) != 0
            ]   # +  [4000, 22000] 

    i_angle_auto = [
            angle
            for angle in np.arange(
                int(float(angle_min)), int(float(angle_max)), int(float(key))
                )
            if angle % (180) != 0
            ]
    return i_angle_auto, i_angle_float

#pick_angles()

# This creates  png and jpg files of the final image, to be saved out to the Pictures/Mandalas folder. Master MandalaMaker uses this.
def  save_screenshot():
    image = PIL.ImageGrab.grab()
    #     image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(f"{my_mandala_pics_path}{my_pic_name}-{my_key}.png", image)
    cv2.imwrite(f"{my_mandala_pics_path}{my_pic_name}-{my_key}.jpeg", image)




























def Bountiful_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, count_limit
    my_script = "Bountiful Mandala"
    startup_script()
    make_folder _runtime()
    t.my_angles, t.my_splash = str_angles, f"{my_project} with {au.my_track}"
    for a.i in range(len(a.i_angle_float)):
        my_angle = a.i_angle_float[a.i]
        t.my_angle = my_angle
        Tm.set_time()
        Lg.logger.info(
            f"{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}"
        )
        f.make_reverse_png_folder_runtime()
        t.my_title = f"{my_script}: {my_angle} Degrees Angle and {au.my_track}"
        turtle.title(t.my_title)
        make_p_turtles()
        my_hue = random.randint(5, 100)
        my_hue_a = random.randint(100, 200)
        Lg.logger.info("The value of my_hue is" + "   " + str(my_hue))
        Lg.logger.info("The value of my_hue_a is" + "   " + str(my_hue_a))
        count = 0
        count_limit = 50 # 510  # Best with multiples of 255
        fd_01, fd_02, fd_03, fd_04 = 1.2, 1.2, 1.2, 1.2
        circ_01, circ_02, circ_03 = 18, 24, 32
        bk_01 = 6
        Lg.logger.info(f"{my_script}:First pass starting @ {Tm.my_date_time}")
        for count in range(
            count_limit
        ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)
            pick_blue()  # Blue pen
            R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
            if count <= 0.75 * count:
                blue_hue_pen.color(D + count % 75, E, F - count % 75)
            else:
                pick_blue()
            turtle.setundobuffer(36)    
            pa.pencolor(M, L - count % 255, E)
            pb.pencolor(R, G - count % 255, count % 255)
            pb.left(my_angle)
            blue_hue_pen.left(my_angle)
            pa.left(-my_angle)
            pb.fd(count / fd_01)
           save_screenshot()
            blue_hue_pen.fd(count + phi)
            save_screenshot()
            pa.fd(count / fd_02)
            save_screenshot()
            pb.rt(my_angle)
            blue_hue_pen.left(-my_angle)
            pa.rt(my_angle)
            blue_hue_pen.fd(count / fd_03)
            save_screenshot()
            pa.fd(count / fd_04)
            save_screenshot()
            pb.circle(count / circ_01, my_angle, 3)
            save_screenshot()
            blue_hue_pen.circle(count / circ_02, my_angle)
            save_screenshot()
            pa.circle(count / circ_03, my_angle)
            save_screenshot()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            save_screenshot()
            pb.pendown()
            pb.pencolor(255, 255, count % 255)
            pb.dot(count / 36)
            save_screenshot()
            blue_hue_pen.pensize(count / 145)
            pb.pensize(count / 150)
            pa.pensize(count / 72)
            process_thumbs_runtime()
        clear_blue_hue_pen()
        clear_pa_pen()
        clear_pb_pen()
        produce_reversing_video_runtime()
#         count = 0
#         Lg.logger.info(f"{my_script}:Second pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_magenta()  # Magenta pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 magenta_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_magenta()
#             pa.pencolor(L - count % 255, M, E)
#             pb.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             magenta_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             magenta_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             magenta_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             magenta_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             magenta_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             magenta_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_magenta_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Third pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_green()  # Green pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 green_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_green()
#             pa.pencolor(E, M, L - count % 255)
#             pb.pencolor(G - count % 255, R, count % 255)
#             pb.left(my_angle)
#             green_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             green_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             green_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             green_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             green_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             green_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_green_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Fourth pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_gold()  # Gold pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 gold_hue_pen.color(F - count % 255, E, count % 255)
#             else:
#                 pick_gold()
#             pa.pencolor(L - count % 255, M, E)
#             pb.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             gold_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             gold_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             gold_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             gold_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             gold_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             gold_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_gold_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Fifth pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_indigo()  # Indigo  pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 indigo_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_indigo()
#             pa.pencolor(G - count % 255, count % 255, R)
#             pb.pencolor(L - count % 255, M, E)
#             pb.left(my_angle)
#             indigo_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             indigo_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             indigo_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             indigo_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             indigo_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             indigo_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_indigo_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Sixth pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)  # .bg_fade_skyblue_to_dark()
#             pick_red()  # Red pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 red_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_red()
#             pa.pencolor(E, M, count % 255)
#             pb.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             red_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             red_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             red_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             red_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             red_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             red_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_red_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Seventh pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_orange()  # Orange pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 orange_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_orange()
#             pa.pencolor(L - count % 255, M, E)
#             pb.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             orange_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             orange_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             orange_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             orange_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             orange_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             orange_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_orange_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Eighth pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)  # .bg_fade_skyblue_to_dark()
#             pick_yellow()  # Yellow pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 yellow_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_yellow()
#             pb.pencolor(L - count % 255, M, E)
#             pa.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             yellow_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             yellow_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             yellow_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             yellow_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             yellow_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             yellow_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_yellow_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Ninth pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_light()  # Light pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 light_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_light()
#             pa.pencolor(L - count % 255, M, E)
#             pb.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             light_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             light_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             light_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             light_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             light_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             light_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_light_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
    produce_reversing_video()
    finalize()


# Bountiful_mandala()



























# +++++++++++MODULE  Bountiful Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''2/10/2024: Located at lines 7367 - 7851. Take-off from the popular courage mandala. first attempt at introducing
a working undo() function, to hopefully create a reversed animation at runtime. It would be good to reverse it and run another reverse
at the end. But we shall see how the code will progress...
'''
def Bountiful_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, count_limit
    my_script = "Bountiful Mandala"
    startup_script()
    make_folder _runtime()
    t.my_angles, t.my_splash = str_angles, f"{my_project} with {au.my_track}"
    for a.i in range(len(a.i_angle_float)):
        my_angle = a.i_angle_float[a.i]
        t.my_angle = my_angle
        Tm.set_time()
        Lg.logger.info(
            f"{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}"
        )
        f.make_reverse_png_folder_runtime()
        t.my_title = f"{my_script}: {my_angle} Degrees Angle and {au.my_track}"
        turtle.title(t.my_title)
        make_p_turtles()
        my_hue = random.randint(5, 100)
        my_hue_a = random.randint(100, 200)
        Lg.logger.info("The value of my_hue is" + "   " + str(my_hue))
        Lg.logger.info("The value of my_hue_a is" + "   " + str(my_hue_a))
        count = 0
        count_limit = 50 # 510  # Best with multiples of 255
        fd_01, fd_02, fd_03, fd_04 = 1.2, 1.2, 1.2, 1.2
        circ_01, circ_02, circ_03 = 18, 24, 32
        bk_01 = 6
        Lg.logger.info(f"{my_script}:First pass starting @ {Tm.my_date_time}")
        for count in range(
            count_limit
        ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)
            pick_blue()  # Blue pen
            R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
            if count <= 0.75 * count:
                blue_hue_pen.color(D + count % 75, E, F - count % 75)
            else:
                pick_blue()
            turtle.setundobuffer(36)    
            pa.pencolor(M, L - count % 255, E)
            pb.pencolor(R, G - count % 255, count % 255)
            pb.left(my_angle)
            blue_hue_pen.left(my_angle)
            pa.left(-my_angle)
            pb.fd(count / fd_01)
            save_screenshot()
            blue_hue_pen.fd(count + phi)
            save_screenshot()
            pa.fd(count / fd_02)
            save_screenshot()
            pb.rt(my_angle)
            blue_hue_pen.left(-my_angle)
            pa.rt(my_angle)
            blue_hue_pen.fd(count / fd_03)
            save_screenshot()
            pa.fd(count / fd_04)
            save_screenshot()
            pb.circle(count / circ_01, my_angle, 3)
            save_screenshot()
            blue_hue_pen.circle(count / circ_02, my_angle)
            save_screenshot()
            pa.circle(count / circ_03, my_angle)
            save_screenshot()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            save_screenshot()
            pb.pendown()
            pb.pencolor(255, 255, count % 255)
            pb.dot(count / 36)
            save_screenshot()
            blue_hue_pen.pensize(count / 145)
            pb.pensize(count / 150)
            pa.pensize(count / 72)
            process_thumbs_runtime()
        clear_blue_hue_pen()
        clear_pa_pen()
        clear_pb_pen()
        produce_reversing_video_runtime()
#         count = 0
#         Lg.logger.info(f"{my_script}:Second pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_magenta()  # Magenta pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 magenta_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_magenta()
#             pa.pencolor(L - count % 255, M, E)
#             pb.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             magenta_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             magenta_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             magenta_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             magenta_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             magenta_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             magenta_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_magenta_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Third pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_green()  # Green pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 green_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_green()
#             pa.pencolor(E, M, L - count % 255)
#             pb.pencolor(G - count % 255, R, count % 255)
#             pb.left(my_angle)
#             green_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             green_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             green_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             green_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             green_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             green_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_green_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Fourth pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_gold()  # Gold pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 gold_hue_pen.color(F - count % 255, E, count % 255)
#             else:
#                 pick_gold()
#             pa.pencolor(L - count % 255, M, E)
#             pb.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             gold_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             gold_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             gold_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             gold_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             gold_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             gold_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_gold_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Fifth pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_indigo()  # Indigo  pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 indigo_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_indigo()
#             pa.pencolor(G - count % 255, count % 255, R)
#             pb.pencolor(L - count % 255, M, E)
#             pb.left(my_angle)
#             indigo_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             indigo_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             indigo_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             indigo_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             indigo_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             indigo_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_indigo_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Sixth pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)  # .bg_fade_skyblue_to_dark()
#             pick_red()  # Red pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 red_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_red()
#             pa.pencolor(E, M, count % 255)
#             pb.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             red_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             red_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             red_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             red_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             red_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             red_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_red_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Seventh pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_orange()  # Orange pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 orange_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_orange()
#             pa.pencolor(L - count % 255, M, E)
#             pb.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             orange_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             orange_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             orange_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             orange_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             orange_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             orange_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_orange_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Eighth pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)  # .bg_fade_skyblue_to_dark()
#             pick_yellow()  # Yellow pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 yellow_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_yellow()
#             pb.pencolor(L - count % 255, M, E)
#             pa.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             yellow_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             yellow_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             yellow_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             yellow_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             yellow_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             yellow_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_yellow_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
#         count = 0
#         Lg.logger.info(f"{my_script}:Ninth pass starting @ {Tm.my_date_time}")
#         for count in range(
#             count_limit
#         ):  # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
#             turtle.bgcolor(0, 0, 0)
#             pick_light()  # Light pen
#             R, G, B, L, M, N, D, E, F = my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255
#             if count <= 0.75 * count:
#                 light_hue_pen.color(F - count % 255, E, D + count % 255)
#             else:
#                 pick_light()
#             pa.pencolor(L - count % 255, M, E)
#             pb.pencolor(G - count % 255, count % 255, R)
#             pb.left(my_angle)
#             light_hue_pen.left(my_angle)
#             pa.left(-my_angle)
#             pb.fd(count / fd_01)
#             save_screenshot()
#             light_hue_pen.fd(count + phi)
#             save_screenshot()
#             pa.fd(count / fd_02)
#             save_screenshot()
#             pb.rt(my_angle)
#             light_hue_pen.left(-my_angle)
#             pa.rt(my_angle)
#             light_hue_pen.fd(count / fd_03)
#             save_screenshot()
#             pa.fd(count / fd_04)
#             save_screenshot()
#             pb.circle(count / circ_01, my_angle, 3)
#             save_screenshot()
#             light_hue_pen.circle(count / circ_02, my_angle)
#             save_screenshot()
#             pa.circle(count / circ_03, my_angle)
#             save_screenshot()
#             pb.penup()
#             pb.left(my_angle)
#             pb.backward(count / bk_01)
#             save_screenshot()
#             pb.pendown()
#             pb.pencolor(255, 255, 10)
#             pb.dot(count / 36)
#             save_screenshot()
#             light_hue_pen.pensize(count / 145)
#             pb.pensize(count / 150)
#             pa.pensize(count / 72)
#             process_thumbs()
#         clear_light_hue_pen()
#         clear_pa_pen()
#         clear_pb_pen()
    produce_reversing_video()
    finalize()


# Bountiful_mandala()
