'''
Copyright (C) 2017 - 2023  Leon R. Hatton
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

MASTER MANDALA MAKER (master_mandala_maker_production.py);
    developer:
    Leon Hatton, elementalsystems1@gmail.com
    Primary Python IDE is Thonny, currently version 4.0.1 on Python 3.10(Ubuntu Studio(ubuntucinnamon); and Python 3.11(Windows 11) .

    Default  platform is Linux. Formerly (May 2022-May 2023) using Kubuntu, which I think
    was a good balance between performance and ease of use. As of May 2023, switched to Linux Mint. See comments
    below why I switched.
    
    Hardware: HP EliteDesk 800 G1, SFF. Includes OEM 320w Power Supply, 4x Intel Core i5-4570CPU @3.20 GHz
    Memory: 28 GB RAM; OEM integrated Mesa Intel HD Graphics 4600; In May 2023,
    upgraded to PowerColor AMD Radeon RX 550 Red Dragon Low Profile Single Fan 4GB GDDR5 PCIe 3.0 Graphics Card

    Modules are imported either from the standard python package or from PyPy through Thonny packages management, and include
    the following: Turtle, MoviePy, PyAutogui, Pyscreenshot, PyDub, NatSort, Numpy, Random, OpenCV-Python, Timer, OS,  Sys, Logging,  gc, 
    DirSync, Pillow, Shutil, PathLib, Glob, Imageio, Functools, Math, Mutagen.
    
    All screenshot apps, including PyautoGui and Pyscreenshot running on Linux need Scrot, which is installed
    from the 'apt' repository (Ubuntu). To run, Scrot requires support from the desktop manager. Wayland, which
    Ubuntu adopted in 2019, has no support for Scrot. Only the legacy X11 desktop display manager used by Linux Mint
    continues to provide functionality for Scrot. This is one of the reasons that I chose Linux Mint as my os of choice and
    necessity.
    
    However, as of August 4, 2023, I have switched from using Linux Mint Cinnamon to trying out Zorin OS.
    I am finding that although Linux Mint is wondeful, Zorin OS is more up-to-date because it provides access to Snap, Flatpack, Apt,
    and Windows apps through Play on Linux and Wine. It also uses X11 desktop display.
    
    As of August 7, 2023, I am switching back to Linux mint, mainly because Kate and some other apps were apparently confused, and confused me, too. Which
    source did it come from: Flatpak, Snap, or Apt? For Linux Mint, the answer is simple: it's from apt, an has no issue initializing.
    
    As of August 12, 2023: Due to severe system drag, I have installed and configured the system to run the ubuntucinnamon "flavor" which has the option to
    select and install components of Ubuntu Studio. With Ubuntu Studio and Cinnamon I think I have achieved a capable and powerful system and
    an eye-pleasing one too. Testing is next of course, but so far, so good. The code is running well.
    
    On 8/19/2023: I received a new 1TB SSD from Temu.com and have installed ubuntucinnamon and ubuntu studio on it. currently setting up Thonny to run on it.
    again, so far, so good...looking for much faster code execution since I am moving from the slower 4.0 GB HDD to the nimble 1.0 TB SDD.
    
    December 21, 2023: After using Ubuntu Studio for a few months, I found it was a bit of overkill for the use that I need. I don't require a full-fledged studio
    to perform the tasks that I need. So, I thought to try out Linux Mint again. But, to my dismay, after installing Linux Mint, the grub boot went down.
    I could not boot anything! After a couple of days and a lot of research, I was able to restore the system by replacing Ubuntu Studio with Mint,
    while retaining all of my critical files. I did not lose anything, but I realized how important a reliable backup is. So, I have implemented a more robust
    and redundant backup, that is being run from within the python modules. The files are being backed up to multiple locations. But I need to resolve the
    automated backup to Git.
    
    I am also taking another look at Zorin OS, too. Trying to keep things simple. I have a tendency to push too far with most things, testing the limits.
    
    
    In addition to the above-listed imported modules from Pypy,
    the the author has developed and is actively maintaining the following custom Python modules, all of which coordinate the
    creation of the mandalas:
        1. master_mandala_maker.py; code repository for the various mandalas, and runs code for the animations.
        2. my_angles.py; processes angle selections to be called by master_mandala_maker.py
        3. my_hues.py; repository for custom color hues
        4. my_splash_screen.py; provides the title screen, the splash screen, end screen, and the watermark. 
        5  File_scripts.py; repository for file manipulations, creations, deletions, sorting, video processing
        6. audio_clips.py; repository of links to audio tracks on the local server and filters audio clips by duration
        7. Timer.py; provides time/date functionality
        8. _A ColorHueTester.py; the only independent module. It outputs a given hue, based on RGB color hue format.
            Screenshot of image is saved to a file.
        9. My_logger.py; provides both file and streaming logger functionality, and replaces more limited print() function.
        10. My_template.py, which sets up the initial environment and is the central repository for global variables.

        Maintained at Git Repository (Currently Private).
        Link: https://github.com/elemenel/mandala-py
'''
import turtle
import time
import sys
import os
from timeit import default_timer as timer
import random
import math
# import pyautogui # For screenshot
import numpy as np # Processes the video
import cv2 # For screenshots
from select import select
import datetime
import My_template as t
import my_angles as a  #Processes angle selections714 Hz
# import my_hues as h # Defines turtle pen names; Aids in color selections
import my_splash_screen as s
import Timer as Tm
import FileScripts as f  # Processes file manipulations
import audio_clips as au # Processes the audio tracks
import logging
import My_logger as Lg
import subprocess as sp
import psutil
import gc


if sys.platform.startswith('linux'):
    my_path = '/home/sels/Modules/'
else:
    my_path = 'D:/'

global my_project, my_angle, my_title, my_script, str_angles, my_range, count, pa, pb, my_pensize, L, R, G, B, M, my_length,my_pensize_a, my_length_bk,  my_random, my_circle, my_script
global file_key, my_key, start, end, count, my_project, logger, formatter, fileHandler, consoleHandler, my_angle, folder_name, turtle


turtle.setup(1950, 1070)  # This is the default screen size. Choose any size.
turtle.title('The Novanno Healing Mandalas by LeonRHatton') # Placeholder. Is unique to each mandala maker
turtle.shape('blank')
turtle.hideturtle()
turtle.mode('standard') #standard
turtle.colormode(255)
turtle.pensize(2)
R = 255
G = 255
B = 255
turtle.bgcolor(R,G,B)

global pi
pi = 4 * math.atan(1)

global phi
phi = ( 1 + math.sqrt(5) ) / 2

global start_time, end_time

file_key = random.randrange(100,90000,1)
my_key = ' -r.' + str(file_key)

my_project = str('The Novanno Project')

folder_name = 'Novanno_Folder'

#Logger set up
logger = Lg.logging.getLogger(t.my_project) # Initialize global logger
fileHandler = Lg.logging.FileHandler(t.my_logfile)
fileHandler.setLevel(Lg.logging.INFO)
consoleHandler = Lg.logging.StreamHandler()
consoleHandler.setLevel(Lg.logging.INFO)
logger.setLevel(Lg.logging.INFO)
logger.addHandler(Lg.fileHandler)
logger.addHandler(Lg.consoleHandler)
Lg.logger.info('Logger Source: MandalaMaker')


def make_turtle_black_dot_pen():
    global Q_seed
    Q_seed = turtle.Turtle()
    Q_seed.color(0,0,0)
    Q_seed.pensize(3)
    Q_seed.shape('blank')
    Q_seed.speed(0)
   
    
def make_turtle_pa():
    global pa
    pa = turtle.Turtle()
    pa.speed(0)
    pa.shape('blank')
    pa.pensize(1)
    pa.penup()
    pa.setpos(0,0)
    pa.pendown()
    
def make_turtle_pb():
    global pb
    pb = turtle.Turtle()
    pb.speed(0)
    pb.shape('blank')
    pb.pensize(1)
    pb.penup()
    pb.setpos(0,0)
    pb.pendown()
    
def make_turtle_pc():
    global pc
    pc = turtle.Turtle()
    pc.speed(0)
    pc.shape('blank')
    pc.pensize(1)
    pc.penup()
    pc.setpos(0,0)
    pc.pendown()
    
    
def make_turtle_pd():
    global pd
    pd = turtle.Turtle()
    pd.speed(0)
    pd.shape('blank')
    pd.pensize(1)
    pd.penup()
    pd.setpos(0,0)
    pd.pendown()
    
def make_turtle_pe():
    global pe
    pe = turtle.Turtle()
    pe.speed(0)
    pe.shape('blank')
    pe.pensize(1)
    pe.penup()
    pe.setpos(0,0)
    pe.pendown()
    
def make_turtle_pf():
    global pf
    pf = turtle.Turtle()
    pf.speed(0)
    pf.shape('blank')
    pf.pensize(1)
    pf.penup()
    pf.setpos(0,0)
    pf.pendown()
    
def make_turtle_pg():
    global pg
    pg= turtle.Turtle()
    pg.speed(0)
    pg.shape('blank')
    pg.pensize(1)
    pg.penup()
    pg.setpos(0,0)
    pg.pendown()
    
def make_turtle_ph():
    global ph
    ph= turtle.Turtle()
    ph.speed(0)
    ph.shape('blank')
    ph.pensize(1)
    ph.penup()
    ph.setpos(0,0)
    ph.pendown()           
    
def make_p_turtles():
    make_turtle_pa()
    make_turtle_pb()
    make_turtle_pc()
    make_turtle_pd()
    make_turtle_pe()
    make_turtle_pf()
    make_turtle_pg()
    make_turtle_ph()
    make_turtle_black_dot_pen()
    


def clear_pa_pen():
    pa.reset()
    make_turtle_pa()
      
def clear_pb_pen():    
    pb.reset()
    make_turtle_pb()
 
def clear_pc_pen():
    pc.reset()
    make_turtle_pc()

def clear_pd_pen():
    pd.reset()
    make_turtle_pd()

def clear_pe_pen():
    pe.reset()
    make_turtle_pe()

def clear_pf_pen():
    pf.reset()
    make_turtle_pf()

def clear_pg_pen():
    pg.reset()
    make_turtle_pg()

def clear_ph_pen():
    ph.reset()
    make_turtle_ph()

def clear_Q_seed_pen():
    Q_seed.reset()
    Q_seed.penup()
    Q_seed.setpos(0,0)
    Q_seed.speed(0)
    Q_seed.pendown()
    gc.collect()
    make_turtle_black_dot_pen()

def clear_p_pens():
    clear_pa_pen()
    clear_pb_pen()
    clear_pc_pen()
    clear_pd_pen()
    clear_pe_pen()
    clear_pf_pen()
    clear_pg_pen()
    clear_ph_pen()
    clear_Q_seed_pen()
    gc.collect()
    make_p_turtles()



#Color Hue Mixer
'''Create Random Hue Mix Pens'''

def make_yellow_hue_pen():
    global yellow_hue_pen
    yellow_hue_pen= turtle.Turtle()
    yellow_hue_pen.speed(0)
    yellow_hue_pen.shape('blank')
    yellow_hue_pen.pensize(1)
    yellow_hue_pen.setpos(0,0)     

def make_orange_hue_pen():
    global orange_hue_pen
    orange_hue_pen= turtle.Turtle()
    orange_hue_pen.speed(0)
    orange_hue_pen.shape('blank')
    orange_hue_pen.pensize(1)
    orange_hue_pen.setpos(0,0)

def make_red_hue_pen():
    global red_hue_pen
    red_hue_pen= turtle.Turtle()
    red_hue_pen.speed(0)
    red_hue_pen.shape('blank')
    red_hue_pen.pensize(1)
    red_hue_pen.setpos(0,0)
    
    
def make_blue_hue_pen():
    global blue_hue_pen
    blue_hue_pen= turtle.Turtle()
    blue_hue_pen.speed(0)
    blue_hue_pen.shape('blank')
    blue_hue_pen.pensize(1)
    blue_hue_pen.setpos(0,0)    
    
def make_green_hue_pen():
    global green_hue_pen
    green_hue_pen= turtle.Turtle()
    green_hue_pen.speed(0)
    green_hue_pen.shape('blank')
    green_hue_pen.pensize(1)
    green_hue_pen.setpos(0,0)


def make_indigo_hue_pen():
    global indigo_hue_pen
    indigo_hue_pen= turtle.Turtle()
    indigo_hue_pen.speed(0)
    indigo_hue_pen.shape('blank')
    indigo_hue_pen.pensize(1)
    indigo_hue_pen.setpos(0,0)


def make_magenta_hue_pen():
    global magenta_hue_pen
    magenta_hue_pen= turtle.Turtle()
    magenta_hue_pen.speed(0)
    magenta_hue_pen.shape('blank')
    magenta_hue_pen.pensize(1)
    magenta_hue_pen.setpos(0,0)


def make_gold_hue_pen():
    global gold_hue_pen
    gold_hue_pen= turtle.Turtle()
    gold_hue_pen.speed(0)
    gold_hue_pen.shape('blank')
    gold_hue_pen.pensize(1)
    gold_hue_pen.setpos(0,0)


def make_dark_hue_pen():
    global dark_hue_pen
    dark_hue_pen= turtle.Turtle()
    dark_hue_pen.speed(0)
    dark_hue_pen.shape('blank')
    dark_hue_pen.pensize(1)
    dark_hue_pen.setpos(0,0)


def make_light_hue_pen():
    global light_hue_pen
    light_hue_pen= turtle.Turtle()
    light_hue_pen.speed(0)
    light_hue_pen.shape('blank')
    light_hue_pen.pensize(1)
    light_hue_pen.setpos(0,0)



def make_random_hue_pen():
    global random_hue_pen
    random_hue_pen= turtle.Turtle()
    random_hue_pen.speed(0)
    random_hue_pen.shape('blank')
    random_hue_pen.pensize(1)
    random_hue_pen.setpos(0,0)



def make_cyan_hue_pen():
    global cyan_hue_pen
    cyan_hue_pen= turtle.Turtle()
    cyan_hue_pen.speed(0)
    cyan_hue_pen.shape('blank')
    cyan_hue_pen.pensize(1)
    cyan_hue_pen.setpos(0,0)


def clear_blue_hue_pen():
    blue_hue_pen.reset()
    make_blue_hue_pen()

def clear_red_hue_pen():
    red_hue_pen.reset()
    make_red_hue_pen()

def clear_gold_hue_pen():
    gold_hue_pen.reset()
    make_gold_hue_pen()

def clear_yellow_hue_pen():
    yellow_hue_pen.reset()
    make_yellow_hue_pen()
    
def clear_indigo_hue_pen():
    indigo_hue_pen.reset()
    make_indigo_hue_pen()    
    
def clear_green_hue_pen():
    green_hue_pen.reset()
    make_green_hue_pen()    
    
def clear_light_hue_pen():
    light_hue_pen.reset()
    make_light_hue_pen()    
    
def clear_dark_hue_pen():
    dark_hue_pen.reset()
    make_dark_hue_pen()    

def clear_magenta_hue_pen():
    magenta_hue_pen.reset()
    make_magenta_hue_pen()
    
def clear_random_hue_pen():
    random_hue_pen.reset()
    make_random_hue_pen()
    
def clear_orange_hue_pen():
    orange_hue_pen.reset()
    make_orange_hue_pen()
    
def clear_cyan_hue_pen():
    cyan_hue_pen.reset()
    make_cyan_hue_pen()    

'''Create the random hue pens(12)'''
def initialize_random_hue_pens():
    make_blue_hue_pen()
    make_red_hue_pen()
    make_gold_hue_pen()
    make_yellow_hue_pen()
    make_indigo_hue_pen()
    make_green_hue_pen()
    make_light_hue_pen()
    make_dark_hue_pen()
    make_magenta_hue_pen()
    make_random_hue_pen()
    make_cyan_hue_pen()
    make_orange_hue_pen()
    

#random yellow hues
def pick_yellow(): #yellow_hue_pen
    r = random.randrange(220, 255, 1)
    g = random.randrange(225, 255, 1)
    b = random.randrange(0, 10, 1)
    I = r
    J = g
    K= b
    yellow_hue_pen.pencolor(I, J, K)
    return yellow_hue_pen
#     print('The pick yellow pen is yellow_hue_pen')

#random orange hues
def pick_orange(): #orange_hue_pen
    r = random.randrange(242, 255, 1)
    g = random.randrange(112, 180, 1)
    b = random.randrange(37, 47, 1)
    Q= r
    L = g
    N= b
    orange_hue_pen.pencolor(Q, L, N)
    return orange_hue_pen
#     print('The pick orange pen is orange_hue_pen')


#random red hues
def pick_red(): #red_hue_pen
    r = random.randrange(200, 255, 1)
    g = random.randrange(0, 80, 1)
    b = random.randrange(25, 50, 1)
    R = r
    G = g
    B = b
    red_hue_pen.pencolor(R, G, B)
    return red_hue_pen
#     print('The pick_red pen is red_hue_pen')


#random blue hues
def pick_blue():  # blue_hue_pen
    r = random.randrange(9, 54, 1)
    g = random.randrange(6, 72, 1)
    b = random.randrange(200, 255, 1)
    L = r
    M = g
    N = b
    blue_hue_pen.pencolor(L, M, N)
    return blue_hue_pen
#     print('The pick_blue pen is blue_hue_pen')



#random green hues
def pick_green(): # green_hue_pen
    r = random.randrange(9, 50, 1)
    g = random.randrange(200, 255, 1)
    b = random.randrange(6, 72, 1)
    O = r
    P = g
    Q = b
    green_hue_pen.pencolor(O, P, Q)
    return green_hue_pen
#     print('The pick_green pen is green_hue_pen')




#random indigo hues
def pick_indigo(): # indigo_hue_pen
    r = random.randrange(25, 75, 1)
    g = random.randrange(0, 5, 1)
    b = random.randrange(75, 150, 1)
    S = r
    T = g
    U = b
    indigo_hue_pen.pencolor(S, T, U)
    return indigo_hue_pen
#     print('The pick_indigo pen is indigo_hue_pen')



#random magenta hues
def pick_magenta(): # magenta_hue_pen
    r = random.randrange(125, 175, 1)
    g = random.randrange(0, 5, 1)
    b = random.randrange(75, 150, 1)
    I = r
    J = g
    K = b
    magenta_hue_pen.pencolor(I, J, K)
    return magenta_hue_pen
#     print('The pick_magenta pen is magenta_hue_pen')

#random gold hues
def pick_gold(): # Pen gold_hue_pen
    r = random.randrange(225, 254,1)
    g = random.randrange(175, 220,1)
    b = random.randrange(10, 50,1)
    V = r
    W = g
    X = b
    gold_hue_pen.pencolor(V, W, X)
    return gold_hue_pen
#     print('The pick_gold pen is gold_hue_pen')



#random dark hues
def pick_dark(): # dark_hue_pen
    r = random.randrange(0, 100, 1)
    g = random.randrange(0, 25, 1)
    b = random.randrange(0, 50, 1)
    X = r
    Y = g
    Z = b
    dark_hue_pen.pencolor(X, Y, Z)
    return dark_hue_pen
#     print('The pick_dark pen is dark_hue_pen')



#random light hues
def pick_light(): # light_hue_pen
    r = random.randrange(190, 215, 1)
    g = random.randrange(191, 254, 1)
    b = random.randrange(200, 253, 1)
    Q = r
    M = g
    U = b
    light_hue_pen.pencolor(Q, M, U)
    return light_hue_pen
#     print('The pick_light pen is light_hue_pen')


#random hues
def pick_random():  #random_hue_pen
    r = random.randrange(50, 255, 1)
    g = random.randrange(50, 255, 1)
    b = random.randrange(50, 255, 1)
    D = r
    E = g
    F = b
    random_hue_pen.pencolor(D, E, F)
    return random_hue_pen
#     print('The pick_random pen is random_hue_pen')

def pick_cyan(): # cyan_hue_pen
    r = random.randrange(10, 50, 1)
    g = random.randrange(180, 255, 1)
    b = random.randrange(200, 255, 1)
    D = r
    E = g
    F = b
    cyan_hue_pen.pencolor(D, E, F)
    return cyan_hue_pen
#     print('The pick_cyan pen is cyan_hue_pen')


    

def reset_random_hue_pens():
    yellow_hue_pen.reset()
    make_yellow_hue_pen()
    yellow_hue_pen.penup()
    yellow_hue_pen.setpos(0,0)
    yellow_hue_pen.pendown()
    
    red_hue_pen.reset()
    make_red_hue_pen()
    red_hue_pen.penup()
    red_hue_pen.setpos(0,0)
    red_hue_pen.pendown()
    
    orange_hue_pen.reset()
    make_orange_hue_pen()
    yellow_hue_pen.penup()
    yellow_hue_pen.setpos(0,0)
    yellow_hue_pen.pendown()
    
    dark_hue_pen.reset()
    make_dark_hue_pen()
    dark_hue_pen.penup()
    dark_hue_pen.setpos(0,0)
    dark_hue_pen.pendown()
    
    indigo_hue_pen.reset()
    make_indigo_hue_pen()
    indigo_hue_pen.penup()
    indigo_hue_pen.setpos(0,0)
    indigo_hue_pen.pendown()
    
    magenta_hue_pen.reset()
    make_magenta_hue_pen()
    magenta_hue_pen.penup()
    magenta_hue_pen.setpos(0,0)
    magenta_hue_pen.pendown()
    
    green_hue_pen.reset()
    make_green_hue_pen()
    green_hue_pen.penup()
    green_hue_pen.setpos(0,0)
    green_hue_pen.pendown()
    
    blue_hue_pen.reset()
    make_blue_hue_pen()
    blue_hue_pen.penup()
    blue_hue_pen.setpos(0,0)
    blue_hue_pen.pendown()
    
    random_hue_pen.reset()
    make_random_hue_pen()
    random_hue_pen.penup()
    random_hue_pen.setpos(0,0)
    random_hue_pen.pendown()
    
    cyan_hue_pen.reset()
    make_cyan_hue_pen()
    cyan_hue_pen.penup()
    cyan_hue_pen.setpos(0,0)
    cyan_hue_pen.pendown()
    
    light_hue_pen.reset()
    make_light_hue_pen()
    light_hue_pen.penup()
    light_hue_pen.setpos(0,0)
    light_hue_pen.pendown()
    
    gold_hue_pen.reset()
    make_gold_hue_pen()
    gold_hue_pen.penup()
    gold_hue_pen.setpos(0,0)
    gold_hue_pen.pendown()
   
    gc.collect()



#Clear all pens to reclaim memory
def reset_all_pens():
    clear_p_pens()
    reset_random_hue_pens()
    
'=================================================================================================================='
'''Modules Section
'''

# Set up Logger
def startup_script(): # Starts module clock, sets up turtle functions, starts log file
    global module_start_time, default_range, start, end, start_time
    Lg.logger.info("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    Lg.logger.info("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    # Start time
    module_start_time = timer()
    start_time = datetime.datetime.now()
    Lg.logger.info(f'StartupScript:{my_script}:Setting up module environment @ {start_time}')
    t.my_venv()
    make_p_turtles()
    initialize_random_hue_pens()
    gc.enable()
    t.set_up_my_pen()
    Lg.logger.info(f'{my_script}:Starting to delete screenshots of {my_script} @ {Tm.this_time}....') # Thumbs are not necesssary after the video is created from them
    f.clear_thumbs() # Deletes all screenshot pngs
    default_range=  765
#     start = f'{Tm.datetime.datetime.fromtimestamp(datetime)}'
#     end = f'{Tm.datetime.datetime.fromtimestamp(datetime)}'
# startup_script()    


#Option to select a single angle instead of creating a specified group from parameters    
def select_angle():
    global my_angle
    default_angle = 120
    my_angle = turtle.numinput('Input Angle:', 'Angle, ', 144)
    if my_angle in range(-24, 24, 1):
        my_angle = default_angle
    return my_angle



# Creates working folders and declares variables; gets things rolling
def make_folder(): # Creates directories for video production; selects audio track to be used; sets watermark(audio track).
    global folder_name, my_project, str_angles, project_title, formatted_angles, my_script
    a.pick_angles()
    a.i_angle = a.i_angle_float
    str_angles = [float(i) for i in (a.i_angle)]
    formatted_angles = [int(i) for i in (a.i_angle)]
    Lg.logger.info(f'{my_script}:The {len(a.i_angle)} angles to be drawn are {formatted_angles}') 
    Lg.logger.info(f'{my_script}:Selecting track from runtime-generated list @ {Tm.this_time}')
    au.pick_bell_format_track() #Set of tones having primary tone as bell; complementary tones constant
#     au.pick_special_track() # Default state is commented out. Use it to select a specific track, specified at line 161 in audio_clips module.
#     au.pick_earth_tone_track()  # Default state is uncommented. Use it to select a randomly selected track in audio_clips module.
    my_project = Lg.my_project
    Lg.my_project = f'({len(a.i_angle)}){formatted_angles} degrees-{my_script}-{au.my_track}-{Tm.project_time}'
    project_title = f'{len(a.i_angle)} ({formatted_angles}) degrees angles; {my_script}; Audio: {au.my_track} @{Tm.project_time}' 
    my_logfile = f'{f.my_work_dir}/Logs/{Lg.my_project}.log'
    Lg.logger.info(f'{my_script}:Starting {Lg.my_project} @ {Tm.this_time}')
    Lg.logger.info(f'{my_script}:This is {Lg.my_project} code')
    Lg.logger.info(f'{my_script}:Setting up directories and files for video production  @ {Tm.this_time}')
    folder_name = Lg.my_project.replace("[","").replace("]","").replace("'","").replace(".0","")  # .replace(" ","") 
    Lg.logger.info(f'{my_script}:The folder_name is {folder_name}')
    t.my_project = Lg.my_project
    t.folder_name = folder_name
    t.project_title = project_title
    s.splash_screen()
    Lg.logger.info(f'{my_script}:Folder name is {t.folder_name}')
    f.make_reverse_png_folder()
#     f.make_archive_folder()
    turtle.title(t.folder_name)
    Lg.logger.info(f'{my_script}:Presenting {t.folder_name}')
#     f.make_daily_activities_log()
    s.watermark()



def process_thumbs():
    global count
    iterable = 0
    if count +1  ==  my_range:
        for iterable in range (360):
            f.save_thumb()
        clear_p_pens()
        reset_random_hue_pens()
#         gc.collect()
    else:
        f.save_thumb() 
       
    


# Starts video creation process
def produce_video():
    reset_all_pens()
    turtle.setup(5,5)
    # Start time
    produce_video_start_time = timer()
    f.save_final_thumb()
    gc.collect()
    Lg.logger.info(f'{my_script}:Starting produce_video script @ {Tm.this_time}........')
    f.set_vid_env()
    Tm.set_time()
    Lg.logger.info(f'{my_script}:Starting merger of video and audio clips @ {Tm.this_time}.........')
    f.sync_av() 
    Tm.set_time()
    Lg.logger.info(f'{my_script}:Making of {my_script} by Leon Hatton completed @ {Tm.now}')
    Tm.set_time()
    Lg.logger.info(f'{my_script}:Stopping  {t.folder_name} by Leon Hatton @ {Tm.this_time}')
    #End time
    produce_video_end_time = timer()
    # Calculate elapsed time
    elapsed_time =  produce_video_end_time - produce_video_start_time
    Lg.logger.info(f'{my_script}:Total Run Time of the produce_video script is {elapsed_time/3600:.2f} hours or {elapsed_time/60:.2f} minutes')
    Lg.logger.info('*********************************************************************************************************************')





def produce_reversing_video():
    turtle.setup(5,5)
    reset_all_pens()
    # Start time
    produce_reversing_video_start_time = timer()
    f.save_final_thumb()
    gc.collect()
    Lg.logger.info(f'{my_script}:Starting produce_reversing_video script @ {Tm.this_time}........')
    f.set_reverse_vid_env()
    Tm.set_time()
    Lg.logger.info(f'{my_script}:Starting merger of video and audio clips @ {Tm.this_time}.........')
    f.sync_av() 
    Tm.set_time()
    Lg.logger.info(f'{my_script}:Making of {my_script} by Leon Hatton completed @ {Tm.now}')
    Tm.set_time()
    Lg.logger.info(f'{my_script}:Stopping  {t.folder_name} by Leon Hatton @ {Tm.this_time}')
    #End time
    produce_reversing_video_end_time = timer()
    # Calculate elapsed time
    elapsed_time =  produce_reversing_video_end_time - produce_reversing_video_start_time
    Lg.logger.info(f'{my_script}:Total Run Time of the produce_reversing_video script is {elapsed_time/3600:.2f} hours or {elapsed_time/60:.2f} minutes')
    Lg.logger.info('****************************************************************************''*************************************************')




# Shuts down module processing and closes Turtle
def finalize():
    global module_end_time, difference, module_elapsed_time, end_time
    Lg.logger.info('************************************************************************')
    Lg.logger.info(f'{my_script}:Preparing to backup and sync all files and folders of {my_script} @ {Tm.this_time}')
    Lg.logger.info(f'{my_script}:Moving files to appropriate folders')
    f.move_all() # Moves files to appropriate locations
    Lg.logger.info(f'{my_script}:Video .mp4 files have been moved to /Videos/')
    Lg.logger.info(f'{my_script}:Image .png files have been moved to /Thumbs/')
    Lg.logger.info(f'{my_script}:Image .jpg files have been moved to /Pictures/Mandala Final Thumbs/')
    Lg.logger.info(f'{my_script}:Pics have been moved to Pictures folder @ {Tm.this_time}')
    Lg.logger.info('================================================================================')
    Tm.set_time()
    Lg.logger.info(f'{my_script}:Screenshots deletions completed @ {Tm.this_time}')
    Lg.logger.info(f'{my_script}:Starting to update the backup files of {my_script} @ {Tm.this_time}')
    f.sync_mandala_folders()  # Sync video and script folders backups
    Lg.logger.info(f'{my_script}:Folders and files of {my_script} have been synced and backed up')
    logger.warning(f'Shutting down this module and resetting logger')
    module_end_time = timer()  
    module_elapsed_time = module_end_time - module_start_time
    Lg.logger.info(f'{my_script}:All modules of {my_script} have been completed successfully.')
    Lg.logger.info(f'{my_script}: Program shutting down @ {Tm.this_time}')
    Lg.logger.info(f'{my_script}:Module Total Run Time: {module_elapsed_time/3600:.2f} hours')
    Lg.logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    Lg.logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    logger.handlers.clear()
#     reset_p_pens()
# finalize()



def reset_turtles():   #Utility to clear screen and reset to sequence next screen drawing
    turtles = turtle.getturtle()
    turtle.clearscreen()
    turtles.reset()
   #     Lg.logger.info('Pausing 9 seconds for user option to permanently manually stop the program at  end of sub-routine  before the next one starts.................')
    Lg.logger.info(f'{my_script}:All instances of turtle have been reset')
    time.sleep(1)
    
def set_random_pen_home(): #Random Pen
    random_hue_pen.penup()
    random_hue_pen.setpos(0,0)  
    random_hue_pen.seth(0)
    random_hue_pen.hideturtle()
    random_hue_pen.pendown()
    
def set_light_pen_home(): # Light Pen
    light_hue_pen.penup()
    light_hue_pen.setpos(0,0)  
    light_hue_pen.seth(0)
    light_hue_pen.hideturtle()
    light_hue_pen.pendown()

def set_gold_pen_home(): # Gold Pen
    gold_hue_pen.penup()
    gold_hue_pen.setpos(0,0)  
    gold_hue_pen.seth(0)
    gold_hue_pen.hideturtle()
    gold_hue_pen.pendown()

def set_blue_pen_home(): # Blue Pen
    blue_hue_pen.penup()
    blue_hue_pen.setpos(0,0)  
    blue_hue_pen.seth(0)
    blue_hue_pen.hideturtle()
    blue_hue_pen.pendown()

def set_yellow_pen_home():  #Yellow Pen
    yellow_hue_pen.penup()
    yellow_hue_pen.setpos(0,0)  
    yellow_hue_pen.seth(0)
    yellow_hue_pen.hideturtle()
    yellow_hue_pen.pendown()

def set_magenta_pen_home(): #Magenta Pen
    magenta_hue_pen.penup()
    magenta_hue_pen.setpos(0,0)  
    magenta_hue_pen.seth(0)
    magenta_hue_pen.hideturtle()
    magenta_hue_pen.pendown()

def set_dark_pen_home(): # Dark Pen
    dark_hue_pen.penup()
    dark_hue_pen.setpos(0,0)  
    dark_hue_pen.seth(0)
    dark_hue_pen.hideturtle()
    dark_hue_pen.pendown()

def set_green_pen_home(): # Green Pen
    green_hue_pen.penup()
    green_hue_pen.setpos(0,0)  
    green_hue_pen.seth(0)
    green_hue_pen.hideturtle()
    green_hue_pen.pendown()

def set_orange_pen_home():  # Orange Pen
    orange_hue_pen.penup()
    orange_hue_pen.setpos(0,0) 
    orange_hue_pen.seth(0)
    orange_hue_pen.hideturtle()
    orange_hue_pen.pendown()

def set_indigo_pen_home(): #Indigo Pen
    indigo_hue_pen.penup()
    indigo_hue_pen.setpos(0,0)  
    indigo_hue_pen.seth(0)
    indigo_hue_pen.hideturtle()
    indigo_hue_pen.pendown()

def set_red_pen_home(): #Red pen
    red_hue_pen.penup()
    red_hue_pen.setpos(0,0)  
    red_hue_pen.seth(0)
    red_hue_pen.hideturtle()
    red_hue_pen.pendown()

def set_random_a_pen_home(): # Random_a Pen
    cyan_hue_pen.penup()
    cyan_hue_pen.setpos(0,0)  
    cyan_hue_pen.seth(0)
    cyan_hue_pen.hideturtle()
    cyan_hue_pen.pendown()
    
def set_pa_home():
    pa.penup()
    pa.setpos(0,0) 
    pa.seth(0)
    pa.hideturtle()
    pa.pendown()
    
def set_pb_home():
    pb.penup()
    pb.setpos(0,0) 
    pb.seth(0)
    pb.hideturtle()
    pb.pendown()
    
def set_pc_home():
    pc.penup()
    pc.setpos(0,0) 
    pc.seth(0)
    pc.hideturtle()
    pc.pendown()
    
def set_pd_home():
    pd.penup()
    pd.setpos(0,0) 
    pd.seth(0)
    pd.hideturtle()
    pd.pendown()
    
def set_pe_home():
    pe.penup()
    pe.setpos(0,0) 
    pe.seth(0)
    pe.hideturtle()
    pe.pendown()
    
def set_pf_home():
    pf.penup()
    pf.setpos(0,0) 
    pf.seth(0)
    pf.hideturtle()
    pf.pendown()
    
def set_pg_home():
    pg.penup()
    pg.setpos(0,0) 
    pg.seth(0)
    pg.hideturtle()
    pg.pendown()
    
def set_ph_home():
    ph.penup()
    ph.setpos(0,0) 
    ph.seth(0)
    ph.hideturtle()
    ph.pendown()    
    
def all_pens_home():
    set_pa_home()
    set_pb_home()
    set_pc_home()
    set_pd_home()
    set_pe_home()
    set_pf_home()
    set_pg_home()
    set_ph_home()
    set_random_pen_home()  #Random Pen
    set_light_pen_home()  # Light Pen  #2
    set_gold_pen_home() #Gold Pen  #3
    set_blue_pen_home()  # Blue Pen  #4
    set_green_pen_home()   #Green Pen  #5
    set_indigo_pen_home()   # Indigo Pen  #6
    set_orange_pen_home()     # Orange Pen  #7
    set_random_a_pen_home()  # Random_a Pen  #8
    set_red_pen_home()     #  Red Pen  #9
    set_yellow_pen_home() # Yellow Pen  #10
    set_dark_pen_home()  # Dark Pen  #11
    set_magenta_pen_home()  #Magenta Pen  #12


def report_loop_count():
    if count % 100 == 0 and count < my_range - 1:
        Lg.logger.info(f'{my_script}:Just completed loop # {count} of {my_script} @ {Tm.this_time}')
    elif count == my_range -1:
        Lg.logger.info(f'{my_script}:Just completed final loop # {count} of {my_script} @ {Tm.this_time}')
    else:
        pass


def check_memory():
#     p = psutil.Process()
#     Lg.logger.info(f'{my_script}:Memory Use: {p.memory_full_info()}')
    pid = os.getpid()
    python_process = psutil.Process(pid)
    memoryUse = python_process.memory_full_info()[7] /2 **30
#     memory usage in GB
    Lg.logger.info(f'{my_script}:Memory Use: {memoryUse:.2f} GB')
    
    
# Future: Using zip function to bind angle and audio file variables for parallel processing
'''Section Short Mandalas'''

def set_titles():
    global my_script, count
    Lg.logger.info(f'{my_script}:Current Mandala is {my_script}; angle to be drawn is {my_angle:.2f} @ {Tm.this_time}') # Employing f-script
    t.my_title = (f'{my_script}: {my_angle:.2f} Degrees Angle  and  {au.my_track}')  # Employing f-script
    turtle.title(t.my_title)
    count = 0
    turtle.bgcolor(0,0,15)
    s.watermark()





'''+++++++++++MODULE++++++++++++++++++++++++++++++++++++++++++++++++++++++
Flower of Life Mandala
Status: Creation Date: 12/25/2023, Last Completed Run: 01/01/2024
'''
def flower_of_life():
    global count, my_script, my_pensize, my_key, my_range, radius, my_angle 
    def draw_center_flower():
        pa.left(my_angle)
        pa.penup()
        pa.fd(radius * 3.5)
        pa.pendown()
        f.save_thumb()
        for n in range(240):
            pa.pencolor(n * 3 %240, n * 4 %240, 10)
            pa.pensize(my_pensize)
            pa.circle(radius)
            pa.dot('white')
            pa.left(my_angle)
            f.save_thumb()

    def draw_outer_flower():
        pa.penup()
        pa.rt(360)
        pa.forward(radius  * 3.5)
        pa.left(my_angle)
        pa.pendown()
        for m in range(240):
            pa.pencolor(m * 3 %240, m * 4 %240, 10)
            pa.pensize(my_pensize / 2)
            pa.circle(radius)
            pa.dot('white')
            pa.left(my_angle)
            f.save_thumb()
            
            
    my_script ='Animated Flower of Life Matrix'
    Lg.logger.info(f'{my_script}:Starting {my_script} @ {Tm.my_time}')
    startup_script()
    make_folder()
   # Ensure that the 'my_angle' variable in the my_angles.py module is set at 60 degrees only!
    radius = 48
    t.my_angles = str_angles
    t.my_splash = f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = a.i_angle_float[a.i]
        make_turtle_pa() # Creates turtle instances
        my_range =  60 # 765 is default; Adjust as needed for output to fit screen; use lower or higher number for testing
        my_key = random.randint(1, 9999)
        my_pensize = 8
        pa.penup()
        pa.setpos(60, -120)
        pa.pendown()
        turtle.bgcolor(0, 0, 50)
        pa.pensize(my_pensize)
        for count in range(6):
            pa.pencolor(count * 5 % 255, count * 42 % 255, random.randint(1, 100))
            for iterable in range(6):
#                 Lg.logger.info(f'Outer Loop: {count}, Inner Loop: {iterable}: {pa.position()}')
               draw_outer_flower()
#             Lg.logger.info(f'Outer Loop: {count}, Inner Loop: {iterable}: {pa.position()}')
            draw_center_flower()
            process_thumbs()  
    produce_video()        
    finalize()

# flower_of_life()



#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Status: Creation Date: 6/2/2023, Last Completed Run: 12/10/2023
Originally named colorful_mandala_short. Changed to Prosper Mandala on 12/10/2023.
 '''    
def prosper_mandala():
    global count, my_script, turtle, my_angle, my_range
    my_script ='Prosper_Mandala'
    Lg.logger.info(f'{my_script}:Starting {my_script} @ {Tm.my_time}')
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = a.i_angle_float[a.i]
        make_p_turtles() # Creates turtle instances
        my_range =  default_range # 765 is default; Adjust as needed for output to fit screen; use lower or higher number for testing
        R, B , L, M  = 0, random.randint(64, 127), random.randint(127, 255), 255  # Randomnizes pencolors
        my_random = random.randint(150,255) # Varies the pencolor where used
        my_pensize, my_pensize_a, my_length, my_circle, my_length_bk = .0125,  .005,  .0862,  .01,  .06  # Multipliers
        count = 0
        turtle.bgcolor(0,0,15)
        set_titles()
        #Prosper_Mandala script
        for count in range(my_range):
            Q_seed.dot(6)
            pa.pencolor(count % 255, count % 255, random.randint(15, 150))
            pb.pencolor(random.randint(15, 150), count % 255, count % 127)           
            pa.pensize(count *my_pensize)
            pb.pensize(count * my_pensize)
            pa.left(my_angle)
            pa.fd(count * my_length_bk)
            f.save_thumb()
            pb.fd(count)
            f.save_thumb()
            pb.right(my_angle)
            pb.fd(count * my_length_bk * 3)
            f.save_thumb()
            pb.right(my_angle)
            pb.fd(count *my_length * 3)
            f.save_thumb()
            pa.left(my_angle)
            pa.circle(count *my_circle *3, - my_angle, 3)
            f.save_thumb()
            pa.fd(count * my_length *2)
            Q_seed.dot(6)
            process_thumbs()
#             report_loop_count() # For testing
    produce_reversing_video()        
    finalize()
# prosper_mandala()     
           
    
def colorful_mandala_wheels():
    global count, my_script, my_script, my_script, turtle, my_angle, my_range
    Lg.logger.info(f'{my_script}:Starting colorful_mandala_wheels')
    my_script = 'colorful_mandala_wheels'
    my_script = my_script
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = a.i_angle_float[a.i]
        make_p_turtles() # Creates turtle instances
        my_range =  default_range # 765 is default; Adjust as needed for output to fit screen; use lower or higher number for testing
        R, B , L, M  = 0, random.randint(64, 127), random.randint(127, 255), 255  # Randomnizes pencolors
        my_random = random.randint(150,255) # Varies the pencolor where used
        my_pensize, my_pensize_a, my_length, my_circle, my_length_bk = .0125,  .005,  .0862,  .01,  .06  # Multipliers
        count = 0
        turtle.bgcolor(0,0,15)
        set_titles()
        # colorful_mandala_wheels
        for count in range(my_range):
             Q_seed.dot(6)
             pa.pencolor(count % 255, count % 255, random.randint(15, 150))
             pb.pencolor(random.randint(15, 150), count % 255, count % 127) 
             pa.pensize(count * my_pensize)
             pb.pensize(count * my_pensize)
             pa.circle(count * my_circle, my_angle)
             f.save_thumb()
             pb.circle(count * my_circle / 2, - my_angle)
             Q_seed.dot(6)
    #          report_loop_count() # For testing
             process_thumbs()
    produce_reversing_video()    
    finalize()
# colorful_mandala_wheels()



# def Utterance_Mandala():
#     global count, my_script, my_script, my_script, turtle, my_angle, my_range
#     my_script ='Utterance_Mandala'
#     Lg.logger.info(f'{my_script}:Starting {my_script} @ {Tm.my_time}')
#     startup_script()
#     make_folder()
#     t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
#     for a.i  in range( len(a.i_angle)):
#         my_angle = a.i_angle_float[a.i]
#         make_p_turtles() # Creates turtle instances
#         my_range =  default_range # 765 is default; Adjust as needed for output to fit screen; use lower or higher number for testing
#         R, B , L, M  = 25, random.randint(64, 127), random.randint(127, 255), 255  # Randomnizes pencolors
#         my_random = random.randint(150,255) # Varies the pencolor where used
#         my_pensize, my_pensize_a, my_length, my_circle, my_length_bk = .0125,  .005,  .2,  .01,  .06  # Multipliers
#         count = 0
#         turtle.bgcolor(0,0,15)
#         set_titles()
#         for count in range(510):
#             Q_seed.dot(6)
#             pick_light()
#     #         pa.pencolor(count % 255, M - count %255,  L - count % 120 )
#             pb.pencolor(count %255, B + count % 60, L  )
#             light_hue_pen.left(my_angle)
#             light_hue_pen.fd(count *1.2)
#             f.save_thumb()
#             light_hue_pen.left(my_angle)
#             light_hue_pen.fd(count * (my_length))
#             f.save_thumb()
#             pb.left(my_angle)
#             pb.fd(count / 300)
#             f.save_thumb()
#             pb.left(my_angle * phi)  # This is the offset angle
#             pb.penup()
#             pb.setpos(0,0)
#             pb.pendown()
#             pb.fd(count /250)
#             f.save_thumb()
#     #         pb.left(my_angle * phi)  # This is the offset angle
#             pick_light()
#             light_hue_pen.left(my_angle)
#             light_hue_pen.fd(count * (my_length))
#             f.save_thumb()
#             light_hue_pen.left(my_angle * 3)
#             light_hue_pen.fd(count *(my_length / 2))
#             f.save_thumb()
#             pb.circle(count / 12, my_angle)
#             f.save_thumb()
#     #         light_hue_pen.pencolor(B, B, count %B)
#             light_hue_pen.dot(count * (my_length_bk / 2))
#             f.save_thumb()
#             pb.left(my_angle * phi) # This is the offset angle
#             pb.fd(count /50)
#             f.save_thumb()
#     #         light_hue_pen.pencolor(R, B, B - count % 64)
#             light_hue_pen.dot(3)
#             f.save_thumb()
#             pb.dot(count * .01)
#             f.save_thumb()
#             pb.pensize(count * (my_pensize / 4))
#             light_hue_pen.pensize(count * (my_pensize / 2))
#             light_hue_pen.right(my_angle)
#             light_hue_pen.fd(count * (my_length * .5))
#             f.save_thumb()
#             pb.left(my_angle * phi) # This is the offset angle
#             pb.fd(count / 25)
#             f.save_thumb()
#             light_hue_pen.right(my_angle)
#             light_hue_pen.fd(count * (my_length))
#             Q_seed.dot(8)
#             report_loop_count() # For testing
#             process_thumbs()
#     produce_reversing_video()    
#     finalize()
# # Utterance_Mandala()    
            
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Status: Creation Date: 6/2/2023, Last Update: 12/10/2023
Originally named Awesome Mandala A Short. Changed name to influence Mandala on 12/9/2023.
 ''' 
def influence_mandala():
    global count, my_script, my_script, my_script, turtle, my_angle, my_range
    my_script ='Influence_Mandala'
    Lg.logger.info(f'{my_script}:Starting {my_script} @ {Tm.my_time}')
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = a.i_angle_float[a.i]
        make_p_turtles() # Creates turtle instances
        my_range =  default_range # 765 is default; Adjust as needed for output to fit screen; use lower or higher number for testing
        R, B , L, M  = 0, random.randint(64, 127), random.randint(127, 255), 255  # Randomnizes pencolors
        my_random = random.randint(150,255) # Varies the pencolor where used
        my_pensize, my_pensize_a, my_length, my_circle, my_length_bk = .0125,  .005,  .0775,  .01,  .06  # Multipliers
        count = 0
        turtle.bgcolor(0,0,15)
        set_titles()
        #influence_mandala
        for count in range(my_range):
            Q_seed.dot(7)
            pc.pencolor(B + count  %120, M - count % 255,  10)
            pc.pensize(count * my_pensize)
            pc.fd(count *(my_length  * 9)) 
            f.save_thumb()
            pc.left(my_angle)
            pc.fd(count *(my_length  *9))
            f.save_thumb()
            pc.rt(my_angle /2)
            pc.fd(count *my_length / 11) 
            f.save_thumb()
            pc.pencolor(255,255,255)
            pc.dot(count * my_pensize + 2)
            f.save_thumb()
            pa.pencolor(B + count % 100, count %255, L)
            pa.pensize(count * (my_pensize))
            pa.fd(count * (my_length * 8))
            f.save_thumb()
            pa.rt(my_angle /2)
            pa.circle(count * (my_circle * 5), my_angle)
            f.save_thumb()
            pa.rt(my_angle)
            pa.circle(count * (my_circle * 5), my_angle, 6)
            f.save_thumb()
            Q_seed.dot(7)
            f.save_thumb()
#             report_loop_count() # For testing
            process_thumbs()
    produce_reversing_video()        
    finalize()
# influence_mandala()    




#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Status: Creation Date: 12/2/2023, Last Completed Run: 12/9/2023
Originally named Awesome Mandala B Short. Changed name to Effective Mandala on 12/9/2023.
 '''  
def effective_mandala():
    global count, my_script, my_script, my_script, turtle, my_angle, my_range
    my_script ='Effective Mandala'
    Lg.logger.info(f'{my_script}:Starting {my_script} @ {Tm.my_time}')
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = a.i_angle_float[a.i]
#         make_p_turtles() # Creates turtle instances
        my_range =  default_range # 765 is default; Adjust as needed for output to fit screen; use lower or higher number for testing
        R, B , L, M  = 0, random.randint(64, 127), random.randint(127, 255), 255  # Randomnizes pencolors
        my_random = random.randint(150,255) # Varies the pencolor where used
        my_pensize, my_pensize_a, my_length, my_circle, my_length_bk = .0125,  .005,  .0862,  .01,  .06  # Multipliers
        count = 0
        turtle.bgcolor(0,0,15)
        set_titles()
        #effective_mandala
        for count in range(my_range):
            Q_seed.dot(6)
            pick_gold() 
            gold_hue_pen.pensize(count *my_pensize)
            gold_hue_pen.fd(count *(my_length /5))
            f.save_thumb()
            gold_hue_pen.left(my_angle)
            gold_hue_pen.fd(count *(my_length /5))
            f.save_thumb()
            if count <= 636:
                indigo_hue_pen.pencolor(B + count %100, count % 255, L - count % 100)
            else:
                 pick_indigo()
                 indigo_hue_pen.pensize((count - count+1) * my_pensize)
            gold_hue_pen.fd(count *(my_length * 12))
            f.save_thumb()   
            gold_hue_pen.left(my_angle)
            gold_hue_pen.fd(count *(my_length /5))
            f.save_thumb()
            gold_hue_pen.left(my_angle)
            gold_hue_pen.fd(count *(my_length /5))
            f.save_thumb()
            gold_hue_pen.pensize(count * my_pensize)
            indigo_hue_pen.pensize(count *my_pensize)
            indigo_hue_pen.fd(count * (my_length * 9))
            f.save_thumb()
            indigo_hue_pen.rt(my_angle)
            indigo_hue_pen.circle(count *my_length, - my_angle, 5)
            f.save_thumb()
            Q_seed.dot(6)
#             report_loop_count() # For testing
            process_thumbs()
    produce_reversing_video()        
    finalize()
# effective_mandala()    
            

#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Status: Creation Date: 6/2/2023, Last Update: 12/10/2023
Originally named Stupendous Mandala Short. Changed name to Assurance Mandala on 12/9/2023.
 '''
def assurance_mandala():
    global count, my_script, my_script, my_script, turtle, my_angle, my_range
    my_script ='Assurance_Mandala'
    Lg.logger.info(f'{my_script}:Starting {my_script} @ {Tm.my_time}')
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = a.i_angle_float[a.i]
        make_p_turtles() # Creates turtle instances
        my_range =  default_range # 765 is default; Adjust as needed for output to fit screen; use lower or higher number for testing
        R, B , L, M  = 0, random.randint(64, 127), random.randint(127, 255), 255  # Randomnizes pencolors
        my_random = random.randint(150,255) # Varies the pencolor where used
        my_pensize, my_pensize_a, my_length, my_circle, my_length_bk = .0125,  .015,  .2,  .09,  .06  # Multipliers
        count = 0
        turtle.bgcolor(0,0,15)
        set_titles()
        # Run assurance_mandala
        for count in range(my_range):
            Q_seed.dot(6)
            pick_yellow() # Yellow_hue_pen (Pen 1)
            pb.pencolor(255 - count % 255, count % 255, count % 255) #Pen magenta_hue_pen  (Pen 2)
            pc.pencolor(count % 255, count % 127, my_random - count % 150) #Pen  (Pen 3)
            yellow_hue_pen.pensize(count * my_pensize)
            pb.pensize(count  *my_pensize_a)
            pc.pensize(count * my_pensize)
            pb.left(my_angle)  # Pen 2
            pb.fd(count * (my_length * 4))  #Pen 2
            f.save_thumb()
            pc.circle(count * (my_circle / 2), - my_angle, 3)  # Pen 3
            f.save_thumb()
            pc.right(my_angle)
            pc.fd(count * (my_length * 5))  # Pen 3
            f.save_thumb()
            yellow_hue_pen.left(my_angle)
            yellow_hue_pen.backward(count * my_length_bk * 8)  # Pen 1
            f.save_thumb()
            yellow_hue_pen.right(my_angle / 2)  # Pen 1
            yellow_hue_pen.fd(count * (my_length * 4))
            f.save_thumb()
            pb.left(my_angle)  #Pen 2
            pb.fd(count * my_length )  #Pen 2
            yellow_hue_pen.rt(my_angle)  # Pen 1
            yellow_hue_pen.fd(count * (my_length * 5))  # Pen 1
            f.save_thumb()
            Q_seed.dot(6)
#             report_loop_count() # For testing
            process_thumbs()
    produce_reversing_video()    
    finalize()
# assurance_mandala()    






'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'



global length
length = 255  #Default is 255; any lower number for testing

# Index of modules:

#Group A : Yin-Yang Series (Three Modules)

#  Group A module_1
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Basic Yin-Yang outputs to 10 minute duration when default settings are applied. Runtime over three days!
# Can re-use the thumbnail pgn output and the no_video poutput to create new videos
def basic_yin_yang(): # **
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range
    my_script = 'Animated Yin-Yang Wheel'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_angle = 180
    my_range = 900
    turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
    for count  in range (2): # Default is 5
        for iterable in range(my_range):  # 1800 is default, duration 10 minutes. Use lower number for testing. The higher the number, the longer the show.
            pa.pensize(10)
            pa.color(0,0,0) # 0,0,0 is default (Black)
            pa.rt(-my_angle + phi)
            pa.circle(250)
            f.save_thumb()
            pa.pensize(10)
            pa.color(255,255,255) # 255,255,255 is default (White)
            pa.rt(-my_angle)
            pa.circle(250)
            f.save_thumb()
          #For reversal of the direction uncomment the below.  
#         count = 0
#         for count in range (1800): # Default is 1800
#             pa.pensize(10)
#             pa.color(0,0,0) # 0,0,0 is default (Black)
#             pa.left(-my_angle + phi)
#             pa.circle(250)
#             f.save_thumb()
#             pa.color(255,255,255) # 255,255,255 is default (White)
#             pa.left(-my_angle)
#             pa.circle(250)
#             f.save_thumb()
        process_thumbs()    
    produce_video()
    finalize()


#  Group A module_2
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
def basic_yin_yang_extended(): # **
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Basic Yin-Yang Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    count = 0
    my_range =  600
    pa.hideturtle()
    my_angle = 180
    turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
    for count in range(my_range ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        pa.pensize(10)
        pa.color(0,0,0) # 0,0,0 is default (Black)
        pa.rt(-my_angle + phi)
        pa.circle(250)
        pa.pensize(10)
        pa.color(255, 255, 255) # 255,255,255 is default (White)
        pa.rt(-my_angle)
        pa.circle(250)
        f.save_thumb()
        Lg.logger.info(f'{my_script}:The value of count is {count}')
        Lg.logger.info(f'{my_script}:The value of Tm.iterable_time is {Tm.iterable_time}')
    turtle.bgcolor(0, 0, 0)
    count = 0
    for count in range (my_range):
        pa.pensize(10)
        pa.color(255,255,255) # 0,0,0 is default (Black)
        pa.left(-my_angle + phi)
        pa.circle(250)
        pa.color(50,255,50) # 255,255,255 is default (White)
        pa.left(-my_angle)
        pa.circle(250)
        f.save_thumb()
        Lg.logger.info(f'{my_script}:The value of count is {count}')
        Lg.logger.info(f'{my_script}:The value of Tm.iterable_time is {Tm.iterable_time}')
    turtle.bgcolor(255,255,255)    
    for count in range(my_range ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        pa.pensize(10)
        pa.color(0,0,0) # 0,0,0 is default (Black)
        pa.rt(-my_angle + phi)
        pa.circle(250)
        pa.pensize(10)
        pa.color(255,50,125) # 255,255,255 is default (White)
        pa.rt(-my_angle)
        pa.circle(250)
        f.save_thumb()
        Lg.logger.info(f'{my_script}:The value of count is {count}')
        Lg.logger.info(f'{my_script}:The value of Tm.iterable_time is {Tm.iterable_time}')
    turtle.bgcolor(252, 148, 10)
    count = 0
    for count in range (my_range):
        turtle.bgcolor(252 - count % 200, 148 + count% 100, 10)
        pa.pensize(10)
        pa.color(125,125,125) # 0,0,0 is default (Black)
        pa.left(-my_angle + phi)
        pa.circle(250)
        pa.color(150,150,255) # 255,255,255 is default (White)
        pa.left(-my_angle)
        pa.circle(250)
        f.save_thumb()
        Lg.logger.info(f'{my_script}:The value of count is {count}')
        Lg.logger.info(f'{my_script}:The value of Tm.iterable_time is {Tm.iterable_time}')
    count = 0
    turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
    for count in range(my_range ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        turtle.bgcolor(125 + count %125, 125 - count % 125, 125)
        pa.pensize(10)
        pa.color(0,0,0) # 0,0,0 is default (Black)
        pa.rt(-my_angle + phi)
        pa.circle(250)
        pa.pensize(10)
        pa.color(255,255,255) # 255,255,255 is default (White)
        pa.rt(-my_angle)
        pa.circle(250)
        f.save_thumb()
        Lg.logger.info(f'{my_script}:The value of count is {count}')
        Lg.logger.info(f'{my_script}:The value of Tm.iterable_time is {Tm.iterable_time}')
    turtle.bgcolor(0, 0, 0)
    count = 0
    for count in range (my_range):
        pa.pensize(10)
        pa.color(255,255,255) # 0,0,0 is default (Black)
        pa.left(-my_angle + phi)
        pa.circle(250)
        pa.color(50,255,50) # 255,255,255 is default (White)
        pa.left(-my_angle)
        pa.circle(250)
        f.save_thumb()
        Lg.logger.info(f'{my_script}:The value of count is {count}')
        Lg.logger.info(f'{my_script}:The value of Tm.iterable_time is {Tm.iterable_time}')
    turtle.bgcolor(255,255,255)    
    for count in range(my_range ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        pa.pensize(10)
        pa.color(0,0,0) # 0,0,0 is default (Black)
        pa.rt(-my_angle + phi)
        pa.circle(250)
        pa.pensize(10)
        pa.color(255,50,125) # 255,255,255 is default (White)
        pa.rt(-my_angle)
        pa.circle(250)
        f.save_thumb()
        Lg.logger.info(f'{my_script}:The value of count is {count}')
        Lg.logger.info(f'{my_script}:The value of Tm.iterable_time is {Tm.iterable_time}')
    turtle.bgcolor(252, 148, 10)
    count = 0
    for count in range (my_range):
        turtle.bgcolor(252 - count % 60, 148, 10 + count % 200)
        pa.pensize(10)
        pa.color(125,125,125) # 0,0,0 is default (Black)
        pa.left(-my_angle + phi)
        pa.circle(250)
        pa.color(150,150,255) # 255,255,255 is default (White)
        pa.left(-my_angle)
        pa.circle(250)
        f.save_thumb()
        Lg.logger.info(f'{my_script}:The value of count is {count}')
        Lg.logger.info(f'{my_script}:The value of Tm.iterable_time is {Tm.iterable_time}')  
    produce_video()
    finalize()


#  Group A module_3
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
def occilating_yin_yang(): # **
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Occillating Yin-Yang'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_angle = 180
    for  count in range(10):
        turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
        for  count in range(199):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
            pa.pensize(10)
            pa.color(0,0,0) # 0,0,0 is default (Black)
            pa.rt(-my_angle + phi)
            pa.circle(250)
            pa.pensize(10)
            pa.color(255,255,255) # 255,255,255 is default (White)
            pa.rt(-my_angle)
            pa.circle(250)
            f.save_thumb()
            Lg.logger.info(f'{my_script}:The value of count is {count}')
            Lg.logger.info(f'{my_script}:The value of Tm.iterable_time is {Tm.iterable_time}')
        turtle.bgcolor(252, 148, 10)
        count = 0
        for count in range(199):
            pa.pensize(10)
            pa.color(255, 50,100) # 0,0,0 is default (RGB Black)
            pa.left(-my_angle + phi)
            pa.circle(250)
            pa.color(150,150,255) # 0,0,0 is default (RGB Whie)
            pa.left(-my_angle)
            pa.circle(250)
            f.save_thumb()
            Lg.logger.info(f'{my_script}:The value of count is {count}')
            Lg.logger.info(f'{my_script}:The value of Tm.iterable_time is {Tm.iterable_time}')
    produce_video()
    finalize()




def breathing_yin_yang(): # **
    Lg.logger.info('########################################################')
# global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Breathing Yin-Yang'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    count = 0
    pa.hideturtle()
    my_angle = 180
    turtle.bgcolor(127,127,127) # Default is 127-127-127. Has to be a neutral shade like grey to contrast the black and white theme.
    Lg.logger.info(f'{my_script}:The background color is Gray')
    Lg.logger.info(f'{my_script}: The Yang color is Blue')
    Lg.logger.info(f'{my_script}: The Yin color is Yellow')
    for count in range(2500):  # 
       if count < 10:
           pa.pensize(count)
       else:
           pa.pensize(10)
       pa.color(0,255,255) # 0,0,0 is default (Black)
       pa.rt(-my_angle + phi)
       pa.circle(count / 10)
       f.save_thumb()
       pa.pensize(10)
       pa.color(255,255,0) # 255,255,255 is default (White)
       pa.rt(-my_angle)
       pa.circle(count /10)
       f.save_thumb()
       if count % 500 == 0:
           Lg.logger.info(f'{my_script}:The value of count is {count} @ {Tm.this_time}')
    Lg.logger.info(f'{my_script}:Stopping breathing_yin-yang at {Tm.this_time}')
    Lg.logger.info('########################################################')
    produce_reversing_video()
    finalize()






#Group B Long Duration Mandalas
    
#  Group B module_4
'''+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Status: Last Update: 6/28/2023, Last Completed Run: 12/29/2023
# Based on pretty_awesome Mandala
# First script completed using updated format. The angle is selected first
# Duration is 12 minutes
'''
def mystical_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range
    my_script = 'Mystical Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = (a.i_angle_float[a.i])
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        R, G, B, L = random.randrange(127, 255, 1), 0, 255,random.randrange(10, 150, 1) 
        Lg.logger.info(f'{my_script}:The value of hue R is {R}')
        Lg.logger.info(f'{my_script}:The value of hue L is {L}')
        M, N, X, Y, Z = 0, 0, 255, 255, 10
        count = 0
        my_length = 2 # Default is 5
        my_pensize = 150 # Default is 150
        my_range = 510 #Try for multiples of 255 to sync with the 255 colormode settings
        def place_pen(): # To be used to centering the mandala if required, default is commented out
            pa.penup()
            pa.setpos(0, - 150)
            pa.pendown()
            pa.speed(0)
        Lg.logger.info(f'{my_script}:Starting main script @ {Tm.this_time}')
        def mystical_script():
            turtle.bgcolor(0,50,100)
            pa.rt(my_angle)
            pa.circle(count / (my_length) / phi, my_angle)
            f.save_thumb()
            pa.pencolor(count * 2 % 124, L, G)
            pa.fd(count / my_length)
            f.save_thumb()
            pa.rt(my_angle)
            pa.fd(count / my_length)
            f.save_thumb()
            pa.rt(my_angle)
            pa.fd(count / my_length)
            report_loop_count() # For testing; comment out for production
            process_thumbs()
            
        Lg.logger.info('**************************************')    
        Lg.logger.info(f'{my_script}:Starting first pass @ {Tm.this_time}....')
        first_pass_start = timer()
#         place_pen() # To be used to centering the mandala if required, default is commented out
        for count in range(my_range):
            pa.pensize(count / my_pensize)
            pa.pencolor(count % 255,  B - count % 150, count % 50)
            mystical_script()
        first_pass_end = timer()
        elapsed_time = first_pass_end - first_pass_start
        Lg.logger.info(f'{my_script}:Elapsed Time: {elapsed_time:.2f} seconds, or {elapsed_time / 60:.2f} minutes')        
        clear_pa_pen() # Clears screen
        
        Lg.logger.info('**************************************')
        Lg.logger.info(f'{my_script}:Starting second pass @ {Tm.this_time}')
        second_pass_start = timer()
        R, G, B = random.randrange(1, 150, 1), 0, 255 
        Lg.logger.info(f'{my_script}:The value of hue R is {R}')
        L = random.randrange(150, 255, 1)
        Lg.logger.info(f'{my_script}:The value of hue L is {L}')
        M, N, X, Y, Z = 0, 0, 255, 255, 10
#         place_pen() # To be used to centering the mandala if required, default is commented out
        count = 0
        for count in range(my_range): # Second pass
            pa.pensize(count / my_pensize)
            pa.pencolor(B - count % 150, count % 50, count % 255)
            mystical_script()
        second_pass_end = timer()
        elapsed_time = second_pass_end - second_pass_start
        Lg.logger.info(f'{my_script}:Elapsed Time: {elapsed_time:.2f} seconds, or {elapsed_time / 60:.2f} minutes')         
        clear_pa_pen() # Clears screen
        
        count = 0
        Lg.logger.info('**************************************')
        Lg.logger.info(f'{my_script}:{my_script}:Starting third pass @ {Tm.this_time}....')
        third_pass_start = timer()
        R, G, B, L = random.randrange(10, 255, 1), 0, 255, random.randrange(10, 255, 1) 
        Lg.logger.info(f'{my_script}:The value of hue R is {R}')
        Lg.logger.info(f'{my_script}:The value of hue L is {L}')
#         place_pen() # To be used to centering the mandala if required, default is commented out
        for count in range(my_range): # Third pass
            pa.pensize(count / my_pensize)
            pa.pencolor(count % 50, count % 255,  B - count % 150 )
            mystical_script()
        third_pass_end = timer()
        elapsed_time = third_pass_end - third_pass_start
        Lg.logger.info(f'{my_script}:Elapsed Time: {elapsed_time:.2f} seconds, or {elapsed_time / 60:.2f} minutes')         
        clear_pa_pen()
        
        count = 0
        Lg.logger.info('**************************************')
        Lg.logger.info(f'{my_script}:{my_script}:Starting fourth pass @ {Tm.this_time}....')
        fourth_pass_start = timer()
#         place_pen() # To be used to centering the mandala if required, default is commented out
        R, G, B, L = random.randrange(25, 150, 1), 0, 255, random.randrange(10, 255, 1)
        Lg.logger.info(f'{my_script}:The value of hue R is {R}')
        Lg.logger.info(f'{my_script}:The value of hue L is {L}')
        for count in range(my_range): # Fourth pass
            pa.pensize(count / my_pensize)
            pa.pencolor(R,  B - count % 150, count % 50)
            mystical_script()
        fourth_pass_end = timer()
        elapsed_time = fourth_pass_end - fourth_pass_start
        Lg.logger.info(f'{my_script}:Elapsed Time: {elapsed_time:.2f} seconds, or {elapsed_time / 60:.2f} minutes')        
        clear_pa_pen() # Clears screen
        
        Lg.logger.info('**************************************')
        Lg.logger.info(f'{my_script}:{my_script}:Starting fifth pass @ {Tm.this_time}....')
        fifth_pass_start = timer()
#         place_pen() # To be used to centering the mandala if required, default is commented out
        R, G, B, L = random.randrange(200, 250, 1), 0, 255, random.randrange(10, 255, 1)
        Lg.logger.info(f'{my_script}:The value of hue R is {R}')
        Lg.logger.info(f'{my_script}:The value of hue L is {L}')
        count= 0
        for count in range(my_range): # Fifth pass
            pa.pensize(count / my_pensize)
            pa.pencolor(count % 255,  L, B - count % 255)
            mystical_script()
        fifth_pass_end = timer()
        elapsed_time = fifth_pass_end - fifth_pass_start
        Lg.logger.info(f'{my_script}:Elapsed Time: {elapsed_time:.2f} seconds, or {elapsed_time / 60:.2f} minutes')      
        clear_pa_pen()
        
        Lg.logger.info('**************************************')
        Lg.logger.info(f'{my_script}:{my_script}:Starting sixth pass @ {Tm.this_time}....')
        sixth_pass_start = timer()
#         place_pen() # To be used to centering the mandala if required, default is commented out
        count = 0
        R, G, B, L = random.randrange(101, 220, 1), 0, 255, random.randrange(10, 255, 1)
        Lg.logger.info(f'{my_script}:The value of hue R is {R}')
        Lg.logger.info(f'{my_script}:The value of hue L is {L}')
        for count in range(my_range): # Sixth pass
            pa.pensize(count / my_pensize)
            pa.pencolor(count % 255,  B - count % 150, R)
            mystical_script()
        sixth_pass_end = timer()
        elapsed_time = sixth_pass_end - sixth_pass_start
        Lg.logger.info(f'{my_script}:Elapsed Time: {elapsed_time:.2f} seconds, or {elapsed_time / 60:.2f} minutes')         
#         clear_pa_pen()
        process_thumbs()
    produce_reversing_video()
    finalize()






#  Group B Module_5
#+++++++++++MODULE 02, Simple Mandala +++++++++++++++++++++++++++++++++++++++++++++++++++++
#Typical duration is 4.09 minutes
def simple_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range
    my_script = 'Simple Mandala'
    startup_script()
    make_folder()
    for a.i  in range( len(a.i_angle)):
        my_angle = int(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
        count = 0
        my_range = 1800 # default is 1800
        my_pensize = 3 # default is 3
        my_length = 2 #default is 2
        Lg.logger.info(f'{my_script}:Starting First Loop @ {Tm.this_time}')
        start = Tm.now
        Lg.logger.info(f'{my_script}:Start time for this loop is {start}')
        pa.pensize(my_pensize)
        red_hue_pen.pensize(my_pensize)
        turtle.bgcolor(0,0,0)
        for count in range( my_range):
            # Random selection of red hue to repeat at 100th iteration; increase green green hue to 255; blue hue at max and decreases  to 0
            pa.pencolor(random.randint(25, 100) + count %100, count % 255, 255- count % 255)
            # Red hue decreases to 0; random selection of green hue to repeat at 100th iteration; blue hue starts at 0 and repeats at 255 
            red_hue_pen.pencolor(255 - count % 255, random.randint(25, 100) + count %100, count % 255)                
            pa.rt(my_angle)
            pa.fd(count / my_length)
    #         turtle.bgcolor(50,20,20)
            f.save_thumb()
            red_hue_pen.rt(-my_angle)
            red_hue_pen.fd(count / my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        end = Tm.now    
        Lg.logger.info(f'{my_script}:End Time for this loop is {end}')
        Lg.logger.info(f'{my_script}:Elapsed Time: {end - start}')
        count = 0
        all_pens_home()
        Lg.logger.info('Starting Second Loop @ ' + Tm.this_time)
        yellow_hue_pen.pensize(my_pensize)
        orange_hue_pen.pensize(my_pensize)
        for count in range(my_range):
            pick_yellow()
            pick_orange()
            yellow_hue_pen.rt(my_angle)
            yellow_hue_pen.fd(count /  my_length)
            f.save_thumb()
            orange_hue_pen.rt(-my_angle)
            orange_hue_pen.fd(count / my_length )
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        pa.pensize(my_pensize)
        red_hue_pen.pensize(my_pensize)
        Lg.logger.info('Starting Third Loop @ ' + Tm.this_time)
        for count in range(my_range):
            # red hue at max, decreases to 127 and repeats; green hue at max and decreases to 0 and repeats; random selection of blue hue to repeat at 100th iteration
            pa.pencolor(255 - count% 127, 255-count  % 255, random.randint(25, 100) + count %100)
            # red hue static at 15; green hue at 0 and increases to max; blue hue at max and deceases to 0
            red_hue_pen.pencolor(random.randint(25, 100) + count %100, count % 255, 255 - count % 255)                 
            pa.rt(my_angle)
            pa.fd(count / my_length)
            f.save_thumb()
            red_hue_pen.rt(-my_angle)
            red_hue_pen.fd(count / my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        yellow_hue_pen.pensize(my_pensize) # Yellow Pen
        green_hue_pen.pensize(my_pensize) # Green pen
        Lg.logger.info('Starting Fourth Loop @ ' + Tm.this_time)
        for count in range(my_range):
            pick_green()
            pick_yellow()
            green_hue_pen.rt(my_angle)
            green_hue_pen.fd(count / my_length)
            f.save_thumb()
            yellow_hue_pen.rt(-my_angle)
            yellow_hue_pen.fd(count / my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        blue_hue_pen.pensize(my_pensize)
        gold_hue_pen.pensize(my_pensize)
        Lg.logger.info('Starting Fifth Loop @ ' + Tm.this_time)
        for count in range(my_range):
            pick_blue()
            pick_gold()
            blue_hue_pen.rt(my_angle)
            blue_hue_pen.fd(count / my_length)
            f.save_thumb()
            gold_hue_pen.rt(-my_angle)
            gold_hue_pen.fd(count /  my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        pa.pensize(my_pensize)
        red_hue_pen.pensize(my_pensize)
        Lg.logger.info('Starting Sixth Loop @ ' + Tm.this_time)
        for count in range(my_range):
            # red hue at max decreases to 127; green hue at max decreases to 0; blue hue increases to 255    
            pa.pencolor(255 - count % 127,255 - count % 255, count % 255)
            # red hue static at 150; green hue increases to 255; random selection of blue hue, increases to 100th iteration and repeats
            red_hue_pen.pencolor(150, count % 255, random.randint(25, 100) + count %100)                 
            pa.rt(my_angle)
            pa.fd(count /  my_length)
            f.save_thumb()
            red_hue_pen.rt(-my_angle)
            red_hue_pen.fd(count / my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        indigo_hue_pen.pensize(my_pensize)
        cyan_hue_pen.pensize(my_pensize)
        Lg.logger.info('Starting Seventh Loop @ ' + Tm.this_time)
        for count in range( my_range):
            pick_indigo()
            pick_random_a()
            indigo_hue_pen.rt(my_angle)
            indigo_hue_pen.fd(count / my_length)
            f.save_thumb()
            cyan_hue_pen.rt(-my_angle)
            cyan_hue_pen.fd(count /  my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        pa.pensize(my_pensize)
        dark_hue_pen.pensize(my_pensize)
        Lg.logger.info('Starting Eighth Loop @ ' + Tm.this_time)
        for count in range( my_range):
            pick_light()
            pick_dark()
            pa.rt(my_angle)
            pa.fd(count / my_length)
            f.save_thumb()
            dark_hue_pen.rt(-my_angle)
            dark_hue_pen.fd(count /  my_length)
            process_thumbs()
#         produce_reversing_video() #Comment out if reversal not wanted
#     produce_video() # Comment out if reversal is wanted
    finalize()
    #exit
# simple_mandala()


#  Group B Module_6
#+++++++++++MODULE Colorful Mandala_Extended+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module has a duration of approximately 5.42 minutes when range and pensize defaults are applied,
# and so will randomly select from the pool of medium clips.
def colorful_mandala_extended():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Colorful Mandala Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        turtle.bgcolor(0,0,0)
        my_range = 650 # Default is 650
        my_pensize = 150 # Default is 150
        Lg.logger.info('Starting creation of sequential screenshots')
        Lg.logger.info('Starting First Loop of 5 @ ' + Tm.this_time)
        for count in range(my_range):
            gold_hue_pen.speed(0)
            indigo_hue_pen.speed(0)
            R =  0
            G =  140
            B =  255
            if G == 0:
                gold_hue_pen.color( count, count, B - count)
                indigo_hue_pen.color( count, 0, B - count)
            else:
                gold_hue_pen.color( count % 255, G - count %140, B - count %100)
                indigo_hue_pen.color( count % 255, G - count %140, B - count % 255)
            gold_hue_pen.fd(count / 2)
            f.save_thumb()
            gold_hue_pen.pensize(count / my_pensize)
            gold_hue_pen.circle(count / 2, my_angle, 6)
            f.save_thumb()
            indigo_hue_pen.fd(count / 2)
            f.save_thumb()
            indigo_hue_pen.right(my_angle)
            indigo_hue_pen.fd(count)
            indigo_hue_pen.pensize(count / my_pensize)
            f.save_thumb()
            if count +1 == my_range:
                f.save_final_thumb()
    #         Lg.logger.info('This is loop # ' + str(count) + ' of first pass') # For testing; comment out for production
        # Start second pass
        Lg.logger.info('Starting Second Loop of 5 @ ' + Tm.this_time)
        count = 244
        count = 0
        all_pens_home()
        for count in range(my_range):
            gold_hue_pen.pensize(count /  my_pensize)
            indigo_hue_pen.pensize(count / my_pensize)
            R =  0
            G =  140
            B =  255
            if R >= 240:
                pick_gold()
                pick_indigo()
            else:
                gold_hue_pen.color(B - count % 240, G - count %140, count % 255)
                indigo_hue_pen.color(count %100, G - count %140, B - count % 240)
            gold_hue_pen.fd(count / 2)
            f.save_thumb()
            gold_hue_pen.circle(count /2, my_angle, 6)
            f.save_thumb()
            indigo_hue_pen.fd(count / 2)
            f.save_thumb()
            indigo_hue_pen.right(my_angle)
            indigo_hue_pen.fd(count)
            f.save_thumb()
            if count +1 == my_range:
                f.save_final_thumb()
        Lg.logger.info('Starting Third Loop of 5 @ ' + Tm.this_time)
        count = 0
        all_pens_home()
        for count in range(my_range):
            gold_hue_pen.pensize(count / my_pensize)
            indigo_hue_pen.pensize(count / my_pensize)
            R =  255
            G =  140
            B = 0
            if B >= 240:
                gold_hue_pen.color( R - count % 255, G + count % 140, 240)
                indigo_hue_pen.color( R - count % 255, G - count % 140, 240)
            else:
                gold_hue_pen.color(count %100, R - count % 255, G - count % 140, )
                indigo_hue_pen.color(R - count %100, count % 255, count % 255 )
            gold_hue_pen.fd(count / 2)
            f.save_thumb()
            gold_hue_pen.circle(count / 2, my_angle, 6)
            f.save_thumb()
            indigo_hue_pen.fd(count / 2)
            f.save_thumb()
            indigo_hue_pen.right(my_angle)
            indigo_hue_pen.fd(count)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        Lg.logger.info('Starting Fourth Loop of 5 @ ' + Tm.this_time )
        count = 0
        all_pens_home()
        for count in range(my_range):
            gold_hue_pen.pensize(count / my_pensize)
            indigo_hue_pen.pensize(count / my_pensize)
            pick_gold() # Pen gold_hue_pen
            pick_indigo() # Pen indigo_hue_pen
            gold_hue_pen.fd(count / 2)
            f.save_thumb()
            gold_hue_pen.circle(count / 2, my_angle, 6)
            f.save_thumb()
            indigo_hue_pen.fd(count / 2)
            f.save_thumb()
            indigo_hue_pen.right(my_angle)
            indigo_hue_pen.fd(count)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        Lg.logger.info('Starting Fifth Loop of 5 @ ' + Tm.this_time )
        count = 0
        all_pens_home()
        for count in range(my_range):
            pa.pensize(count / my_pensize)
            dark_hue_pen.pensize(count / my_pensize)
            pick_dark() # Pen dark_hue_pen
            pick_light() # Pen pa
            pa.fd(count / 2)
            f.save_thumb()
            pa.circle(count / 2, my_angle, 6)
            f.save_thumb()
            dark_hue_pen.fd(count / 2)
            f.save_thumb()
            dark_hue_pen.right(my_angle)
            dark_hue_pen.fd(count)
            process_thumbs()
#     produce_reversing_video()
    finalize()
    #exit



#  Group B Module_7
#+++++++++++MODULE Glorious Mandala_a+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module has a duration of approximately six minutes when range and pensize defaults are applied,
# and so will randomly select from the pool of medium clips, typically 6 minutes or greater.
def glorious_mandala_a():  # Based on Awesome Manadala
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range
    my_script = 'Glorious Mandala A'
    startup_script()
    make_folder()
    def glorious_mandala_a_script():
        pa.fd(count/2)
        f.save_thumb()
        pa.left(my_angle) 
        gold_hue_pen.circle(count/phi,-my_angle, 5) 
        f.save_thumb()
        pa.penup()
        pa.fd(count)
        f.save_thumb()
        pa.left(my_angle)
        pa.pendown()
        pa.fd(count)
        f.save_thumb()
        pb.fd(count)
        f.save_thumb()
        pb.rt(my_angle)
        pa.pensize(count/pensize_a)
        pb.pensize(count/pensize_b)
        if count  + 1 == my_range:
            Lg.logger.info(f'{my_script}:Count value is {count}; end of loop.')
            f.save_final_thumb()
    for a.i  in range( len(a.i_angle)):
        my_angle = int(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
        R = 255
        B = random.randrange(112,155, 1)
        Lg.logger.info(f'{my_script}:The value of hue B is {B}')
        L = random.randrange(10, 150, 1)
        Lg.logger.info(f'{my_script}:The value of hue L is {L}')
        E = random.randrange(150, 255, 1)
        Lg.logger.info(f'{my_script}:The value of hue E is {E}')
        pensize_a = 45
        pensize_b = 120
        count = 0
        my_range = 637  # 360 is default, use lower number for testing.
        turtle.bgcolor(10,30,40)
        # First Pass
        Lg.logger.info('Starting creation of sequential screenshots')
        Lg.logger.info(f'{my_script}:Starting First Loop of 4 @ {Tm.this_time}')
        for count in range (my_range):
            pa = pa
            pb = indigo_hue_pen
            if count <= int(my_range *.66):
                pa.pencolor(L, count  %102, count %102)
                indigo_hue_pen.pencolor(B, R-count %102, count %51)
            else:
                pick_indigo() # Pen li
                pick_light() # Pen el
                indigo_hue_pen.fd(count/2)
            glorious_mandala_a_script()    
        Lg.logger.info(f'{my_script}:Completing First Loop # {count} @ {Tm.this_time}')   
        # Second Pass
        count = 0
        all_pens_home()
        Lg.logger.info(f'{my_script}:Starting Second Loop of 4 @ {Tm.this_time}')
        for count in range (int(my_range *.66)):
            pa = green_hue_pen
            pb = gold_hue_pen
            if count <= 255:
                green_hue_pen.pencolor(count %102,count %102, L)
                gold_hue_pen.pencolor(count %51, R - count %102, E)
            else:
                pick_green() # Pen green_hue_pen
                pick_gold()   #Pen gold_hue_pen
            glorious_mandala_a_script()   
        #  Third Pass
        count = 0
        all_pens_home()
        Lg.logger.info(f'{my_script}:Starting Third Loop of 4 @ {Tm.this_time}')
        for count in range (int(my_range *.66)):
            pa = yellow_hue_pen
            pb = dark_hue_pen
            if count <= 255:
                pa.pencolor(L, count %51, B)
                pb.pencolor(B, R-count %102, count %102)
            else:
                pick_dark() # Pen lz
                pick_yellow() # Pen ly
            glorious_mandala_a_script()  
        # Fourth Pass
        count = 0
        all_pens_home()
        Lg.logger.info(f'{my_script}:Starting Fourth Loop of 4 @ {Tm.this_time}')
        for count in range (int(my_range *.66)):
            pa = blue_hue_pen
            pb = random_hue_pen
            if count <= 255:
                pa.pencolor(E, count %51, count %102)
                pb.pencolor(count %51, R-count %102, L)
            else:
                pick_blue() # Pen lb
                pick_random() # Pen ce
            glorious_mandala_a_script()
            process_thumbs()
    produce_reversing_video()        
    finalize()
    #exit
# glorious_mandala_a()                     





#+++++++++++MODULE Glorious Mandala_b+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module has a duration of approximately six minutes when range and pensize defaults are applied,
# and so will randomly select from the pool of medium clips, typically 6 minutes or greater.

def glorious_mandala_b():  # Based on Awesome Manadala
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range, pa, pb
    my_script = 'Glorious Mandala B'
    startup_script()
    make_folder()
    def glorious_mandala_b_script():
        pa.left(my_angle)
        pa.fd(count / 4 ) #2)
        f.save_thumb()
        pb.circle(count/phi, -my_angle, 9) 
        f.save_thumb()
        pa.penup()
        pa.fd(count)
        f.save_thumb()
        pa.left(my_angle)
        pa.pendown()
        pa.fd(count / 2)
        f.save_thumb()
        pb.rt(my_angle)
        pb.fd(count / 2)
        f.save_thumb()
        pa.pensize(count/pensize_a)
        pb.pensize(count/pensize_b)
        if count  + 1 == my_range:
            f.save_final_thumb()    
    for a.i  in range( len(a.i_angle)):
        my_angle = float(a.i_angle_float[a.i])
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        turtle.setup(1950, 1070)
        turtle.clearscreen()
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
        R = 255
        B = random.randrange(112,155, 1)
        Lg.logger.info(f'{my_script}:The value of hue B is {B}')
        L = random.randrange(10, 150, 1)
        Lg.logger.info(f'{my_script}:The value of hue L is {L}')
        E = random.randrange(150, 255, 1)
        Lg.logger.info(f'{my_script}:The value of hue E is {E}')
        pensize_a = 20 #45
        pensize_b = 50 #120
        count = 0
        my_range = 382  # 510 is default, adjust as needed.
        turtle.colormode(255)
        turtle.bgcolor(10,30,40)
        make_turtle_pa()
        make_turtle_pb()
        # First Pass
        Lg.logger.info('Starting creation of sequential screenshots')
        Lg.logger.info(f'{my_script}:Starting First Loop of 4 of {t.my_title} @ {Tm.this_time}')
        count = 0
        all_pens_home()
        for count in range (my_range):
            pa = cyan_hue_pen
            pb = magenta_hue_pen
            if count <= int(my_range *.66):
                cyan_hue_pen.pencolor(L, count %102, count %51)
                magenta_hue_pen.pencolor(B, R-count %51, count %204)
            else:    
               pick_random_a() # Pen lr
               pick_magenta() # Pen me
            glorious_mandala_b_script()    
       # Second Pass
        count = 0
        all_pens_home()
        Lg.logger.info(f'{my_script}:Starting Second Loop of 4 of {t.my_title} @ {Tm.this_time}')
        for count in range (my_range):
            pa = red_hue_pen
            pb = orange_hue_pen
            if count <= int(my_range *.66):
                red_hue_pen.pencolor(count %102,count %51, L)
                orange_hue_pen.pencolor(count %51, R-count %102, E)
            else:
                pick_red() # Pen lu
                pick_orange() # Pen lq    
            glorious_mandala_b_script()
        # Third Pass        
        Lg.logger.info(f'{my_script}:Starting Third Loop of 4 of {t.my_title} @ {Tm.this_time}')
        all_pens_home()
        count = 0
        for count in range (my_range):
            pa = gold_hue_pen
            pb = indigo_hue_pen
            if count <= int(my_range *.66):
                pa.pencolor(L, count %51, count %102)
                pb.pencolor(R-count %51, E, count %102)
            else:
                pick_indigo() # Pen li
                pick_gold() # Pen go
            glorious_mandala_b_script()
        # Fouth Pass
        count = 0
        all_pens_home()
        Lg.logger.info(f'{my_script}:Starting Fourth Loop of 4 of {t.my_title} @ {Tm.this_time}')
        for count in range (my_range):
            pa = pa
            pb = dark_hue_pen
            if count <= int(my_range *.66):
                pa.pencolor(count %102,count %51, L)
                pb.pencolor(count %51, R-count %51, B)
            else:
                pick_light() # Pen el
                pick_dark() # Pen lz
            glorious_mandala_b_script()
        process_thumbs()
    produce_reversing_video()    
    finalize()
# glorious_mandala_b()     
    
    



#  module_16
#**************************************************************************************************************
  # First Published to YouTube on 11/21/2021; Revised to employ the most recent coding practices that I have picked up.
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def random_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, my_range, count, pa, pb, my_pensize, L, R, G, B, M, my_length,my_pensize_a, my_length_bk,  my_random, my_circle, my_script
#     my_script = 'Random Mandalas'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = a.i_angle_float[a.i]
        make_p_turtles() # Creates turtle instances
        my_range =  25 # 765 is default; Adjust as needed for output to fit screen; use lower or higher number for testing
        R, B , L, M  = 0, random.randint(64, 127), random.randint(127, 255), 255  # Randomnizes pencolors
        my_random = random.randint(150,255) # Varies the pencolor where used
        my_pensize, my_pensize_a, my_length, my_circle, my_length_bk = .0125,  .005,  .0862,  .01,  .06  # Multipliers
        count = 0
        turtle.bgcolor(0,0,15)
        pick_mandala_script()
        reset_turtles()
    finalize()



    
#  Group B Module_9
#+++++++++++MODULE Bold Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''This project can select and run a sequence of angles as a single video. It will select and retain a single audio track
for the duration of the video track.'''    
def reversing_simple_mandala():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Reversing Simple Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info('Current angle to be drawn is ' + str(my_angle))
#         au.pick_custom_length_track()
        turtle.title('A Reversing Simple Mandala: ' + str(my_angle) + '  Angle ' + ' and  ' + str(au.my_track))
#         Lg.logger.info('Selecting angle from input box')
#         Lg.logger.info('Current angle to be drawn is ' + str(my_angle))
        count = 0
        my_range = 1530 # default is 1785
        my_pensize = 2 # default is 3
        my_length = 2 #default is 2
        Lg.logger.info('Starting First Loop @ ' + Tm.this_time)
        start = Tm.now
        Lg.logger.info('Start time for this loop is ' + str(start))
        magenta_hue_pen.pensize(my_pensize)
        orange_hue_pen.pensize(my_pensize)
        turtle.bgcolor(0,0,0)
        for count in range(my_range):
            pick_red()  # Pen red_hue_pen
            pick_light() # Pen pa
            red_hue_pen.rt(my_angle)
            red_hue_pen.fd(count /  my_length)
            f.save_thumb()
            pa.rt(-my_angle)
            pa.fd(count / my_length )
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        green_hue_pen.pensize(my_pensize) # Yellow Pen
        yellow_hue_pen.pensize(my_pensize) # Green pen
        Lg.logger.info('Starting Second Loop @ ' + Tm.this_time)
        for count in range(my_range):
            pick_green() #Pen green_hue_pen
            pick_yellow() # Pen yellow_hue_pen
            green_hue_pen.rt(my_angle)
            green_hue_pen.fd(count / my_length)
            f.save_thumb()
            yellow_hue_pen.rt(-my_angle)
            yellow_hue_pen.fd(count / my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
    produce_reversing_video() #Comment out if reversal not wanted
#     produce_video()
    finalize()
    
    
  
    
    

#  Group B Module_8
#+++++++++++MODULE Bold Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''This project can select and run a sequence of angles as a single video. It will select and retain a single audio track
for the duration.'''
def bold_mandala():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Bold Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info('Current angle to be drawn is ' + str(my_angle))
#         au.pick_custom_length_track()
        turtle.title('A Bold Mandala: ' + str(my_angle) + '  Angle ' + ' and  ' + str(au.my_track))
        my_pensize = 30
        turtle.bgcolor(0,0,0)
        my_range = 25
        count = 0
    #     my_range = count
        for count in range(my_range):      #255 is default. Use lower number for testing.
            pick_indigo() # indigo_hue_pen;Indigo hues
            pick_gold() #gold_hue_pen; Gold hues
            indigo_hue_pen.left(my_angle) #Indigo pen
            indigo_hue_pen.penup()
            indigo_hue_pen.setpos(0,0)
            indigo_hue_pen.pendown()
            indigo_hue_pen.pensize(count / my_pensize)
            indigo_hue_pen.circle(count, my_angle)
            f.save_thumb()
            gold_hue_pen.pensize(count / my_pensize)  #Gold pen
            gold_hue_pen.left(my_angle)
            gold_hue_pen.backward(count * phi)
            f.save_thumb()
            gold_hue_pen.left(my_angle)
            gold_hue_pen.fd(count)
            f.save_thumb()
            turtle.bgcolor(count, count, count)
            f.save_thumb()
        count = 0
        all_pens_home()
        turtle.bgcolor(255, 255, 255)
        for count in range( my_range):
            pick_red() #red_hue_pen; red hues
            pick_blue() #blue_hue_pen; blue hues
            red_hue_pen.left(my_angle) 
            red_hue_pen.penup()
            red_hue_pen.setpos(0,0)
            red_hue_pen.pendown()
            red_hue_pen.pensize(count /my_pensize)
            red_hue_pen.circle(count, my_angle) # Red Pen
            f.save_thumb()
            blue_hue_pen.pensize(count / my_pensize)  #Blue pen
            blue_hue_pen.left(my_angle)
            blue_hue_pen.backward(count * phi)
            f.save_thumb()
            blue_hue_pen.left(my_angle)
            blue_hue_pen.fd(count)
            f.save_thumb()
            turtle.bgcolor(255 - count, 255 - count, 255 - count)
            f.save_thumb()
        count = 0
        all_pens_home()
        turtle.bgcolor(0,0,0)
        for count in range(my_range):
            pick_green() #green_hue_pen; green hues
            pick_yellow() #yellow_hue_pen; yellow hues
            green_hue_pen.left(my_angle) 
            green_hue_pen.penup()
            green_hue_pen.setpos(0,0)
            green_hue_pen.pendown()
            green_hue_pen.pensize(count / my_pensize)
            green_hue_pen.circle(count, my_angle) # Green Pen
            f.save_thumb()
            yellow_hue_pen.pensize(count / my_pensize)  
            yellow_hue_pen.left(my_angle)
            yellow_hue_pen.backward(count * phi) # Yellow pen 
            f.save_thumb()
            yellow_hue_pen.left(my_angle)
            yellow_hue_pen.fd(count)
            f.save_thumb()
            turtle.bgcolor(count, count, count)
            f.save_thumb()
        count = 0
        all_pens_home()
        turtle.bgcolor(255, 255, 255) # Background opens at White; fades to Green    
        for count in range(my_range):      #255 is default. Use lower number for testing.
            pick_random() #random_hue_pen; random hues
            pick_magenta() #magenta_hue_pen; magenta hues
            random_hue_pen.left(my_angle) #Random pen
            random_hue_pen.penup()
            random_hue_pen.setpos(0,0)
            random_hue_pen.pendown()
            random_hue_pen.pensize(count / my_pensize)
            random_hue_pen.circle(count, my_angle)
            f.save_thumb()
            magenta_hue_pen.pensize(count / my_pensize) 
            magenta_hue_pen.left(my_angle)
            magenta_hue_pen.backward(count * phi)  # Magenta pen 
            f.save_thumb()
            magenta_hue_pen.left(my_angle)
            magenta_hue_pen.fd(count)
            f.save_thumb()
            turtle.bgcolor(255 - count, 255, 255 - count)
            f.save_thumb()
        count = 0
        all_pens_home()
        turtle.bgcolor(0, 255, 0)   # Background opens at Green; fades to light blue 
        for count in range(my_range):      #255 is default. Use lower number for testing.
            pick_orange() #orange_hue_pen; orange hues
            pick_random_a() #cyan_hue_pen; random hues
            orange_hue_pen.left(my_angle) 
            orange_hue_pen.penup()
            orange_hue_pen.setpos(0,0)
            orange_hue_pen.pendown()
            orange_hue_pen.pensize(count / my_pensize)
            orange_hue_pen.circle(count, my_angle) # Orange pen
            f.save_thumb()
            cyan_hue_pen.pensize(count / my_pensize) 
            cyan_hue_pen.left(my_angle)
            cyan_hue_pen.backward(count * phi)   #Random pen
            f.save_thumb()
            cyan_hue_pen.left(my_angle)
            cyan_hue_pen.fd(count)
            f.save_thumb()
            turtle.bgcolor(0, 255, count)
            f.save_thumb()
        count = 0
        all_pens_home()
        turtle.bgcolor(0, 255, 255)  # Background opens at light blue; fades to black
        for count in range(my_range):
            pick_dark() #dark_hue_pen; dark hues
            pick_light() #pa; light hues
            dark_hue_pen.left(my_angle) #Dark pen
            dark_hue_pen.setpos(0,0)
            dark_hue_pen.pendown()
            dark_hue_pen.pensize(count /my_pensize)
            dark_hue_pen.circle(count, my_angle)
            f.save_thumb()
            pa.pensize(count / my_pensize)  
            pa.left(my_angle)
            pa.backward(count * phi)  #light pen
            f.save_thumb()
            pa.left(my_angle)
            pa.fd(count)
            f.save_thumb()
            turtle.bgcolor(0, 255 - count, 255 - count)
            f.save_thumb()
#     produce_video() # Ends with completed mandala; comment out if reversal is specified
    produce_reversing_video() #Ends with blank screen; commit out if full image is needed at the end
    finalize()




def strong_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range, pa, pb
    my_script = 'Strong Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = float(a.i_angle_auto[a.i])
        make_p_turtles()
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        my_range = 1275
        count = 0
        pa = pa
        for count in range(my_range):
            turtle.bgcolor(25, 10, 10)
            R =  0
            G =  0
            B =  90
            pa.color(count % 255 , G, B )
            pa.pensize(2)
            pa.fd(count / 3 )
            f.save_thumb()
            pa.left(my_angle)
            R = 0
            G = 230
            B = 255
            pa.color(count % 255, G, B - count % 255)
            pa.circle(7, my_angle, 6)
            f.save_thumb()
            pa.backward(10)
            f.save_thumb()
            pa.pensize(5)
            pa.setposition(-30, 0)
            f.save_thumb()
            pa.circle(count / 5, my_angle, 72)
            f.save_thumb()
        pa.clear()
        pa.penup()
        pa.setpos(0,0)
        pa.pendown()
        count = 0
        Lg.logger.info('Angle being drawn is ' + str(my_angle *3))
        for count in range(my_range):
            turtle.bgcolor(25, 10, 10)
            R =  0
            G =  0
            B =  90
            pa.color(count % 255 , G, B )
            pa.pensize(2)
            pa.fd(count / 3 )
            f.save_thumb()
            pa.left(my_angle * 3)
            R = 0
            G = 230
            B = 255
            pa.color(count % 255, G, B - count % 255)
            pa.circle(7, my_angle * 3, 6)
            f.save_thumb()
            pa.backward(10)
            f.save_thumb()
            pa.pensize(5)
            pa.setposition(-30, 0)
            f.save_thumb()
            pa.circle(count / 5, my_angle * 3, 72)
            f.save_thumb()
    produce_reversing_video()
    finalize()
# strong_mandala()




#module_41
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def glorious_mandala():  # Based on Awesome Manadala
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Glorious Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range(len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info('Current angle to be drawn is ' + str(my_angle))
        t.my_title = f'Glorious Mandala: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        B = random.randint(112,155)
        Lg.logger.info(f'{my_script}:The value of hue B is {B}')
        L = random.randint(10, 150)
        Lg.logger.info(f'{my_script}:The value of hue L is {L}')
        E = random.randint(150, 255)
        Lg.logger.info(f'{my_script}:The value of hue E is {L}')
        R = 255
        G = 255
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        turtle.bgcolor(0, 10, 0)
        t.set_up_lb()
        t.set_up_go()
        set_gold_pen_home()
        set_blue_pen_home()
        my_range =  1275  #Default is 1275
        for count in range(my_range):
            gold_hue_pen.pensize(count / 150)
            blue_hue_pen.pensize(count / 135)
            if count <= 255:
                blue_hue_pen.pencolor(L + count % 50, M + count % 255, E)
                gold_hue_pen.pencolor(R - count, B, Z + count %200)
            else:
                pick_gold()
                pick_blue()
            gold_hue_pen.left(my_angle)
            gold_hue_pen.fd(count / 18)
            f.save_thumb()
            blue_hue_pen.circle(count / 24, - my_angle, 6)
            f.save_thumb()
            gold_hue_pen.left(my_angle)
            gold_hue_pen.penup()
            blue_hue_pen.penup()
            gold_hue_pen.right(my_angle)
            gold_hue_pen.fd(count / 24)
            f.save_thumb()
            blue_hue_pen.rt(my_angle)
            gold_hue_pen.pendown()
            blue_hue_pen.pendown()
            gold_hue_pen.fd(count / phi)
            f.save_thumb()
            blue_hue_pen.fd(count / phi)
            f.save_thumb()
            gold_hue_pen.backward(count / 24)
            f.save_thumb()
        gold_hue_pen.reset()
        blue_hue_pen.reset()
    produce_reversing_video()
    finalize()






#  module_6
#+++++++++++MODULE FANTASTIC MANDALA+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Fantastic_Mandala():  
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Fantastic Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range(len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info('Current angle to be drawn is ' + str(my_angle))
        t.my_title = f'{my_script}: {my_angle} Degrees Angle with {au.my_track}'
        turtle.title(f'{my_script}: {my_angle} Angle with {au.my_track}')
        count = 0
        my_range = 1020  #default is 1020; use lower number for testing
        set_indigo_pen_home() # Indigo Pen used normally
        set_gold_pen_home()  #Gold Pen
        set_light_pen_home() # Light Pen used normally
        set_red_pen_home() #Red Pen
        turtle.bgcolor(0,0,20)
        for count in range(my_range):
            pick_red()
            red_hue_pen.pensize(count /2040)
            red_hue_pen.left(my_angle)
            red_hue_pen.circle(count / 24, my_angle, 6)
            f.save_thumb()
            indigo_hue_pen.pensize(count / 125)
            indigo_hue_pen.pencolor(count % 255, 255, 255 - count % 255)
            indigo_hue_pen.fd(count)
            f.save_thumb()
            indigo_hue_pen.right(my_angle)
            pick_gold()
            gold_hue_pen.pensize(count / 1020)
            gold_hue_pen.circle(count / 3, my_angle)
            f.save_thumb()
            pa.pensize(count / 200)
            pa.right(my_angle)
            pa.pencolor(0, count % 255, 255)
            pa.fd(count / 12)
            f.save_thumb()
        gc.enable()
        gc.collect()
        gc.disable()
            # For testing purposes only; comment out for production run
#             Lg.logger.info('Ending Loop Count ' + str(count))
    produce_reversing_video()
    finalize()








#  Group B Module_8
#+++++++++++MODULE Awesome Mandala_Extended+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module has a duration of approximately 18 minutes when range and pensize defaults are applied,
# and so will randomly select from the pool of long clips.
def awesome_mandala_extended():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Awesome Mandala Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        R = 0
        G = 0
        B = random.randrange(10, 100, 3)
        L = random.randrange(100, 255, 3)
        Lg.logger.info('The Value of color B is    ' + str(B))
        Lg.logger.info('The Value of color L is    ' + str(L))
        M = 255
        N = 110
        X = 10
        Y = 255
        Z = 255
        my_pensize = 2500 # Default is 2500
        my_range = 2500 # Default is 2500 for 18 minutes
        forward_count = 5 # Default is 5 
        circ_rad = 12 # Default is 12
        Lg.logger.info('My pensize = '+ str(my_pensize)+'; Default is 6000')
        Lg.logger.info('Loop Count = '+ str(my_range)+'; Default is 6000')
        Lg.logger.info('Forward Count  = '+ str(forward_count)+'; Default is 18')
        Lg.logger.info('Circ_rad = ' + str(circ_rad)+'; Default is 45')
        count = 0
        all_pens_home()
        Lg.logger.info('Starting First Pass @ ' + Tm.this_time)
        for count in range(my_range):  # First pass
            pick_red() #Pen lu
            red_hue_pen.pensize(count / my_pensize)
            red_hue_pen.fd(count / forward_count * phi)
            f.save_thumb()
            red_hue_pen.rt(my_angle)
            t.lm.pensize(count / my_pensize * 2)
            t.lm.rt(my_angle)
            if count <= 255:
                t.lm.pencolor(L, M - count % 50, M - count)
            elif count in range(256, 1500):
                t.lm.pencolor(M, L, B)
            else:
                t.lm.pencolor(M, Y, B)
            t.lm.circle(count / circ_rad, - my_angle, 9)
            f .save_thumb()
   #         Lg.logger.info('Completed loop # ' + str(count)) # Uncomment for testing purposes only
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + '  of First Pass @ ' + Tm.this_time)
                f.save_final_thumb()
        all_pens_home()
        count = 0
        Lg.logger.info('Starting Second Pass @ ' + Tm.this_time)
        for count in range( my_range):
            pick_green() #Pen lg
            turtle.bgcolor(X, 0, 0)
            green_hue_pen.pensize(count / my_pensize)
            green_hue_pen.fd(count / forward_count * phi)
            f.save_thumb()
            green_hue_pen.rt(my_angle)
            t.lm.pensize(count / my_pensize * 2)
            t.lm.rt(my_angle)
            if count <= 255:
                t.lm.pencolor(R + count, M - count % 50, B)
            else:
                t.lm.pencolor(M, M, X)
            t.lm.circle(count / circ_rad, - my_angle, 9)
            f.save_thumb()
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + 'of Second Pass @ ' + Tm.this_time)
                f.save_final_thumb()
        all_pens_home()
        count = 0
        Lg.logger.info:('Starting Third Pass @ ' + Tm.this_time)
        for count in range(my_range):  # 3000 is default, use any number Third pass
            pick_indigo() #Pen li
            pick_gold()  #Pen go
            indigo_hue_pen.pensize(count / my_pensize)
            indigo_hue_pen.rt(my_angle)
            indigo_hue_pen.fd(count / forward_count * phi)
            f.save_thumb()
            gold_hue_pen.pensize(count / my_pensize)
            gold_hue_pen.rt(my_angle)
            gold_hue_pen.circle(count / circ_rad, - my_angle, 9)
            f.save_thumb()
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + 'of Third Pass @ ' + Tm.this_time)
                f.save_final_thumb()
        all_pens_home()
        count = 0
        Lg.logger.info:('Starting Fourth Pass @ ' + Tm.this_time)
        for count in range(my_range):  # 3000 is default, use any number Third pass
            pick_blue() #Pen lb
            pick_random()  #Pen ce
            blue_hue_pen.pensize(count / my_pensize)
            blue_hue_pen.rt(my_angle)
            blue_hue_pen.fd(count / forward_count * phi)
            f.save_thumb()
            random_hue_pen.pensize(count / my_pensize)
            random_hue_pen.rt(my_angle)
            random_hue_pen.circle(count / circ_rad, - my_angle, 9)
            f.save_thumb()
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + 'of Fourth Pass @ ' + Tm.this_time)
                f.save_final_thumb()
        all_pens_home()
        count = 0
        Lg.logger.info:('Starting Fifth Pass @ ' + Tm.this_time)
        for count in range(my_range):  # 3000 is default, use any number Third pass
            pick_magenta() #Pen me
            pick_orange()  #Pen lq
            magenta_hue_pen.pensize(count / my_pensize)
            magenta_hue_pen.rt(my_angle)
            magenta_hue_pen.fd(count / forward_count * phi)
            f.save_thumb()
            orange_hue_pen.pensize(count / my_pensize)
            orange_hue_pen.rt(my_angle)
            orange_hue_pen.circle(count / circ_rad, - my_angle, 9)
            f.save_thumb()
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + 'of Fifth Pass @ ' + Tm.this_time)
                f.save_final_thumb()
        all_pens_home()
        count = 0
        Lg.logger.info:('Starting Sixth Pass @ ' + Tm.this_time)
        for count in range(my_range):  # 3000 is default, use any number Third pass
            pick_light() #Pen el
            pick_random_a()  #Pen lr
            pa.pensize(count / my_pensize)
            pa.rt(my_angle)
            pa.fd(count / forward_count * phi)
            f.save_thumb()
            cyan_hue_pen.pensize(count / my_pensize)
            cyan_hue_pen.rt(my_angle)
            cyan_hue_pen.circle(count / circ_rad, - my_angle, 9)
            f.save_thumb()
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + 'of Sixth Pass @ ' + Tm.this_time)
                f.save_final_thumb()
    produce_video()
    finalize()







#  Group B Module_9
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Uses pens go(gold) and lb(blue); Based on Mystical Mandala
def joyous_mandala():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Joyous Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = float(a.i_angle_auto[a.i])
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        my_length = 5
        Lg.logger.info('The value of my_length is: ' + str(my_length))
        my_pensize = 360
        Lg.logger.info('The value of my_pensize is: ' +str(my_pensize))
        my_range = 1800
        Lg.logger.info('The valu of my_range is: ' + str(my_range))
        Lg.logger.info('Starting main script at ' + str(Tm.this_time))
        for my_loops in range(1,3):
            Lg.logger.info('Starting first pass of  loop  ' + str(my_loops)  + '@ ' + str(Tm.this_time))
            turtle.bgcolor(0, 0, my_loops * 18)
            all_pens_home()
            for count in range(my_range):
                pick_gold()
                blue_hue_pen.pencolor(my_loops * 80, count % 255, count % 255)
                gold_hue_pen.pensize(count / my_pensize / my_loops)
                blue_hue_pen.pensize(count / my_pensize / my_loops)
                blue_hue_pen.left(my_angle)
                gold_hue_pen.rt(my_angle)
                blue_hue_pen.fd(count / my_length)
                f.save_thumb()
                gold_hue_pen.fd(count / my_length)
                f.save_thumb()
                blue_hue_pen.left(my_angle / 2)
                gold_hue_pen.rt(my_angle / 2)
                blue_hue_pen.fd(count / my_length / 2)
                f.save_thumb()
                gold_hue_pen.fd(count / my_length / 2)
                f.save_thumb()
                gold_hue_pen.circle(count / my_length / phi, my_angle)
                f.save_thumb()
                blue_hue_pen.circle(count / my_length / phi, -my_angle)
                f.save_thumb()
            all_pens_home()
            Lg.logger.info('Starting second pass of  loop  ' + str(my_loops)  + '@ ' + str(Tm.this_time))
            count = 0
            turtle.bgcolor(my_loops * 50, my_loops * 45, my_loops * 20)
            for count in range(my_range):
                '''Second pass'''
                if my_loops == 2:
                    pick_magenta()
                    gold_hue_pen.pencolor(my_loops * 80, my_loops * count % 255, my_range - count % 152)
                    gold_hue_pen.pensize(count / my_pensize / my_loops)
                    magenta_hue_pen.pensize(count / my_pensize / my_loops)
                    magenta_hue_pen.rt(my_angle)        
                    gold_hue_pen.left(my_angle)
                    magenta_hue_pen.fd(count / my_length)
                    f.save_thumb()
                    gold_hue_pen.fd(count / my_length)
                    f.save_thumb()
                    magenta_hue_pen.rt(my_angle / 2)
                    gold_hue_pen.left(my_angle / 2)
                    magenta_hue_pen.fd(count / my_length / 2)
                    f.save_thumb()
                    gold_hue_pen.fd(count / my_length / 2)
                    f.save_thumb()
                    magenta_hue_pen.circle(count / my_length / phi, my_angle)
                    f.save_thumb()
                    gold_hue_pen.circle(count / my_length / phi, - my_angle)
                    f.save_thumb()
                elif my_loops == 3:
                    pick_green()
                    gold_hue_pen.pencolor(my_loops * count % 255, my_loops * 80, my_range - count % 127)
                    gold_hue_pen.pensize(count / my_pensize / my_loops)
                    green_hue_pen.pensize(count / my_pensize / my_loops)
                    green_hue_pen.rt(my_angle)        
                    gold_hue_pen.left(my_angle)
                    green_hue_pen.fd(count / my_length)
                    f.save_thumb()
                    gold_hue_pen.fd(count / my_length)
                    f.save_thumb()
                    green_hue_pen.rt(my_angle / 2)
                    gold_hue_pen.left(my_angle / 2)
                    green_hue_pen.fd(count / my_length / 2)
                    f.save_thumb()
                    gold_hue_pen.fd(count / my_length / 2)
                    f.save_thumb()
                    green_hue_pen.circle(count / my_length / phi, my_angle)
                    f.save_thumb()
                    gold_hue_pen.circle(count / my_length / phi, - my_angle)
                    f.save_thumb()
    produce_video()
    finalize()



#  Group B Module_10
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module outputs 10 minute duration @ 1800 my_range setting, and 14 minutes @ 2040 my_range setting
# This module uses three pens per pass (4 passes)
# Last Run date
def stupendous_mandala():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Stupendous Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range(len(a.i_angle)):
        t.my_venv()
        make_p_turtles()
        my_angle = float(a.i_angle_auto[a.i])
        Lg.logger.info('Current angle to be drawn is ' + str(my_angle))
        t.my_title = f'Stupendous Mandala: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(f'Stupendous Mandala: {my_angle} Angle with {au.my_track}')
        count = 0
        turtle.bgcolor(10,10,20)
        my_range = 255 * 6  #Default is 2040; make it a multiple of 255 to sync end of cycle to 255 RGB modulo functions            
        all_pens_home() # Brings all pens, whether used or unused in this module, to 0,0 (Home) and setheader to angle.
        my_random = random.randint(150,255) # Varies the pencolor where used
        my_pensize = 180 # Divisor. Greater the number, the thinner the line drawn
        my_pensize_a = 280 # Divisor. Greater the number, the thinner the line drawn
        my_length = 6 # Divisor. Greater the number, the shorter the line drawn
        my_circle = 8 # Divisor. Greater the number, the shorter the line drawn
        my_length_bk = 6 # Divisor. Greater the number, the shorter the line drawn
        count = 0
        Lg.logger.info(f'{my_script}:Starting First Pass @ {Tm.this_time}')
        pa =  red_hue_pen
        pb =  magenta_hue_pen
        pc =  pa
        pa.setpos(0,0)
        pb.setpos(0,0)
        pc.setpos(0,0)
        for count in range(my_range): # First Pass
            pa.pencolor(my_random, 255, count % 150) # Pen red_hue_pen (Pen 1)
            pb.pencolor(255-count % 255, count % 255, count % 255) #Pen magenta_hue_pen  (Pen 2)
            pc.pencolor(count % 255, count % 127, my_random - count % 150) #Pen pa  (Pen 3)
            turtle.bgcolor(10,0,0)
            run_stupendous()
        Lg.logger.info(f'{my_script}:Starting Second Pass @ {Tm.this_time}')
        pa =  indigo_hue_pen
        pb =  green_hue_pen
        pc =  gold_hue_pen
        pa.setpos(0,0)
        pb.setpos(0,0)
        pc.setpos(0,0)
        for count in range(my_range): # Second Pass
            pa.pencolor(count % 255, my_random, 255) #Pen indigo_hue_pen (Pen 1)
            pb.pencolor(25, count % 255, count % 127) #Pen green_hue_pen (Pen 2)
            pc.pencolor(count % 127, count % 255, 255 -count % 255) # Pen gold_hue_pen (Pen 3)
            turtle.bgcolor(0,10,0)
            run_stupendous()
        pa =  red_hue_pen
        pb =  magenta_hue_pen
        pc =  pa  
        pa.setpos(0,0)
        pb.setpos(0,0)
        pc.setpos(0,0)    
        Lg.logger.info(f'{my_script}:Starting Third Pass @ {Tm.this_time}')
        for count in range(my_range): # Third Pass
            pa.pencolor(127 - count % 127, 255-count% 255, count % 255) # Pen red_hue_pen (Pen 1)
            pb.pencolor(count % 255, my_random, 255 - count% 255) #Pen magenta_hue_pen  (Pen 2)
            pc.pencolor(255- count % 255, count % 255, 255) #Pen pa  (Pen 3)
            turtle.bgcolor(0,0,10)
            run_stupendous()
        pa =  indigo_hue_pen
        pb =  green_hue_pen
        pc =  gold_hue_pen    
        pa.setpos(0,0)
        pb.setpos(0,0)
        pc.setpos(0,0)
        Lg.logger.info(f'{my_script}:Starting Fourth Pass @ {Tm.this_time}')
        for count in range(my_range): # Fourth Pass
           
           pick_gold() #Pen gold_hue_pen (Pen 3)
           pb.pencolor(count % 255, 255 - count % 255, 255 - count % 255) #Pen green_hue_pen (Pen 2)
           pa.pencolor(count % 127, count % 255, 255 - count % 255) # Pen gold_hue_pen (Pen 3)
           turtle.bgcolor(10,10,0)
           run_stupendous()
            
    reset_all()    
    produce_reversing_video()
    finalize()
# stupendous_mandala()



#  Group B Module_11
#**************************************************************************************************************
'''This script features pens: pa, pb, blue_hued_pen, magenta_hued_pen, red_hued_pen, gold_hued_pen,
indigo_hued_pen, green_hued_pen, light_hued_pen, yellow_hued_pen.
#They follow separate yet coordinated routes to compose the mandala.
#Duration at 18 minutes for length value of 600.
'''
#+++++++++++MODULE  Courage Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
def courage_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range
    my_script = 'Courage Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = int(a.i_angle_float[a.i])
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        make_p_turtles()
        my_hue = random.randint(5, 100)
        my_hue_a = random.randint(100, 200)
        Lg.logger.info('The value of my_hue is' + '   ' + str(my_hue))
        Lg.logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
        count = 0
        my_range =  255 # Best with multiples of 255
        fd_01, fd_02, fd_03, fd_04 = 1.2, 1.2, 1.2, 1.2
        circ_01, circ_02, circ_03 = 18, 24, 32
        bk_01 = 6
        Lg.logger.info(f'{my_script}:First pass starting @ {Tm.my_time}')
        for count in range(my_range): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)      
            pick_blue() # Blue pen
            R, G, B, L, M, N, D, E, F=  my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255  
            if count <= .75*count:
                blue_hue_pen.color( D + count %75, E, F - count %75)
            else:
                pick_blue()
            pa.pencolor( M, L - count %255, E)   
            pb.pencolor( R, G - count %255 ,  count %255)
            pb.left(my_angle)
            blue_hue_pen.left(my_angle)
            pa.left( -my_angle)
            pb.fd( count / fd_01)
            f.save_thumb()
            blue_hue_pen.fd( count + phi )
            f.save_thumb()
            pa.fd( count / fd_02)
            f.save_thumb()
            pb.rt(my_angle)
            blue_hue_pen.left( - my_angle)
            pa.rt( my_angle)
            blue_hue_pen.fd(count /fd_03)
            f.save_thumb()
            pa.fd(count  / fd_04)
            f.save_thumb()
            pb.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            blue_hue_pen.circle(count / circ_02,  my_angle)
            f.save_thumb()
            pa.circle(count / circ_03, my_angle)
            f.save_thumb()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            f.save_thumb()
            pb.pendown()
            pb.pencolor(255,255, count % 255)
            pb.dot(count/36)
            f.save_thumb()
            blue_hue_pen.pensize(count /145)
            pb.pensize(count /150 )
            pa.pensize(count /72)
            process_thumbs()
        count = 0
        reset_p_pens()
        reset_random_hue_pens()
        all_pens_home()
        Lg.logger.info(f'{my_script}:Second pass starting @ {Tm.my_time}')
        for count in range(my_range): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0) 
            pick_magenta() # Magenta pen 
            R, G, B, L, M, N, D, E, F=  my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255  
            if count <= .75*count:
                magenta_hue_pen.color(F - count %255, E, D + count %255)
            else:
                pick_magenta()
            pa.pencolor( L - count %255, M,  E)   
            pb.pencolor( G - count %255 ,  count %255, R )
            pb.left(my_angle)
            magenta_hue_pen.left(my_angle)
            pa.left( -my_angle)
            pb.fd( count / fd_01)
            f.save_thumb()
            magenta_hue_pen.fd( count + phi )
            f.save_thumb()
            pa.fd( count / fd_02)
            f.save_thumb()
            pb.rt(my_angle)
            magenta_hue_pen.left( - my_angle)
            pa.rt( my_angle)
            magenta_hue_pen.fd(count /fd_03)
            f.save_thumb()
            pa.fd(count  / fd_04)
            f.save_thumb()
            pb.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            magenta_hue_pen.circle(count / circ_02,  my_angle)
            f.save_thumb()
            pa.circle(count / circ_03, my_angle)
            f.save_thumb()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            f.save_thumb()
            pb.pendown()
            pb.pencolor(255,255,10)
            pb.dot(count/36)
            f.save_thumb()
            magenta_hue_pen.pensize(count  / 145)
            pb.pensize(count  / 150 )
            pa.pensize(count  / 72)
            process_thumbs()
        count = 0
        reset_p_pens()
        reset_random_hue_pens()
        all_pens_home()    
        Lg.logger.info(f'{my_script}:Third pass starting @ {Tm.my_time}')
        for count in range(my_range): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)     
            pick_green() # Green pen
            R, G, B, L, M, N, D, E, F=  my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255  
            if count <= .75*count:
                 green_hue_pen.color(F - count %255, E, D + count %255)
            else:
                pick_green()
            pa.pencolor( E, M, L - count %255)   
            pb.pencolor( G - count %255,  R, count %255)
            pb.left(my_angle)
            green_hue_pen.left(my_angle)
            pa.left( -my_angle)
            pb.fd( count / fd_01)
            f.save_thumb()
            green_hue_pen.fd( count + phi )
            f.save_thumb()
            pa.fd( count / fd_02)
            f.save_thumb()
            pb.rt(my_angle)
            green_hue_pen.left( - my_angle)
            pa.rt( my_angle)
            green_hue_pen.fd(count /fd_03)
            f.save_thumb()
            pa.fd(count  / fd_04)
            f.save_thumb()
            pb.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            green_hue_pen.circle(count / circ_02,  my_angle)
            f.save_thumb()
            pa.circle(count / circ_03, my_angle)
            f.save_thumb()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            f.save_thumb()
            pb.pendown()
            pb.pencolor(255,255,10)
            pb.dot(count/36)
            f.save_thumb()
            green_hue_pen.pensize(count  / 145)
            pb.pensize(count  / 150 )
            pa.pensize(count  / 72)
            process_thumbs()
        count = 0
        reset_p_pens()
        reset_random_hue_pens()
        all_pens_home()    
        Lg.logger.info(f'{my_script}:Fourth pass starting @ {Tm.my_time}')
        for count in range(my_range): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)     
            pick_gold() # Gold pen 
            R, G, B, L, M, N, D, E, F=  my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255  
            if count <= .75*count:
                gold_hue_pen.color(F - count %255, E, count %255)
            else:
                pick_gold()
            pa.pencolor( L - count %255, M,  E)   
            pb.pencolor( G - count %255 ,  count %255, R )
            pb.left(my_angle)
            gold_hue_pen.left(my_angle)
            pa.left( -my_angle)
            pb.fd( count / fd_01)
            f.save_thumb()
            gold_hue_pen.fd( count + phi )
            f.save_thumb()
            pa.fd( count / fd_02)
            f.save_thumb()
            pb.rt(my_angle)
            gold_hue_pen.left( - my_angle)
            pa.rt( my_angle)
            gold_hue_pen.fd(count /fd_03)
            f.save_thumb()
            pa.fd(count  / fd_04)
            f.save_thumb()
            pb.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            gold_hue_pen.circle(count / circ_02,  my_angle)
            f.save_thumb()
            pa.circle(count / circ_03, my_angle)
            f.save_thumb()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            f.save_thumb()
            pb.pendown()
            pb.pencolor(255,255,10)
            pb.dot(count/36)
            f.save_thumb()
            gold_hue_pen.pensize(count  / 145)
            pb.pensize(count  / 150 )
            pa.pensize(count  / 72)
            process_thumbs()
        count = 0
        reset_p_pens()
        reset_random_hue_pens()
        all_pens_home()
        Lg.logger.info(f'{my_script}:Fifth pass starting @ {Tm.my_time}')
        for count in range(my_range): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0) 
            pick_indigo() # Indigo  pen
            R, G, B, L, M, N, D, E, F=  my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255  
            if count <= .75*count:
                 indigo_hue_pen.color(F - count %255, E, D + count %255)
            else:
                pick_indigo()
            pa.pencolor(G - count %255 ,  count %255, R )   
            pb.pencolor(L - count %255, M,  E )
            pb.left(my_angle)
            indigo_hue_pen.left(my_angle)
            pa.left( -my_angle)
            pb.fd( count / fd_01)
            f.save_thumb()
            indigo_hue_pen.fd( count + phi )
            f.save_thumb()
            pa.fd( count / fd_02)
            f.save_thumb()
            pb.rt(my_angle)
            indigo_hue_pen.left( - my_angle)
            pa.rt( my_angle)
            indigo_hue_pen.fd(count /fd_03)
            f.save_thumb()
            pa.fd(count  / fd_04)
            f.save_thumb()
            pb.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            indigo_hue_pen.circle(count / circ_02,  my_angle)
            f.save_thumb()
            pa.circle(count / circ_03, my_angle)
            f.save_thumb()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            f.save_thumb()
            pb.pendown()
            pb.pencolor(255,255,10)
            pb.dot(count/36)
            f.save_thumb()
            indigo_hue_pen.pensize(count  / 145)
            pb.pensize(count  / 150 )
            pa.pensize(count  / 72)
            process_thumbs()
        count = 0
        reset_p_pens()
        reset_random_hue_pens()
        all_pens_home()    
        Lg.logger.info(f'{my_script}:Sixth pass starting @ {Tm.my_time}')
        for count in range(my_range): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)      #.bg_fade_skyblue_to_dark()
            pick_red() # Red pen 
            R, G, B, L, M, N, D, E, F=  my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255  
            if count <= .75*count:
                red_hue_pen.color(F - count %255, E, D + count %255)
            else:
                pick_red()
            pa.pencolor( E, M, count %255)   
            pb.pencolor( G - count %255 ,  count %255, R )
            pb.left(my_angle)
            red_hue_pen.left(my_angle)
            pa.left( -my_angle)
            pb.fd( count / fd_01)
            f.save_thumb()
            red_hue_pen.fd( count + phi )
            f.save_thumb()
            pa.fd( count / fd_02)
            f.save_thumb()
            pb.rt(my_angle)
            red_hue_pen.left( - my_angle)
            pa.rt( my_angle)
            red_hue_pen.fd(count /fd_03)
            f.save_thumb()
            pa.fd(count  / fd_04)
            f.save_thumb()
            pb.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            red_hue_pen.circle(count / circ_02,  my_angle)
            f.save_thumb()
            pa.circle(count / circ_03, my_angle)
            f.save_thumb()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            f.save_thumb()
            pb.pendown()
            pb.pencolor(255,255,10)
            pb.dot(count/36)
            f.save_thumb()
            red_hue_pen.pensize(count  / 145)
            pb.pensize(count  / 150 )
            pa.pensize(count  / 72)
            process_thumbs()
        count = 0
        reset_p_pens()
        reset_random_hue_pens()
        all_pens_home()
        Lg.logger.info(f'{my_script}:Seventh pass starting @ {Tm.my_time}')
        for count in range(my_range): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0) 
            pick_orange() # Orange pen
            R, G, B, L, M, N, D, E, F=  my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255  
            if count <= .75*count:
                orange_hue_pen.color(F - count %255, E, D + count %255)
            else:
                pick_orange()
            pa.pencolor( L - count %255, M,  E)   
            pb.pencolor( G - count %255 ,  count %255, R )
            pb.left(my_angle)
            orange_hue_pen.left(my_angle)
            pa.left( -my_angle)
            pb.fd( count / fd_01)
            f.save_thumb()
            orange_hue_pen.fd( count + phi )
            f.save_thumb()
            pa.fd( count / fd_02)
            f.save_thumb()
            pb.rt(my_angle)
            orange_hue_pen.left( - my_angle)
            pa.rt( my_angle)
            orange_hue_pen.fd(count /fd_03)
            f.save_thumb()
            pa.fd(count  / fd_04)
            f.save_thumb()
            pb.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            orange_hue_pen.circle(count / circ_02,  my_angle)
            f.save_thumb()
            pa.circle(count / circ_03, my_angle)
            f.save_thumb()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            f.save_thumb()
            pb.pendown()
            pb.pencolor(255,255,10)
            pb.dot(count/36)
            f.save_thumb()
            orange_hue_pen.pensize(count  / 145)
            pb.pensize(count  / 150 )
            pa.pensize(count  / 72)
            process_thumbs()
        count = 0
        reset_p_pens()
        reset_random_hue_pens()
        all_pens_home()    
        Lg.logger.info(f'{my_script}:Eighth pass starting @ {Tm.my_time}')
        for count in range(my_range): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)      #.bg_fade_skyblue_to_dark()
            pick_yellow() # Yellow pen 
            R, G, B, L, M, N, D, E, F=  my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255  
            if count <= .75*count:
                yellow_hue_pen.color(F - count %255, E, D + count %255)
            else:
                pick_yellow()
            pb.pencolor( L - count %255, M,  E)   
            pa.pencolor( G - count %255 ,  count %255, R )
            pb.left(my_angle)
            yellow_hue_pen.left(my_angle)
            pa.left( -my_angle)
            pb.fd( count / fd_01)
            f.save_thumb()
            yellow_hue_pen.fd( count + phi )
            f.save_thumb()
            pa.fd( count / fd_02)
            f.save_thumb()
            pb.rt(my_angle)
            yellow_hue_pen.left( - my_angle)
            pa.rt( my_angle)
            yellow_hue_pen.fd(count /fd_03)
            f.save_thumb()
            pa.fd(count  / fd_04)
            f.save_thumb()
            pb.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            yellow_hue_pen.circle(count / circ_02,  my_angle)
            f.save_thumb()
            pa.circle(count / circ_03, my_angle)
            f.save_thumb()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            f.save_thumb()
            pb.pendown()
            pb.pencolor(255,255,10)
            pb.dot(count/36)
            f.save_thumb()
            yellow_hue_pen.pensize(count  / 145)
            pb.pensize(count  / 150 )
            pa.pensize(count  / 72)
            process_thumbs()
        count = 0
        reset_p_pens()
        reset_random_hue_pens()
        all_pens_home()
        Lg.logger.info(f'{my_script}:Ninth pass starting @ {Tm.my_time}')
        for count in range(my_range): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0) 
            pick_light() # Light pen 
            R, G, B, L, M, N, D, E, F=  my_hue, 255, 0, 255, my_hue_a, 0, 0, my_hue, 255  
            if count <= .75*count:
                light_hue_pen.color(F - count %255, E, D + count %255)
            else:
                pick_light()
            pa.pencolor( L - count %255, M,  E)   
            pb.pencolor( G - count %255 ,  count %255, R )
            pb.left(my_angle)
            light_hue_pen.left(my_angle)
            pa.left( -my_angle)
            pb.fd( count / fd_01)
            f.save_thumb()
            light_hue_pen.fd( count + phi )
            f.save_thumb()
            pa.fd( count / fd_02)
            f.save_thumb()
            pb.rt(my_angle)
            light_hue_pen.left( - my_angle)
            pa.rt( my_angle)
            light_hue_pen.fd(count /fd_03)
            f.save_thumb()
            pa.fd(count  / fd_04)
            f.save_thumb()
            pb.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            light_hue_pen.circle(count / circ_02,  my_angle)
            f.save_thumb()
            pa.circle(count / circ_03, my_angle)
            f.save_thumb()
            pb.penup()
            pb.left(my_angle)
            pb.backward(count / bk_01)
            f.save_thumb()
            pb.pendown()
            pb.pencolor(255,255,10)
            pb.dot(count/36)
            f.save_thumb()
            light_hue_pen.pensize(count  / 145)
            pb.pensize(count  / 150 )
            pa.pensize(count  / 72)
            process_thumbs()
    produce_reversing_video()        
    finalize()
# courage_mandala()

#  Group B Module_12
#**************************************************************************************************************
'''This script features pens: pa, pb, blue_hue_pen, red_hue_pen, 
green_hue_pen, yellow_hue_pen. The intent is to follow the four primary colors
red, yellow, green, blue.
They follow separate yet coordinated routes to compose the mandala.
'''
#+++++++++++MODULE  Courage Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
def spectrum_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range
    my_script = 'Spectrum Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = int(a.i_angle_float[a.i])
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        make_p_turtles()
        my_hue = random.randint(5, 100)
        my_hue_a = random.randint(100, 200)
        Lg.logger.info(f'The value of my_hue is {my_hue}')
        Lg.logger.info(f'The value of my_hue_a is {my_hue_a}')
        count = 0
        my_range = 509 # Best with multiples of 255
        fd_01, fd_02, fd_03, fd_04 = 1.2, 1.2, 1.2, 1.2
        circ_01, circ_02, circ_03 = 18, 24, 32
        bk_01 = 6
        def spectrum_mandala_script():
            my_p_pen_02.left(my_angle)
            my_p_pen_02.fd(count / fd_01)
            f.save_thumb()
            
            my_hue_pen.left(my_angle)
            my_hue_pen.fd(count / fd_02)
            f.save_thumb()
            
            my_p_pen_01.rt(my_angle)
            my_p_pen_01.fd(count / fd_02)
            f.save_thumb()
            
            my_hue_pen.rt(my_angle)
            my_hue_pen.fd(count / fd_03)
            f.save_thumb()
            
            my_p_pen_02.left(my_angle)
            my_p_pen_02.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            
            my_hue_pen.left(my_angle /2)
            my_hue_pen.circle(count / circ_02,  my_angle)
            f.save_thumb()
            
            my_p_pen_01.rt(my_angle)
            my_p_pen_01.fd(count / fd_04)
            my_p_pen_01.circle(count / circ_03, my_angle)
            f.save_thumb()
            
            my_p_pen_02.penup()
            my_p_pen_02.left(my_angle)
            my_p_pen_02.backward(count / bk_01)
            f.save_thumb()
            my_p_pen_02.pendown()
            my_p_pen_02.pencolor(255, 255, 255) # White Dot
            my_p_pen_02.dot(count / 20)
            f.save_thumb()
            
            my_hue_pen.pensize(count / 145)
            my_p_pen_02.pensize(count / 145)
            my_p_pen_01.pensize(count / 126)
            process_thumbs()
         

        Lg.logger.info(f'{my_script}:First pass starting @ {Tm.my_time}')
        Lg.logger.info(f'Drawing with pens orange_hue_pen, pa, pb')
        for count in range(my_range): 
            turtle.bgcolor(0, 100, 150)      
            pick_orange() # Orange pen
            my_hue_pen = orange_hue_pen
            my_p_pen_01 = pa
            my_p_pen_02 = pb
            if count <= my_range / 2:
                my_p_pen_01.pencolor(count %255, 0, 0)
                my_p_pen_02.pencolor(128, 255 - count %128, 255 - count %255)
            else:
                my_p_pen_01.pencolor(255, 0, 0)  
                my_p_pen_02.pencolor(128, 128, random.randint(15,75))
            spectrum_mandala_script()
        count = 0
        clear_pa_pen()
        clear_pb_pen()
        clear_orange_hue_pen()
       
        
        Lg.logger.info(f'{my_script}:Second pass starting @ {Tm.my_time}')
        Lg.logger.info(f'Drawing with pens yellow_hue_pen, pa, pb')
        for count in range(my_range): 
            turtle.bgcolor(0, 50, 100)      
            pick_yellow() # yellow hue pen
            my_hue_pen = yellow_hue_pen
            my_p_pen_01 = pa
            my_p_pen_02 = pb
            if count <= my_range / 2:
                my_p_pen_01.pencolor(0, count %255, count %255)
                my_p_pen_02.pencolor(128, 255 - count %128, 255 - count %255)
            else:
                my_p_pen_01.pencolor(0, 255, 255)  
                my_p_pen_02.pencolor(random.randint(15,75), 128, 128)
            spectrum_mandala_script()
        count = 0
        clear_pa_pen()
        clear_pb_pen()
        clear_yellow_hue_pen()    
                  
         
        Lg.logger.info(f'{my_script}:Third pass starting @ {Tm.my_time}') #Green Band of Spectrum
        Lg.logger.info(f'Drawing with pens green_hue_pen, pa, pb')
        for count in range(my_range): #
            turtle.bgcolor(50, 150, 0)      
            pick_green() # green hue pen
            my_hue_pen = green_hue_pen
            my_p_pen_01 = pa
            my_p_pen_02 = pb
            if count <= my_range / 2:
                my_p_pen_02.pencolor(count %255, 0, count %255 )
                my_p_pen_01.pencolor(128, 255 - count %128, 255 - count %255)
            else:
                my_p_pen_02.pencolor(255, 0, 255)  
                my_p_pen_01.pencolor(128, random.randint(15,75), 128)
            spectrum_mandala_script()
        count = 0
        clear_pa_pen()
        clear_pb_pen()
        clear_green_hue_pen()    
            
         
        Lg.logger.info(f'{my_script}:Fourth pass starting @ {Tm.my_time}')
        Lg.logger.info(f'Drawing with pens blue_hue_pen, pa, pb')
        for count in range(my_range): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 50, 0)
            pick_blue() #Blue hue pen
            my_hue_pen = blue_hue_pen
            my_p_pen_01 = pa
            my_p_pen_02 = pb
            if count <= my_range / 2:
                my_p_pen_01.pencolor(count %255, 0, 0)
                my_p_pen_02.pencolor(255 - count %220, 255 - count %255, count %75)
            else:
                my_p_pen_01.pencolor(255, 0, 0)  
                my_p_pen_02.pencolor(220, 240, random.randint(15,75))
            spectrum_mandala_script()
        count = 0
        clear_pa_pen()
        clear_pb_pen()
        clear_blue_hue_pen() 
                

        Lg.logger.info(f'{my_script}:Fifth pass starting @ {Tm.my_time}')
        Lg.logger.info(f'Drawing with pens gold_hue_pen, light_hue_pen, cyan_hue_pen')
        for count in range(my_range): 
            turtle.bgcolor(0, 0, 0)      
            pick_gold() # Red hue pen
            pick_light() #Green hue pen
            pick_cyan()  #Cyan hue Pen
            my_hue_pen = gold_hue_pen
            my_p_pen_01 = light_hue_pen
            my_p_pen_02 = cyan_hue_pen
            spectrum_mandala_script()
        count = 0
        clear_gold_hue_pen()
        clear_cyan_hue_pen()
        clear_light_hue_pen()
      
    produce_reversing_video()        
    finalize()
# spectrum_mandala()


#  Group B Module_11
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala_extended():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Brave Mandala Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        for r in range(2):
            pa.penup()
            magenta_hue_pen.penup()
            pa.setpos(0,0)
            magenta_hue_pen.setpos(0,0)
            pa.seth(my_angle)
            magenta_hue_pen.seth(my_angle)
            pa.pendown()
            magenta_hue_pen.pendown()
            pa.speed(0)
            magenta_hue_pen.speed(0)
            turtle.bgcolor(0,0,0)
            R = 0
            G = 0
            B = 255
            L = random.randrange(10, 100, 10)
            Lg.logger.info('The value of color L :   ' + str(L))
            M = 255
            N = 255
            X = 255
            Y = 255
            Z =  random.randrange(175, 255, 10)
            Lg.logger.info('The value of color Z :   ' + str(Z))
            my_pensize = 36
            my_range = 500
            pa.seth(my_angle)
            magenta_hue_pen.seth(my_angle)
            Lg.logger.info('Starting 1st Loop...')
            for count in range( my_range):  # First Pass
                pa.pensize(count / my_pensize)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()  #Screenshot as a png
                pa.pencolor(count %255, 100 - count %75 , L)
                magenta_hue_pen.pensize(count /  my_pensize / 3)
                magenta_hue_pen.pencolor(Y - count %255, Z, L)
                magenta_hue_pen.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                pa.rt(my_angle)
                pa.pencolor(L, M - count %127, N - count %127)
                pa.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()  #Screenshot as a png
            all_pens_home()
            Lg.logger.info('Starting 2nd Loop...')
            for count in range( my_range + 3): # Second Pass
                pa.pensize(count/ my_pensize)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()  #Screenshot as a png
                magenta_hue_pen.pencolor(B - count %100, R, G + count %99 )
                magenta_hue_pen.pensize(count /  my_pensize /3)
                pa.pencolor(count %200, 255 - count %150, L)
                magenta_hue_pen.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                pa.rt(my_angle)
                pa.pencolor(Z, M - count %127, N)
                pa.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()    #Screenshot as a png
            all_pens_home()
            Lg.logger.info('Starting 3rd Loop...')
            for  count  in range(my_range + 6):  #Third Pass
                pa.pensize(count /  my_pensize)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()  #Screenshot as a png
                pa.pencolor(count %90,  count %90, B - count %150)
                magenta_hue_pen.pensize(count /  my_pensize /3)
                magenta_hue_pen.pencolor(Z, 255 - count %100, L)
                magenta_hue_pen.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                pa.rt(my_angle)
                pa.pencolor(L, M - count %127, N - count %127)
                pa.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()    #Screenshot as a png
            all_pens_home()
            Lg.logger.info('Starting 4th Loop...')
            for count in range( my_range + 12): # Fourth Pass
                pa.pensize(count / my_pensize)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()  #Screenshot as a png
                magenta_hue_pen.pencolor(L,  Z, B - count %75)
                magenta_hue_pen.pensize(count / my_pensize/3)
                pa.pencolor(255 - count %150, R, L)
                magenta_hue_pen.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                pa.rt(my_angle)
                pa.pencolor(L, 255 - count %127, 255 - count %127)
                pa.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()  #Screenshot as a png
            all_pens_home()
            Lg.logger.info('Starting 5th Loop...')
            for count in range( my_range + 18): # Fifth Pass
                pa.pensize(count / my_pensize)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()  #Screenshot as a png
                pa.pencolor(R, count %84, count %125)
                magenta_hue_pen.pensize(count / my_pensize/3)
                magenta_hue_pen.pencolor(R, 255 - count %100, L)
                magenta_hue_pen.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                pa.rt(my_angle)
                pa.pencolor(Z, M - count %127, N)
                pa.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()    #Screenshot as a png
            all_pens_home()
            Lg.logger.info('Starting 6th Loop...')
            for count  in range(my_range + 24):  # Sixth Pass
                pa.pensize(count / my_pensize)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()  #Screenshot as a png
                magenta_hue_pen.pencolor(R, count %25, 100 - count %50)
                magenta_hue_pen.pensize(count / my_pensize /3)
                magenta_hue_pen.pencolor(Z, 255 - count %150, L)
                magenta_hue_pen.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                pa.rt(my_angle)
                pa.pencolor(L, 255 - count %255,  count %255)
                pa.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()    #Screenshot as a png     
            all_pens_home()
            Lg.logger.info('Starting 7th Loop...')
            for count  in range(my_range + 30): # Seventh Pass
                pick_light() #Pen light_hue_pen
                pick_magenta() # Pen magenta_hue_pen
                pa.pensize(count / my_pensize)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()  #Screenshot as a png
                magenta_hue_pen.pencolor(100 - count %50, Z, L)
                magenta_hue_pen.pensize(count/my_pensize /3)
                magenta_hue_pen.pencolor(R, 255 - count %150, L)
                magenta_hue_pen.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                pa.rt(my_angle)
                pa.pencolor(L, count %127, Z)
                pa.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()    #Screenshot as a png     
    produce_video()
    finalize()    
        
            

#  module_5
#*****************************************************************************************************************************
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def reverent_mandala():  # Uses 2 pens with offset phi angle
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range
    my_script = 'Reverent Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        all_pens_home()
        my_angle = a.i_angle_float[a.i]
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle:.2f} @ {Tm.this_time}')
        turtle.title(f'Reverent Mandala: {my_angle} Degrees Angle and {au.my_track}')
        t.my_title = turtle.title
        count = 0
        my_range =  765
        blue_hue_pen.speed(0)
        gold_hue_pen.speed(0)
        red_hue_pen.speed(0)
        turtle.bgcolor(10, 0, 15)
        for count in range(my_range):    #900 is default. Use lower number for testing.
                magenta_hue_pen.pensize(count / 300)
                gold_hue_pen.pensize(count / 300)
                green_hue_pen.pensize(count / 225)
                pick_magenta() #magenta_hue_pen
                pick_gold() # gold_hue_pen
                pick_green() # green_hue_pen
                gold_hue_pen.left(my_angle / phi)
                gold_hue_pen.left(my_angle)
                gold_hue_pen.fd((count * .8)*.33)
                f.save_thumb()
                gold_hue_pen.penup()
                gold_hue_pen.fd((count * .8)*.33)
                f.save_thumb()
                gold_hue_pen.pendown()
                gold_hue_pen.fd((count * .8)*.34)
                f.save_thumb()
                magenta_hue_pen.left(my_angle)
                magenta_hue_pen.circle(count / 4, my_angle, 6)
                f.save_thumb()
                green_hue_pen.rt(my_angle)
                green_hue_pen.fd(count / phi)
                f.save_thumb()
                gold_hue_pen.left(my_angle)
                gold_hue_pen.fd(count /4)
                f.save_thumb()
                magenta_hue_pen.left(my_angle)
                magenta_hue_pen.fd(count / 4)
                process_thumbs()
        reset_random_hue_pens()
    produce_reversing_video()
    finalize()
# reverent_mandala()







#  module_7
#+++++++++++MODULE DARK MANDALA+++++++++++++++++++++++++++++++++++++++++++++++++++++
def dark_mandala():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Dark Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        all_pens_home()
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info(f'{my_script}:DarkMandala: Current angle to be drawn is {my_angle:.2f}')
        turtle.title(f'dark_mandala: {my_angle} Degrees Angle and {au.my_track}')
        t.my_title = f'dark_mandala: {my_angle} Degrees Angle and {au.my_track}'
        turtle.bgcolor(50, 50, 10)
        for count in range(150):
            dark_hue_pen.pensize(count / 36)
            magenta_hue_pen.pensize(count /84)
            indigo_hue_pen.pensize(count / 48)
            if count <= 75:
                dark_hue_pen.pencolor(200, 50, 255- count % 150)
                magenta_hue_pen.pencolor(255 - count % 150, 10, 30)
                indigo_hue_pen.pencolor(count % 50, 10, 100)
            else:
                pick_magenta() #pen magenta_hue_pen
                pick_dark()  # pen dark_hue_pen
                pick_indigo() # pen indigo_hue_pen
#             dark_hue_pen.circle(count, my_angle)
#             f.save_thumb()
            dark_hue_pen.penup()
            dark_hue_pen.right(my_angle)
            dark_hue_pen.backward(count)
            f.save_thumb()
            dark_hue_pen.pendown()
            indigo_hue_pen.fd(count / t.pi)
            f.save_thumb()
            dark_hue_pen.right(my_angle)
            dark_hue_pen.fd(count )
            f.save_thumb()
            indigo_hue_pen.right(my_angle)
            indigo_hue_pen.fd(count )
            f.save_thumb()
            indigo_hue_pen.fd(count / phi)
            f.save_thumb()
#             indigo_hue_pen.circle(count  - my_angle)
#             f.save_thumb()
        #make dots
            magenta_hue_pen.left(my_angle)
            magenta_hue_pen.fd(count )
            f.save_thumb()
            magenta_hue_pen.dot(count /50)
            f.save_thumb()
            magenta_hue_pen.penup()
            magenta_hue_pen.backward(count)
            f.save_thumb()
            magenta_hue_pen.pendown()
            magenta_hue_pen.fd(count)
            f.save_thumb()
            magenta_hue_pen.dot(3)
            f.save_thumb()
#             magenta_hue_pen.circle(count, my_angle)
#             f.save_thumb()
    produce_reversing_video()
    finalize()




#  module_18
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Status: Last Update: 11/29/2023, Last Completed Run: 11/29/2023
  Uses local turtle pens pa and yellow_hue_pen; Implmented re-intializing the pens
  to speed up the drawing. Fine-tuning the timer functions to document execution time.
  Duration is based upon quantity of angles selected.
 '''
def Vanguard_Mandala():  # Formerly Pretty Awesome Mandala (name changed on 11/29/2023)
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range, pa
    my_script = 'Vanguard Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_range = 512  * 3 #Default is 512; use shorter range to test
    my_pensize = 84 * 4 # Default is 84
    my_pensize_a = 102 * 4 # Default is 102
    for a.i  in range( len(a.i_angle)):
        my_angle = a.i_angle_float[a.i]
        Lg.logger.info(f'{my_script}: Starting to draw {my_angle:.2f} degrees angles at {Tm.this_time}')
        turtle.title(f'{my_script}:{my_angle} Degrees Angle and {au.my_track}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.bgcolor(10, 0, 0)
        make_turtle_pa()
        all_pens_home()
        R = 0
        G = 255
        B = random.randrange(100, 255, 1)
        Lg.logger.info(f'{my_script}:The value of hue B is  {B}')
        L = random.randrange(1, 100, 1)
        Lg.logger.info(f'{my_script}:The value of hue L is  {L}')
        all_pens_home()
        # 255 is default, use lower number for testing
        for count in range(my_range):
            pick_gold()
            gold_hue_pen.circle(count /t.pi, -my_angle, 3)
            f.save_thumb()
            gold_hue_pen.pensize(count / my_pensize_a)
            pa.pencolor(count % 180, B, G - count %240)
            pa.fd(count /9)
            f.save_thumb()
            pa.left(my_angle)
            pa.pensize(count / my_pensize)
            process_thumbs()
        reset_all_pens()    
    produce_reversing_video()
    finalize()
# Vanguard_Mandala()






def Plain_mandala():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Plain Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_range, my_pensize = 900, 150  # 900, 150 are default
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info(f'{my_script}:PlainMandala:Current angle to be drawn is {my_angle:.2f}')
        turtle.title(f'Plain_mandala: {my_angle} Degrees Angle and {au.my_track}')
        t.my_title = f'Plain_mandala: {my_angle} Degrees Angle and {au.my_track}'
        turtle.bgcolor(0, 0, 10)
        t.set_up_lg()
        t.set_up_ly()
        t.set_up_me()
        t.set_up_el()
        t.set_up_go()
        t.set_up_li()
        t.set_up_lu()
        t.set_up_lb()
        t.set_up_lq()
        t.set_up_ce()
        t.set_up_lg()
        t.set_up_lr()
        for count in range(my_range):
            pick_green() # Pen green_hue_pen
            pick_yellow() # Pen yellow_hue_pen
            yellow_hue_pen.left(my_angle)
            yellow_hue_pen.fd(count )
            f.save_thumb()
            green_hue_pen.rt(my_angle)
            green_hue_pen.fd(count)
            f.save_thumb()
            yellow_hue_pen.pensize(count / my_pensize)
            green_hue_pen.pensize(count / my_pensize)
        all_pens_home()    
        for count in range(my_range):
            pick_magenta() # Pen magenta_hue_pen
            pick_light() # Pen pa
            pa.left(my_angle)
            pa.fd(count )
            f.save_thumb()
            magenta_hue_pen.rt(my_angle)
            magenta_hue_pen.fd(count)
            f.save_thumb()
            pa.pensize(count / my_pensize)
            magenta_hue_pen.pensize(count / my_pensize)
        all_pens_home()                              
        for count in range(my_range):
            pick_indigo() # Pen indigo_hue_pen
            pick_gold() # Pen gold_hue_pen
            indigo_hue_pen.left(my_angle)
            indigo_hue_pen.fd(count )
            f.save_thumb()
            gold_hue_pen.rt(my_angle)
            gold_hue_pen.fd(count)
            f.save_thumb()
            indigo_hue_pen.pensize(count / my_pensize)
            gold_hue_pen.pensize(count / my_pensize)
        all_pens_home()    
        for count in range(my_range):
            pick_red() # Pen red_hue_pen
            pick_blue() # Pen blue_hue_pen
            red_hue_pen.left(my_angle)
            red_hue_pen.fd(count )
            f.save_thumb()
            blue_hue_pen.rt(my_angle)
            blue_hue_pen.fd(count)
            f.save_thumb()
            red_hue_pen.pensize(count / my_pensize)
            blue_hue_pen.pensize(count / my_pensize)
        all_pens_home()    
        for count in range(my_range):
            pick_orange() # Pen orange_hue_pen
            pick_random() # Pen random_hue_pen
            orange_hue_pen.left(my_angle)
            orange_hue_pen.fd(count )
            f.save_thumb()
            random_hue_pen.rt(my_angle)
            random_hue_pen.fd(count)
            f.save_thumb()
            orange_hue_pen.pensize(count / my_pensize)
            random_hue_pen.pensize(count / my_pensize)
        all_pens_home()     
        for count in range(my_range):
            pick_green() # Pen green_hue_pen
            pick_random_a() # Pen cyan_hue_pen
            cyan_hue_pen.left(my_angle)
            cyan_hue_pen.fd(count )
            f.save_thumb()
            green_hue_pen.rt(my_angle)
            green_hue_pen.fd(count)
            f.save_thumb()
            green_hue_pen.pensize(count / my_pensize)
            cyan_hue_pen.pensize(count / my_pensize)    
    produce_reversing_video()
    finalize()        
        



#  module_19
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Status: Last Update: 09/22/2023, Last Completed Run: 09/22/2023
  Uses local turtle pens pa and pb; Discovered that re-intializing the pens speeds up the drawing.
  Using local functions; will revise subsequent scripts using this one as a model structure.
  Duration is based upon quantity of angles selected.
 '''
def mighty_awesome_mandala():  # Based on pretty_awesome Mandala
    global my_project, my_angle, my_title, my_script, str_angles, my_range, count, pa, pb
    my_script = 'Mighty Awesome Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        def make_turtle_pa():
            global pa
            pa = turtle.Turtle()
            pa.speed(0)
            pa.shape('blank')
            pa.pensize(1)
            pa.setpos(0,0)
        def make_turtle_pb():
            global pb
            pb = turtle.Turtle()
            pb.speed(0)
            pb.shape('blank')
            pb.pensize(1)
            pb.setpos(0,0)
        my_angle = float(a.i_angle_float[a.i])
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:Current angle to be drawn is {my_angle:.2f}')
        t.my_title = f'MightyAwesomeMandala: {my_angle:.2f} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0, 0, 10)
        all_pens_home()
        t.my_angles = str_angles
        t.my_splash = my_project + str(au.my_track)
        R = random.randint(10, 200)
        G = 0
        B = 255
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:The value of hue R is {R}')
        L = random.randint(10, 100)
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:The value of hue L is {L}')
        def do_mighty_awesome():
                pa.pensize(count / my_pensize)
                pb.pensize(count / my_pensize)
                pa.rt(my_angle)
                pa.fd(count)
                f.save_thumb()
                pb.rt(my_angle)
                pb.circle(count, - my_angle)
    #             pb.circle(count + phi, - my_angle)
                f.save_thumb()
                check_memory() # Uncomment for testing
        my_range = 765 #Default is 510
        count = 0
        my_pensize = 72
        make_turtle_pa()
        make_turtle_pb()
        def reset_pa_pb():
            pa.reset()
            pb.reset()
            gc.collect()
            make_turtle_pa()
            make_turtle_pb()
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:Starting First Pass @ {Tm.this_time}')
        for count in range(my_range):
            pa.pencolor(R + count % 55, count % 255, B - count % 255)
            pb.pencolor(L + count % 155, B - count %B, count % B )
            do_mighty_awesome()
            Lg.logger.info(f'MightyAwesomeMandala:Completed loop count {count} of First Pass, {my_angle}: {Tm.this_time}') # Uncomment for testing
        R = random.randint(10, 200)
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:The value of hue R is {R} ')
        L = random.randint(175, 255)
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:The value of hue L is {L}')
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:Starting Second Pass @ {Tm.this_time}')
        reset_pa_pb()
        for count in range(my_range): # Second pass
            pa.pencolor(B - count % 100, count % B, L - count % 175)
            pb.pencolor(B - count % B, count % 50, count %B)
            do_mighty_awesome()
            Lg.logger.info(f'{my_script}:MightyAwesomeMandala:Completed loop count {count} of Second Pass, {my_angle}: {Tm.this_time}') # Uncomment for testing
        count = 0
        R = random.randint(10, 200)
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:The value of hue R is {R}')
        L = random.randint(10, 200)
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:The value of hue L is {L}')
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:Starting Third Pass @ {Tm.this_time}')
        reset_pa_pb()
        for count in range(my_range): # Third pass
            pa.pencolor(count % 84, count % B, R + count % 55)
            pb.pencolor(count % 50, L + count % 55, R + count %55)                                                                                                                                                                                                                                                                                                                                                                            
            do_mighty_awesome()
            Lg.logger.info(f'MightyAwesomeMandala:Completed loop count {count} of Third Pass, {my_angle}: {Tm.this_time}')
        count = 0
        R = random.randint(10, 200)
        Lg.logger.info(f'MightyAwesomeMandala:The value of hue R is {R}')
        L = random.randint(10, 150)
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:The value of hue L is {L}')
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:Starting Fourth Pass @ {Tm.this_time}')
        reset_pa_pb()
        for count in range(my_range): # Fourth Pass
            pa.pencolor(L + count %100, count % B, R + count % 50)
            pb.pencolor(count % B, count%127, B - count %B)
            do_mighty_awesome()
            Lg.logger.info(f'{my_script}:MightyAwesomeMandala:Completed loop count {count} of Fourth Pass, {my_angle}: {Tm.this_time}')
        count = 0
        R = random.randint(10, 200)
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:The value of hue R is {R}')
        L = random.randint(100, 255)
        Lg.logger.info(f'{my_script}:MightyAwesomeMandala:The value of hue L is {L}')
        Lg.logger.info(f'MightyAwesomeMandala:Starting Fifth Pass @ {Tm.this_time}')
        reset_pa_pb()
        for count in range(my_range): # Fifth pass
            pa.pencolor(count % 84, L, count % B)
            pb.pencolor(L, count % B, R)
            do_mighty_awesome()
            Lg.logger.info(f'{my_script}:MightyAwesomeMandala:Completed loop count {count} of Fifth Pass, {my_angle}: {Tm.this_time}')
        reset_pa_pb()
    produce_reversing_video()
    finalize()


#  module_8
#+++++++++++MODULE 8 - Iridescent Polygram+++++++++++++++++++++++++++++++++++++++++++++++++++++
def iridescent_polygram():  # Uses 2 pens with offset phi angle
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Iridescent Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(50, 10, 255)
        pa.right(my_angle /2)
        magenta_hue_pen.right(my_angle / 2)
        while  count in range (0, 255):  #255 is default. Use lower number for testing.
            t.bg_fade_yellow_to_dark()
            pa.pensize(count / 49)
            magenta_hue_pen.pensize(count / 72)
            pa.right(my_angle)
            pa.fd(count + phi)
            magenta_hue_pen.left(my_angle * phi)  # This is the offset angle
            magenta_hue_pen.pencolor(random.randint(100,200), random.randint(0,75) + count %150,  random.randint(175,255) - count %150)
            pa.pencolor(random.randint(0,128) + count %126, random.randint(150,255)- count %126, random.randint(100, 200))
            pa.circle( count - pi, -my_angle, 8)
            magenta_hue_pen.circle(count / pi, my_angle * phi) # This is the offset angle
            pa.pencolor(255,255,random.randint(100, 200))
            magenta_hue_pen.pencolor(255,random.randint(100, 200), 255)
            pa.dot(count / phi / 18)
            magenta_hue_pen.dot(count / phi / 9)
            f.save_thumb()
            # count_it_bg()
        produce_video()
    finalize()










#  module_10
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Uses 2 pens with offset phi angle
def hued_gradiant_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, my_range, count, pa, pb, my_pensize
    my_script = 'Hued Gradiant Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    
    for a.i  in range( len(a.i_angle)):
        my_angle = (float(a.i_angle_float[a.i]))
        Lg.logging.info('The offset angle value is  ' + str(my_angle * phi))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,10)
        make_turtle_pa()
        make_turtle_pb()
        pa.pensize(1)
        pb.pencolor(200, 99, 102)
        pa.left(my_angle / 2)
        pb.left(my_angle / 2)
        my_range = 382 #Default is 382
        count = 0
        my_pensize = 48
        make_turtle_pa()
        make_turtle_pb()
        hued_gradiant_script()
        reset_pa_pb()    
    produce_reversing_video()
    finalize()
        
 #  module_11
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def animated_abstraction():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Animated Abstraction'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logging.info('The offset angle value is  ' + str(my_angle * phi))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        pa.pensize(1)
        magenta_hue_pen.pencolor(200, 99, 102)
        count = 0
        for count in range(length):  # 255 is default. Use lower number for testing.
            pa.setpos(0,0)
            turtle.bgcolor(count %200, count % 250, count % 50)
            R = 0
            G = 20
            B = 255
            pa.color( R + count %150, G + count %150,   B - count %100)
            pa.pensize(5)
            pa.setposition(-700, 300)
            pa.circle(count/3, my_angle, 7)
            pa.backward(100)
            pa.circle(9, my_angle, 6)
            pa.pencolor('green')
            pa.dot(18)
            pa.penup()
            pa.setpos(0,0)
            pa.pendown()
            pa.pencolor(R + count, G + count % 190, B - count)
            pa.pensize(count % 20 + phi /18 )
            pa.circle(150, -my_angle, 4)
            pa.penup()
            pa.setposition(700, 300)
            pa.pendown()
            pa.pensize(5)
            pa.color( R + count %250, G + count %190,   B - count %200)
            pa.circle(count/3, my_angle, 7)
            pa.fd(100)
            pa.circle(9, my_angle, 6)
            count += 2
            f.save_thumb()
    produce_video()
    finalize()





#  module_12
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gradiant_mandala():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Gradiant Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logging.info('The offset angle value is  ' + str(my_angle * phi))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(10,0,15)
        pa.pensize(1)
        magenta_hue_pen.pencolor(200, 99, 102)
        pa.left(my_angle / 2)
        magenta_hue_pen.rt(my_angle / 2)
        for count in range(252):  #250 is default. Use lower number for testing, 300 for audio add.
            pa.pensize(count/18)
            pa.right(my_angle)
            R = 0
            G = 255
            B = 255
            pa.color(R + count, G - count, B - count)
            pa.fd(count)
            turtle.bgcolor(20, count, count)
            f.save_thumb()
            turtle.bgcolor(2,9,3)
            t.my_pen.color( 10, 15, 50)
            Tm.end_time()
    produce_video()
    finalize()




#  module_13
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def growing_yin_yang(): #Published to YouTube 11/11/2021
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Growing Yin-Yang'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_angle = 180
    turtle.bgcolor('aqua') # Has to be a neutral shade like grey to contrast the black and white theme.
    for count in range(400):  #360 is default. Use lower number for testing. The higher the number, the longer the show.
        pa.pensize(count / 18)
        pa.color(0,0,0)
        pa.left(-my_angle - phi)
        pa.circle(count / 2)
        pa.color(255,255,255)
        pa.left(my_angle)
        pa.circle(count / 2)
        f.save_thumb()
    produce_video()
    finalize()




#  module_14
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Uses 2 pens with offset phi angle
def animated_hued_polygram():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Animated Hued Polygram'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        for count in range(500):
            t.bg_fade_dark_to_green_to_dark()
            pick_light()
            pa.right(my_angle)
            pa.fd(count / pi)
            pick_indigo()
            indigo_hue_pen.left(-my_angle)
            indigo_hue_pen.fd(count / pi)
            pa.rt(my_angle)
            pa.backward(count / phi)
            pick_gold()
            gold_hue_pen.fd(count  + phi)
            pick_dot()
            t.ld.dot(count /48 * phi)
            gold_hue_pen.circle(count / 6, my_angle, 3)
            pa.pensize(count / 15)
            indigo_hue_pen.pensize(count / 18)
            gold_hue_pen.pensize(count / 33)
            # count_it()
            t.bg_count += 1
            f.save_thumb()
    produce_video()
    finalize()




#  module_15 NEEDS WORK
'''#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_polygonial():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Pretty Polygonial'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        with Timer("Elapsed time to run this code: {} minutes"):
            turtle.bgcolor(0,0,0)
            Lg.logger.info(str('The featured angle is     ') + str(my_angle))
            count = 0
            gold_hue_pen.pensize(1)
            green_hue_pen.pensize(1)
            t.lm.pensize(3)
            for count in range(300): # 255 is default. Use lower number for testing
                pick_gold()
                pick_green()
                pick_random()
                pick_magenta()
                cyan_hue_pen.dot(count / 9)
                gold_hue_pen.pensize(count / 144)
                gold_hue_pen.left(my_angle)
                gold_hue_pen.fd(count * phi)
                green_hue_pen.pensize(count / 36)
                green_hue_pen.left(my_angle)
                green_hue_pen.fd(count * phi)
                t.lm.pensize(count / 54)
                t.lm.left(my_angle)
                t.lm.dot(count / phi / 18)
                t.lm.fd(count + pi)
                green_hue_pen.left(my_angle)
                green_hue_pen.circle(-count /9, my_angle, 9)
\               f.save_thumb()
                # count_it()
            reset_all()
            t.my_venv()
    produce_video()
    finalize()
    

'''
#  module_22
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def multi_hued_polygram():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Multi-Hued Polygram'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        pa.right(t.my_angle / 2)
        pa.speed(0)
        gold_hue_pen.speed(0)
        N =  random.randint(1, 100)
        for count in range(500): #Determines size of graphic on the screen by the count of loops
            pick_green()
            pick_gold()
            R =  0
            G =  255
            B =  255
            L =  0
            M =  0
            gold_hue_pen.pensize(count /120)
            pa.pensize(count / 64)
            pa.color( R + count %255, G - count %255, B - count %255)
            pa.right(t.my_angle)
            pa.fd(count + phi)
            gold_hue_pen.circle(count + phi, t.my_angle, 3)
#             pa.circle(count * phi, -t.my_angle)
            pa.right(t.my_angle)
            pa.fd(count * phi)
            t.bg_fade_dark_to_green()
            t.bg_count += 1
            # count_it()
            f.save_thumb()
#             gc.collect()
    produce_video()
    finalize()




#module_23 NEEDS WORK

#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala(): # Uses pens pa, pb
    global my_project, my_angle, my_title, my_script, str_angles, my_range, count, pa, pb, my_pensize
    my_script = 'Brave Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = (float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,25)
        make_turtle_pa()
        make_turtle_pb()
        R = random.randrange(150, 250, 10)
        G = 0
        B = 255
        L = random.randint(10, 200)
        Lg.logger.info('The value of color R :   ' + str(R))
        Lg.logger.info('The value of color L :   ' + str(L))
        my_range = 765
        for count in range(my_range):
            pa.pencolor(R, count % 255, B - count % 255)
            pa.pensize(count / 210)
            pa.fd(count / 3)
            f.save_thumb()
            pa.left(my_angle)
            pa.fd(count /1.5)
            f.save_thumb()
            pb.pensize(count / B)
            pb.pencolor(R, B - count % 255, L)
            pb.circle(count / 3, my_angle, 3)
            f.save_thumb()
            pa.rt(my_angle)
            pa.pencolor(L, B - count % 255, B - count % 255)
            pa.circle(count / 3, - my_angle, 2)
            f.save_thumb()
            pb.left(my_angle)
            pb.backward(count / 36)
            process_thumbs()
        clear_pa_pen()
        clear_pb_pen()
    produce_reversing_video()
    finalize()
    
            
#module_24
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala_decimated():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Angle-Fractioned Brave Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    x = 3
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        Lg.logger.info(str('The featured angle is     ') + str(my_angle) + ',' + '  fractional =  ' + str(x) + ',' + '  fractional angle = ' + str(my_angle/x))
        R = random.randrange(175, 255, 10)
        Lg.logger.info('The value of color R :   ' + str(R))
        G = 0
        B = 255
        L = random.randrange(10, 200, 1)
        Lg.logger.info('The value of color L :   ' + str(L))
        M = 255
        N = 255
        X = 255
        Y = 255
        Z = 10
        count = 0
        t.bg_count = 0
        for count in range(255): # First Pass
            t.bg_fade_dark_to_green()
            pa.pensize(count/45)
            pa.left(my_angle/x)
            pa.fd(count)
            pa.pencolor(G + count, B - count, R)
            magenta_hue_pen.pensize(count /18)
            magenta_hue_pen.pencolor(Y - count, R, L)
            magenta_hue_pen.circle(count / phi, my_angle/x)
            pa.rt(my_angle/x)
            pa.pencolor(L, M - count, N - count)
            pa.circle(count * 1.26, - my_angle/x)
            # #count_it()
            t.bg_count += 1
            f.save_thumb()  #Screenshot as a png set set up mp4
        count = 0
        pa.penup()
        magenta_hue_pen.penup()
        pa.setpos(0,0)
        magenta_hue_pen.setpos(0,0)
        pa.pendown()
        magenta_hue_pen.pendown()
        pa.speed(0)
        magenta_hue_pen.speed(0)
        t.bgbg_count = 0
        for count in range(510): # Second Pass
            t.bg_fade_green_to_dark()
            pa.pensize(count/56)
            pa.left(my_angle/ x)
            pa.fd(count)
            pa.pencolor(R, G + count % 255, B - count % 255)
            magenta_hue_pen.pensize(count/18)
            magenta_hue_pen.pencolor(R, Y - count % 255, L)
            magenta_hue_pen.circle(count / phi, my_angle/x)
            pa.rt(my_angle/x)
            pa.pencolor(Z + count % 225, M - count % 100, N)
            pa.circle(count, - my_angle/x)
            # count_it()
            # # count += 1
            t.bg_count += 1
            f.save_thumb()    #Screenshot as a png set set up mp4
        count = 0
        pa.penup()
        magenta_hue_pen.penup()
        pa.setpos(0,0)
        magenta_hue_pen.setpos(0,0)
        pa.pendown()
        magenta_hue_pen.pendown()
        pa.speed(0)
        magenta_hue_pen.speed(0)
        t.bg_count = 0
        for count in range(765): # Third Pass
            Lg.logger.info('The value of Tm.iterable_time is ' + str(Tm.iterable_time))
            Lg.logger.info('The value of count is  ' + str(count))
            pa.pensize(count/56)
            pa.left(my_angle/x)
            pa.fd(count)
            pa.pencolor(R, G + count% 255, B - count% 255)
            magenta_hue_pen.pensize(count/27)
            magenta_hue_pen.pencolor(R, Y - count% 255, L)
            magenta_hue_pen.circle(count / phi, my_angle/x)
            pa.rt(my_angle / x)
            pa.pencolor(L, M - count% 255, N - count% 255)
            pa.circle(count, - my_angle/x)
            # count_it()
            # # count += 1
            t.bg_count += 1
            f.save_thumb()    #Screenshot as a png set set up mp4
    produce_reversing_video()
    finalize()




#module_25
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def color_shifting_mandala():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Color-Shifting Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        R = 255
        G = 150
        B = 18
        A = 0
        H = 0
        C = 255
        turtle.bgcolor(A,H,C)
        time.sleep(4)
        pa.left(my_angle/2)
        t.bg_count = 0
        while  count <= 360: # 360 is default for audio clip add, use lower number for testing
            pa.pensize(count/ 90)
            pa.dot(3)
            pa.color( R - count %60,  G - count %140, B + count %200)
            pa.left(my_angle)
            pa.circle(count / phi, my_angle, 3)
            t.bg_fade_skyblue_to_dark()
            t.bg_count += 1
            f.save_thumb()
    produce_reversing_video()
    finalize()





#module_26
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gold_red_mandala():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Gold-Red Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor("indigo")
        for count in range(300): #252 is default, use lower number for testing; 300 for audio clip add
            pick_gold()
            pick_red()
            pick_light()
            gold_hue_pen.pensize(count / 27)
            gold_hue_pen.circle(count *phi, - my_angle)
            red_hue_pen.pensize(count/18)
            red_hue_pen.backward(count *pi)
            red_hue_pen.right(my_angle)
            pa.dot(5)
            pa.left(my_angle)
            pa.fd(count/2)
            f.save_thumb()
    produce_reversing_video()
    finalize()


'''

#module_27
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gold_red_mandala_extended():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Gold-Red Mandala Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor("indigo")
        for count in range(250): # First Pass
            pick_gold()
            pick_red()
            pick_light()
            gold_hue_pen.pensize(count / 27)
            gold_hue_pen.circle(count *phi, - my_angle)
            red_hue_pen.pensize(count/18)
            red_hue_pen.backward(count *pi)
            red_hue_pen.right(my_angle)
            pa.dot(5)
            pa.left(my_angle)
            pa.fd(count/2)
            f.save_thumb()
            # count_it()

        gold_hue_pen.penup()
        red_hue_pen.penup()
        pa.penup()
        gold_hue_pen.setpos(0,0)
        red_hue_pen.setpos(0,0)
        pa.setpos(0,0)
        gold_hue_pen.pendown()
        red_hue_pen.pendown()
        pa.pendown()
        gold_hue_pen.speed(0)
        red_hue_pen.speed(0)
        pa.speed(0)
        count = 0
        for count in range(505): # Second Pass
            pick_gold()
            pick_red()
            pick_light()
            red_hue_pen.pensize(count / 27)
            red_hue_pen.circle(count *phi, - my_angle)
            gold_hue_pen.pensize(count/18)
            gold_hue_pen.backward(count *pi)
            gold_hue_pen.right(my_angle)
            pa.dot(5)
            pa.left(my_angle)
            pa.fd(count/2)
            f.save_thumb()
            # count_it()
            # # count += 1

        gold_hue_pen.penup()
        red_hue_pen.penup()
        pa.penup()
        gold_hue_pen.setpos(0,0)
        red_hue_pen.setpos(0,0)
        pa.setpos(0,0)
        gold_hue_pen.pendown()
        red_hue_pen.pendown()
        pa.pendown()
        gold_hue_pen.speed(0)
        red_hue_pen.speed(0)
        pa.speed(0)
        count = 0
        for count in range(755): # Third Pass
            pick_gold()
            pick_red()
            pick_light()
            pa.pensize(count / 27)
            pa.circle(count *phi, - my_angle)
            red_hue_pen.pensize(count/18)
            red_hue_pen.backward(count *pi)
            red_hue_pen.right(my_angle)
            gold_hue_pen.dot(5)
            gold_hue_pen.left(my_angle)
            gold_hue_pen.fd(count/2)
            f.save_thumb()
            # count_it()
            # # count += 1
    produce_reversing_video()
    finalize()




#module_28
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Hued_freedom_star():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Hued Freedom Star'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        pa.color(122,133,215)
        R = 0
        G = 50
        B = 255
        turtle.bgcolor(R, G, B)
        def white_dot():
            pa.pencolor(255,255,255)
            pa.dot(15)
            pa.pencolor(123,135,216)
        def purple_dot():
            pa.pencolor(123,135,216)
            pa.dot(15)
        for count in range(300): # 720 is default, use lower number for testing
            if count <= 255:
                turtle.bgcolor(R + count, G, B)
            else:
                turtle.bgcolor(255, G, B)
            pa.pensize(count/50)
            pa.fd(count * phi ) #+ 63)
            white_dot()
            pa.rt(my_angle)
            pa.pencolor(123 + count %100 ,135,216 -count %200)
            pa.fd(count * phi)
            white_dot()
            pa.rt(my_angle)
            pa.circle(count / phi, my_angle, 9)
            white_dot()
            f.save_thumb()
            for i in range(2):
                purple_dot()
            f.save_thumb()
    produce_reversing_video()
    finalize()



#module_29
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def blue_orange_mandala_144():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Hued Gradiant Mandala'
    startup_script()
    make_folder()
    my_angle - 144
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    Lg.logger.info(str('The featured angle is     ') + str(my_angle))
    R = 255
    G = 255
    B = 255
    L = 0
    C = 0
    H = 0
    Z = 255
    pa.penup()
    pa.setpos(0, -100)
    pa.pendown()
    pa.speed(0)
    pa.shape("circle")
    pa.shapesize(1)
    pa.pensize(1)
    for count in range(252): #252 is default, use lower number for testing
        turtle.bgcolor(L, C, H + count)
        pa.pensize(10)
        pa.right(my_angle)
        pa.color(L, C, H + count % 150)
        pa.fd(count  + phi)
        f.save_thumb()
        for g in range(12):
            R = 0 + count % 150
            Y = 100
            B = 255 - count % 150
            pa.left(my_angle)
            pa.color(R, Y, B)
            pa.pensize(2)
            pa.fd(500)
    produce_reversing_video()
    finalize()



'''
#module_30
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def ribbons_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range
    my_script = 'Ribbons Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        count = 0
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        R = 255
        G = 255
        B = 255
        L = 0
        C = 0
        H = 0
        Z = 255
        turtle.bgcolor(L, C, H)
        pa.penup()
        pa.setpos(0,  -25)
        pa.pendown()
        pa.shape("blank") #circle is default
        pa.shapesize(1)
        pa.pensize(1)
        pa.speed(0)
        my_range = 25 # 765 is default, use lower number for testing
        for count in range(my_range): 
            turtle.bgcolor(10, 0, 25)
            pa.pensize(3) # 1 is default
            pa.right(my_angle)
            pa.color(L +count % 255, C, H + count %127 )
            pa.fd(count  + phi)
            f.save_thumb()
            for g in range(12):  #10 is the default
                R = 127 + count %127
                G = 127 - count %127
                B = 25 - count %25
                pa.left(my_angle)
                pa.color(R, G, B)
                pa.pensize(g/12) # 100 is default
                pa.circle(72, my_angle, 7)
                f.save_thumb()
                
        pa.reset()
        t.set_up_el()
        set_light_pen_home()
        produce_reversing_video()       
    finalize()




#module_31
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def circular_mandala_205():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Hued Gradiant Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_angle = 205
    Lg.logger.info(f'{my_script}:The featured angle is {round(my_angle)}')
    R = 255
    G = 255
    B = 255
    L = 0
    C = 0
    H = 0
    Z = 255
    turtle.color(R, G, B)
    turtle.bgcolor(L, C, H)
    pa.penup()
    pa.setpos(0, -150)
    pa.pendown()
    pa.speed(0)
    pa.shape("circle")
    pa.shapesize(1)
    pa.pensize(1)
    pa.hideturtle()
    pa.color(R, G, B)
    for count in range(200): #200 is default, use lower number for testing
        turtle.bgcolor(L, C, H + count %299)
        pa.pensize(10)
        pa.right(my_angle)
        pa.color(L +count, C + count %80, H)
        pa.fd(count  * phi)
        f.save_thumb()
        for g in range(4):
            R = 101 + count %133
            Y = 101 - count %130
            B = 25 + count %100
            pa.left(my_angle)
            pa.color(R, G - count, B)
            pa.pensize(2)
            pa.circle(175, my_angle, 11)
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    produce_reversing_video()
    finalize()




#module_32
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def occillating_polygon(): # Needs work
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Occillating Polygon'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        count = 0
        pa.pensize(1)
        Lg.logger.info(f'{my_script}:The Angle is {my_angle}')
        for count in range(149):
            # Default is 149; can use lower number for testing
            R = random.randrange(10,100)
            G = 255  #  random.randrange(171, 255)
            B =  0
            pa.color( R + count, G - count, B + count)
            turtle.bgcolor(155 - count, 155 - count, 10)
            pick_red()
            red_hue_pen.dot(count / 6)
            red_hue_pen.left( - my_angle /2)
            red_hue_pen.fd(count/2 +phi)
            red_hue_pen.circle(count * phi, my_angle, 6)
            red_hue_pen.rt(my_angle)
            pa.left(my_angle)
            pa.circle( count * 3, my_angle)
            red_hue_pen.dot(count / 6)
            pa.pensize(count / 27)
            # count_it()
            f.save_thumb()
    produce_reversing_video()
    finalize()
        
#module_33
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def arc_star():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Arc-Star'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        count = 0
        pa.pensize(1)
        count = 0
        pa.pensize(3)
#             pa.right(my_angle * 2 )
        for count in range(300):
            if count <= 255:
                turtle.bgcolor(25, 50, count)
            else:
                turtle.bgcolor(25,50,255)
            R =  0
            G =  0
            B =  90
            if count <= 255:
                pa.color( R + count , G + count, B )
            else:
                pa.color(255, 255, B)
            pa.left(my_angle)
            pa.penup()
            pa.fd( count / phi )
            pa.pendown()
            pa.pensize(6)
            pa.fd(count /phi)
            pa.rt(my_angle)
            R = 0
            G = 230
            B = 255
            pa.color( count %255, G - count %54, B - count %255 )
            pa.penup()
            pa.fd(75)
            pa.pensize(3)
            pa.circle(24, my_angle, 10)
            pa.pendown()
            pa.backward(count)
            pa.pensize(count / 72)
            pa.penup()
            pa.setposition(0, 0)
            pa.pendown()
            pa.color(R + count %255, count %75, 0)
            pa.circle(count + phi, my_angle, 5)
            # count_it()
            f.save_thumb()
    produce_reversing_video()
    finalize()


#module_34
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def home_star():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Home-Star'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        pa.pensize(3)
        for count in range(359): #359 is default
            turtle.bgcolor(10 + count % 240, 50 + count % 200, count %255)
            R = 150
            G = 230
            B = 0
            pa.color(count % 104, G - count %200, count %254 )
            pa.left(my_angle)
            pa.penup()
            pa.fd(count / phi )
            pa.pendown()
            pa.pensize(6)
            pa.fd(count / phi)
            pa.rt(my_angle)
            pa.penup()
            pa.fd(27)
            pa.pensize(3)
            pa.pendown()
            pa.circle(12, my_angle, 9)
            pa.backward(count + phi)
            pa.pensize(count / 72)
            pa.penup()
            pa.setposition(0, 0)
            pa.pendown()
            pa.circle(count, my_angle, 5)
            # count_it()
#         time.sleep(10) #for testing only
            f.save_thumb()
    produce_reversing_video()
    finalize()



#module_35
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#Deals best with whole number angles
def use_abs():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Absolute Function Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        count = 0
        pa.pensize(1)
        # count = 0
        pa.pensize(3)
        pa.color('brown', 'green')
        pa.begin_fill()
        while True:
            pa.left(my_angle)
            pa.fd(250)
            f.save_thumb()
            if abs(pa.pos()) < 1:
                break
        pa.end_fill()
    produce_reversing_video()
    finalize()




#module_36
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Six-Pointed Mandalas or doubles.
def double_take():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Double Take'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        R = random.randrange(155,255, 5)
        G = 255
        B = 0
        Lg.logger.info('The value of color R is    ' + str(R))
        for count in range(359):
            pa.pensize(4)
            indigo_hue_pen.pensize(4)
            pa.left(my_angle)
            pa.color(R, G - count %255, B + count %255)
            pa.fd(count * phi)
            indigo_hue_pen.color(R, G - count %250, B + count %250)
            indigo_hue_pen.right(my_angle)
            indigo_hue_pen.fd(count * phi)
            f.save_thumb()
    produce_video()
    finalize()





#module_37
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Cloverleaf Cross Mandala.
def cloverleaf():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Cloverleaf Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = float(a.i_angle_auto[a.i])
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        t.set_up_el()
        pa.setpos(0,0)
        turtle.bgcolor(0,0,0)
        for count in range(765): # Default is 1020; use lower number for testing
            turtle.bgcolor(25, 0, 10)
            f.save_thumb()
            pa.pencolor(count %255, 255 - count % 255, count % 127)
            pa.pensize(count / 510)
            pa.circle(count, my_angle)
            f.save_thumb()
            pa.penup()
            pa.fd(count /2)
            f.save_thumb()
            pa.pendown()
            f.save_thumb()
        clear_pa_pen()    
    Lg.logger.info(f'{my_script}:Stopping {my_script} by Leon Hatton @ {Tm.this_time}')
    Lg.logger.info('###############################################################')
    produce_reversing_video()
    finalize()






#module_38
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Cloverleaf Extended Cross Mandala.
def cloverleaf_extended():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Cloverleaf Extended Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        Lg.logger.info('Starting First Pass at  ' + str(Tm.this_time))
        t.ld.speed(0)
        t.ld.pencolor(0, 255,0)
        turtle.bgcolor(0,0,0)
        count = 0
        global my_pensize
        my_pensize = count / 56
        global my_range
        my_range = 396 # 400 is default; use any number for testing, etc
        Lg.logger.info(' The program will loop  ' + str(my_range) + '  times')
        for i in range(2):
            t.ld.penup()
            t.ld.setpos(0,0)
            t.ld.seth(my_angle)
            t.ld.pendown()
            for count in range(my_range):
                my_pensize = count / 56
                if i ==  0:
                    t.ld.pencolor(255 - count % 255 , 255 - count % 255 ,  count % 255)  # Fade yellwo to blue
                else:
                    t.ld.pencolor( count % 255, 255, 0)
                t.ld.circle(count / phi, my_angle)
                f.save_thumb()
                t.ld.penup()
                t.ld.fd(count / phi)
                f.save_thumb()
                t.ld.pendown()
                t.ld.pensize(my_pensize)
                Lg.logger.info('t.ld.pensize is  ' + str(my_pensize) + '( for  ' +  str(count))
                f.save_thumb()
        Lg.logger.info('Starting Second Pass at  ' + str(Tm.this_time))
        turtle.bgcolor(0,0,0)
        del my_range
        del count
        del t.ld
        gc.collect()
        count = 0
        my_range = 396 # 400 is default; use any number for testing, etc
        t.lm.speed(0)
        turtle.colormode(255)
        for i in range(2):
            t.lm.penup()
            t.lm.setpos(0,0)
            t.lm.seth(my_angle)
            t.lm.pendown()
            for count in range(my_range):
                my_pensize = count / 56
                if i == 0:
                    t.lm.pencolor(count % 255,  255 - count % 255 , 255 - count % 255 )  # Fade aqua to red
                else:
                    t.lm.pencolor(255, 0, count %  255)
                t.lm.pensize(my_pensize)
                t.lm.circle(count / phi, my_angle)
                f.save_thumb()
                t.lm.penup()
                t.lm.fd(count / phi)
                t.lm.pendown()
                f.save_thumb()
                Lg.logger.info(f'{my_script}:t.lm.pencolor is {t.lm.pencolor}')
        Lg.logger.info(f'{my_script}:Starting Third Pass at {Tm.this_time}')
        turtle.bgcolor(0,0,0)
        del count
        del t.lm
        del my_range
        gc.collect()
        count = 0
        my_range = 396 # 400 is default; use any number for testing, etc
        t.lc.speed(0)
        turtle.colormode(255)
        for i in range(2):
             t.lc.penup()
             t.lc.setpos(0,0)
             t.lc.seth(my_angle)
             t.lc.pendown()
             for count in range(my_range):
                 my_pensize = count / 56
                 t.lc.pensize(my_pensize)
                 if i == 0:
                     t.lc.pencolor(count % 25, 255 - count % 250, 255 - count % 100)  # Fade yellow to red
                 else:
                     t.lc.pencolor( 255 - count % 100, count % 25, 126)
                 t.lc.circle(count / phi, my_angle)
                 t.lc.penup()
                 t.lc.fd(count / phi)
                 t.lc.pendown()
                 f.save_thumb()
        Lg.logger.info(f'{my_script}:Starting Fourth Pass at {Tm.this_time}')
        turtle.bgcolor(0,0,0)
        del my_range
        del count
        del t.lc
        gc.collect()
        count = 0
        my_range = 396 # 400 is default; use any number for testing, etc
        dark_hue_pen.speed(0)
        pa.speed(0)
        turtle.colormode(255)
        for i in range(2):
            yellow_hue_pen.penup()
            green_hue_pen.penup()
            yellow_hue_pen.setpos(0,0)
            green_hue_pen.setpos(0,0)
            yellow_hue_pen.seth(my_angle)
            green_hue_pen.seth(my_angle)
            yellow_hue_pen.pendown()
            green_hue_pen.pendown()
            for count in range(my_range):
                my_pensize = count / 56
                yellow_hue_pen.pensize(my_pensize)
                green_hue_pen.pensize(my_pensize)
                pick_yellow() # Pen yellow_hue_pen
                pick_green() # Pen green_hue_pen
                yellow_hue_pen.circle(count / phi, my_angle)
                f.save_thumb()
                green_hue_pen.circle(count / phi, -my_angle)
                f.save_thumb()
                yellow_hue_pen.penup()
                green_hue_pen.penup()
                green_hue_pen.backward(count / phi)
                f.save_thumb()
                yellow_hue_pen.fd(count / phi)
                green_hue_pen.pendown()
                yellow_hue_pen.pendown()
                f.save_thumb()
        Lg.logger.info(f'{my_script}:Starting Fifth Pass at {Tm.this_time}')
        turtle.bgcolor(0,0,0)
        del my_range
        del count
        del yellow_hue_pen
        del green_hue_pen
        gc.collect()
        count = 0
        my_range = 396 # 400 is default; use any number for testing, etc
        magenta_hue_pen.speed(0)
        turtle.colormode(255)
        for i in range(2):
            magenta_hue_pen.penup()
            magenta_hue_pen.setpos(0,0)
            magenta_hue_pen.pendown()
            for count in range(my_range):
                my_pensize = count / 56
                magenta_hue_pen.pensize(my_pensize)
                magenta_hue_pen.pencolor(count %100, count % 255, 255 * i)
                magenta_hue_pen.circle(count / phi, my_angle)
                f.save_thumb()
                magenta_hue_pen.penup()
                magenta_hue_pen.fd(count / phi)
                magenta_hue_pen.pendown()
                f.save_thumb()
        Lg.logger.info(f'{my_script}:Starting Sixth Pass at {Tm.this_time}')
        turtle.bgcolor(0,0,0)
        del my_range
        del count
        del magenta_hue_pen
        gc.collect()
        count = 0
        my_range = 396 # 400 is default; use any number for testing, etc
        orange_hue_pen.speed(0)
        blue_hue_pen.speed(0)
        turtle.colormode(255)
        for i in range(2):
            blue_hue_pen.penup()
            orange_hue_pen.penup()
            blue_hue_pen.setpos(0,0)
            blue_hue_pen.seth(my_angle)
            orange_hue_pen.setpos(0,0)
            orange_hue_pen.seth(my_angle)
            blue_hue_pen.pendown()
            orange_hue_pen.pendown()
            for count in range(my_range):
                my_pensize = count / 56
                blue_hue_pen.pensize(my_pensize) 
                orange_hue_pen.pensize(my_pensize) 
                pick_blue() # Pen blue_hue_pen
                pick_orange() # Pen orange_hue_pen
                blue_hue_pen.circle(count / phi, my_angle)
                f.save_thumb()
                orange_hue_pen.circle(count / phi, -my_angle)
                f.save_thumb()
                blue_hue_pen.penup()
                orange_hue_pen.penup()
                blue_hue_pen.backward(count / phi)
                orange_hue_pen.fd(count / phi)
                blue_hue_pen.pendown()
                orange_hue_pen.pendown()
                f.save_thumb()
        Lg.logger.info(f'{my_script}:Starting Seventh Pass at {Tm.this_time}')
        turtle.bgcolor(0,0,0)
        del my_range
        del count
        del blue_hue_pen
        del orange_hue_pen
        gc.collect()
        count = 0
        turtle.colormode(255)
        my_range = 396 # 400 is default; use any number for testing, etc
        t.ll.speed(0)
        pa.speed(0)
        for i in range(2):
            pa.penup()
            t.ll.penup()
            pa.setpos(0,0)
            t.ll.setpos(0,0)
            t.ll.seth(my_angle)
            pa.seth(my_angle)
            pa.pendown()
            t.ll.pendown()
            for count in range(my_range):
                my_pensize = count / 56
                pa.pensize(my_pensize)
                t.ll.pensize(my_pensize)
                pa.pencolor(count % 21, count % 60, 255 - count % 10)
                t.ll.pencolor(i * 255, 255 - count % 255, count % 50)
                pa.circle(count / phi, -my_angle)
                f.save_thumb()
                t.ll.circle(count / phi, my_angle)
                pa.penup()
                t.ll.penup()
                pa.fd(count)
                t.ll.fd(count)
                pa.pendown()
                t.ll.pendown()
                f.save_thumb()
            produce_video()
    finalize()



#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Majestic Extended Mandala.
def majestic_mandala_extended():
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Majestic Mandala Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    Lg.logger.info('##########################################################')
    t.set_up_el()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        rand_hue = random.randint(10, 155)
        my_length = 500
        my_pensize = 66
        for r in range(3):
            pa.speed(0)
            turtle.bgcolor(0,25,0)
            pa.penup()
            pa.setpos(0,0)
            pa.seth(my_angle)
            pa.pendown()
            count = 0
            pa.speed(0)
            pa.pencolor(0, 255,0)
            turtle.bgcolor(0,0,0)
            a.report_angle_status()
            Lg.logger.info(f'{my_script}:The featured angle is {my_angle}')
            Lg.logger.info(f'{my_script}:The soundtrack selected for this project is {au.my_track}')
            Lg.logger.info(f'{my_script}:Starting First Pass at {Tm.this_time}')
            pa.seth(my_angle)
            for count in range(my_length):
                pa.pensize(count /my_pensize)
                pa.pencolor(count % 255, 255 - count % 127, rand_hue)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()
                pa.penup()
                pa.left(my_angle)
                pa.fd(count / phi)
                pa.pendown()
                pa.left(my_angle)
                pa.fd(count + pi)
                f.save_thumb()
            Lg.logger.info(f'{my_script}:Starting Second Pass at {Tm.this_time}')
            pa.seth(my_angle)
            pa.speed(0)
            turtle.bgcolor(0,25,0)
            pa.penup()
            pa.setpos(0,0)
            pa.pendown()
            count = 0
            for count in range(my_length):
                pa.pensize(count / my_pensize)
                pa.pencolor(255 - count % 127, 255 - count % 127, rand_hue)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()
                pa.penup()
                pa.left(my_angle)
                pa.fd(count / phi)
                pa.pendown()
                pa.left(my_angle)
                pa.fd(count + pi)
                f.save_thumb()
            Lg.logger.info(f'{my_script}:Starting Third Pass at {Tm.this_time}')
            pa.seth(my_angle)
            pa.speed(0)
            turtle.bgcolor(25, 0, 0)
            pa.penup()
            pa.setpos(0,0)
            pa.pendown()
            count = 0
            for count in range(my_length):
                pa.pensize(count /my_pensize)
                pa.pencolor(rand_hue, 255 - count% 127, 255 - count% 255)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()
                pa.penup()
                pa.left(my_angle)
                pa.fd(count /phi)
                pa.pendown()
                pa.left(my_angle)
                pa.fd(count + pi)
                f.save_thumb()
            Lg.logger.info(f'{my_script}:Starting Fourth Pass at {Tm.this_time}')
            pa.seth(my_angle)
            pa.speed(0)
            turtle.bgcolor(0,0,25)
            pa.penup()
            pa.setpos(0,0)
            pa.pendown()
            count = 0
            for count in range(my_length):
                pa.pensize(count /my_pensize)
                pa.pencolor(count % 127, rand_hue, 255 - count % 72)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()
                pa.penup()
                pa.left(my_angle)
                pa.fd(count / phi)
                pa.pendown()
                pa.left(my_angle)
                pa.fd(count + pi)
                f.save_thumb()
            Lg.logger.info(f'{my_script}:Starting Fifth Pass at {Tm.this_time}')
            pa.seth(my_angle)
            pa.speed(0)
            turtle.bgcolor(25, 0, 25)
            pa.penup()
            pa.setpos(0,0)
            pa.pendown()
            count = 0
            for count in range(my_length):
                pa.pensize(count /my_pensize)
                pa.pencolor(255 - count %255, count % 127, count % 255)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()
                pa.penup()
                pa.left(my_angle)
                pa.fd(count / phi)
                pa.pendown()
                pa.left(my_angle)
                pa.fd(count + pi)
                f.save_thumb()
            Lg.logger.info(f'{my_script}:Starting Sixth Pass at {Tm.this_time}')
            pa.seth(my_angle)
            pa.speed(0)
            turtle.bgcolor(25, 25, 25)
            pa.penup()
            pa.setpos(0,0)
            pa.pendown()
            count = 0
            for count in range(my_length):
                pa.pensize(count /my_pensize)
                pa.pencolor(count % 72, count% 255, rand_hue)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()
                pa.penup()
                pa.left(my_angle)
                pa.fd(count /phi)
                pa.pendown()
                pa.left(my_angle)
                pa.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Seventh Pass at  '  +  Tm.this_time)
            pa.seth(my_angle)
            pa.speed(0)
            turtle.bgcolor(0, 25, 25)
            pa.penup()
            pa.setpos(0,0)
            pa.pendown()
            count = 0
            for count in range(my_length):
                pa.pensize(count /my_pensize)
                pa.pencolor( rand_hue, count % 255, count % 255)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()
                pa.penup()
                pa.left(my_angle)
                pa.fd(count / phi)
                pa.pendown()
                pa.left(my_angle)
                pa.fd(count + pi)
                f.save_thumb()
            Lg.logger.info(f'{my_script}:Starting Eighth Pass at {Tm.this_time}')
            pa.seth(my_angle)
            pa.speed(0)
            turtle.bgcolor(10, 35, 25)
            pa.penup()
            pa.setpos(0,0)
            pa.pendown()
            count = 0
            for count in range(my_length):
                pa.pensize(count /my_pensize)
                pa.pencolor( rand_hue, 255 - count % 200, count % 200)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()
                pa.penup()
                pa.left(my_angle)
                pa.fd(count / phi)
                pa.pendown()
                pa.left(my_angle)
                pa.fd(count + pi)
                f.save_thumb()
            Lg.logger.info(f'{my_script}:Starting Ninth Pass at {Tm.this_time}')
            pa.seth(my_angle)
            pa.speed(0)
            turtle.bgcolor(25, 0, 25)
            pa.penup()
            pa.setpos(0,0)
            pa.pendown()
            count = 0
            for count in range(my_length):
                pa.pensize(count /my_pensize)
                pa.pencolor( count % 100, 255 - count % 100, rand_hue)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()
                pa.penup()
                pa.left(my_angle)
                pa.fd(count / phi)
                pa.pendown()
                pa.left(my_angle)
                pa.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Tenth Pass at  '  +  Tm.this_time)
            pa.seth(my_angle)
            pa.speed(0)
            turtle.bgcolor(0, 0, 0)
            pa.penup()
            pa.setpos(0,0)
            pa.pendown()
            count = 0
            for count in range(my_length):
                pa.pensize(count /my_pensize)
                pa.pencolor( count % 150, rand_hue, count % 150)
                pa.left(my_angle)
                pa.fd(count / phi)
                f.save_thumb()
                pa.penup()
                pa.left(my_angle)
                pa.fd(count / phi)
                pa.pendown()
                pa.left(my_angle)
                pa.fd(count + pi)
                f.save_thumb()     
    produce_reversing_video()
    finalize()


#module_43
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def sirius_mandala():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_script, str_angles, my_range, count, pa, pb, my_pensize
    my_script = 'Sirius Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = (a.i_angle_float[a.i])
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        make_turtle_pa()
        make_turtle_pb()
        make_turtle_pc()
        my_range = 765
        turtle.bgcolor(100,50,0)
        for count in range(my_range):
            if count < 255:
                pa.color( 0, count % 127, random.randint(150, 255)) #Blue/Coral
            else:
                pa.color(0, 0, count % 127) # Black/Blue
            
            pa.rt(my_angle)
            pa.fd(count / phi)
            f.save_thumb()
            pa.pensize(count / 163)
            pa.circle(count / 10, - my_angle)
            pa.rt(my_angle)
            
            f.save_thumb()
           
            pb.pencolor(255, 0, count % 255) #Red/Magenta
            pb.rt(my_angle)
            pb.fd(count / phi)
            f.save_thumb()
            pb.pensize(count / 172)
            pa.rt(my_angle)
            pb.circle(count / 14, - my_angle)
            f.save_thumb()
                  
            if count < 510:
                pc.color( count %255, count % 255, 255) #Coral/White
            else:
                pc.color(255,  random.randint(100, 255), 255) # White
            pc.rt(my_angle)
            pc.fd(count / t.pi)   
            f.save_thumb()
            pc.pensize(count / 181)
            pa.rt(my_angle)
            pc.circle(count / 18,  - my_angle, 7)
            f.save_thumb()
        reset_pa_pb()
        reset_pc()
    produce_reversing_video()
    finalize()






#module_44
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wall_show():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Wall Show'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        turtle.bgcolor(30,255,60)
        Lg.logger.info(f'{my_script}:The soundtrack being used for this show is: {au.my_track}')
        Lg.logger.info(f'{my_script}:The featured angle is {my_angle}')
        Lg.logger.info(f'{my_script}:The value of t.rand_num is {t.rand_num}')
        Lg.logger.info(f'{my_script}:The value of t.rand_pick is {t.rand_pick}')
        Lg.logger.info('......................................................................................')
        for count in range(255):
            R =  0
            G =  150
            B =  255
            pa.color( R + count, G - count % 130, B - count)
            pa.fd(count * phi)
            pa.left(my_angle)
            pa.pensize(count /36)
            pa.color(count, t.rand_num, 255 - count)
            pa.right(my_angle)
            pa.circle(count / 3, my_angle, 6)
            random_hue_pen.color( B - count, G - count % 150, R + count )
            random_hue_pen.fd(count * phi)
            random_hue_pen.right(my_angle)
            random_hue_pen.fd(count * phi)
            random_hue_pen.pensize(count / 27)
            random_hue_pen.color(255 - count, count, t.rand_pick)
            # count_it()
            turtle.bgcolor(30, 256 - count, 60)
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        Tm.end_time()
    Lg.logger.info(f'{my_script}:Stopping {my_script} by Leon Hatton on {Tm.this_time}')
    Lg.logger.info('************************************************************************')
    reset_all()





#module_45
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wall_show_extended():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Wall Show Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        turtle.bgcolor(30,255,60)
        Lg.logger.info(f'{my_script}:The soundtrack being used for this show is: {au.my_track}')
        Lg.logger.info(f'{my_script}:The featured angle is {my_angle}')
        Lg.logger.info(f'{my_script}:The value of t.rand_num is {t.rand_num}')
        Lg.logger.info(f'{my_script}:The value of t.rand_pick is {t.rand_pick}')
        Lg.logger.info('......................................................................................')
        for count in range(250):
            R =  0
            G =  150
            B =  255
            pa.color( R + count, G - count % 130, B - count)
            pa.fd(count * phi)
            pa.left(my_angle)
            pa.pensize(count /36)
            pa.color(count, t.rand_num, 255 - count)
            pa.right(my_angle)
            pa.circle(count / 3, my_angle, 6)
            random_hue_pen.color( B - count, G - count % 150, R + count )
            random_hue_pen.fd(count * phi)
            random_hue_pen.right(my_angle)
            random_hue_pen.fd(count + phi)
            random_hue_pen.pensize(count / 27)
            random_hue_pen.color(255 - count, count, t.rand_pick)
            # count_it()
            turtle.bgcolor(30, 256 - count, 60)
            f.save_thumb()
        pa.penup()
        random_hue_pen.penup()
        pa.setpos(0,0)
        random_hue_pen.setpos(0,0)
        pa.pendown()
        random_hue_pen.pendown()
        pa.speed(0)
        random_hue_pen.speed(0)
        count = 0
        for count in range(503):
            R =  255
            G =  150
            B =  0
#             Lg.logger.info(str(pa.color))
            pa.color(R - count % 255, G - count % 130, B + count %255)
            pa.fd(count * phi)
            pa.left(my_angle)
            pa.pensize(count /36)
            pa.color(R - count, t.rand_num, count)
            pa.right(my_angle)
            pa.circle(count / 3, my_angle, 6)
            random_hue_pen.color(R - count % 255, G - count % 150, B + count % 255 )
            random_hue_pen.fd(count * phi)
            random_hue_pen.right(my_angle)
            random_hue_pen.fd(count * phi)
            random_hue_pen.pensize(count / 27)
            random_hue_pen.color(R - count % 255, t.rand_num, t.rand_pick)
            # # count += 1
            # count_it()
            f.save_thumb()
        pa.penup()
        random_hue_pen.penup()
        pa.setpos(0,0)
        random_hue_pen.setpos(0,0)
        pa.pendown()
        random_hue_pen.pendown()
        pa.speed(0)
        random_hue_pen.speed(0)
        count = 0
        for count in range(758):
            R =  150
            G =  0
            B =  255
            pa.color(R - count % 145, count, B - count % 255)
            pa.fd(count * phi)
            pa.left(my_angle)
            pa.pensize(count /36)
            pa.color(count, t.rand_num, B - count % 255)
            pa.right(my_angle)
            pa.circle(count / 3, my_angle, 6)
            random_hue_pen.color( R - count % 100, B - count % 255, t.rand_pick)
            random_hue_pen.fd(count * phi)
            random_hue_pen.right(my_angle)
            random_hue_pen.fd(count * phi)
            random_hue_pen.pensize(count / 27)
            random_hue_pen.color(R - count % 150, count % 255, t.rand_pick)
            # # count += 1
            # count_it()
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        Tm.end_time()
    Lg.logger.info(f'{my_script}:Stopping {my+script} by Leon Hatton on  {Tm.this_time}')
    Lg.logger.info('************************************************************************')
    reset_all()





#module_46
#===========================================================================
#Code for Black Seed of Life
def black_seed():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_script, str_angles
    my_script = 'Black Seed Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    t.set_up_ce()
    for a.i  in range( len(a.i_angle)):
        Lg.logger.info('===============================================================================')
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'{my_script}:Current angle to be drawn is {my_angle} @ {Tm.this_time}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        pa.speed(30)
        pa.pensize(36)
        random_hue_pen.speed(30)
        random_hue_pen.pensize(54)
        random_hue_pen.pencolor(255,255,255)
        length = 234
        my_image = 'TBD'
#         my_angle = 135 # 60 is default
        my_base = int(3600/ my_angle) # for loop integrity of the number of loops of the ce pen
        pa.speed(30)
        pa.pensize(36)
        random_hue_pen.speed(30)
        random_hue_pen.pensize(54)
        random_hue_pen.pencolor(255,255,255)
        global b
        count = 0
        for x in range(3): # 3 is default
            if x == 0:
                 b = count , count % 18, count % 63
            elif x == 1:
                 b = count % 63, count, count % 18
            else:
                b = count % 18, count % 63, count

            for i in range(my_base):
                random_hue_pen.left(my_angle)
                random_hue_pen.circle(length)
                count = 0
            for count in range(254):
                if x == 0:
                    b = count, count % 18, count % 33
                elif x == 1:
                    b = count % 33, count, count % 18
                else:
                    b = count % 18, count % 33, count
                    pa.pencolor(b)
#                 Lg.logger.info(f'{my_script}:Base is: {my_base}')
#                 Lg.logger.info(f'{my_script}:count  : {Tm.iterable_time}')
#                 Lg.logger.info(f'{my_script}:Pen color:  {b}')
#                 Lg.logger.info(f'{my_script}:x = {x}')
                pa.left(my_angle)
                pa.circle(length)
                f.save_thumb()
                # count_it()

                del count
                gc.collect()
                count = 255
                while count >= 2:
                    if x == 0:
                        b = count , count % 33, count % 18
                    elif x == 1:
                        b = count % 18, count, count % 33
                    else:
                        b = count % 33, count % 18, count
                    pa.pencolor(b)
#                     Lg.logger.info(f'{my_script}:count  :{Tm.iterable_time}')
#                     Lg.logger.info(f'{my_script}:Pen color: {b}')
#                     Lg.logger.info(f'{my_script}: x = {x}')
                    pa.left(my_angle)
                    pa.circle(length)
                    f.save_thumb()
        pa.reset()
        t.set_up_el()
        set_light_pen_home()
        random_hue_pen.reset()
        t.set_up_ce()
        set_random_pen_home()
    produce_reversing_video()
    finalize()
    
'#  module_47'
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Name: Dark Mandala Extended.
Status: Creation Date:1/4/2023; Last Update: 12/4/2023; Last Completed Run: 12/4/2023
Uses local randomized hues pens magenta, indigo, blue, green, red, gold, dark, light.
Includes special center black dot pen. Duration is based upon quantity of angles selected.
 '''  
def dark_mandala_extended():  #Work on some more
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range, pa
    my_script = 'Dark Mandala Extended Version'
    Lg.logger.info(f'{my_script}:Status: Creation Date: 12/2/2023; Last Update: {Tm.my_date}')
    Lg.logger.info(f'{my_script}:Uses local randomized hues pens magenta, indigo, green, red, gold, dark, light.')
    Lg.logger.info(f'{my_script}:Phi constant is used to apply increasing line size with each loop.') 
    Lg.logger.info(f'{my_script}:Includes special center black dot pen. Duration is based upon quantity of angles selected.')
    startup_script()
    make_folder()
    t.my_angles, t.my_splash,= str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        all_pens_home()
        my_angle = a.i_angle_float[a.i]
        Lg.logger.info(f'{my_script}: Starting to draw {my_angle:.2f} degrees angles at {Tm.this_time}')
        turtle.title(f'{my_script}:{my_angle} Degrees Angle and {au.my_track}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.bgcolor(255, 255,100)
        my_range = 255 # 300 is default; use lower number for testing
        Lg.logger.info(f'{my_script}:Starting Loop One @ {Tm.my_time}')
        for count in range(my_range):
            Q_seed.dot(3)
            turtle.bgcolor(150, 100, 0)
            pick_magenta() 
            pick_dark()  
            pick_indigo() 

            dark_hue_pen.right(my_angle / 2) 
            dark_hue_pen.pensize(count / 54)
            dark_hue_pen.circle(count / 3, my_angle, 6)
            f.save_thumb()
            dark_hue_pen.penup()
            dark_hue_pen.backward(count / phi + count)
            f.save_thumb()
            dark_hue_pen.pendown()

            indigo_hue_pen.right(my_angle) 
            indigo_hue_pen.pensize(count / 54)
            indigo_hue_pen.backward(count / phi)
            f.save_thumb()

            dark_hue_pen.right(my_angle / 2) 
            dark_hue_pen.fd(count  / 2)
            f.save_thumb()

            indigo_hue_pen.right(my_angle) 
            indigo_hue_pen.fd(count )
            f.save_thumb()

            dark_hue_pen.penup() 
            dark_hue_pen.right(my_angle)
            dark_hue_pen.fd(count/9)
            f.save_thumb()
            dark_hue_pen.pendown()
            dark_hue_pen.fd(count * phi)
            f.save_thumb()

            indigo_hue_pen.left(my_angle)
            indigo_hue_pen.backward(count / phi) 
            indigo_hue_pen.circle(count /3, - my_angle, 9)
            f.save_thumb()

            #make dots
            magenta_hue_pen.pensize(count/24) 
            magenta_hue_pen.left(my_angle / 2)
            magenta_hue_pen.dot(count /24)
            f.save_thumb()
            magenta_hue_pen.penup()
            magenta_hue_pen.backward(count)
            f.save_thumb()
            magenta_hue_pen.pendown()
            magenta_hue_pen.fd(count / 60)
            Q_seed.dot(3)
            process_thumbs()
       
        Lg.logger.info(f'{my_script}:Starting Loop Two @ {Tm.my_time}')
        count = 0
        for count in range(my_range):
            Q_seed.dot(3)
            turtle.bgcolor(100, 150, 0)
            pick_blue() 
            pick_green() 
            pick_light() 

            light_hue_pen.right(my_angle / 2) 
            light_hue_pen.pensize(count / 54)
            light_hue_pen.circle(count / 3, my_angle, 6)
            f.save_thumb()
            light_hue_pen.penup()
            light_hue_pen.backward(count / phi  + count)
            f.save_thumb()
            light_hue_pen.pendown()

            green_hue_pen.right(my_angle) 
            green_hue_pen.pensize(count / 54)
            green_hue_pen.backward(count / phi)
            f.save_thumb()
            light_hue_pen.right(my_angle / 2) 
            light_hue_pen.fd(count  / 2)
            f.save_thumb()
            green_hue_pen.right(my_angle)  
            green_hue_pen.fd(count )
            f.save_thumb()
            light_hue_pen.penup()  
            light_hue_pen.right(my_angle)
            light_hue_pen.fd(count/9)
            f.save_thumb()
            light_hue_pen.pendown()
            light_hue_pen.fd(count * phi)
            f.save_thumb()

            green_hue_pen.left(my_angle)
            green_hue_pen.backward(count / phi) 
            f.save_thumb()
            green_hue_pen.circle(count /3, - my_angle, 9)
            f.save_thumb()
            
            #make blue hued dots
            blue_hue_pen.pensize(count/24)  
            blue_hue_pen.left(my_angle / 2)
            blue_hue_pen.dot(count /24)
            f.save_thumb()
            blue_hue_pen.penup()
            blue_hue_pen.backward(count)
            f.save_thumb()
            blue_hue_pen.pendown()
            blue_hue_pen.fd(count / 60)
            Q_seed.dot(3)
            process_thumbs()
            
#         reset_all_pens()
        Lg.logger.info(f'{my_script}:Starting Loop Three @ {Tm.my_time}')
        count = 0
        for count in range(my_range):
            Q_seed.dot(3)
            turtle.bgcolor(10, 200, 200)
            pick_dark() 
            pick_gold()  
            pick_red() 

            red_hue_pen.right(my_angle / 2) 
            red_hue_pen.pensize(count / 54)
            red_hue_pen.circle(count / 3, my_angle, 6)
            f.save_thumb()
            red_hue_pen.penup()
            red_hue_pen.backward(count / phi + count)
            f.save_thumb()
            red_hue_pen.pendown()

            dark_hue_pen.right(my_angle) 
            dark_hue_pen.pensize(count / 54)
            dark_hue_pen.backward(count / phi)
            f.save_thumb()

            red_hue_pen.right(my_angle / 2) 
            red_hue_pen.fd(count  / 2)
            f.save_thumb()

            dark_hue_pen.right(my_angle)  
            dark_hue_pen.fd(count )
            f.save_thumb()

            red_hue_pen.penup()  
            red_hue_pen.right(my_angle)
            red_hue_pen.fd(count/9)
            f.save_thumb()
            red_hue_pen.pendown()
            red_hue_pen.fd(count * phi)
            f.save_thumb()

            dark_hue_pen.left(my_angle)
            dark_hue_pen.backward(count / phi)
            f.save_thumb()
            dark_hue_pen.circle(count /3, - my_angle, 9)
            f.save_thumb()
            
            #make gold hued dots
            gold_hue_pen.pensize(count/24)
            gold_hue_pen.left(my_angle / 2) 
            gold_hue_pen.dot(count /24)
            f.save_thumb()
            gold_hue_pen.penup()
            gold_hue_pen.backward(count)
            f.save_thumb()
            gold_hue_pen.pendown()
            gold_hue_pen.fd(count / 60)
            f.save_thumb()
            Q_seed.dot(3)
#             Lg.logger.info(f'The value of count is {count}')
            process_thumbs()
            
    produce_reversing_video()
    finalize()
# dark_mandala_extended()



#  module_48
#**************************************************************************************************************
  # First Published to YouTube on 11/21/2021
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Status: Last Update: 11/30/2023, Last Completed Run: 11/30/2023
  Uses local turtle pens pa and indigo_hue_pen; changed name from Awesome_Mandala_Old to
  Intense_Mandala. Impemented special center black dot pen, quantum_seed. Duration is based upon quantity of angles selected.
 '''  
def Intense_Mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range, pa
    my_script = 'Intense Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash,= str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        all_pens_home()
        my_angle = a.i_angle_float[a.i]
        Lg.logger.info(f'{my_script}: Starting to draw {my_angle:.2f} degrees angles at {Tm.this_time}')
        turtle.title(f'{my_script}:{my_angle} Degrees Angle and {au.my_track}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        my_range = 255 * 4
        R , G = 0, 0
        M, N, X, Y, Z = 255, 110, 10, 155, 255
        B = random.randint(10, 50)
        L = random.randint(150, 255)
        pick_indigo() # indigo_hue_pen
        indigo_hue_pen.left(my_angle/2)
        pa.left(my_angle/2)
        Lg.logger.info(f'{my_script}:The Value of color B is: {B}')
        Lg.logger.info(f'{my_script}:The Value of color L is: {L}')   
        for count in range(my_range):
            pick_indigo() # indigo_hue_pen
            turtle.bgcolor(0, B, 0)
            indigo_hue_pen.pensize(count/120)
            indigo_hue_pen.left(my_angle)
            indigo_hue_pen.fd(count /4)
            f.save_thumb()
            pa.pensize(count / 200)
            pa.rt(my_angle)
            if count <= 255:
                pa.pencolor(L, M - count, M - count)
            else:
                pa.pencolor(L, count% 255, X)
            pa.circle(count *.25, - my_angle, 9)
            f.save_thumb()
            Q_seed.dot(3)
            process_thumbs()
        pa.clear()
        indigo_hue_pen.reset()
    produce_reversing_video()
    finalize()
# Intense_Mandala()



#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Status: Creation Date: 12/2/2023, Last Completed Run: 12/4/2023
  Uses local turtle pens pa and indigo_hue_pen; spun off from Intense Mandala.
  Features first attempt to freeze the size of the mandala, spin it and change the coloring, as well as
  focusing on resonant frequencies of color and sound.
 '''  
def Resonance_Mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range, pa
    my_script = 'Resonance Mandala'
    Lg.logger.info(f'{my_script}:Status: Creation Date: 12/2/2023; Last Update/Run: {Tm.my_date}')
    Lg.logger.info(f'{my_script}:Uses local turtle pens pa and indigo_hue_pen; spun off from Intense Mandala.')
    Lg.logger.info(f'{my_script}:Features first attempt to freeze the size of the mandala,') 
    Lg.logger.info(f'{my_script}:Spin the mandala and change the coloring; portraying resonant frequencies of color and sound.')
    startup_script()
    make_folder()
    t.my_angles, t.my_splash,= str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        all_pens_home()
        my_angle = a.i_angle_float[a.i]
        Lg.logger.info(f'{my_script}: Starting to draw {my_angle:.2f} degrees angles at {Tm.this_time}')
        turtle.title(f'{my_script}:{my_angle} Degrees Angle and {au.my_track}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        my_range = 1148
        R , G = 0, 0
        M, N, X, Y, Z = 255, 110, 10, 155, 255
        B = random.randint(10, 50)
        L = random.randint(150, 255)
        pick_orange() # orange_hue_pen
        orange_hue_pen.left(my_angle/2)
        pa.left(my_angle/2)
        Lg.logger.info(f'{my_script}:The Value of color B is: {B}')
        Lg.logger.info(f'{my_script}:The Value of color L is: {L}')   
        for count in range(my_range):
            turtle.bgcolor(10, 75, 80)
            pa.pensize(count / 120)
            pa.rt(my_angle)
            if count <= my_range  * .66:
                Q_seed.dot(5)
                f.save_thumb()
                pa.pencolor(L, Y - count % 150, M - count % 240)
                pa.fd(count / 2)
                f.save_thumb()
                pa.penup()
                pa.fd(count /2)
                f.save_thumb()
                pa.pendown()
                pa.fd(count /2)
                f.save_thumb()
                pick_orange() # orange_hue_pen
                orange_hue_pen.pensize(count/120)
                orange_hue_pen.left(my_angle /2)
                orange_hue_pen.fd(count /3)
                f.save_thumb()
                Q_seed.dot(5)
                f.save_thumb
            else:
                # indigo_hue_pen as light_hue_pen
                Q_seed.dot(5)
                f.save_thumb()
                orange_hue_pen.pencolor(random.randrange(190, 215, 1), random.randrange(191, 254, 1),random.randrange(200, 253, 1))  
                orange_hue_pen.pensize(count/120)
                orange_hue_pen.left(my_angle /2)
                orange_hue_pen.fd(count /3)
                f.save_thumb()
                Q_seed.dot(5)
                f.save_thumb()
#                 print(f'The count is {count}') # Uncomment for testing
        process_thumbs()  
        pa.clear()
        indigo_hue_pen.reset()
    produce_reversing_video()
    finalize()
# Resonance_Mandala()
#  module_49
#***************************
''' Status: Creation Date: 12/7/2023, Last Completed Run: 12/7/2023
  Created specifically ot benchmark the time to process a directory of
  100 png files. To be used only for internal testing only.
  '''  
def benchmark_mandala():
    global my_project, my_angle, my_title, my_script, str_angles, count, my_range, pa
    my_script = 'benchmark_mandala'
    Lg.logger.info(f'{my_script}:Status: Creation Date: 12/7/2023; Last Update: {Tm.my_date}')
    startup_script()
    make_folder()
    t.my_angles, t.my_splash,= str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        all_pens_home()
        my_angle = a.i_angle_float[a.i]
        Lg.logger.info(f'{my_script}: Starting to draw {my_angle:.2f} degrees angles at {Tm.this_time}')
        turtle.title(f'{my_script}:{my_angle} Degrees Angle and {au.my_track}')
        t.my_title = f'{my_script}: {my_angle} Degrees Angle and {au.my_track}'
        my_range = 50 #count will be doubled for reversed video
        for count in range(my_range):
            turtle.bgcolor(10, 75, 80)
            pa.pencolor(200 ,200, 20)
            pa.pensize(count /50)
            pa.rt(my_angle)
            pa.fd(count * 2)
            f.save_thumb()
            Lg.logger.info(f'The count is {count}')
            print(f'The count is {count}') # Uncomment for testing
    produce_reversing_video()
    finalize()       
        
# benchmark_mandala()  

'''--------------------------------------------------------Multiple Scripts Processor---------------------------------------------------------------------------
12/10/2023: Originally created to run the short scripts above, This section sets up any selected mandala modules into a list that can
then execute them, one by one, in a series. The angle or set of angles are the same, but for each module, a differnt audio clip is
randomly selected, unless I  switch. I might try to automate the selection options later.
'''
global my_script, script
my_script = [influence_mandala, Vanguard_Mandala, assurance_mandala, effective_mandala, prosper_mandala, brave_mandala]
# my_script = [effective_mandala] # Uncomment to test a single function
my_script_count = len(my_script)

def pick_mandala_script():
    global my_script, script
    Lg.logger.info(f'{my_script}:Preparing to run {my_script_count} scripts @ {Tm.this_time}')
    pick_script_starttime = timer()
    for script in my_script:
        script()
    Lg.logger.info(f'{my_script}:Completed the execution of {my_script_count} scripts @ {Tm.this_time}')
    pick_script_endtime = timer()
    elapsed_time = pick_script_endtime - pick_script_starttime
    Lg.logger.info(f'Total time to run this session of pick_mandala_script: {elapsed_time/3600:.2f} hours')
    exit()
pick_mandala_script()   

#nomega 
'''***************************************************************************************************************************************''
 List of modules. To run, uncomment the function row. Caution: Computer memory and speed can take a hit with the 250+ looping  screenshots, image creation,
 and video creation associated with each image file. No load testing has been made at this time. Also, because of the looping screenshots a dedicated,
 always-on monitor is needed while the module is running. The screenshot scripts will capture anything that is on the monitor screen while it is running.
 Power-saving and screensaver apps should be disabled while this code is running.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
'''
'====================================================================================================================================================================='
# Tested and ran successfully using medium clips, faster speed
# basic_yin_yang()  # ( module_1)   Tested and verified on 1/3/2023; Located @ line 165 - 195, 1st module of 48. An animated rendition of the ancient chinese yin-yang graphic. My original; currently
                    # the most popular one on YouTube. Added the working do_video on 1/14/2022 which converts the png files/
                    #to gif, mp4, and avi files. Successfully automated video (.avi) creation 1/20/2022.
                    #Successfully lengthened and added long audio clips on 8/17/2022.
# basic_yin_yang_extended()
# cloverleaf_extended() #Located @ line 3921 - 4154, 38th module of 50' Created 11/ 17/2022



#  This first group of modules are extended versions of their parent script, as indicated by their name. The are set to also empoly the list of extended music clips.
'============================================================================================================================================================='
'''Runs with Solfeggio:

'''
# majestic_mandala_extended()  # Completed major update of format to start with angle selection to prevent faulty looping, by prioritizing angle selection.
# mystical_mandala()  #Completed major update of code to start with angle selection. #Working ok as of 7/1/ 2023; runs well with Solfeggio; 7 minutes duration
# simple_mandala() # module_2; formerly titiled colorful mandala before 4/27/2023. Modified to run very fast; uses 8 loops. Tested and verified on 1/19/2023; Row 236 - 440, First one over 200 lines of code; #2 of 48
# reversing_simple_mandala() #Based on simple mandala; has option to include multiple angles;  exclusively uses the pick_hues function to select colors.
# strong_mandala()
# colorful_mandala_extended() # Tested and verified on 1/3/2023; 'Located @ line 260 - 385,  3rd module of 48', created on 11/6/2022
# glorious_mandala_extended()  #Created 11/13/2022 Located @ line 2990- 3111, 32nd module of 48.  # Output duration is 6 minutes; last ran on 5/19/2023; created number box for single angle selection
# awesome_mandala_extended() # Completed major update of format to start with angle selection to prevent faulty looping, by prioritizing angle selection.
# joyous_mandala() # Runs for 12 minutes
# stupendous_mandala() # module_21 Reworked and tested 1/16/2023. First to use the t.fade function, extends the loop count beyond the 255 limit imposed by RGB. Row 1652 - 1101, number 17 of 48.
    #Derived from Vanguard_Mandala. Created 1/8/2022. added print to file 3/1/2022Features a more prominent center than it's parent.  Works well.
# courage_mandala() # module_22 #Tested and verified on 1/12/2023; Located @ line 1937 -2546, 24th module of 48' 4 of 48, Published to YouTube on 11/2/2021
# brave_mandala_extended() #Completed major update of format to start with angle selection to prevent faulty looping, by prioritizing angle selection.Located @ line 1645 -1736, 20th module of 48
# bold_mandala()  # module_9 Modified, tested and verified on 1/8/2023; Located @ line 713 - 782, 9th module of 48', Updated to automate video creation  Implemented 'phi Offset' Angle on 4/28/2022.

# reversing_awesome_mandala()  # last run on 7/25/2023
# Plain_mandala() last run on 9/6/2023

# dark_mandala() #module_7 Tested and verified 1/4/2023;  Revised 7/30/2023
# Vanguard_Mandala() # module_19; Tested and verified 1/10/2023; Located @ line 1331- 1380, 18th module of 48. Derived from awesome_mandala. # Processed 90 degrees to MP4 on 12/15/2021

# Fantastic_Mandala() Implemented many upgrades, ran multiple times 8/8 - 8/13 2023 and loaded to YouTube
# glorious_mandala() # module_18 Tested and verified 1/10/2023; Created 4/6/2022, based on stupendous mandala. Located @ line 3153- 3219, 41st module of 48. 2 minute duration video.
# breathing_yin_yang()
'Run Date: 09/11 - 9/12/2023'
# ribbons_mandala()  #(Edited from Mandala_160_09292020); converted to mult-angles on 1/20/2022; updated and run on 9/6/2023
'Run date: 09/18/2023 - 9/22/2023'
# mighty_awesome_mandala() # Ran with many improvements 9/22/2023; Tested and verified 01/11/2023; Loaded to YouTube channel; Based on pretty awesome mandala
'Run Date: 9/22/23 - 9/26/2023'
# hued_gradiant_mandala()  #module_9 Row 647 - 733, 9 of 48
'Run Date: 09/26/2023 - 09/28/2023'
# brave_mandala() #module_19 Located @ line 1386 -1449, Derived from awesome_mandala; 18 of 48
'Run Date: 09/28/2023 - 10/2/2023'
# sirius_mandala() # module_33  Located @2335 - 2408. Developed June 2022, Added 6/28/2022. 33rd module of 48. Makes beautiful diagrams.
'Run Date:10/2/2023 -'
# awesome_mandala()  #  Tested and verified on 1/7/2023. module_15 15 of 48, Located at lines 2052 - 2109. Processed to mp4 and published to YouTube on 11/21/2021. modified 11/20/2021, This is exceptional.
'Run Date:10/20/2023 -'
# random_mandala()  # Successfully modified the awesome mandala to run four distinct scripts, currently two from the former awesome mandala, from the hued gradiant, and from the stupendous. Fine-tuning ongoing.
# ribbons_mandala()
# black_seed()   # module_35 Needs more work

# cloverleaf() # module_33 31 of 48, Located at line  2247 - 2304. Created 3/6/2022.


# Work on cloverleaf_extended()


'======================================================================================================================================================='


#

# # Intense_Mandala()

# # wall_show_extended() #Located @ line 3266- 3393, 34th module of 41.

# brave_mandala_decimated()
# WORK ON BG COLOR dark_mandala_extended() # Tested and verified on 1/6/2023; Created 1/4/2023; Located at lines 3717 - 3873; 47th module of 48.

'''
Run long_clips
'''



'''Run short clips
'''

'===================================================================================================================================================================='
#  This second group of modules specifies a single angle; has no looping lists of angles



# occilating_yin_yang() #Based on basic_yin_yang; introduces hue changes and direction changes.

# growing_yin_yang() #module_3 12 of 48, Published to YouTube 11/11/2021, Need to work on further as of 4/3/2022


# circular_mandala_205()  # module_4 25 of 48; Added 12/9/2021 (Edited from Mandala_160_09292020) Processed to mp4 12/9/2021
'======================================================================================================================================================================='
# This third group of modules specifies a list of angles to loop


#
# joyous_mandala() # module_5; Tested and verified 1/4/2023; Rows 465 - 515,   5th module of 48. Features Blue and Red Hues. Modified 12/17/2021 Updated to automate video creation#


# iridescent_polygram()  # module_8; Tested and verified 1/4/2023; Row 645 - 723, 8 of 48; Modified 1/2/2022 Updated to automate video creation

# animated_abstraction()  #  module_9 10 of 48, Thumbs created 11/21/2021
# animated_hued_polygram()  # module_13  Located @ line 929 - 989, number 13 of 48, created 11/14/2021; added print to file 3/1/2022
#
#






# color_shifting_mandala() # module_20 Rows 1274 - 1327, 19 of 48 work on
# Hued_freedom_star() # module_26 Row 1358 - 1428, 22 of 48; Added 12/4/2021
# arc_star() #module_28 27 of 48; Located at lines 1586 - 1654. Added 01/06/2022. Derived from a Thought Matrix arc-star wriiten by me in 2020.\
#                       # Employs first use of automated creation of angle lists using numpy arange.
# home_star() #module_ 28 of 48; Located at lines 2007 - 2078.  Added 01/06/2022. Derived from a Thought Matrix arc-star scripted by me in 2020.\

# use_abs() # module_31 29 of 48; Located at line 1890. Uses the abs() function to draw the sides and points such that it continues until the point of origin is reached.
# double_take() # module_32 30 of 48; Located at line 1843 - 1881. Facilitates the creation of a hexagram by using 2 pens drawn\
#                    # with same angles in opposite directions. Using specific angle array named a.i.angle_doublewall_show() # module_34 of 48. Located @ line 2408- 2474. Working on a suitable product to frame and display on a wall. Began development August 2022.


'===================================================================================================================================================='
# This set of modules require tweaking and modification

# # # #     #NEEDS Work -- Too Slow!# gold_red_mandala_extended() # Created 11/18/2022; 'Located @ line 1856 - 1961, 21st module of 48')  # 4:12 minutes
# #     #NEEDS Work -- Too slow!# gold_red_mandala()  # module_25 Located @ line 1801 - 1852, 21st module of 48 Added 12/3/2021; processed to mp4 12/16/2021(added 3 degrees)


# NEEDS SOME TWEAKING blue_orange_mandala_144() #module_23  23 of 48; Located at rows 1510 - 1568. Added 12/7/2021 (Edited from Mandala_160_09292020) Processed to mp4 12/7/2021


# gradiant_mandala() #  module_14 Row  785 - 852, 11 of 48. Last run date: 2/1/2022
# pretty_polygonial()   # module_16   Row 856, 14 of 48, modified 11/19/2021  nEEDS WORK!
# Work on some more  multi_hued_polygram() # module_23 Row  1125 - 1180, 20 of 48
# black_seed()   # module_35 Needs more work
# occillating_polygon() # module_27 NEED WORK ON THE UNDO FUNCTION Located @ line 1891 - 1968, 26th module of 48; Added 12/28/2021  Is first attempt to use undo function as way to create occillation
'======================================================================================================================================================================================================='
# Finalizing scripts to sync all files and folders
# turtle.setup(550,550) # Minimized turtle window to observe screen and read shell output
# f.move_all() # Moves files to appropriate locations
# Lg.logger.info(f'MasterMandalaMaker: All files have been moved to their final home')
# f.sync_mandala_folders()  # Sync video and script folders backups
# Lg.logger.info(f'MasterMandalaMaker: Folders and files have been synced and backed up')
# Lg.logger.warning('Program is terminating')
# turtle.bye()  # End the program;  Default is to leave uncommented
# exit()
