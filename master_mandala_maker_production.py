'''
Copyright (C) 2017 - 2023  Leon Hatton
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
    Primary Python IDE is Thonny, currently version 4.0.1 on Python 3.10.

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
from datetime import datetime
import My_template as t
import my_angles as a  #Processes angle selections714 Hz
import my_hues as h # Defines turtle pen names; Aids in color selections
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

global file_key, my_key # Used to set a random number to avoid making duplicate file names.
import random
file_key = random.randrange(100,90000,1)
my_key = ' -r.' + str(file_key)

# global L

global start, end

global count
count = 0

global my_angle

global my_project
my_project = str('The Novanno Project')

global folder_name
folder_name = 'Novanno_Folder'

global logger
global formatter, fileHandler, consoleHandler
logger = Lg.logging.getLogger(t.my_project) # Initialize global logger
fileHandler = Lg.logging.FileHandler(t.my_logfile)
fileHandler.setLevel(Lg.logging.INFO)
consoleHandler = Lg.logging.StreamHandler()
consoleHandler.setLevel(Lg.logging.INFO)
logger.setLevel(Lg.logging.INFO)
logger.addHandler(Lg.fileHandler)
logger.addHandler(Lg.consoleHandler)
Lg.logger.info('Logger Source: MandalaMaker')

#Create a local turtle clone
def initialize_loc_pen():
    global loc_pen
    loc_pen = turtle.Turtle()
    loc_pen.speed(0)
    loc_pen.shape('blank')
    loc_pen.hideturtle()
    loc_pen.pensize(1)
    loc_pen.penup()
    loc_pen.setpos(0,0)
    loc_pen.seth(0) 
    loc_pen.pendown()
initialize_loc_pen()    
#     
def initialize_loc_pen_a():
    global loc_pen_a
    loc_pen_a = turtle.Turtle()
    loc_pen_a.speed(0)
    loc_pen_a.shape('blank')
    loc_pen_a.pensize(1)
    loc_pen_a.penup()
    loc_pen_a.setpos(0,0)
    loc_pen_a.seth(my_angle) 
    loc_pen_a.pendown()
# initialize_loc_pen_a()

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

def reset_pa_pb():
    pa.reset()
    pb.reset()
    gc.collect()
    make_turtle_pa()
    make_turtle_pb()        
    
# Set up Logger
def startup_script(): # Starts module clock, sets up turtle functions, starts log file
    global module_start_time
    module_start_time = Tm.datetime.datetime.now()
    t.my_venv()
    gc.enable()
    t.set_up_my_pen()
#     start = str(Tm.datetime.datetime.fromtimestamp(datetime))
#     end = str(Tm.datetime.datetime.fromtimestamp(datetime))
    
    
    
def select_angle():
    global my_angle
    default_angle = 120
    my_angle = turtle.numinput('Input Angle:', 'Angle, ', 144)
    if my_angle in range(-24, 24, 1):
        my_angle = default_angle
    return my_angle

# Creates working folders and declares variables; gets things rolling
def make_folder(): # Creates directories for video production; selects audio track to be used; sets watermark(audio track)
    global folder_name, my_project, str_angles, project_title
    a.pick_angles()
    a.i_angle = a.i_angle_float
    str_angles = [int(i) for i in (a.i_angle)]
    Lg.logger.info(f'The {len(a.i_angle)} angles to be drawn are {str_angles}') 
    Lg.logger.info('Selecting track from runtime-generated list')
#     au.get_special_track()
    au.pick_custom_length_track()
    my_project = Lg.my_project
    Lg.my_project = f'{my_mandala_name}-({len(a.i_angle)}){str_angles} angles-Audio-{au.my_track}-{Tm.project_time}'
    project_title = f'{my_mandala_name} with {len(a.i_angle)} ({str_angles}) angles; Audio: {au.my_track} @{Tm.project_time}' 
    my_logfile = f'{f.my_work_dir}/Logs/{Lg.my_project}.log'
    Lg.logger.info(f'Starting {Lg.my_project} @ {Tm.start_time()}')
    Lg.logger.info(f'This is {Lg.my_project} code')
    Lg.logger.info(f'Setting up directories and files for video production  @ {Tm.my_time}')
    folder_name = Lg.my_project.replace("[","").replace("]","").replace("'","").replace(".0","") # .replace(" ","")
    t.my_project = Lg.my_project
    t.folder_name = folder_name
    t.project_title = project_title
    s.splash_screen()
    Lg.logger.info(f'Folder name is {t.folder_name}')
    f.make_reverse_png_folder()
    f.make_archive_folder()
    turtle.title(t.folder_name)
    Lg.logger.info(f'Presenting {t.folder_name}')
#     f.make_daily_activities_log()
    s.watermark()

#random magenta hues
def pick_magenta(): # Pen t.me
    r = random.randrange(125, 175, 1)
    g = random.randrange(0, 5, 1)
    b = random.randrange(75, 150, 1)
    I = r
    J = g
    K = b
    loc_pen.pencolor(I, J, K)
    return loc_pen



def process_thumbs():
    if count == my_range - 1:
        f.save_final_thumb()
        for i in range (60):
            f.save_thumb()
    else:
        f.save_thumb() 
    


# Starts video creation process
def stage_video():
    f.save_final_thumb()
    turtle.bye()
    Lg.logger.info(f'Starting video creation @ {Tm.my_time}.........')
    f.set_vid_env()
    Lg.logger.info(f'Starting merger of video and audio clips @ {Tm.my_time}..........')
    f.sync_av()
    Lg.logger.info(f'Making of {my_mandala_name} by Leon Hatton completed @ {Tm.date_time}')
    Lg.logger.info(f'Stopping {t.folder_name} by Leon Hatton on {Tm.my_time}')
    Lg.logger.info('****************************************************************************')
    
def stage_reverse_video():
    f.save_final_thumb()
    turtle.bye()
    gc.collect()
    Tm.set_time()
    Lg.logger.info(f'Starting video creation @ {Tm.my_time}........')
    f.set_reverse_vid_env()
    Tm.set_time()
    Lg.logger.info(f'Starting merger of video and audio clips @ {Tm.my_time}.........')
    f.sync_av()
    Tm.set_time()
    Lg.logger.info(f'Making of {my_mandala_name} by Leon Hatton completed @ {Tm.date_time}')
    Tm.set_time()
    Lg.logger.info(f'Stopping  {t.folder_name} by Leon Hatton @ {Tm.my_time}')
    Lg.logger.info('****************************************************************************')


# Shuts down module processing and closes Turtle
def finalize():
    global module_end_time, difference, elapsed_time
    module_end_time = Tm.datetime.datetime.now()
    difference = module_end_time - module_start_time
    elapsed_time = difference.total_seconds() /3600
    Lg.logger.info(f'Module Run Time: {elapsed_time} Hours')
    Lg.logger.info('************************************************************************')
    Lg.logger.info(f'Preparing to backup and sync all files and folders @ {Tm.my_time}')
    Lg.logger.info('Moving files to appropriate folders')
    f.move_all() # Moves files to appropriate locations
    Lg.logger.info('Video .mp4 files have been moved to /Videos/')
    Lg.logger.info('Image .png files have been moved to /Thumbs/')
    Lg.logger.info('Image .jpg files have been moved to /Pictures/Mandala Final Thumbs/')
    Lg.logger.info('Pics have been moved to Pictures folder')
    Lg.logger.info('================================================================================')
    Lg.logger.info(f'Starting to delete screenshots @ {Tm.my_time}....') # Thumbs are not necesssary after the video is created from them
    f.clear_thumbs()
    Tm.set_time()
    Lg.logger.info(f'Screenshots deletions completed @ {Tm.my_time}')
    Lg.logger.info('Starting to update the backup files.....')
    f.sync_mandala_folders()  # Sync video and script folders backups
    Lg.logger.info('Folders and files have been synced and backed up')
    logger.warning('Shutting down this module and resetting logger')
    Tm.set_time()
    Lg.logger.info(f'All modules have been completed successfully. MandalaMaker Program shutting down @ {Tm.end_time()}')
    logger.handlers.clear()
    exit()
# finalize()

def reset_all():   #Utility to clear screen and reset to sequence next screen drawing
    turtle.clearscreen()
    t.my_pen.reset()
    t.el.reset()
    t.ce.reset()
    t.lr.reset()
    t.li.reset()
    t.lq.reset()
    t.lu.reset()
    t.go.reset()
    t.lg.reset()
    t.lb.reset()
    t.me.reset()
    t.lz.reset()
    t.ly.reset()
    turtle.reset()
#     Lg.logger.info('Pausing 9 seconds for user option to permanently manually stop the program at  end of sub-routine  before the next one starts.................')
    Lg.logger.info('All instances of turtle have been reset')
    time.sleep(3)
    
def set_ce_home(): #Random Pen
    t.ce.penup()
    t.ce.setpos(0,0)  
    t.ce.seth(0)
    t.ce.hideturtle()
    t.ce.pendown()
    
def set_el_home(): # Light Pen
    t.el.penup()
    t.el.setpos(0,0)  
    t.el.seth(0)
    t.el.hideturtle()
    t.el.pendown()

def set_go_home(): # Gold Pen
    t.go.penup()
    t.go.setpos(0,0)  
    t.go.seth(0)
    t.go.hideturtle()
    t.go.pendown()

def set_lb_home(): # Blue Pen
    t.lb.penup()
    t.lb.setpos(0,0)  
    t.lb.seth(0)
    t.lb.hideturtle()
    t.lb.pendown()

def set_ly_home():  #Yellow Pen
    t.ly.penup()
    t.ly.setpos(0,0)  
    t.ly.seth(0)
    t.ly.hideturtle()
    t.ly.pendown()

def set_me_home(): #Magenta Pen
    t.me.penup()
    t.me.setpos(0,0)  
    t.me.seth(0)
    t.me.hideturtle()
    t.me.pendown()

def set_lz_home(): # Dark Pen
    t.lz.penup()
    t.lz.setpos(0,0)  
    t.lz.seth(0)
    t.lz.hideturtle()
    t.lz.pendown()

def set_lg_home(): # Green Pen
    t.lg.penup()
    t.lg.setpos(0,0)  
    t.lg.seth(0)
    t.lg.hideturtle()
    t.lg.pendown()

def set_lq_home():  # Orange Pen
    t.lq.penup()
    t.lq.setpos(0,0) 
    t.lq.seth(0)
    t.lq.hideturtle()
    t.lq.pendown()

def set_li_home(): #Indigo Pen
    t.li.penup()
    t.li.setpos(0,0)  
    t.li.seth(0)
    t.li.hideturtle()
    t.li.pendown()

def set_lu_home(): #Red pen
    t.lu.penup()
    t.lu.setpos(0,0)  
    t.lu.seth(0)
    t.lu.hideturtle()
    t.lu.pendown()

def set_lr_home(): # Random_a Pen
    t.lr.penup()
    t.lr.setpos(0,0)  
    t.lr.seth(0)
    t.lr.hideturtle()
    t.lr.pendown()


def all_pens_home():
    # Random Pen   #1
    t.ce.penup()
    t.ce.setpos(0,0) 
    t.ce.seth(0)
    t.ce.hideturtle()
    t.ce.pendown()
    # Light Pen  #2
    t.el.penup()
    t.el.setpos(0,0)  
    t.el.seth(0)
    t.el.hideturtle()
    t.el.pendown()
    #Gold Pen  #3
    t.go.penup()
    t.go.setpos(0,0)  
    t.go.seth(0)
    t.go.hideturtle()
    t.go.pendown()
    # Blue Pen  #4
    t.lb.penup()
    t.lb.setpos(0,0) 
    t.lb.seth(0)
    t.lb.hideturtle()
    t.lb.pendown()
    #Green Pen  #5
    t.lg.penup()
    t.lg.setpos(0,0)  
    t.lg.seth(0)
    t.lg.hideturtle()
    t.lg.pendown()
    # Indigo Pen  #6
    t.li.penup()
    t.li.setpos(0,0)  
    t.li.seth(0)
    t.li.hideturtle()
    t.li.pendown()
     # Orange Pen  #7
    t.lq.penup()
    t.lq.setpos(0,0)  
    t.lq.seth(0)
    t.lq.hideturtle()
    t.lq.pendown()
    # Random_a Pen  #8
    t.lr.penup()
    t.lr.setpos(0,0)  
    t.lr.seth(0)
    t.lr.hideturtle()
    t.lr.pendown()
    #  Red Pen  #9
    t.lu.penup()
    t.lu.setpos(0,0)  
    t.lu.seth(0)
    t.lu.hideturtle()
    t.lu.pendown()
    # Yellow Pen  #10
    t.ly.penup()
    t.ly.setpos(0,0) 
    t.ly.seth(0)
    t.ly.hideturtle()
    t.ly.pendown()
    # Dark Pen  #11
    t.lz.penup()
    t.lz.setpos(0,0)  
    t.lz.seth(0)
    t.lz.hideturtle()
    t.lz.pendown()
    #Magenta Pen  #12
    t.me.penup()
    t.me.setpos(0,0)  
    t.me.seth(0)
    t.me.hideturtle()
    t.me.pendown()
    
   
def check_memory():
#     p = psutil.Process()
#     Lg.logger.info(f'Memory Use: {p.memory_full_info()}')
    pid = os.getpid()
    python_process = psutil.Process(pid)
    memoryUse = python_process.memory_full_info()[7] /2 **30
#     memory usage in GB
    Lg.logger.info(f'Memory Use: {memoryUse:.2f} GB')
    
    
# Future: Using zip function to bind angle and audio file variables for parallel processing


def colorful_mandala_script():
    loc_pen.pensize(count / 103)
    loc_pen_a.pensize(count / 103)
    loc_pen.left(my_angle)
    loc_pen.fd(count / phi)
    loc_pen_a.fd(count)
    loc_pen_a.right(my_angle / 2)
    loc_pen_a.fd(count / pi)
    loc_pen_a.right(my_angle)
    loc_pen_a.fd(count / pi)
    loc_pen.left(my_angle)
    loc_pen.circle(count / phi, - my_angle, 3)
    loc_pen.fd(count / pi)
    
def colorful_mandala_wheels():
    loc_pen.speed(0)
    loc_pen_a.speed(0)
    loc_pen.pensize(count / 103)
    loc_pen_a.pensize(count / 103)
    loc_pen.circle(count / 1, my_angle)
    loc_pen_a.circle(count / 2, - my_angle)

def hued_gradiant_script():
    global count
    for count in range(my_range):
        turtle.bgcolor(0,0,0)
        R =  random.randint(100,200)
        G =  0
        B =  255
        L = 255
        M = random.randint(100,200)
        N = 0
        pa.pencolor( R , count %21, B - count %42 )
        pb.pencolor(L - count % 42, M, N + count %21)
        pa.fd( count * t.phi)
        process_thumbs()
        pb.fd( count + t.phi)
        process_thumbs()
        pa.left(my_angle)
        pb.left(my_angle * t.phi)  # This is the offset angle
        pb.fd(count / 2)
        process_thumbs()
        pa.fd(count / 3)
        process_thumbs()
        pa.left(my_angle)
        pb.left(my_angle * t.phi) # This is the offset angle
        pa.fd(count / 33)
        process_thumbs()
        pb.circle(count / t.phi, my_angle * t.phi, 6)
        process_thumbs()
        pa.pencolor(255, 255, count %255)
        pa.dot(9)
        process_thumbs()
        pa.right(my_angle)
        pb.right(my_angle * t.phi) # This is the offset angle
        pa.fd(count / t.phi)
        process_thumbs()
        pb.fd(count / t.phi)
        process_thumbs()
        pa.pencolor(random.randint(100,200), 255, 255)
        pa.dot(9)
        process_thumbs()
        pb.dot(9)
        process_thumbs()
        pb.pensize(count / my_pensize)
        pa.pensize(count / my_pensize)
        process_thumbs()           


global length
length = 255  #Default is 255; any lower number for testing

# Index of modules:

#Group A : Yin-Yang Series (Three Modules)

#  Group A module_1
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Basic Yin-Yang outputs to 10 minute duration when default settings are applied. Runtime over three days!
# Can re-use the thumbnail pgn output and the no_video poutput to create new videos
def basic_yin_yang(): # **
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Basic Yin-Yang'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_angle = 180
    turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
    for count  in range (5): # Default is 5
        for count in range(1800):  # 1800 is default, duration 10 minutes. Use lower number for testing. The higher the number, the longer the show.
            t.el.pensize(10)
            t.el.color(0,0,0) # 0,0,0 is default (Black)
            t.el.rt(-my_angle + t.phi)
            t.el.circle(250)
            process_thumbs()
            t.el.pensize(10)
            t.el.color(255,255,255) # 255,255,255 is default (White)
            t.el.rt(-my_angle)
            t.el.circle(250)
            process_thumbs()
            
        count = 0
        for count in range (1800): # Default is 1800
            t.el.pensize(10)
            t.el.color(0,0,0) # 0,0,0 is default (Black)
            t.el.left(-my_angle + t.phi)
            t.el.circle(250)
            process_thumbs()
            t.el.color(255,255,255) # 255,255,255 is default (White)
            t.el.left(-my_angle)
            t.el.circle(250)
            process_thumbs()
    stage_video()
    finalize()


#  Group A module_2
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
def basic_yin_yang_extended(): # **
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Basic Yin-Yang Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    count = 0
    my_range =  600
    t.el.hideturtle()
    my_angle = 180
    turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
    for count in range(my_range ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        t.el.pensize(10)
        t.el.color(0,0,0) # 0,0,0 is default (Black)
        t.el.rt(-my_angle + phi)
        t.el.circle(250)
        t.el.pensize(10)
        t.el.color(255, 255, 255) # 255,255,255 is default (White)
        t.el.rt(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        Lg.logger.info('The value of count is  '+ str(count))
        Lg.logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(0, 0, 0)
    count = 0
    for count in range (my_range):
        t.el.pensize(10)
        t.el.color(255,255,255) # 0,0,0 is default (Black)
        t.el.left(-my_angle + phi)
        t.el.circle(250)
        t.el.color(50,255,50) # 255,255,255 is default (White)
        t.el.left(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        Lg.logger.info('The value of count is  '+ str(count))
        Lg.logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(255,255,255)    
    for count in range(my_range ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        t.el.pensize(10)
        t.el.color(0,0,0) # 0,0,0 is default (Black)
        t.el.rt(-my_angle + phi)
        t.el.circle(250)
        t.el.pensize(10)
        t.el.color(255,50,125) # 255,255,255 is default (White)
        t.el.rt(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        Lg.logger.info('The value of count is  '+ str(count))
        Lg.logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(252, 148, 10)
    count = 0
    for count in range (my_range):
        turtle.bgcolor(252 - count % 200, 148 + count% 100, 10)
        t.el.pensize(10)
        t.el.color(125,125,125) # 0,0,0 is default (Black)
        t.el.left(-my_angle + phi)
        t.el.circle(250)
        t.el.color(150,150,255) # 255,255,255 is default (White)
        t.el.left(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        Lg.logger.info('The value of count is  '+ str(count))
        Lg.logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    count = 0
    turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
    for count in range(my_range ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        turtle.bgcolor(125 + count %125, 125 - count % 125, 125)
        t.el.pensize(10)
        t.el.color(0,0,0) # 0,0,0 is default (Black)
        t.el.rt(-my_angle + phi)
        t.el.circle(250)
        t.el.pensize(10)
        t.el.color(255,255,255) # 255,255,255 is default (White)
        t.el.rt(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        Lg.logger.info('The value of count is  '+ str(count))
        Lg.logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(0, 0, 0)
    count = 0
    for count in range (my_range):
        t.el.pensize(10)
        t.el.color(255,255,255) # 0,0,0 is default (Black)
        t.el.left(-my_angle + phi)
        t.el.circle(250)
        t.el.color(50,255,50) # 255,255,255 is default (White)
        t.el.left(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        Lg.logger.info('The value of count is  '+ str(count))
        Lg.logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(255,255,255)    
    for count in range(my_range ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        t.el.pensize(10)
        t.el.color(0,0,0) # 0,0,0 is default (Black)
        t.el.rt(-my_angle + phi)
        t.el.circle(250)
        t.el.pensize(10)
        t.el.color(255,50,125) # 255,255,255 is default (White)
        t.el.rt(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        Lg.logger.info('The value of count is  '+ str(count))
        Lg.logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(252, 148, 10)
    count = 0
    for count in range (my_range):
        turtle.bgcolor(252 - count % 60, 148, 10 + count % 200)
        t.el.pensize(10)
        t.el.color(125,125,125) # 0,0,0 is default (Black)
        t.el.left(-my_angle + phi)
        t.el.circle(250)
        t.el.color(150,150,255) # 255,255,255 is default (White)
        t.el.left(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        Lg.logger.info('The value of count is  '+ str(count))
        Lg.logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))    
    stage_video()
    finalize()


#  Group A module_3
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
def occilating_yin_yang(): # **
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Occillating Yin-Yang'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_angle = 180
    for  count in range(10):
        turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
        for  count in range(199):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
            t.el.pensize(10)
            t.el.color(0,0,0) # 0,0,0 is default (Black)
            t.el.rt(-my_angle + phi)
            t.el.circle(250)
            t.el.pensize(10)
            t.el.color(255,255,255) # 255,255,255 is default (White)
            t.el.rt(-my_angle)
            t.el.circle(250)
            f.save_thumb()
            Lg.logger.info('The value of count is  '+ str(count))
            Lg.logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
        turtle.bgcolor(252, 148, 10)
        count = 0
        for count in range(199):
            t.el.pensize(10)
            t.el.color(255, 50,100) # 0,0,0 is default (RGB Black)
            t.el.left(-my_angle + phi)
            t.el.circle(250)
            t.el.color(150,150,255) # 0,0,0 is default (RGB Whie)
            t.el.left(-my_angle)
            t.el.circle(250)
            f.save_thumb()
            Lg.logger.info('The value of count is  '+ str(count))
            Lg.logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    stage_video()
    finalize()




def breathing_yin_yang(): # **
    Lg.logger.info('########################################################')
# global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Breathing Yin-Yang'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    count = 0
    t.el.hideturtle()
    my_angle = 180
    turtle.bgcolor(127,127,127) # Default is 127-127-127. Has to be a neutral shade like grey to contrast the black and white theme.
    Lg.logger.info(f'The background color is Gray')
    Lg.logger.info(f' The Yang color is Blue')
    Lg.logger.info(f' The Yin color is Yellow')
    for count in range(2500):  # 
       if count < 10:
           t.el.pensize(count)
       else:
           t.el.pensize(10)
       t.el.color(0,255,255) # 0,0,0 is default (Black)
       t.el.rt(-my_angle + t.phi)
       t.el.circle(count / 10)
       f.save_thumb()
       t.el.pensize(10)
       t.el.color(255,255,0) # 255,255,255 is default (White)
       t.el.rt(-my_angle)
       t.el.circle(count /10)
       f.save_thumb()
       if count % 500 == 0:
           Lg.logger.info(f'The value of count is {count} @ {Tm.my_time}')
    Lg.logger.info(f'Stopping breathing_yin-yang at {Tm.my_time}')
    Lg.logger.info('########################################################')
    stage_reverse_video()
    finalize()






#Group B Long Duration Mandalas
    
#  Group B module_4
'''+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Status: Last Update: 6/28/2023, Last Completed Run: 6/28/2023
# Uses loc_pen; Based on pretty_awesome Mandala
# First script completed using updated format. The angle is selected first, and enumerate is utilized.
# Duration is 12 minutes
'''
def mystical_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Mystical Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        R = random.randrange(127, 255, 1)
        G = 0
        B = 255
        Lg.logger.info('The value of hue /R/ is   ' + str(R))
        L = random.randrange(10, 150, 1)
        Lg.logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        count = 0
        my_length = 5 # Default is 5
        my_pensize = 250 # Default is 150
        my_range = 1250 #Default is 1200
        Lg.logger.info('Starting main script at ' + str(Tm.my_time))
        Lg.logger.info('Starting first pass....')
        initialize_loc_pen()
        start = Tm.date_time
        for count in range(my_range):
            
            loc_pen.pensize(count / my_pensize)
            loc_pen.pencolor(count % 255,  B - count % 150, count % 50)
            loc_pen.rt(my_angle)
            loc_pen.circle(count / my_length / t.phi, my_angle)
            f.save_thumb()
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
        end = Tm.date_time
        Lg.logger.info('Elapsed Time: ' + str(end - start))        
    #             Lg.logger.info('Loop count is ' + str(count)) # For testing; comment out for production
    #         loc_pen.reset() # Clears screen
        initialize_loc_pen()
        R = random.randrange(1, 150, 1)
        G = 0
        B = 255
        Lg.logger.info('The value of hue /R/ is   ' + str(R))
        L = random.randrange(150, 255, 1)
        Lg.logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        Lg.logger.info('Starting second pass @ ' + str(Tm.my_time))
        count = 0
        for count in range(my_range): # Second pass
            turtle.bgcolor(0,0,0)
            loc_pen.pensize(count / my_pensize)
            loc_pen.pencolor(B - count % 150, count % 50, count % 255)
            loc_pen.rt(my_angle)
            loc_pen.circle(count / my_length / t.phi, my_angle)
            f.save_thumb()
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
        count = 0
    #         loc_pen.reset() # Clears screen
        initialize_loc_pen()
        R = random.randrange(10, 255, 1)
        G = 0
        B = 255
        Lg.logger.info('The value of hue /R/ is   ' + str(R))
        L = random.randrange(10, 255, 1)
        Lg.logger.info('The value of hue /L/ is   ' + str(L))
        Lg.logger.info('**************************************')
        Lg.logger.info('Starting third pass @ ' + str(Tm.my_time))
        for count in range(my_range + 3): # Third pass
            turtle.bgcolor(0,0,0)
            loc_pen.pensize(count / my_pensize)
            loc_pen.pencolor(count % 50, count % 255,  B - count % 150 )
            loc_pen.rt(my_angle)
            loc_pen.circle(count / my_length / t.phi, my_angle)
            f.save_thumb()
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
        count = 0
        loc_pen.reset()
        initialize_loc_pen()
        R = random.randrange(25, 150, 1)
        G = 0
        B = 255
        Lg.logger.info('The value of hue /R/ is   ' + str(R))
        L= random.randrange(10, 255, 1)
        Lg.logger.info('The value of hue /L/ is   ' + str(L))
        Lg.logger.info('**************************************')
        Lg.logger.info('Starting fourth pass @ ' + str(Tm.my_time))
        for count in range(my_range + 4): # Fourth pass
            turtle.bgcolor(0,0,0)
            loc_pen.pensize(count / my_pensize)
            loc_pen.pencolor(R,  B - count % 150, count % 50)
            loc_pen.rt(my_angle)
            loc_pen.circle(count / my_length / t.phi, my_angle)
            f.save_thumb()
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
        count = 0
    #         loc_pen.reset() # Clears screen
        initialize_loc_pen()
        R = random.randrange(200, 250, 1)
        G = 0
        B = 255
        Lg.logger.info('The value of hue /R/ is   ' + str(R))
        L = random.randrange(10, 255, 1)
        Lg.logger.info('The value of hue /L/ is   ' + str(L))
        Lg.logger.info('**************************************')
        Lg.logger.info('Starting fifth pass @ ' + str(Tm.my_time))
        for count in range(my_range + 5): # Fifth pass
            turtle.bgcolor(0,0,0)
            loc_pen.pensize(count / my_pensize)
            loc_pen.pencolor(count % 255,  L, B - count % 255)
            loc_pen.rt(my_angle)
            loc_pen.circle(count / my_length / t.phi, my_angle)
            f.save_thumb()
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
        count = 0
    #         loc_pen.reset() Clears screen
        initialize_loc_pen()
        R = random.randrange(101, 220, 1)
        G = 0
        B = 255
        Lg.logger.info('The value of hue /R/ is   ' + str(R))
        L = random.randrange(10, 255, 1)
        Lg.logger.info('The value of hue /L/ is   ' + str(L))
        Lg.logger.info('**************************************')
        Lg.logger.info('Starting sixth pass @ ' + str(Tm.my_time))
        for count in range(my_range + 6): # Sixth pass
            turtle.bgcolor(0,0,0)
            loc_pen.pensize(count / my_pensize)
            loc_pen.pencolor(count % 255,  B - count % 150, R)
            loc_pen.rt(my_angle)
            loc_pen.circle(count / my_length / t.phi, my_angle)
            f.save_thumb()
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
            loc_pen.rt(my_angle)
            loc_pen.fd(count / my_length)
            f.save_thumb()
    loc_pen.reset()
    stage_video()
    finalize()

    

#  Group B Module_5
#+++++++++++MODULE 02, Simple Mandala +++++++++++++++++++++++++++++++++++++++++++++++++++++
#Typical duration is 18 minutes
def simple_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Simple Mandala'
    startup_script()
    make_folder()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title).my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
        count = 0
        my_range = 2550 # default is 1800
        my_pensize = 3 # default is 3
        my_length = 5 #default is 2
        Lg.logger.info('Starting First Loop @ ' + Tm.my_time)
        start = Tm.date_time
        Lg.logger.info('Start time for this loop is ' + str(start))
        t.el.pensize(my_pensize)
        t.lu.pensize(my_pensize)
        turtle.bgcolor(0,0,0)
        for count in range( my_range):
            # Random selection of red hue to repeat at 100th iteration; increase green green hue to 255; blue hue at max and decreases  to 0
            t.el.pencolor(random.randint(25, 100) + count %100, count % 255, 255- count % 255)
            # Red hue decreases to 0; random selection of green hue to repeat at 100th iteration; blue hue starts at 0 and repeats at 255 
            t.lu.pencolor(255 - count % 255, random.randint(25, 100) + count %100, count % 255)                
            t.el.rt(my_angle)
            t.el.fd(count / my_length)
    #         turtle.bgcolor(50,20,20)
            f.save_thumb()
            t.lu.rt(-my_angle)
            t.lu.fd(count / my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        end = Tm.date_time    
        Lg.logger.info('End Time for this loop is  ' + str(end))
        Lg.logger.info('Elapsed Time:'+ str(end - start))
        count = 0
        all_pens_home()
        Lg.logger.info('Starting Second Loop @ ' + Tm.my_time)
        t.ly.pensize(my_pensize)
        t.lq.pensize(my_pensize)
        for count in range(my_range):
            h.pick_yellow()
            h.pick_orange()
            t.ly.rt(my_angle)
            t.ly.fd(count /  my_length)
            f.save_thumb()
            t.lq.rt(-my_angle)
            t.lq.fd(count / my_length )
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        t.el.pensize(my_pensize)
        t.lu.pensize(my_pensize)
        Lg.logger.info('Starting Third Loop @ ' + Tm.my_time)
        for count in range(my_range):
            # red hue at max, decreases to 127 and repeats; green hue at max and decreases to 0 and repeats; random selection of blue hue to repeat at 100th iteration
            t.el.pencolor(255 - count% 127, 255-count  % 255, random.randint(25, 100) + count %100)
            # red hue static at 15; green hue at 0 and increases to max; blue hue at max and deceases to 0
            t.lu.pencolor(random.randint(25, 100) + count %100, count % 255, 255 - count % 255)                 
            t.el.rt(my_angle)
            t.el.fd(count / my_length)
            f.save_thumb()
            t.lu.rt(-my_angle)
            t.lu.fd(count / my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        t.ly.pensize(my_pensize) # Yellow Pen
        t.lg.pensize(my_pensize) # Green pen
        Lg.logger.info('Starting Fourth Loop @ ' + Tm.my_time)
        for count in range(my_range):
            h.pick_green()
            h.pick_yellow()
            t.lg.rt(my_angle)
            t.lg.fd(count / my_length)
            f.save_thumb()
            t.ly.rt(-my_angle)
            t.ly.fd(count / my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        t.lb.pensize(my_pensize)
        t.go.pensize(my_pensize)
        Lg.logger.info('Starting Fifth Loop @ ' + Tm.my_time)
        for count in range(my_range):
            h.pick_blue()
            h.pick_gold()
            t.lb.rt(my_angle)
            t.lb.fd(count / my_length)
            f.save_thumb()
            t.go.rt(-my_angle)
            t.go.fd(count /  my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        t.el.pensize(my_pensize)
        t.lu.pensize(my_pensize)
        Lg.logger.info('Starting Sixth Loop @ ' + Tm.my_time)
        for count in range(my_range):
            # red hue at max decreases to 127; green hue at max decreases to 0; blue hue increases to 255    
            t.el.pencolor(255 - count % 127,255 - count % 255, count % 255)
            # red hue static at 150; green hue increases to 255; random selection of blue hue, increases to 100th iteration and repeats
            t.lu.pencolor(150, count % 255, random.randint(25, 100) + count %100)                 
            t.el.rt(my_angle)
            t.el.fd(count /  my_length)
            f.save_thumb()
            t.lu.rt(-my_angle)
            t.lu.fd(count / my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        t.li.pensize(my_pensize)
        t.lr.pensize(my_pensize)
        Lg.logger.info('Starting Seventh Loop @ ' + Tm.my_time)
        for count in range( my_range):
            h.pick_indigo()
            h.pick_random_a()
            t.li.rt(my_angle)
            t.li.fd(count / my_length)
            f.save_thumb()
            t.lr.rt(-my_angle)
            t.lr.fd(count /  my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        t.el.pensize(my_pensize)
        t.lz.pensize(my_pensize)
        Lg.logger.info('Starting Eighth Loop @ ' + Tm.my_time)
        for count in range( my_range):
            h.pick_light()
            h.pick_dark()
            t.el.rt(my_angle)
            t.el.fd(count / my_length)
            f.save_thumb()
            t.lz.rt(-my_angle)
            t.lz.fd(count /  my_length)
            f.save_thumb()
            if count == my_range:
                pass
    stage_reverse_video() #Comment out if reversal not wanted
#     stage_video() # Comment out if reversal is wanted
    finalize()



#  Group B Module_6
#+++++++++++MODULE Colorful Mandala_Extended+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module has a duration of approximately 5.42 minutes when range and pensize defaults are applied,
# and so will randomly select from the pool of medium clips.
def colorful_mandala_extended():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Colorful Mandala Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        turtle.bgcolor(0,0,0)
        my_range = 650 # Default is 650
        my_pensize = 150 # Default is 150
        Lg.logger.info('Starting creation of sequential screenshots')
        Lg.logger.info('Starting First Loop of 5 @ ' + Tm.my_time)
        for count in range(my_range):
            t.go.speed(0)
            t.li.speed(0)
            R =  0
            G =  140
            B =  255
            if G == 0:
                t.go.color( count, count, B - count)
                t.li.color( count, 0, B - count)
            else:
                t.go.color( count % 255, G - count %140, B - count %100)
                t.li.color( count % 255, G - count %140, B - count % 255)
            t.go.fd(count / 2)
            f.save_thumb()
            t.go.pensize(count / my_pensize)
            t.go.circle(count / 2, my_angle, 6)
            f.save_thumb()
            t.li.fd(count / 2)
            f.save_thumb()
            t.li.right(my_angle)
            t.li.fd(count)
            t.li.pensize(count / my_pensize)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
    #         Lg.logger.info('This is loop # ' + str(count) + ' of first pass') # For testing; comment out for production
        # Start second pass
        Lg.logger.info('Starting Second Loop of 5 @ ' + Tm.my_time)
        count = 244
        count = 0
        all_pens_home()
        for count in range(my_range):
            t.go.pensize(count /  my_pensize)
            t.li.pensize(count / my_pensize)
            R =  0
            G =  140
            B =  255
            if R >= 240:
                h.pick_gold()
                h.pick_indigo()
            else:
                t.go.color(B - count % 240, G - count %140, count % 255)
                t.li.color(count %100, G - count %140, B - count % 240)
            t.go.fd(count / 2)
            f.save_thumb()
            t.go.circle(count /2, my_angle, 6)
            f.save_thumb()
            t.li.fd(count / 2)
            f.save_thumb()
            t.li.right(my_angle)
            t.li.fd(count)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        Lg.logger.info('Starting Third Loop of 5 @ ' + Tm.my_time)
        count = 0
        all_pens_home()
        for count in range(my_range):
            t.go.pensize(count / my_pensize)
            t.li.pensize(count / my_pensize)
            R =  255
            G =  140
            B = 0
            if B >= 240:
                t.go.color( R - count % 255, G + count % 140, 240)
                t.li.color( R - count % 255, G - count % 140, 240)
            else:
                t.go.color(count %100, R - count % 255, G - count % 140, )
                t.li.color(R - count %100, count % 255, count % 255 )
            t.go.fd(count / 2)
            f.save_thumb()
            t.go.circle(count / 2, my_angle, 6)
            f.save_thumb()
            t.li.fd(count / 2)
            f.save_thumb()
            t.li.right(my_angle)
            t.li.fd(count)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        Lg.logger.info('Starting Fourth Loop of 5 @ ' + Tm.my_time )
        count = 0
        all_pens_home()
        for count in range(my_range):
            t.go.pensize(count / my_pensize)
            t.li.pensize(count / my_pensize)
            h.pick_gold() # Pen t.go
            h.pick_indigo() # Pen t.li
            t.go.fd(count / 2)
            f.save_thumb()
            t.go.circle(count / 2, my_angle, 6)
            f.save_thumb()
            t.li.fd(count / 2)
            f.save_thumb()
            t.li.right(my_angle)
            t.li.fd(count)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        Lg.logger.info('Starting Fifth Loop of 5 @ ' + Tm.my_time )
        count = 0
        all_pens_home()
        for count in range(my_range):
            t.el.pensize(count / my_pensize)
            t.lz.pensize(count / my_pensize)
            h.pick_dark() # Pen t.lz
            h.pick_light() # Pen t.el
            t.el.fd(count / 2)
            f.save_thumb()
            t.el.circle(count / 2, my_angle, 6)
            f.save_thumb()
            t.lz.fd(count / 2)
            f.save_thumb()
            t.lz.right(my_angle)
            t.lz.fd(count)
            f.save_thumb()
            if count == my_range:
                pass
    stage_reverse_video()
    finalize()




#  Group B Module_7
#+++++++++++MODULE Glorious Mandala_Extended+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module has a duration of approximately six minutes when range and pensize defaults are applied,
# and so will randomly select from the pool of medium clips, typically 6 minutes or greater.
def glorious_mandala_extended():  # Based on Awesome Manadala
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Glorious Mandala Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        R = 255
        B = random.randrange(112,155, 1)
        Lg.logger.info('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 150, 1)
        Lg.logger.info('The value of hue /L/ is   ' + str(L))
        E = random.randrange(150, 255, 1)
        Lg.logger.info('The value of hue /E/ is   ' + str(L))
        pensize_a = 45
        pensize_b = 120
        count = 0
        my_range = 360  # 360 is default, use lower number for testing.
        turtle.bgcolor(10,40,60)
        # First Pass
        Lg.logger.info('Starting creation of sequential screenshots')
        Lg.logger.info('Starting First Loop of 8 @ ' + Tm.my_time)
        for count in range (my_range): 
            if count <= 255:
                t.el.pencolor(L, count  %102, count %102)
                t.li.pencolor(B, R-count, count %51)
                t.li.fd(count / 2)
                t.li.left(my_angle) 
                f.save_thumb()
                t.el.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.li.penup()
                t.li.fd(count)
                t.li.left(my_angle)
                t.li.pendown()
                f.save_thumb()
                t.li.fd(count)
                f.save_thumb()
                t.el.fd(count)
                t.el.left(- my_angle)
                t.li.pensize(count/pensize_a)
                t.el.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
            else:
                h.pick_indigo() # Pen li
                h.pick_light() # Pen el
                t.li.fd(count/2)
                t.li.left(my_angle)
                f.save_thumb()
                t.el.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.li.penup()
                t.li.fd(count)
                t.li.left(my_angle)
                t.li.pendown()
                f.save_thumb()
                t.li.fd(count)
                f.save_thumb()
                t.el.fd(count)
                t.el.rt(my_angle)
                t.li.pensize(count/pensize_a)
                t.el.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
    #     Lg.logger.info('Completing First Loop # ' + str(count) + ' @ ' + Tm.my_time) # For testing only. Default is to leave commented
        # Second Pass
        count = 0
        all_pens_home()
        Lg.logger.info('Starting Second Loop of 8 @ ' + Tm.my_time)
        for count in range (my_range): # 360 is default, use lower number for testing.
            if count <= 255:
                t.lg.pencolor(count %102,count %102, L)
                t.go.pencolor(count %51, R - count %102, E)
                t.lg.fd(count/2)
                t.lg.left(my_angle) 
                f.save_thumb()
                t.go.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.lg.penup()
                t.lg.fd(count)
                t.lg.left(my_angle)
                f.save_thumb()
                t.lg.pendown()
                t.lg.fd(count)
                f.save_thumb()
                t.go.fd(count)
                t.go.rt(my_angle)
                t.lg.pensize(count/pensize_a)
                t.go.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
            else:
                h.pick_green() # Pen lg
                h.pick_gold() # Pen go
                t.lg.fd(count/2)
                t.lg.left(my_angle)
                f.save_thumb()
                t.go.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.lg.penup()
                t.lg.fd(count)
                t.lg.left(my_angle)
                f.save_thumb()
                t.lg.pendown()
                t.lg.fd(count)
                f.save_thumb()
                t.go.fd(count)
                t.go.rt(my_angle)
                t.lg.pensize(count/pensize_a)
                t.go.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
        #  Third Pass
        count = 0
        all_pens_home()
        Lg.logger.info('Starting Third Loop of 8 @ ' + Tm.my_time)
        for count in range (my_range): 
            if count <= 255:
                t.ly.pencolor(L, count %51, B)
                t.lz.pencolor(B, R-count, count %102)
                t.lz.fd(count/2)
                t.lz.left(my_angle) 
                f.save_thumb()
                t.ly.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.lz.penup()
                t.lz.fd(count)
                t.lz.left(my_angle)
                t.lz.pendown()
                f.save_thumb()
                t.lz.fd(count)
                f.save_thumb()
                t.ly.fd(count)
                t.ly.rt(my_angle)
                t.lz.pensize(count/pensize_a)
                t.ly.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
            else:
                h.pick_dark() # Pen lz
                h.pick_yellow() # Pen ly
                t.lz.fd(count/2)
                t.lz.left(my_angle)
                f.save_thumb()
                t.ly.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.lz.penup()
                t.lz.fd(count)
                t.lz.left(my_angle)
                t.lz.pendown()
                f.save_thumb()
                t.lz.fd(count)
                f.save_thumb()
                t.ly.fd(count)
                t.ly.rt(my_angle)
                t.lz.pensize(count/pensize_a)
                t.ly.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
        # Fourth Pass
        count = 0
        all_pens_home()
        Lg.logger.info('Starting Fourth Loop of 8 @ ' + Tm.my_time)
        for count in range (my_range): # 360 is default, use lower number for testing.
            if count <= 255:
                t.lb.pencolor(E, count %51, count %102)
                t.ce.pencolor(count %51, R-count %102, L)
                t.lb.fd(count/2)
                t.lb.left(my_angle) 
                f.save_thumb()
                t.ce.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.lb.penup()
                t.lb.fd(count)
                t.lb.left(my_angle)
                f.save_thumb()
                t.lb.pendown()
                t.lb.fd(count)
                f.save_thumb()
                t.ce.fd(count)
                t.ce.rt(my_angle)
                t.lb.pensize(count/pensize_a)
                t.ce.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
            else:
                h.pick_blue() # Pen lb
                h.pick_random() # Pen ce
                t.lb.fd(count/2)
                t.lb.left(my_angle) 
                f.save_thumb()
                t.ce.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.lb.penup()
                t.lb.fd(count)
                t.lb.left(my_angle)
                f.save_thumb()
                t.lb.pendown()
                t.lb.fd(count)
                f.save_thumb()
                t.ce.fd(count)
                t.ce.rt(my_angle)
                t.lb.pensize(count/pensize_a)
                t.ce.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
        # Fifth Pass        
        Lg.logger.info('Starting Fifth Loop of 8 @ ' + Tm.my_time)
        count = 0
        all_pens_home()
        for count in range (my_range): 
            if count <= 255:
                t.me.pencolor(L, count %102, count %51)
                t.lr.pencolor(B, R-count %51, count %204)
                t.lr.fd(count/2)
                t.lr.left(my_angle)
                f.save_thumb()
                t.me.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.lr.penup()
                t.lr.fd(count)
                t.lr.left(my_angle)
                t.lr.pendown()
                f.save_thumb()
                t.lr.fd(count)
                f.save_thumb()
                t.me.fd(count)
                t.me.rt(my_angle)
                t.lr.pensize(count/pensize_a)
                t.me.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
            else:
                h.pick_random_a() # Pen lr
                h.pick_magenta() # Pen me
                t.lr.fd(count/2)
                t.lr.left(my_angle)
                f.save_thumb()
                t.me.circle(count/t.phi,-my_angle) # Light Pen
                f.save_thumb()
                t.lr.penup()
                t.lr.fd(count)
                t.lr.left(my_angle)
                t.lr.pendown()
                f.save_thumb()
                t.lr.fd(count)
                f.save_thumb()
                t.me.fd(count)
                t.me.rt(my_angle)
                t.lr.pensize(count/pensize_a)
                t.me.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
        # Sixth Pass
        count = 0
        all_pens_home()
        Lg.logger.info('Starting Sixth Loop of 8 @ ' + Tm.my_time)
        for count in range (my_range): # 360 is default, use lower number for testing.
            if count <= 255:
                t.lu.pencolor(count %102,count %51, L)
                t.lq.pencolor(count %51, R-count %102, E)
                t.lu.fd(count/2)
                t.lu.left(my_angle)
                f.save_thumb()
                t.lq.circle(count/t.phi,-my_angle) # Gold Pen
                f.save_thumb()
                t.lu.penup()
                t.lu.fd(count)
                t.lu.left(my_angle)
                f.save_thumb()
                t.lu.pendown()
                t.lu.fd(count)
                f.save_thumb()
                t.lq.fd(count)
                t.lq.rt(my_angle)
                t.lu.pensize(count/pensize_a)
                t.lq.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
            else:
                h.pick_red() # Pen lu
                h.pick_orange() # Pen lq
                t.lu.fd(count/2)
                t.lu.left(my_angle)
                f.save_thumb()
                t.lq.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.lu.penup()
                t.lu.fd(count)
                t.lu.left(my_angle)
                f.save_thumb()
                t.lu.pendown()
                t.lu.fd(count)
                f.save_thumb()
                t.lq.fd(count)
                t.lq.rt(my_angle)
                t.lu.pensize(count/pensize_a)
                t.lq.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
        # Seventh Pass        
        Lg.logger.info('Starting Seventh Loop of 8 @ ' + Tm.my_time)
        all_pens_home()
        count = 0
        for count in range (my_range): 
            if count <= 255:
                t.go.pencolor(L, count %51, count %102)
                t.li.pencolor(R-count %51, E, count %102)
                t.li.fd(count/2)
                t.li.left(my_angle)
                f.save_thumb()
                t.go.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.li.penup()
                t.li.fd(count)
                t.li.left(my_angle)
                t.li.pendown()
                f.save_thumb()
                t.li.fd(count)
                f.save_thumb()
                t.go.fd(count)
                t.go.rt(my_angle)
                t.li.pensize(count/pensize_a)
                t.go.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
            else:
                h.pick_indigo() # Pen li
                h.pick_gold() # Pen go
                t.li.fd(count/2)
                t.li.left(my_angle)
                f.save_thumb()
                t.go.circle(count/t.phi,-my_angle) # Light Pen
                f.save_thumb()
                t.li.penup()
                t.li.fd(count)
                t.li.left(my_angle)
                t.li.pendown()
                f.save_thumb()
                t.li.fd(count)
                f.save_thumb()
                t.go.fd(count)
                t.go.rt(my_angle)
                t.li.pensize(count/pensize_a)
                t.go.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
        # Eighth Pass
        count = 0
        all_pens_home()
        Lg.logger.info('Starting Eighth Loop of 8 @ ' + Tm.my_time)
        for count in range (my_range): # 360 is default, use lower number for testing.
            if count <= 255:
                t.el.pencolor(count %102,count %51, L)
                t.lz.pencolor(count %51, R-count %51, B)
                t.el.fd(count/2)
                t.el.left(my_angle)
                f.save_thumb()
                t.lz.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.el.penup()
                t.el.fd(count)
                t.el.left(my_angle)
                f.save_thumb()
                t.el.pendown()
                t.el.fd(count)
                f.save_thumb()
                t.lz.fd(count)
                t.lz.rt(my_angle)
                t.el.pensize(count/pensize_a)
                t.lz.pensize(count/pensize_b)
                f.save_thumb()
                if count == my_range:
                    f.save_final_thumb()
            else:
                h.pick_light() # Pen el
                h.pick_dark() # Pen lz
                t.el.fd(count/2)
                t.el.left(my_angle)
                f.save_thumb()
                t.lz.circle(count/t.phi,-my_angle) 
                f.save_thumb()
                t.el.penup()
                t.el.fd(count)
                t.el.left(my_angle)
                f.save_thumb()
                t.el.pendown()
                t.el.fd(count)
                f.save_thumb()
                t.lz.fd(count)
                t.lz.rt(my_angle)
                t.el.pensize(count/pensize_a)
                t.lz.pensize(count/pensize_b)
                f.save_thumb()            
    stage_reverse_video()
    finalize()
    
    



#  module_16
#**************************************************************************************************************
  # First Published to YouTube on 11/21/2021; Revised to employ the most recent coding practices that I have picked up.
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def reversing_awesome_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Reversing Awesome Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        all_pens_home()
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info(f'Current angle to be drawn is {my_angle:.2f}') # Employing f-script
        turtle.title(f'Reversing Awesome Mandala: {my_angle} Degrees Angle  and  {au.my_track}')  # Employing f-script
        t.my_title = f'Reversing Awesome Mandala: {my_angle} Degrees Angle  and  {au.my_track}'  # Employing f-script
        s.title_screen()
        count = 0
        my_range =   2550
        my_pensize = 4200
        my_length = 13
        R = 0
        G = 0
        B = random.randint(1, 127)
        L = random.randint(127, 255)
        M = 255
        h.pick_gold() #Pen go
#             Lg.logger.info('The Value of color B is    ' + str(B)) # Use for testing
#             Lg.logger.info('The Value of color L is    ' + str(L))  # Use for testing
        turtle.bgcolor(0,0,15)
        for count in range(my_range):
            # 450 is default, use any number
            h.pick_gold() #Pen go
            t.go.pensize(count /my_pensize)
            t.go.left(my_angle)
            t.go.fd(count /my_length * t.phi)
            f.save_thumb()
            if count <= 2900:
                t.el.pencolor(B, count % 255, L)
            else:
                h.pick_light()
            t.go.left(my_angle)
            t.go.pensize(count / my_pensize)
            t.go.fd(count /my_length * t.phi)
            f.save_thumb()
            t.el.pensize(count /my_pensize)
            t.el.rt(my_angle)
            t.el.fd(count / my_length)
            f.save_thumb()
            t.el.rt(my_angle)
            t.el.circle(count /my_length, - my_angle, 5)
            f.save_thumb()
        all_pens_home()        
        for count in range(my_range):
            if count <= 2900:
                t.lm.pencolor(B + count %120, M,  10)
            else:
                h.pick_indigo() #Pen li
            t.li.pensize(count / my_pensize)
            t.li.left(my_angle)
            t.li.fd(count /my_length * t.phi) 
            f.save_thumb()
            t.lm.pensize(count /my_pensize)
            t.lm.rt(my_angle)
            t.lm.fd(count / my_length)
            f.save_thumb()
            t.lm.rt(my_angle)
            t.lm.circle(count / my_length, - my_angle, 5)
            f.save_thumb()
    stage_reverse_video()
    finalize()



    
#  Group B Module_9
#+++++++++++MODULE Bold Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''This project can select and run a sequence of angles as a single video. It will select and retain a single audio track
for the duration of the video track.'''    
def reversing_simple_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Reversing Simple Mandala'
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
        Lg.logger.info('Starting First Loop @ ' + Tm.my_time)
        start = Tm.date_time
        Lg.logger.info('Start time for this loop is ' + str(start))
        t.me.pensize(my_pensize)
        t.lq.pensize(my_pensize)
        turtle.bgcolor(0,0,0)
        for count in range(my_range):
            h.pick_red()  # Pen t.lu
            h.pick_light() # Pen t.el
            t.lu.rt(my_angle)
            t.lu.fd(count /  my_length)
            f.save_thumb()
            t.el.rt(-my_angle)
            t.el.fd(count / my_length )
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        t.lg.pensize(my_pensize) # Yellow Pen
        t.ly.pensize(my_pensize) # Green pen
        Lg.logger.info('Starting Second Loop @ ' + Tm.my_time)
        for count in range(my_range):
            h.pick_green() #Pen t.lg
            h.pick_yellow() # Pen t.ly
            t.lg.rt(my_angle)
            t.lg.fd(count / my_length)
            f.save_thumb()
            t.ly.rt(-my_angle)
            t.ly.fd(count / my_length)
            f.save_thumb()
            if count == my_range:
                f.save_final_thumb()
    stage_reverse_video() #Comment out if reversal not wanted
#     stage_video()
    finalize()
    
    
  
    
    

#  Group B Module_8
#+++++++++++MODULE Bold Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''This project can select and run a sequence of angles as a single video. It will select and retain a single audio track
for the duration.'''
def bold_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Bold Mandala'
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
            h.pick_indigo() # t.li;Indigo hues
            h.pick_gold() #t.go; Gold hues
            t.li.left(my_angle) #Indigo pen
            t.li.penup()
            t.li.setpos(0,0)
            t.li.pendown()
            t.li.pensize(count / my_pensize)
            t.li.circle(count, my_angle)
            f.save_thumb()
            t.go.pensize(count / my_pensize)  #Gold pen
            t.go.left(my_angle)
            t.go.backward(count * t.phi)
            f.save_thumb()
            t.go.left(my_angle)
            t.go.fd(count)
            f.save_thumb()
            turtle.bgcolor(count, count, count)
            f.save_thumb()
        count = 0
        all_pens_home()
        turtle.bgcolor(255, 255, 255)
        for count in range( my_range):
            h.pick_red() #t.lu; red hues
            h.pick_blue() #t.lb; blue hues
            t.lu.left(my_angle) 
            t.lu.penup()
            t.lu.setpos(0,0)
            t.lu.pendown()
            t.lu.pensize(count /my_pensize)
            t.lu.circle(count, my_angle) # Red Pen
            f.save_thumb()
            t.lb.pensize(count / my_pensize)  #Blue pen
            t.lb.left(my_angle)
            t.lb.backward(count * t.phi)
            f.save_thumb()
            t.lb.left(my_angle)
            t.lb.fd(count)
            f.save_thumb()
            turtle.bgcolor(255 - count, 255 - count, 255 - count)
            f.save_thumb()
        count = 0
        all_pens_home()
        turtle.bgcolor(0,0,0)
        for count in range(my_range):
            h.pick_green() #t.lg; green hues
            h.pick_yellow() #t.ly; yellow hues
            t.lg.left(my_angle) 
            t.lg.penup()
            t.lg.setpos(0,0)
            t.lg.pendown()
            t.lg.pensize(count / my_pensize)
            t.lg.circle(count, my_angle) # Green Pen
            f.save_thumb()
            t.ly.pensize(count / my_pensize)  
            t.ly.left(my_angle)
            t.ly.backward(count * t.phi) # Yellow pen 
            f.save_thumb()
            t.ly.left(my_angle)
            t.ly.fd(count)
            f.save_thumb()
            turtle.bgcolor(count, count, count)
            f.save_thumb()
        count = 0
        all_pens_home()
        turtle.bgcolor(255, 255, 255) # Background opens at White; fades to Green    
        for count in range(my_range):      #255 is default. Use lower number for testing.
            h.pick_random() #t.ce; random hues
            h.pick_magenta() #t.me; magenta hues
            t.ce.left(my_angle) #Random pen
            t.ce.penup()
            t.ce.setpos(0,0)
            t.ce.pendown()
            t.ce.pensize(count / my_pensize)
            t.ce.circle(count, my_angle)
            f.save_thumb()
            t.me.pensize(count / my_pensize) 
            t.me.left(my_angle)
            t.me.backward(count * t.phi)  # Magenta pen 
            f.save_thumb()
            t.me.left(my_angle)
            t.me.fd(count)
            f.save_thumb()
            turtle.bgcolor(255 - count, 255, 255 - count)
            f.save_thumb()
        count = 0
        all_pens_home()
        turtle.bgcolor(0, 255, 0)   # Background opens at Green; fades to light blue 
        for count in range(my_range):      #255 is default. Use lower number for testing.
            h.pick_orange() #t.lq; orange hues
            h.pick_random_a() #t.lr; random hues
            t.lq.left(my_angle) 
            t.lq.penup()
            t.lq.setpos(0,0)
            t.lq.pendown()
            t.lq.pensize(count / my_pensize)
            t.lq.circle(count, my_angle) # Orange pen
            f.save_thumb()
            t.lr.pensize(count / my_pensize) 
            t.lr.left(my_angle)
            t.lr.backward(count * t.phi)   #Random pen
            f.save_thumb()
            t.lr.left(my_angle)
            t.lr.fd(count)
            f.save_thumb()
            turtle.bgcolor(0, 255, count)
            f.save_thumb()
        count = 0
        all_pens_home()
        turtle.bgcolor(0, 255, 255)  # Background opens at light blue; fades to black
        for count in range(my_range):
            h.pick_dark() #t.lz; dark hues
            h.pick_light() #t.el; light hues
            t.lz.left(my_angle) #Dark pen
            t.lz.setpos(0,0)
            t.lz.pendown()
            t.lz.pensize(count /my_pensize)
            t.lz.circle(count, my_angle)
            f.save_thumb()
            t.el.pensize(count / my_pensize)  
            t.el.left(my_angle)
            t.el.backward(count * t.phi)  #light pen
            f.save_thumb()
            t.el.left(my_angle)
            t.el.fd(count)
            f.save_thumb()
            turtle.bgcolor(0, 255 - count, 255 - count)
            f.save_thumb()
#     stage_video() # Ends with completed mandala; comment out if reversal is specified
    stage_reverse_video() #Ends with blank screen; commit out if full image is needed at the end
    finalize()




def strong_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Strong Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        my_range = 1275
        count = 0
        for count in range(my_range):
            turtle.bgcolor(25, 10, 10)
            R =  0
            G =  0
            B =  90
            t.el.color(count % 255 , G, B )
            t.el.pensize(2)
            t.el.fd(count / 3 )
            f.save_thumb()
            t.el.left(my_angle)
            R = 0
            G = 230
            B = 255
            t.el.color(count % 255, G, B - count % 255)
            t.el.circle(7, my_angle, 6)
            f.save_thumb()
            t.el.backward(10)
            f.save_thumb()
            t.el.pensize(5)
            t.el.setposition(-30, 0)
            f.save_thumb()
            t.el.circle(count / 5, my_angle, 72)
            f.save_thumb()
        t.el.clear()
        t.el.penup()
        t.el.setpos(0,0)
        t.el.pendown()
        count = 0
        Lg.logger.info('Angle being drawn is ' + str(my_angle *3))
        for count in range(my_range):
            turtle.bgcolor(25, 10, 10)
            R =  0
            G =  0
            B =  90
            t.el.color(count % 255 , G, B )
            t.el.pensize(2)
            t.el.fd(count / 3 )
            f.save_thumb()
            t.el.left(my_angle * 3)
            R = 0
            G = 230
            B = 255
            t.el.color(count % 255, G, B - count % 255)
            t.el.circle(7, my_angle * 3, 6)
            f.save_thumb()
            t.el.backward(10)
            f.save_thumb()
            t.el.pensize(5)
            t.el.setposition(-30, 0)
            f.save_thumb()
            t.el.circle(count / 5, my_angle * 3, 72)
            f.save_thumb()
    stage_reverse_video()
    finalize()





#module_41
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def glorious_mandala():  # Based on Awesome Manadala
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Glorious Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range(len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info('Current angle to be drawn is ' + str(my_angle))
        t.my_title = f'Glorious Mandala: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        B = random.randint(112,155)
        Lg.logger.info(f'The value of hue B is {B}')
        L = random.randint(10, 150)
        Lg.logger.info(f'The value of hue L is {L}')
        E = random.randint(150, 255)
        Lg.logger.info(f'The value of hue E is {L}')
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
        set_go_home()
        set_lb_home()
        my_range =  1275  #Default is 1275
        for count in range(my_range):
            t.go.pensize(count / 150)
            t.lb.pensize(count / 135)
            if count <= 255:
                t.lb.pencolor(L + count % 50, M + count % 255, E)
                t.go.pencolor(R - count, B, Z + count %200)
            else:
                h.pick_gold()
                h.pick_blue()
            t.go.left(my_angle)
            t.go.fd(count / 18)
            f.save_thumb()
            t.lb.circle(count / 24, - my_angle, 6)
            f.save_thumb()
            t.go.left(my_angle)
            t.go.penup()
            t.lb.penup()
            t.go.right(my_angle)
            t.go.fd(count / 24)
            f.save_thumb()
            t.lb.rt(my_angle)
            t.go.pendown()
            t.lb.pendown()
            t.go.fd(count / t.phi)
            f.save_thumb()
            t.lb.fd(count / t.phi)
            f.save_thumb()
            t.go.backward(count / 24)
            f.save_thumb()
        t.go.reset()
        t.lb.reset()
    stage_reverse_video()
    finalize()






#  module_6
#+++++++++++MODULE FANTASTIC MANDALA+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Fantastic_Mandala():  
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Fantastic Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range(len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info('Current angle to be drawn is ' + str(my_angle))
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle with {au.my_track}'
        turtle.title(f'{my_mandala_name}: {my_angle} Angle with {au.my_track}')
        count = 0
        my_range = 1020  #default is 1020; use lower number for testing
        set_li_home() # Indigo Pen used normally
        set_go_home()  #Gold Pen
        set_el_home() # Light Pen used normally
        set_lu_home() #Red Pen
        turtle.bgcolor(0,0,20)
        for count in range(my_range):
            h.pick_red()
            t.lu.pensize(count /2040)
            t.lu.left(my_angle)
            t.lu.circle(count / 24, my_angle, 6)
            f.save_thumb()
            t.li.pensize(count / 125)
            t.li.pencolor(count % 255, 255, 255 - count % 255)
            t.li.fd(count)
            f.save_thumb()
            t.li.right(my_angle)
            h.pick_gold()
            t.go.pensize(count / 1020)
            t.go.circle(count / 3, my_angle)
            f.save_thumb()
            t.el.pensize(count / 200)
            t.el.right(my_angle)
            t.el.pencolor(0, count % 255, 255)
            t.el.fd(count / 12)
            f.save_thumb()
        gc.enable()
        gc.collect()
        gc.disable()
            # For testing purposes only; comment out for production run
#             Lg.logger.info('Ending Loop Count ' + str(count))
    stage_reverse_video()
    finalize()








#  Group B Module_8
#+++++++++++MODULE Awesome Mandala_Extended+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module has a duration of approximately 18 minutes when range and pensize defaults are applied,
# and so will randomly select from the pool of long clips.
def awesome_mandala_extended():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Awesome Mandala Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
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
        Lg.logger.info('Starting First Pass @ ' + Tm.my_time)
        for count in range(my_range):  # First pass
            h.pick_red() #Pen lu
            t.lu.pensize(count / my_pensize)
            t.lu.fd(count / forward_count * t.phi)
            f.save_thumb()
            t.lu.rt(my_angle)
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
                Lg.logger.info('Completed Loop # '+ str(count) + '  of First Pass @ ' + Tm.my_time)
                f.save_final_thumb()
        all_pens_home()
        count = 0
        Lg.logger.info('Starting Second Pass @ ' + Tm.my_time)
        for count in range( my_range):
            h.pick_green() #Pen lg
            turtle.bgcolor(X, 0, 0)
            t.lg.pensize(count / my_pensize)
            t.lg.fd(count / forward_count * t.phi)
            f.save_thumb()
            t.lg.rt(my_angle)
            t.lm.pensize(count / my_pensize * 2)
            t.lm.rt(my_angle)
            if count <= 255:
                t.lm.pencolor(R + count, M - count % 50, B)
            else:
                t.lm.pencolor(M, M, X)
            t.lm.circle(count / circ_rad, - my_angle, 9)
            f.save_thumb()
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + 'of Second Pass @ ' + Tm.my_time)
                f.save_final_thumb()
        all_pens_home()
        count = 0
        Lg.logger.info:('Starting Third Pass @ ' + Tm.my_time)
        for count in range(my_range):  # 3000 is default, use any number Third pass
            h.pick_indigo() #Pen li
            h.pick_gold()  #Pen go
            t.li.pensize(count / my_pensize)
            t.li.rt(my_angle)
            t.li.fd(count / forward_count * t.phi)
            f.save_thumb()
            t.go.pensize(count / my_pensize)
            t.go.rt(my_angle)
            t.go.circle(count / circ_rad, - my_angle, 9)
            f.save_thumb()
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + 'of Third Pass @ ' + Tm.my_time)
                f.save_final_thumb()
        all_pens_home()
        count = 0
        Lg.logger.info:('Starting Fourth Pass @ ' + Tm.my_time)
        for count in range(my_range):  # 3000 is default, use any number Third pass
            h.pick_blue() #Pen lb
            h.pick_random()  #Pen ce
            t.lb.pensize(count / my_pensize)
            t.lb.rt(my_angle)
            t.lb.fd(count / forward_count * t.phi)
            f.save_thumb()
            t.ce.pensize(count / my_pensize)
            t.ce.rt(my_angle)
            t.ce.circle(count / circ_rad, - my_angle, 9)
            f.save_thumb()
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + 'of Fourth Pass @ ' + Tm.my_time)
                f.save_final_thumb()
        all_pens_home()
        count = 0
        Lg.logger.info:('Starting Fifth Pass @ ' + Tm.my_time)
        for count in range(my_range):  # 3000 is default, use any number Third pass
            h.pick_magenta() #Pen me
            h.pick_orange()  #Pen lq
            t.me.pensize(count / my_pensize)
            t.me.rt(my_angle)
            t.me.fd(count / forward_count * t.phi)
            f.save_thumb()
            t.lq.pensize(count / my_pensize)
            t.lq.rt(my_angle)
            t.lq.circle(count / circ_rad, - my_angle, 9)
            f.save_thumb()
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + 'of Fifth Pass @ ' + Tm.my_time)
                f.save_final_thumb()
        all_pens_home()
        count = 0
        Lg.logger.info:('Starting Sixth Pass @ ' + Tm.my_time)
        for count in range(my_range):  # 3000 is default, use any number Third pass
            h.pick_light() #Pen el
            h.pick_random_a()  #Pen lr
            t.el.pensize(count / my_pensize)
            t.el.rt(my_angle)
            t.el.fd(count / forward_count * t.phi)
            f.save_thumb()
            t.lr.pensize(count / my_pensize)
            t.lr.rt(my_angle)
            t.lr.circle(count / circ_rad, - my_angle, 9)
            f.save_thumb()
            if count == my_range:
                Lg.logger.info('Completed Loop # '+ str(count) + 'of Sixth Pass @ ' + Tm.my_time)
                f.save_final_thumb()
    stage_video()
    finalize()







#  Group B Module_9
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Uses pens go(gold) and lb(blue); Based on Mystical Mandala
def joyous_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Joyous Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        my_length = 5
        Lg.logger.info('The value of my_length is: ' + str(my_length))
        my_pensize = 360
        Lg.logger.info('The value of my_pensize is: ' +str(my_pensize))
        my_range = 1800
        Lg.logger.info('The valu of my_range is: ' + str(my_range))
        Lg.logger.info('Starting main script at ' + str(Tm.my_time))
        for my_loops in range(1,3):
            Lg.logger.info('Starting first pass of  loop  ' + str(my_loops)  + '@ ' + str(Tm.my_time))
            turtle.bgcolor(0, 0, my_loops * 18)
            all_pens_home()
            for count in range(my_range):
                h.pick_gold()
                t.lb.pencolor(my_loops * 80, my_range - count % 255, count % 255)
                t.go.pensize(count / my_pensize / my_loops)
                t.lb.pensize(count / my_pensize / my_loops)
                t.lb.left(my_angle)
                t.go.rt(my_angle)
                t.lb.fd(count / my_length)
                f.save_thumb()
                t.go.fd(count / my_length)
                f.save_thumb()
                t.lb.left(my_angle / 2)
                t.go.rt(my_angle / 2)
                t.lb.fd(count / my_length / 2)
                f.save_thumb()
                t.go.fd(count / my_length / 2)
                f.save_thumb()
                t.go.circle(count / my_length / t.phi, my_angle)
                f.save_thumb()
                t.lb.circle(count / my_length / t.phi, -my_angle)
                f.save_thumb()
            all_pens_home()
            Lg.logger.info('Starting second pass of  loop  ' + str(my_loops)  + '@ ' + str(Tm.my_time))
            count = 0
            turtle.bgcolor(my_loops * 50, my_loops * 45, my_loops * 20)
            for count in range(my_range):
                '''Second pass'''
                if my_loops == 2:
                    h.pick_magenta()
                    t.go.pencolor(my_loops * 80, my_loops * count % 255, my_range - count % 152)
                    t.go.pensize(count / my_pensize / my_loops)
                    t.me.pensize(count / my_pensize / my_loops)
                    t.me.rt(my_angle)        
                    t.go.left(my_angle)
                    t.me.fd(count / my_length)
                    f.save_thumb()
                    t.go.fd(count / my_length)
                    f.save_thumb()
                    t.me.rt(my_angle / 2)
                    t.go.left(my_angle / 2)
                    t.me.fd(count / my_length / 2)
                    f.save_thumb()
                    t.go.fd(count / my_length / 2)
                    f.save_thumb()
                    t.me.circle(count / my_length / t.phi, my_angle)
                    f.save_thumb()
                    t.go.circle(count / my_length / t.phi, - my_angle)
                    f.save_thumb()
                elif my_loops == 3:
                    h.pick_green()
                    t.go.pencolor(my_loops * count % 255, my_loops * 80, my_range - count % 127)
                    t.go.pensize(count / my_pensize / my_loops)
                    t.lg.pensize(count / my_pensize / my_loops)
                    t.lg.rt(my_angle)        
                    t.go.left(my_angle)
                    t.lg.fd(count / my_length)
                    f.save_thumb()
                    t.go.fd(count / my_length)
                    f.save_thumb()
                    t.lg.rt(my_angle / 2)
                    t.go.left(my_angle / 2)
                    t.lg.fd(count / my_length / 2)
                    f.save_thumb()
                    t.go.fd(count / my_length / 2)
                    f.save_thumb()
                    t.lg.circle(count / my_length / t.phi, my_angle)
                    f.save_thumb()
                    t.go.circle(count / my_length / t.phi, - my_angle)
                    f.save_thumb()
    stage_video()
    finalize()



#  Group B Module_10
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module outputs 10 minute duration @ 1800 my_range setting, and 14 minutes @ 2040 my_range setting
# This module uses three pens per pass (4 passes)
# Last Run date
def stupendous_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Stupendous Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range(len(a.i_angle)):
        t.my_venv()
        t.set_up_all_pens()
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
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
        def run_stupendous():
            pen_01.pensize(count / my_pensize)
            pen_02.pensize(count / my_pensize_a)
            pen_03.pensize(count /my_pensize)
            pen_02.left(my_angle)  # Pen 2
            pen_02.fd(count / my_length)  #Pen 2
            f.save_thumb()
            pen_03.circle(count / my_circle, - my_angle, 3)  # Pen 3
            f.save_thumb()
            pen_03.right(my_angle)
            pen_03.fd(count / my_length)  # Pen 3
            f.save_thumb()
            pen_01.left(my_angle)
            pen_01.backward(count / my_length_bk)  # Pen 1
            f.save_thumb()
            pen_01.right(my_angle / 2)  # Pen 1
            pen_01.fd(count / my_length)
            f.save_thumb()
            pen_02.left(my_angle)  #Pen 2
            pen_02.fd(count / my_length )  #Pen 2
            pen_01.rt(my_angle)  # Pen 1
            pen_01.fd(count / my_length)  # Pen 1
            f.save_thumb()
#         all_pens_home()
        count = 0
        Lg.logger.info(f'Starting First Pass @ {Tm.my_time}')
        pen_01 = t.lu
        pen_02 = t.me
        pen_03 = t.el
        pen_01.setpos(0,0)
        pen_02.setpos(0,0)
        pen_03.setpos(0,0)
        for count in range(my_range): # First Pass
            pen_01.pencolor(my_random, 255, count % 150) # Pen t.lu (Pen 1)
            pen_02.pencolor(255-count % 255, count % 255, count % 255) #Pen t.me  (Pen 2)
            pen_03.pencolor(count % 255, count % 127, my_random - count % 150) #Pen t.el  (Pen 3)
            turtle.bgcolor(10,0,0)
            run_stupendous()
        Lg.logger.info(f'Starting Second Pass @ {Tm.my_time}')
        pen_01 = t.li
        pen_02 = t.lg
        pen_03 = t.go
        pen_01.setpos(0,0)
        pen_02.setpos(0,0)
        pen_03.setpos(0,0)
        for count in range(my_range): # Second Pass
            pen_01.pencolor(count % 255, my_random, 255) #Pen t.li (Pen 1)
            pen_02.pencolor(25, count % 255, count % 127) #Pen t.lg (Pen 2)
            pen_03.pencolor(count % 127, count % 255, 255 -count % 255) # Pen t.go (Pen 3)
            turtle.bgcolor(0,10,0)
            run_stupendous()
        pen_01 = t.lu
        pen_02 = t.me
        pen_03 = t.el  
        pen_01.setpos(0,0)
        pen_02.setpos(0,0)
        pen_03.setpos(0,0)    
        Lg.logger.info(f'Starting Third Pass @ {Tm.my_time}')
        for count in range(my_range): # Third Pass
            pen_01.pencolor(127 - count % 127, 255-count% 255, count % 255) # Pen t.lu (Pen 1)
            pen_02.pencolor(count % 255, my_random, 255 - count% 255) #Pen t.me  (Pen 2)
            pen_03.pencolor(255- count % 255, count % 255, 255) #Pen t.el  (Pen 3)
            turtle.bgcolor(0,0,10)
            run_stupendous()
        pen_01 = t.li
        pen_02 = t.lg
        pen_03 = t.go    
        pen_01.setpos(0,0)
        pen_02.setpos(0,0)
        pen_03.setpos(0,0)
        Lg.logger.info(f'Starting Fourth Pass @ {Tm.my_time}')
        for count in range(my_range): # Fourth Pass
           
           h.pick_gold() #Pen t.go (Pen 3)
           pen_02.pencolor(count % 255, 255 - count % 255, 255 - count % 255) #Pen t.lg (Pen 2)
           pen_01.pencolor(count % 127, count % 255, 255 - count % 255) # Pen t.go (Pen 3)
           turtle.bgcolor(10,10,0)
           run_stupendous()
            
    reset_all()    
    stage_reverse_video()
    finalize()




#  Group B Module_11
#**************************************************************************************************************
#This script features pens: el, me, go, ly, ce, lu, lg, and lb.
#They follow separate yet coordinated routes to compose the mandala.
#Duration at 18 minutes for length value of 600.
#+++++++++++MODULE  Courage Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
def courage_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Courage Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        my_hue = random.randint(5, 100)
        my_hue_a = random.randint(100, 200)
        Lg.logger.info('The value of my_hue is' + '   ' + str(my_hue))
        Lg.logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
        count = 0
        my_length = 637 # Best with multiples of 255
        fd_01, fd_02, fd_03, fd_04 = 1.2, 1.2, 1.2, 1.2
        circ_01, circ_02, circ_03 = 18, 24, 32
        bk_01 = 6
        # First pass
        for count in range(my_length): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)      
            h.pick_blue() # Blue pen is t.lb
            R =  my_hue  #Pen el color
            G =  255  #Pen el color
            B =  0  #Pen el color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            t.el.color( R , G - int(count) %255 ,  int(count) %255 )
            t.me.color( L - count %255, M,  count % 255 )
    #         t.lb.color( D + count %75, E, F - count %75)
            t.el.left(my_angle)
            t.me.left(my_angle)
            t.lb.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.me.fd( count + t.phi )
            f.save_thumb()
            t.lb.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.me.left( - my_angle)
            t.lb.rt( my_angle)
            t.me.fd(count / fd_03)
            f.save_thumb()
            t.lb.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.me.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.lb.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            f.save_thumb()
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.me.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.lb.pensize(count  / 150)
        count = 0
        all_pens_home()
        # Second pass
        for count in range(my_length): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0) 
            h.pick_magenta() # Magenta pen is t.me
            R =  my_hue  #Pen le color
            G = 255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            Lg.logger.info('The value of my_hue is' + '   ' + str(my_hue))
            Lg.logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
            t.el.color( G - count %255 ,  count %255, R )
    #         t.me.color( L - count %255, M,  E)
            t.lb.color(F - count %255, E, D + count %255)
            t.el.left(my_angle)
            t.me.left(my_angle)
            t.lb.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.me.fd( count + t.phi )
            f.save_thumb()
            t.lb.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.me.left( - my_angle)
            t.lb.rt( my_angle)
            t.me.fd(count /fd_03)
            f.save_thumb()
            t.lb.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.me.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.lb.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            f.save_thumb()
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.me.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.lb.pensize(count  / 150)
        count = 0
        all_pens_home()    
        # Third pass
        for count in range(my_length): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)      #.bg_fade_skyblue_to_dark()
            h.pick_green() # Green pen is t.lg
            R =  my_hue  #Pen le color
            G =  255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            t.el.color( R , G - count %255 ,  count %255 )
            t.me.color( L - count %255, M,  count %255 )
    #         t.lg.color( D + count %255, E, F - count %255)
            t.el.left(my_angle)
            t.me.left(my_angle)
            t.lg.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.me.fd( count + t.phi )
            f.save_thumb()
            t.lg.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.me.left( - my_angle)
            t.lg.rt( my_angle)
            t.me.fd(count / fd_03)
            f.save_thumb()
            t.lg.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.me.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.lg.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            f.save_thumb()
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.me.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.lg.pensize(count  / 150)
    #     count = 0
    #     all_pens_home()
    #     # Fourth pass
    #     for count in range(my_length): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
    #         turtle.bgcolor(0, 0, 0) 
    #         h.pick_magenta() # Magenta pen t.me
    #         R =  my_hue  #Pen le color
    #         G = 255  #Pen le color
    #         B =  0  #Pen le color
    #         L = 255  #Pen me color
    #         M = my_hue_a  #Pen me color
    #         N = 0  #Pen me color
    #         D = 0  #Pen lb color
    #         E = my_hue  #Pen lb color
    #         F = 255  #Pen lb color
    #         Lg.logger.info('The value of my_hue is' + '   ' + str(my_hue))
    #         Lg.logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
    #         t.el.color( G - count %255 ,  count %255, R )
    # #         t.me.color( L - count %255, M,  E)
    #         t.lb.color(F - count %255, E, D + count %255)
    #         t.el.left(my_angle)
    #         t.me.left(my_angle)
    #         t.lb.left( my_angle / t.phi)
    #         t.el.fd( count / fd_01)
    #         f.save_thumb()
    #         t.me.fd( count + t.phi )
    #         f.save_thumb()
    #         t.lb.fd( count / fd_02)
    #         f.save_thumb()
    #         t.el.rt(my_angle)
    #         t.me.left( - my_angle)
    #         t.lb.rt( my_angle)
    #         t.me.fd(count /fd_03)
    #         f.save_thumb()
    #         t.lb.fd(count  / fd_04)
    #         f.save_thumb()
    #         t.el.circle(count / circ_01,  my_angle, 3)
    #         f.save_thumb()
    #         t.me.circle(count / circ_02,  my_angle)
    #         f.save_thumb()
    #         t.lb.circle(count / circ_03, my_angle)
    #         f.save_thumb()
    #         t.el.penup()
    #         t.el.left(my_angle)
    #         t.el.backward(count / bk_01)
    #         f.save_thumb()
    #         t.el.pendown()
    #         t.el.pencolor(255,255,10)
    #         t.el.dot(3)
    #         f.save_thumb()
    #         t.me.pensize(count  / 145)
    #         t.el.pensize(count  / 150 )
    #         t.lb.pensize(count  / 150)
        count = 0
        all_pens_home()    
        # Fifth pass
        for count in range(my_length): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)      #.bg_fade_skyblue_to_dark()
            h.pick_gold() # Gold pen is t.go
            R =  my_hue  #Pen le color
            G =  255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            t.el.color( R , G - count %255 ,  count %255 )
            t.me.color( L - count %255, M,  count %255 )
    #         t.go.color( D + count %255, E, F - count %255)
            t.el.left(my_angle)
            t.me.left(my_angle)
            t.go.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.me.fd( count + t.phi )
            f.save_thumb()
            t.go.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.me.left( - my_angle)
            t.go.rt( my_angle)
            t.me.fd(count / fd_03)
            f.save_thumb()
            t.go.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.me.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.go.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            f.save_thumb()
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.me.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.go.pensize(count  / 150)
        count = 0
        all_pens_home()
        # Sixth pass
        for count in range(my_length): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0) 
            h.pick_yellow() # Yellow  pen is t.ly
            R =  my_hue  #Pen le color
            G = 255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            Lg.logger.info('The value of my_hue is' + '   ' + str(my_hue))
            Lg.logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
            t.el.color( G - count %255 ,  count %255, R )
            t.me.color( L - count %255, M,  E)
    #         t.ly.color(F - count %255, E, D + count %255)
            t.el.left(my_angle)
            t.me.left(my_angle)
            t.ly.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.me.fd( count + t.phi )
            f.save_thumb()
            t.ly.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.me.left( - my_angle)
            t.ly.rt( my_angle)
            t.me.fd(count / fd_03)
            f.save_thumb()
            t.ly.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.me.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.ly.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.me.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.ly.pensize(count  / 150)
        count = 0
        all_pens_home()    
        # Seventh pass
        for count in range(my_length): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)      #.bg_fade_skyblue_to_dark()
            h.pick_red() # Red pen is t.lu
            R =  my_hue  #Pen le color
            G =  255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            t.el.color( R , G - count %255 ,  count %255 )
            t.me.color( L - count %255, M,  count %255 )
    #         t.lu.color( D + count %255, E, F - count %255)
            t.el.left(my_angle)
            t.me.left(my_angle)
            t.lu.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.me.fd( count + t.phi )
            f.save_thumb()
            t.lu.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.me.left( - my_angle)
            t.lu.rt( my_angle)
            t.me.fd(count / fd_03)
            f.save_thumb()
            t.lu.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.me.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.lu.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            f.save_thumb()
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.me.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.lu.pensize(count  / 150)
        count = 0
        all_pens_home()
        # Eighth pass
        for count in range(my_length): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0) 
            h.pick_orange() # Orange pen is t.lq
            R =  my_hue  #Pen le color
            G = 255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            Lg.logger.info('The value of my_hue is' + '   ' + str(my_hue))
            Lg.logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
            t.el.color( G - count %255 ,  count %255, R )
            t.me.color( L - count %255, M,  E)
    #         t.lq.color(F - count %255, E, D + count %255)
            t.el.left(my_angle)
            t.me.left(my_angle)
            t.lq.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.me.fd( count + t.phi )
            f.save_thumb()
            t.lq.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.me.left( - my_angle)
            t.lu.rt( my_angle)
            t.me.fd(count / fd_03)
            f.save_thumb()
            t.lq.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.me.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.lq.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            f.save_thumb()
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.me.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.lq.pensize(count  / 150)
        count = 0
        all_pens_home()    
        # Ninth pass
        for count in range(my_length): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0)      #.bg_fade_skyblue_to_dark()
            h.pick_blue() # Blue pen is t.lb
            R =  my_hue  #Pen le color
            G =  255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            t.el.color( R , G - count %255 ,  count %255 )
            t.me.color( L - count %255, M,  count %255 )
    #         t.lb.color( D + count %255, E, F - count %255)
            t.el.left(my_angle)
            t.me.left(my_angle)
            t.lb.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.me.fd( count + t.phi )
            f.save_thumb()
            t.lb.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.me.left( - my_angle)
            t.lb.rt( my_angle)
            t.me.fd(count / fd_03)
            f.save_thumb()
            t.lb.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.me.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.lb.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.me.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.lb.pensize(count  / 150)
        count = 0
        all_pens_home()
        # Tenth pass
        for count in range(my_length): # 600 is default. Use lower number for testing. Loop count is  limited by maximum color value of 255 (0-255).
            turtle.bgcolor(0, 0, 0) 
            h.pick_indigo() # Indigo pen is t.li
            R =  my_hue  #Pen le color
            G = 255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            Lg.logger.info('The value of my_hue is' + '   ' + str(my_hue))
            Lg.logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
            t.el.color( G - count %255 ,  count %255, R )
    #         t.li.color( L - count %255, M,  E)
            t.lb.color(F - count %255, E, D + count %255)
            t.el.left(my_angle)
            t.li.left(my_angle)
            t.lb.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.li.fd( count + t.phi )
            f.save_thumb()
            t.lb.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.li.left( - my_angle)
            t.lb.rt( my_angle)
            t.li.fd(count / fd_03)
            f.save_thumb()
            t.lb.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.li.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.lb.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.li.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.lb.pensize(count  / 150)
        count = 0
        all_pens_home()    
        # Eleventh pass
        for count in range(my_length): #250 is default. Use lower number for testing. Loops limited by maximum color value of 255.
            turtle.bgcolor(0, 0, 0)      #.bg_fade_skyblue_to_dark()
            h.pick_dark() # Dark pen is t.lz
            R =  my_hue  #Pen le color
            G =  255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            t.el.color( R , G - count %255 ,  count %255 )
            t.me.color( L - count %255, M,  count %255 )
    #             t.lb.color( D + count %255, E, F - count %255)
            t.el.left(my_angle)
            t.me.left(my_angle)
            t.lz.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.me.fd( count + t.phi )
            f.save_thumb()
            t.lz.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.me.left( - my_angle)
            t.lz.rt( my_angle)
            t.me.fd(count / fd_03)
            f.save_thumb()
            t.lz.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.me.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.lz.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            f.save_thumb()
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.me.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.lz.pensize(count  / 150)
        count = 0
        all_pens_home()
        # Twelfth pass
        for count in range(my_length): #255 is default. Use lower number for testing. Loops limited by maximum color value of 255.
            turtle.bgcolor(0, 0, 0) 
            h.pick_random() # Random pen is t.ce
            R =  my_hue  #Pen le color
            G = 255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            Lg.logger.info('The value of my_hue is' + '   ' + str(my_hue))
            Lg.logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
            t.el.color( G - count %255 ,  count %255, R )
    #             t.ce.color( L - count %255, M,  E)
            t.lb.color(F - count %255, E, D + count %255)
            t.el.left(my_angle)
            t.ce.left(my_angle)
            t.lb.left( my_angle / t.phi)
            t.el.fd( count / fd_01)
            f.save_thumb()
            t.ce.fd( count + t.phi )
            f.save_thumb()
            t.lb.fd( count / fd_02)
            f.save_thumb()
            t.el.rt(my_angle)
            t.ce.left( - my_angle)
            t.lb.rt( my_angle)
            t.ce.fd(count / fd_03)
            f.save_thumb()
            t.lb.fd(count  / fd_04)
            f.save_thumb()
            t.el.circle(count / circ_01,  my_angle, 3)
            f.save_thumb()
            t.ce.circle(count / circ_02,  my_angle)
            f.save_thumb()
            t.lb.circle(count / circ_03, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.left(my_angle)
            t.el.backward(count / bk_01)
            f.save_thumb()
            t.el.pendown()
            t.el.pencolor(255,255,10)
            t.el.dot(3)
            f.save_thumb()
            t.ce.pensize(count  / 145)
            t.el.pensize(count  / 150 )
            t.lb.pensize(count  / 150)
    stage_video()
    finalize()




#  Group B Module_11
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala_extended():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Brave Mandala Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        for r in range(2):
            t.el.penup()
            t.me.penup()
            t.el.setpos(0,0)
            t.me.setpos(0,0)
            t.el.seth(my_angle)
            t.me.seth(my_angle)
            t.el.pendown()
            t.me.pendown()
            t.el.speed(0)
            t.me.speed(0)
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
            t.el.seth(my_angle)
            t.me.seth(my_angle)
            Lg.logger.info('Starting 1st Loop...')
            for count in range( my_range):  # First Pass
                t.el.pensize(count / my_pensize)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()  #Screenshot as a png
                t.el.pencolor(count %255, 100 - count %75 , L)
                t.me.pensize(count /  my_pensize / 3)
                t.me.pencolor(Y - count %255, Z, L)
                t.me.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                t.el.rt(my_angle)
                t.el.pencolor(L, M - count %127, N - count %127)
                t.el.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()  #Screenshot as a png
            all_pens_home()
            Lg.logger.info('Starting 2nd Loop...')
            for count in range( my_range + 3): # Second Pass
                t.el.pensize(count/ my_pensize)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()  #Screenshot as a png
                t.me.pencolor(B - count %100, R, G + count %99 )
                t.me.pensize(count /  my_pensize /3)
                t.el.pencolor(count %200, 255 - count %150, L)
                t.me.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                t.el.rt(my_angle)
                t.el.pencolor(Z, M - count %127, N)
                t.el.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()    #Screenshot as a png
            all_pens_home()
            Lg.logger.info('Starting 3rd Loop...')
            for  count  in range(my_range + 6):  #Third Pass
                t.el.pensize(count /  my_pensize)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()  #Screenshot as a png
                t.el.pencolor(count %90,  count %90, B - count %150)
                t.me.pensize(count /  my_pensize /3)
                t.me.pencolor(Z, 255 - count %100, L)
                t.me.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                t.el.rt(my_angle)
                t.el.pencolor(L, M - count %127, N - count %127)
                t.el.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()    #Screenshot as a png
            all_pens_home()
            Lg.logger.info('Starting 4th Loop...')
            for count in range( my_range + 12): # Fourth Pass
                t.el.pensize(count / my_pensize)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()  #Screenshot as a png
                t.me.pencolor(L,  Z, B - count %75)
                t.me.pensize(count / my_pensize/3)
                t.el.pencolor(255 - count %150, R, L)
                t.me.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                t.el.rt(my_angle)
                t.el.pencolor(L, 255 - count %127, 255 - count %127)
                t.el.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()  #Screenshot as a png
            all_pens_home()
            Lg.logger.info('Starting 5th Loop...')
            for count in range( my_range + 18): # Fifth Pass
                t.el.pensize(count / my_pensize)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()  #Screenshot as a png
                t.el.pencolor(R, count %84, count %125)
                t.me.pensize(count / my_pensize/3)
                t.me.pencolor(R, 255 - count %100, L)
                t.me.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                t.el.rt(my_angle)
                t.el.pencolor(Z, M - count %127, N)
                t.el.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()    #Screenshot as a png
            all_pens_home()
            Lg.logger.info('Starting 6th Loop...')
            for count  in range(my_range + 24):  # Sixth Pass
                t.el.pensize(count / my_pensize)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()  #Screenshot as a png
                t.me.pencolor(R, count %25, 100 - count %50)
                t.me.pensize(count / my_pensize /3)
                t.me.pencolor(Z, 255 - count %150, L)
                t.me.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                t.el.rt(my_angle)
                t.el.pencolor(L, 255 - count %255,  count %255)
                t.el.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()    #Screenshot as a png     
            all_pens_home()
            Lg.logger.info('Starting 7th Loop...')
            for count  in range(my_range + 30): # Seventh Pass
                h.pick_light() #Pen el
                h.pick_magenta() # Pen me
                t.el.pensize(count / my_pensize)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()  #Screenshot as a png
                t.me.pencolor(100 - count %50, Z, L)
                t.me.pensize(count/my_pensize /3)
                t.me.pencolor(R, 255 - count %150, L)
                t.me.circle(count, my_angle, 3)
                f.save_thumb()  #Screenshot as a png
                t.el.rt(my_angle)
                t.el.pencolor(L, count %127, Z)
                t.el.circle(count / t.pi, - my_angle, 3)
                f.save_thumb()    #Screenshot as a png     
    stage_video()
    finalize()    
        
            

#  module_5
#*****************************************************************************************************************************
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def hued_polygonial():  # Uses 2 pens with offset phi angle
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Hued Polygonial'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        all_pens_home()
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info(f'Current angle to be drawn is {my_angle:.2f}')
        turtle.title(f'Reversing Hued Polygonial Mandala: {my_angle} Degrees Angle and {au.my_track}')
        t.my_title = f'Reversing Hued Polygonial Mandala: {my_angle} Degrees Angle and {au.my_track}'
        count = 0
        t.lb.speed(0)
        t.go.speed(0)
        t.lu.speed(0)
        turtle.bgcolor(10, 0, 15)
        for count in range(900):    #900 is default. Use lower number for testing.
            t.lb.pensize(count / 300)
            t.go.pensize(count / 300)
            t.lu.pensize(count / 150)
            h.pick_blue() # t.lb
            h.pick_gold() # t.go
            h.pick_red() # t.lu
            t.go.left(my_angle / t.phi)
            t.go.left(my_angle)
            t.go.fd(count / t.phi)
            f.save_thumb()
            t.lb.left(my_angle)
            t.lb.circle(count / 9, my_angle, 6)
            f.save_thumb()
            t.lu.rt(my_angle)
            t.lu.fd(count / 3)
            f.save_thumb()
            t.lb.left(my_angle)
            t.lb.fd(count / 6)
            if count == 900:
                f.save_final_thumb()
            else:
                f.save_thumb()
    stage_reverse_video()
    finalize()








#  module_7
#+++++++++++MODULE DARK MANDALA+++++++++++++++++++++++++++++++++++++++++++++++++++++
def dark_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Dark Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        all_pens_home()
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info(f'Current angle to be drawn is {my_angle:.2f}')
        turtle.title(f'dark_mandala: {my_angle} Degrees Angle and {au.my_track}')
        t.my_title = f'dark_mandala: {my_angle} Degrees Angle and {au.my_track}'
        turtle.bgcolor(50, 50, 10)
        for count in range(150):
            t.lz.pensize(count / 36)
            t.me.pensize(count /84)
            t.li.pensize(count / 48)
            if count <= 75:
                t.lz.pencolor(200, 50, 255- count % 150)
                t.me.pencolor(255 - count % 150, 10, 30)
                t.li.pencolor(count % 50, 10, 100)
            else:
                h.pick_magenta() #pen t.me
                h.pick_dark()  # pen t.lz
                h.pick_indigo() # pen t.li
#             t.lz.circle(count, my_angle)
#             f.save_thumb()
            t.lz.penup()
            t.lz.right(my_angle)
            t.lz.backward(count)
            f.save_thumb()
            t.lz.pendown()
            t.li.fd(count / t.pi)
            f.save_thumb()
            t.lz.right(my_angle)
            t.lz.fd(count )
            f.save_thumb()
            t.li.right(my_angle)
            t.li.fd(count )
            f.save_thumb()
            t.li.fd(count / t.phi)
            f.save_thumb()
#             t.li.circle(count  - my_angle)
#             f.save_thumb()
        #make dots
            t.me.left(my_angle)
            t.me.fd(count )
            f.save_thumb()
            t.me.dot(count /50)
            f.save_thumb()
            t.me.penup()
            t.me.backward(count)
            f.save_thumb()
            t.me.pendown()
            t.me.fd(count)
            f.save_thumb()
            t.me.dot(3)
            f.save_thumb()
#             t.me.circle(count, my_angle)
#             f.save_thumb()
    stage_reverse_video()
    finalize()




#  module_18
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_awesome_mandala():  # Based on Awesome Mandala
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Pretty Awesome Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_range = 512  * 4 #Default is 512; use shorter range to test
    my_pensize = 84 * 4 # Default is 84
    my_pensize_a = 102 * 4 # Default is 102
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info(f'Current angle to be drawn is {my_angle:.2f}')
        turtle.title(f'pretty_awesome_mandala: {my_angle} Degrees Angle and {au.my_track}')
        t.my_title = f'pretty_awesome_mandala: {my_angle} Degrees Angle and {au.my_track}'
        turtle.bgcolor(10, 0, 0)
        all_pens_home()
        R = 0
        G = 255
        B = random.randrange(100, 255, 1)
        Lg.logger.info('The value of hue /B/ is   ' + str(B))
        L = random.randrange(1, 100, 1)
        Lg.logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        t.el.left(my_angle/2)
        t.me.rt(my_angle/2)
        for count in range(my_range):      # 255 is default, use lower number for testing
#             t.bg_fade_yellow_to_dark()
            t.el.left(my_angle)
            t.el.pencolor(R + count % 180, B, G - count %120)
            t.el.fd(count /18)
            f.save_thumb()
            t.me.rt(my_angle)
            t.me.pencolor(L, M + count % 180, N + count % 75)
            t.me.circle(count / t.pi, - my_angle, 3)
            f.save_thumb()
            t.el.pensize(count / my_pensize)
            t.me.pensize(count / my_pensize_a)
            f.save_thumb()
    stage_reverse_video()
    finalize()







def Plain_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Plain Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_range, my_pensize = 900, 150  # 900, 150 are default
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logger.info(f'Current angle to be drawn is {my_angle:.2f}')
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
            h.pick_green() # Pen t.lg
            h.pick_yellow() # Pen t.ly
            t.ly.left(my_angle)
            t.ly.fd(count )
            f.save_thumb()
            t.lg.rt(my_angle)
            t.lg.fd(count)
            f.save_thumb()
            t.ly.pensize(count / my_pensize)
            t.lg.pensize(count / my_pensize)
        all_pens_home()    
        for count in range(my_range):
            h.pick_magenta() # Pen t.me
            h.pick_light() # Pen t.el
            t.el.left(my_angle)
            t.el.fd(count )
            f.save_thumb()
            t.me.rt(my_angle)
            t.me.fd(count)
            f.save_thumb()
            t.el.pensize(count / my_pensize)
            t.me.pensize(count / my_pensize)
        all_pens_home()                              
        for count in range(my_range):
            h.pick_indigo() # Pen t.li
            h.pick_gold() # Pen t.go
            t.li.left(my_angle)
            t.li.fd(count )
            f.save_thumb()
            t.go.rt(my_angle)
            t.go.fd(count)
            f.save_thumb()
            t.li.pensize(count / my_pensize)
            t.go.pensize(count / my_pensize)
        all_pens_home()    
        for count in range(my_range):
            h.pick_red() # Pen t.lu
            h.pick_blue() # Pen t.lb
            t.lu.left(my_angle)
            t.lu.fd(count )
            f.save_thumb()
            t.lb.rt(my_angle)
            t.lb.fd(count)
            f.save_thumb()
            t.lu.pensize(count / my_pensize)
            t.lb.pensize(count / my_pensize)
        all_pens_home()    
        for count in range(my_range):
            h.pick_orange() # Pen t.lq
            h.pick_random() # Pen t.ce
            t.lq.left(my_angle)
            t.lq.fd(count )
            f.save_thumb()
            t.ce.rt(my_angle)
            t.ce.fd(count)
            f.save_thumb()
            t.lq.pensize(count / my_pensize)
            t.ce.pensize(count / my_pensize)
        all_pens_home()     
        for count in range(my_range):
            h.pick_green() # Pen t.lg
            h.pick_random_a() # Pen t.lr
            t.lr.left(my_angle)
            t.lr.fd(count )
            f.save_thumb()
            t.lg.rt(my_angle)
            t.lg.fd(count)
            f.save_thumb()
            t.lg.pensize(count / my_pensize)
            t.lr.pensize(count / my_pensize)    
    stage_reverse_video()
    finalize()        
        



#  module_19
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
''' Status: Last Update: 09/22/2023, Last Completed Run: 09/22/2023
  Uses local turtle pens pa and pb; Discovered that re-intializing the pens speeds up the drawing.
  Using local functions; will revise subsequent scripts using this one as a model structure.
  Duration is based upon quantity of angles selected.
 '''
def mighty_awesome_mandala():  # Based on pretty_awesome Mandala
    global my_project, my_angle, my_title, my_mandala_name, str_angles, my_range, count, pa, pb
    my_mandala_name = 'Mighty Awesome Mandala'
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
        Lg.logger.info(f'Current angle to be drawn is {my_angle:.2f}')
        t.my_title = f'mighty_awesome_mandala: {my_angle:.2f} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0, 0, 10)
        all_pens_home()
        t.my_angles = str_angles
        t.my_splash = my_project + str(au.my_track)
        R = random.randint(10, 200)
        G = 0
        B = 255
        Lg.logger.info(f'The value of hue R is {R}')
        L = random.randint(10, 100)
        Lg.logger.info(f'The value of hue L is {L}')
        def do_mighty_awesome():
                pa.pensize(count / my_pensize)
                pb.pensize(count / my_pensize)
                pa.rt(my_angle)
                pa.fd(count)
                process_thumbs()
                pb.rt(my_angle)
                pb.circle(count, - my_angle)
    #             pb.circle(count + t.phi, - my_angle)
                process_thumbs()
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
        Lg.logger.info(f'Starting First Pass @ {Tm.my_time}')
        for count in range(my_range):
            pa.pencolor(R + count % 55, count % 255, B - count % 255)
            pb.pencolor(L + count % 155, B - count %B, count % B )
            do_mighty_awesome()
            Lg.logger.info(f'Completed loop count {count} of First Pass, {my_angle}: {Tm.my_time}') # Uncomment for testing
        R = random.randint(10, 200)
        Lg.logger.info(f'The value of hue R is {R} ')
        L = random.randint(175, 255)
        Lg.logger.info(f'The value of hue L is {L}')
        Lg.logger.info(f'Starting Second Pass @ {Tm.my_time}')
        reset_pa_pb()
        for count in range(my_range): # Second pass
            pa.pencolor(B - count % 100, count % B, L - count % 175)
            pb.pencolor(B - count % B, count % 50, count %B)
            do_mighty_awesome()
            Lg.logger.info(f'Completed loop count {count} of Second Pass, {my_angle}: {Tm.my_time}') # Uncomment for testing
        count = 0
        R = random.randint(10, 200)
        Lg.logger.info(f'The value of hue R is {R}')
        L = random.randint(10, 200)
        Lg.logger.info(f'The value of hue L is {L}')
        Lg.logger.info(f'Starting Third Pass @ {Tm.my_time}')
        reset_pa_pb()
        for count in range(my_range): # Third pass
            pa.pencolor(count % 84, count % B, R + count % 55)
            pb.pencolor(count % 50, L + count % 55, R + count %55)                                                                                                                                                                                                                                                                                                                                                                            
            do_mighty_awesome()
            Lg.logger.info(f'Completed loop count {count} of Third Pass, {my_angle}: {Tm.my_time}')
        count = 0
        R = random.randint(10, 200)
        Lg.logger.info(f'The value of hue R is {R}')
        L = random.randint(10, 150)
        Lg.logger.info(f'The value of hue L is {L}')
        Lg.logger.info(f'Starting Fourth Pass @ {Tm.my_time}')
        reset_pa_pb()
        for count in range(my_range): # Fourth Pass
            pa.pencolor(L + count %100, count % B, R + count % 50)
            pb.pencolor(count % B, count%127, B - count %B)
            do_mighty_awesome()
            Lg.logger.info(f'Completed loop count {count} of Fourth Pass, {my_angle}: {Tm.my_time}')
        count = 0
        R = random.randint(10, 200)
        Lg.logger.info(f'The value of hue R is {R}')
        L = random.randint(100, 255)
        Lg.logger.info(f'The value of hue L is {L}')
        Lg.logger.info(f'Starting Fifth Pass @ {Tm.my_time}')
        reset_pa_pb()
        for count in range(my_range): # Fifth pass
            pa.pencolor(count % 84, L, count % B)
            pb.pencolor(L, count % B, R)
            do_mighty_awesome()
            Lg.logger.info(f'Completed loop count {count} of Fifth Pass, {my_angle}: {Tm.my_time}')
        reset_pa_pb()
    stage_reverse_video()
    finalize()


#  module_8
#+++++++++++MODULE 8 - Iridescent Polygram+++++++++++++++++++++++++++++++++++++++++++++++++++++
def iridescent_polygram():  # Uses 2 pens with offset phi angle
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Iridescent Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(50, 10, 255)
        t.el.right(my_angle /2)
        t.me.right(my_angle / 2)
        while  count in range (0, 255):  #255 is default. Use lower number for testing.
            t.bg_fade_yellow_to_dark()
            t.el.pensize(count / 49)
            t.me.pensize(count / 72)
            t.el.right(my_angle)
            t.el.fd(count + t.phi)
            t.me.left(my_angle * t.phi)  # This is the offset angle
            t.me.pencolor(random.randint(100,200), random.randint(0,75) + count %150,  random.randint(175,255) - count %150)
            t.el.pencolor(random.randint(0,128) + count %126, random.randint(150,255)- count %126, random.randint(100, 200))
            t.el.circle( count - pi, -my_angle, 8)
            t.me.circle(count / pi, my_angle * t.phi) # This is the offset angle
            t.el.pencolor(255,255,random.randint(100, 200))
            t.me.pencolor(255,random.randint(100, 200), 255)
            t.el.dot(count / t.phi / 18)
            t.me.dot(count / t.phi / 9)
            process_thumbs()
            # count_it_bg()
        stage_video()
    finalize()










#  module_10
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Uses 2 pens with offset phi angle
def hued_gradiant_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles, my_range, count, pa, pb, my_pensize
    my_mandala_name = 'Hued Gradiant Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    
    for a.i  in range( len(a.i_angle)):
        my_angle = (float(a.i_angle_float[a.i]))
        Lg.logging.info('The offset angle value is  ' + str(my_angle * t.phi))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
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
    stage_reverse_video()
    finalize()
        
 #  module_11
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def animated_abstraction():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Animated Abstraction'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logging.info('The offset angle value is  ' + str(my_angle * t.phi))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        t.el.pensize(1)
        t.me.pencolor(200, 99, 102)
        count = 0
        for count in range(length):  # 255 is default. Use lower number for testing.
            t.el.setpos(0,0)
            turtle.bgcolor(count %200, count % 250, count % 50)
            R = 0
            G = 20
            B = 255
            t.el.color( R + count %150, G + count %150,   B - count %100)
            t.el.pensize(5)
            t.el.setposition(-700, 300)
            t.el.circle(count/3, my_angle, 7)
            t.el.backward(100)
            t.el.circle(9, my_angle, 6)
            t.el.pencolor('green')
            t.el.dot(18)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.pendown()
            t.el.pencolor(R + count, G + count % 190, B - count)
            t.el.pensize(count % 20 + t.phi /18 )
            t.el.circle(150, -my_angle, 4)
            t.el.penup()
            t.el.setposition(700, 300)
            t.el.pendown()
            t.el.pensize(5)
            t.el.color( R + count %250, G + count %190,   B - count %200)
            t.el.circle(count/3, my_angle, 7)
            t.el.fd(100)
            t.el.circle(9, my_angle, 6)
            count += 2
            f.save_thumb()
    stage_video()
    finalize()





#  module_12
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gradiant_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Gradiant Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Lg.logging.info('The offset angle value is  ' + str(my_angle * t.phi))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(10,0,15)
        t.el.pensize(1)
        t.me.pencolor(200, 99, 102)
        t.el.left(my_angle / 2)
        t.me.rt(my_angle / 2)
        for count in range(252):  #250 is default. Use lower number for testing, 300 for audio add.
            t.el.pensize(count/18)
            t.el.right(my_angle)
            R = 0
            G = 255
            B = 255
            t.el.color(R + count, G - count, B - count)
            t.el.fd(count)
            turtle.bgcolor(20, count, count)
            f.save_thumb()
            turtle.bgcolor(2,9,3)
            t.my_pen.color( 10, 15, 50)
            Tm.end_time()
    stage_video()
    finalize()




#  module_13
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def growing_yin_yang(): #Published to YouTube 11/11/2021
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Growing Yin-Yang'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_angle = 180
    turtle.bgcolor('aqua') # Has to be a neutral shade like grey to contrast the black and white theme.
    for count in range(400):  #360 is default. Use lower number for testing. The higher the number, the longer the show.
        t.el.pensize(count / 18)
        t.el.color(0,0,0)
        t.el.left(-my_angle - t.phi)
        t.el.circle(count / 2)
        t.el.color(255,255,255)
        t.el.left(my_angle)
        t.el.circle(count / 2)
        f.save_thumb()
    stage_video()
    finalize()




#  module_14
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Uses 2 pens with offset t.phi angle
def animated_hued_polygram():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Animated Hued Polygram'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        for count in range(500):
            t.bg_fade_dark_to_green_to_dark()
            h.pick_light()
            t.el.right(my_angle)
            t.el.fd(count / pi)
            h.pick_indigo()
            t.li.left(-my_angle)
            t.li.fd(count / pi)
            t.el.rt(my_angle)
            t.el.backward(count / t.phi)
            h.pick_gold()
            t.go.fd(count  + t.phi)
            h.pick_dot()
            t.ld.dot(count /48 * t.phi)
            t.go.circle(count / 6, my_angle, 3)
            t.el.pensize(count / 15)
            t.li.pensize(count / 18)
            t.go.pensize(count / 33)
            # count_it()
            t.bg_count += 1
            f.save_thumb()
    stage_video()
    finalize()




#  module_15 NEEDS WORK
'''#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_polygonial():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Pretty Polygonial'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        with Timer("Elapsed time to run this code: {} minutes"):
            turtle.bgcolor(0,0,0)
            Lg.logger.info(str('The featured angle is     ') + str(my_angle))
            count = 0
            t.go.pensize(1)
            t.lg.pensize(1)
            t.lm.pensize(3)
            for count in range(300): # 255 is default. Use lower number for testing
                h.pick_gold()
                h.pick_green()
                h.pick_random()
                h.pick_magenta()
                t.lr.dot(count / 9)
                t.go.pensize(count / 144)
                t.go.left(my_angle)
                t.go.fd(count * t.phi)
                t.lg.pensize(count / 36)
                t.lg.left(my_angle)
                t.lg.fd(count * t.phi)
                t.lm.pensize(count / 54)
                t.lm.left(my_angle)
                t.lm.dot(count / t.phi / 18)
                t.lm.fd(count + pi)
                t.lg.left(my_angle)
                t.lg.circle(-count /9, my_angle, 9)
\               f.save_thumb()
                # count_it()
            reset_all()
            t.my_venv()
    stage_video()
    finalize()
    

'''
#  module_22
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def multi_hued_polygram():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Multi-Hued Polygram'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        t.el.right(t.my_angle / 2)
        t.el.speed(0)
        t.go.speed(0)
        N =  random.randint(1, 100)
        for count in range(500): #Determines size of graphic on the screen by the count of loops
            h.pick_green()
            h.pick_gold()
            R =  0
            G =  255
            B =  255
            L =  0
            M =  0
            t.go.pensize(count /120)
            t.el.pensize(count / 64)
            t.el.color( R + count %255, G - count %255, B - count %255)
            t.el.right(t.my_angle)
            t.el.fd(count + t.phi)
            t.go.circle(count + t.phi, t.my_angle, 3)
#             t.el.circle(count * t.phi, -t.my_angle)
            t.el.right(t.my_angle)
            t.el.fd(count * t.phi)
            t.bg_fade_dark_to_green()
            t.bg_count += 1
            # count_it()
            f.save_thumb()
#             gc.collect()
    stage_video()
    finalize()




#module_23 NEEDS WORK

#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala(): # Uses pens pa, pb
    global my_project, my_angle, my_title, my_mandala_name, str_angles, my_range, count, pa, pb, my_pensize
    my_mandala_name = 'Brave Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = (float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,25)
        make_turtle_pa()
        make_turtle_pb()
        R = random.randrange(150, 250, 10)
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
        my_range = 827
        for count in range(my_range):
            pa.pencolor(R, count % 255, B - count % 255)
            pa.pensize(count/210)
            pa.fd(count / 3)
            process_thumbs()
            pa.left(my_angle)
            pa.fd(count /1.5)
            process_thumbs()
            pb.pensize(count /255)
            pb.pencolor(R, Y - count % 255, L)
            pb.circle(count /3, my_angle, 3)
            process_thumbs()
            pa.rt(my_angle)
            pa.pencolor(L, M - count % 255, N - count % 255)
            pa.circle(count /3, - my_angle, 2)
            process_thumbs()
            pb.left(my_angle)
            pb.backward(count / 36)
            process_thumbs()
        reset_pa_pb()
              
              
            

    stage_reverse_video()
    finalize()
'''    
            
#module_24
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala_decimated():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Angle-Fractioned Brave Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    x = 3
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
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
            t.el.pensize(count/45)
            t.el.left(my_angle/x)
            t.el.fd(count)
            t.el.pencolor(G + count, B - count, R)
            t.me.pensize(count /18)
            t.me.pencolor(Y - count, R, L)
            t.me.circle(count / t.phi, my_angle/x)
            t.el.rt(my_angle/x)
            t.el.pencolor(L, M - count, N - count)
            t.el.circle(count * 1.26, - my_angle/x)
            # #count_it()
            t.bg_count += 1
            f.save_thumb()  #Screenshot as a png set set up mp4
        count = 0
        t.el.penup()
        t.me.penup()
        t.el.setpos(0,0)
        t.me.setpos(0,0)
        t.el.pendown()
        t.me.pendown()
        t.el.speed(0)
        t.me.speed(0)
        t.bgbg_count = 0
        for count in range(510): # Second Pass
            t.bg_fade_green_to_dark()
            t.el.pensize(count/56)
            t.el.left(my_angle/ x)
            t.el.fd(count)
            t.el.pencolor(R, G + count % 255, B - count % 255)
            t.me.pensize(count/18)
            t.me.pencolor(R, Y - count % 255, L)
            t.me.circle(count / t.phi, my_angle/x)
            t.el.rt(my_angle/x)
            t.el.pencolor(Z + count % 225, M - count % 100, N)
            t.el.circle(count, - my_angle/x)
            # count_it()
            # # count += 1
            t.bg_count += 1
            f.save_thumb()    #Screenshot as a png set set up mp4
        count = 0
        t.el.penup()
        t.me.penup()
        t.el.setpos(0,0)
        t.me.setpos(0,0)
        t.el.pendown()
        t.me.pendown()
        t.el.speed(0)
        t.me.speed(0)
        t.bg_count = 0
        for count in range(765): # Third Pass
            Lg.logger.info('The value of Tm.iterable_time is ' + str(Tm.iterable_time))
            Lg.logger.info('The value of count is  ' + str(count))
            t.el.pensize(count/56)
            t.el.left(my_angle/x)
            t.el.fd(count)
            t.el.pencolor(R, G + count% 255, B - count% 255)
            t.me.pensize(count/27)
            t.me.pencolor(R, Y - count% 255, L)
            t.me.circle(count / t.phi, my_angle/x)
            t.el.rt(my_angle / x)
            t.el.pencolor(L, M - count% 255, N - count% 255)
            t.el.circle(count, - my_angle/x)
            # count_it()
            # # count += 1
            t.bg_count += 1
            f.save_thumb()    #Screenshot as a png set set up mp4
    stage_reverse_video()
    finalize()




#module_25
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def color_shifting_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Color-Shifting Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
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
        t.el.left(my_angle/2)
        t.bg_count = 0
        while  count <= 360: # 360 is default for audio clip add, use lower number for testing
            t.el.pensize(count/ 90)
            t.el.dot(3)
            t.el.color( R - count %60,  G - count %140, B + count %200)
            t.el.left(my_angle)
            t.el.circle(count / t.phi, my_angle, 3)
            t.bg_fade_skyblue_to_dark()
            t.bg_count += 1
            f.save_thumb()
    stage_reverse_video()
    finalize()





#module_26
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gold_red_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Gold-Red Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor("indigo")
        for count in range(300): #252 is default, use lower number for testing; 300 for audio clip add
            h.pick_gold()
            h.pick_red()
            h.pick_light()
            t.go.pensize(count / 27)
            t.go.circle(count *t.phi, - my_angle)
            t.lu.pensize(count/18)
            t.lu.backward(count *pi)
            t.lu.right(my_angle)
            t.el.dot(5)
            t.el.left(my_angle)
            t.el.fd(count/2)
            f.save_thumb()
    stage_reverse_video()
    finalize()




#module_27
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gold_red_mandala_extended():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Gold-Red Mandala Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor("indigo")
        for count in range(250): # First Pass
            h.pick_gold()
            h.pick_red()
            h.pick_light()
            t.go.pensize(count / 27)
            t.go.circle(count *t.phi, - my_angle)
            t.lu.pensize(count/18)
            t.lu.backward(count *pi)
            t.lu.right(my_angle)
            t.el.dot(5)
            t.el.left(my_angle)
            t.el.fd(count/2)
            f.save_thumb()
            # count_it()

        t.go.penup()
        t.lu.penup()
        t.el.penup()
        t.go.setpos(0,0)
        t.lu.setpos(0,0)
        t.el.setpos(0,0)
        t.go.pendown()
        t.lu.pendown()
        t.el.pendown()
        t.go.speed(0)
        t.lu.speed(0)
        t.el.speed(0)
        count = 0
        for count in range(505): # Second Pass
            h.pick_gold()
            h.pick_red()
            h.pick_light()
            t.lu.pensize(count / 27)
            t.lu.circle(count *t.phi, - my_angle)
            t.go.pensize(count/18)
            t.go.backward(count *pi)
            t.go.right(my_angle)
            t.el.dot(5)
            t.el.left(my_angle)
            t.el.fd(count/2)
            f.save_thumb()
            # count_it()
            # # count += 1

        t.go.penup()
        t.lu.penup()
        t.el.penup()
        t.go.setpos(0,0)
        t.lu.setpos(0,0)
        t.el.setpos(0,0)
        t.go.pendown()
        t.lu.pendown()
        t.el.pendown()
        t.go.speed(0)
        t.lu.speed(0)
        t.el.speed(0)
        count = 0
        for count in range(755): # Third Pass
            h.pick_gold()
            h.pick_red()
            h.pick_light()
            t.el.pensize(count / 27)
            t.el.circle(count *t.phi, - my_angle)
            t.lu.pensize(count/18)
            t.lu.backward(count *pi)
            t.lu.right(my_angle)
            t.go.dot(5)
            t.go.left(my_angle)
            t.go.fd(count/2)
            f.save_thumb()
            # count_it()
            # # count += 1
    stage_reverse_video()
    finalize()




#module_28
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Hued_freedom_star():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Hued Freedom Star'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        t.el.color(122,133,215)
        R = 0
        G = 50
        B = 255
        turtle.bgcolor(R, G, B)
        def white_dot():
            t.el.pencolor(255,255,255)
            t.el.dot(15)
            t.el.pencolor(123,135,216)
        def purple_dot():
            t.el.pencolor(123,135,216)
            t.el.dot(15)
        for count in range(300): # 720 is default, use lower number for testing
            if count <= 255:
                turtle.bgcolor(R + count, G, B)
            else:
                turtle.bgcolor(255, G, B)
            t.el.pensize(count/50)
            t.el.fd(count * t.phi ) #+ 63)
            white_dot()
            t.el.rt(my_angle)
            t.el.pencolor(123 + count %100 ,135,216 -count %200)
            t.el.fd(count * t.phi)
            white_dot()
            t.el.rt(my_angle)
            t.el.circle(count / t.phi, my_angle, 9)
            white_dot()
            f.save_thumb()
            for i in range(2):
                purple_dot()
            f.save_thumb()
    stage_reverse_video()
    finalize()



#module_29
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def blue_orange_mandala_144():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Hued Gradiant Mandala'
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
    t.el.penup()
    t.el.setpos(0, -100)
    t.el.pendown()
    t.el.speed(0)
    t.el.shape("circle")
    t.el.shapesize(1)
    t.el.pensize(1)
    for count in range(252): #252 is default, use lower number for testing
        turtle.bgcolor(L, C, H + count)
        t.el.pensize(10)
        t.el.right(my_angle)
        t.el.color(L, C, H + count % 150)
        t.el.fd(count  + t.phi)
        f.save_thumb()
        for g in range(12):
            R = 0 + count % 150
            Y = 100
            B = 255 - count % 150
            t.el.left(my_angle)
            t.el.color(R, Y, B)
            t.el.pensize(2)
            t.el.fd(500)
    stage_reverse_video()
    finalize()




#module_30
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def ribbons_mandala():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Ribbons Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        R = 255
        G = 255
        B = 255
        L = 0
        C = 0
        H = 0
        Z = 255
        turtle.bgcolor(L, C, H)
        t.el.penup()
        t.el.setpos(0,  -25)
        t.el.pendown()
        t.el.shape("blank") #circle is default
        t.el.shapesize(1)
        t.el.pensize(1)
        t.el.speed(0)
        my_range = 765 # 510 is default, use lower number for testing
        for count in range(my_range): 
            turtle.bgcolor(10, 0, 25)
            t.el.pensize(3) # 1 is default
            t.el.right(my_angle)
            t.el.color(L +count % 255, C, H + count %127 )
            t.el.fd(count  + t.phi)
            f.save_thumb()
            for g in range(12):  #10 is the default
                R = 127 + count %127
                G = 127 - count %127
                B = 25 - count %25
                t.el.left(my_angle)
                t.el.color(R, G, B)
                t.el.pensize(g/12) # 100 is default
                t.el.circle(72, my_angle, 7)
                f.save_thumb()
        t.el.reset()
        t.set_up_el()
        set_el_home()
    stage_reverse_video()       
    finalize()




#module_31
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def circular_mandala_205():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Hued Gradiant Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    my_angle = 205
    Lg.logger.info(str('The featured angle is     ') + str(round(my_angle)))
    R = 255
    G = 255
    B = 255
    L = 0
    C = 0
    H = 0
    Z = 255
    turtle.color(R, G, B)
    turtle.bgcolor(L, C, H)
    t.el.penup()
    t.el.setpos(0, -150)
    t.el.pendown()
    t.el.speed(0)
    t.el.shape("circle")
    t.el.shapesize(1)
    t.el.pensize(1)
    t.el.hideturtle()
    t.el.color(R, G, B)
    for count in range(200): #200 is default, use lower number for testing
        turtle.bgcolor(L, C, H + count %299)
        t.el.pensize(10)
        t.el.right(my_angle)
        t.el.color(L +count, C + count %80, H)
        t.el.fd(count  * t.phi)
        f.save_thumb()
        for g in range(4):
            R = 101 + count %133
            Y = 101 - count %130
            B = 25 + count %100
            t.el.left(my_angle)
            t.el.color(R, G - count, B)
            t.el.pensize(2)
            t.el.circle(175, my_angle, 11)
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    stage_reverse_video()
    finalize()




#module_32
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def occillating_polygon(): # Needs work
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Occillating Polygon'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        count = 0
        t.el.pensize(1)
        Lg.logger.info('The Angle is   ' + str(my_angle))
        for count in range(149):
            # Default is 149; can use lower number for testing
            R = random.randrange(10,100)
            G = 255  #  random.randrange(171, 255)
            B =  0
            t.el.color( R + count, G - count, B + count)
            turtle.bgcolor(155 - count, 155 - count, 10)
            h.pick_red()
            t.lu.dot(count / 6)
            t.lu.left( - my_angle /2)
            t.lu.fd(count/2 +t.phi)
            t.lu.circle(count * t.phi, my_angle, 6)
            t.lu.rt(my_angle)
            t.el.left(my_angle)
            t.el.circle( count * 3, my_angle)
            t.lu.dot(count / 6)
            t.el.pensize(count / 27)
            # count_it()
            f.save_thumb()
    stage_reverse_video()
    finalize()
        
#module_33
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def arc_star():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Arc-Star'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        count = 0
        t.el.pensize(1)
        count = 0
        t.el.pensize(3)
#             t.el.right(my_angle * 2 )
        for count in range(300):
            if count <= 255:
                turtle.bgcolor(25, 50, count)
            else:
                turtle.bgcolor(25,50,255)
            R =  0
            G =  0
            B =  90
            if count <= 255:
                t.el.color( R + count , G + count, B )
            else:
                t.el.color(255, 255, B)
            t.el.left(my_angle)
            t.el.penup()
            t.el.fd( count / t.phi )
            t.el.pendown()
            t.el.pensize(6)
            t.el.fd(count /t.phi)
            t.el.rt(my_angle)
            R = 0
            G = 230
            B = 255
            t.el.color( count %255, G - count %54, B - count %255 )
            t.el.penup()
            t.el.fd(75)
            t.el.pensize(3)
            t.el.circle(24, my_angle, 10)
            t.el.pendown()
            t.el.backward(count)
            t.el.pensize(count / 72)
            t.el.penup()
            t.el.setposition(0, 0)
            t.el.pendown()
            t.el.color(R + count %255, count %75, 0)
            t.el.circle(count + t.phi, my_angle, 5)
            # count_it()
            f.save_thumb()
    stage_reverse_video()
    finalize()


#module_34
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def home_star():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Home-Star'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        t.el.pensize(3)
        for count in range(359): #359 is default
            turtle.bgcolor(10 + count % 240, 50 + count % 200, count %255)
            R = 150
            G = 230
            B = 0
            t.el.color(count % 104, G - count %200, count %254 )
            t.el.left(my_angle)
            t.el.penup()
            t.el.fd(count / t.phi )
            t.el.pendown()
            t.el.pensize(6)
            t.el.fd(count / t.phi)
            t.el.rt(my_angle)
            t.el.penup()
            t.el.fd(27)
            t.el.pensize(3)
            t.el.pendown()
            t.el.circle(12, my_angle, 9)
            t.el.backward(count + t.phi)
            t.el.pensize(count / 72)
            t.el.penup()
            t.el.setposition(0, 0)
            t.el.pendown()
            t.el.circle(count, my_angle, 5)
            # count_it()
#         time.sleep(10) #for testing only
            f.save_thumb()
    stage_reverse_video()
    finalize()



#module_35
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#Deals best with whole number angles
def use_abs():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Absolute Function Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        count = 0
        t.el.pensize(1)
        # count = 0
        t.el.pensize(3)
        t.el.color('brown', 'green')
        t.el.begin_fill()
        while True:
            t.el.left(my_angle)
            t.el.fd(250)
            f.save_thumb()
            if abs(t.el.pos()) < 1:
                break
        t.el.end_fill()
    stage_reverse_video()
    finalize()




#module_36
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Six-Pointed Mandalas or doubles.
def double_take():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Double Take'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        turtle.bgcolor(0,0,0)
        R = random.randrange(155,255, 5)
        G = 255
        B = 0
        Lg.logger.info('The value of color R is    ' + str(R))
        for count in range(359):
            t.el.pensize(4)
            t.li.pensize(4)
            t.el.left(my_angle)
            t.el.color(R, G - count %255, B + count %255)
            t.el.fd(count * t.phi)
            t.li.color(R, G - count %250, B + count %250)
            t.li.right(my_angle)
            t.li.fd(count * t.phi)
            f.save_thumb()
    stage_video()
    finalize()





#module_37
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Cloverleaf Cross Mandala.
def cloverleaf():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Hued Gradiant Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        t.set_up_el()
        t.el.setpos(0,0)
        turtle.bgcolor(0,0,0)
        for count in range(1020): # Default is 1020; use lower number for testing
            turtle.bgcolor(count %25, 0, count % 10)
            f.save_thumb()
            t.el.pencolor(count %255, 255 - count % 255, count % 127)
            t.el.pensize(count / 1020)
            t.el.circle(count / 3, my_angle)
            f.save_thumb()
            t.el.penup()
            t.el.fd(count /3)
            f.save_thumb()
            t.el.pendown()
            f.save_thumb()
        t.el.reset()    
    Lg.logger.info(f'Stopping Cloverleaf Mandala by Leon Hatton @ {Tm.my_time}')
    Lg.logger.info('###############################################################')
    stage_reverse_video()
    finalize()




#module_38
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Cloverleaf Extended Cross Mandala.
def cloverleaf_extended():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Hued Gradiant Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        Lg.logger.info('Starting First Pass at  ' + str(Tm.my_time))
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
                t.ld.circle(count / t.phi, my_angle)
                f.save_thumb()
                t.ld.penup()
                t.ld.fd(count / t.phi)
                f.save_thumb()
                t.ld.pendown()
                t.ld.pensize(my_pensize)
                Lg.logger.info('t.ld.pensize is  ' + str(my_pensize) + '( for  ' +  str(count))
                f.save_thumb()
        Lg.logger.info('Starting Second Pass at  ' + str(Tm.my_time))
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
                t.lm.circle(count / t.phi, my_angle)
                f.save_thumb()
                t.lm.penup()
                t.lm.fd(count / t.phi)
                t.lm.pendown()
                f.save_thumb()
                Lg.logger.info('t.lm.pencolor is  ' + str(t.lm.pencolor))
        Lg.logger.info('Starting Third Pass at  ' + str(Tm.my_time))
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
                 t.lc.circle(count / t.phi, my_angle)
                 t.lc.penup()
                 t.lc.fd(count / t.phi)
                 t.lc.pendown()
                 f.save_thumb()
        Lg.logger.info('Starting Fourth Pass at  ' + str(Tm.my_time))
        turtle.bgcolor(0,0,0)
        del my_range
        del count
        del t.lc
        gc.collect()
        count = 0
        my_range = 396 # 400 is default; use any number for testing, etc
        t.lz.speed(0)
        t.el.speed(0)
        turtle.colormode(255)
        for i in range(2):
            t.ly.penup()
            t.lg.penup()
            t.ly.setpos(0,0)
            t.lg.setpos(0,0)
            t.ly.seth(my_angle)
            t.lg.seth(my_angle)
            t.ly.pendown()
            t.lg.pendown()
            for count in range(my_range):
                my_pensize = count / 56
                t.ly.pensize(my_pensize)
                t.lg.pensize(my_pensize)
                h.pick_yellow() # Pen t.ly
                h.pick_green() # Pen t.lg
                t.ly.circle(count / t.phi, my_angle)
                f.save_thumb()
                t.lg.circle(count / t.phi, -my_angle)
                f.save_thumb()
                t.ly.penup()
                t.lg.penup()
                t.lg.backward(count / t.phi)
                f.save_thumb()
                t.ly.fd(count / t.phi)
                t.lg.pendown()
                t.ly.pendown()
                f.save_thumb()
        Lg.logger.info('Starting Fifth Pass at  ' + str(Tm.my_time))
        turtle.bgcolor(0,0,0)
        del my_range
        del count
        del t.ly
        del t.lg
        gc.collect()
        count = 0
        my_range = 396 # 400 is default; use any number for testing, etc
        t.me.speed(0)
        turtle.colormode(255)
        for i in range(2):
            t.me.penup()
            t.me.setpos(0,0)
            t.me.pendown()
            for count in range(my_range):
                my_pensize = count / 56
                t.me.pensize(my_pensize)
                t.me.pencolor(count %100, count % 255, 255 * i)
                t.me.circle(count / t.phi, my_angle)
                f.save_thumb()
                t.me.penup()
                t.me.fd(count / t.phi)
                t.me.pendown()
                f.save_thumb()
        Lg.logger.info('Starting Sixth Pass at  ' + str(Tm.my_time))
        turtle.bgcolor(0,0,0)
        del my_range
        del count
        del t.me
        gc.collect()
        count = 0
        my_range = 396 # 400 is default; use any number for testing, etc
        t.lq.speed(0)
        t.lb.speed(0)
        turtle.colormode(255)
        for i in range(2):
            t.lb.penup()
            t.lq.penup()
            t.lb.setpos(0,0)
            t.lb.seth(my_angle)
            t.lq.setpos(0,0)
            t.lq.seth(my_angle)
            t.lb.pendown()
            t.lq.pendown()
            for count in range(my_range):
                my_pensize = count / 56
                t.lb.pensize(my_pensize) 
                t.lq.pensize(my_pensize) 
                h.pick_blue() # Pen t.lb
                h.pick_orange() # Pen t.lq
                t.lb.circle(count / t.phi, my_angle)
                f.save_thumb()
                t.lq.circle(count / t.phi, -my_angle)
                f.save_thumb()
                t.lb.penup()
                t.lq.penup()
                t.lb.backward(count / t.phi)
                t.lq.fd(count / t.phi)
                t.lb.pendown()
                t.lq.pendown()
                f.save_thumb()
        Lg.logger.info('Starting Seventh Pass at  ' + str(Tm.my_time))
        turtle.bgcolor(0,0,0)
        del my_range
        del count
        del t.lb
        del t.lq
        gc.collect()
        count = 0
        turtle.colormode(255)
        my_range = 396 # 400 is default; use any number for testing, etc
        t.ll.speed(0)
        t.el.speed(0)
        for i in range(2):
            t.el.penup()
            t.ll.penup()
            t.el.setpos(0,0)
            t.ll.setpos(0,0)
            t.ll.seth(my_angle)
            t.el.seth(my_angle)
            t.el.pendown()
            t.ll.pendown()
            for count in range(my_range):
                my_pensize = count / 56
                t.el.pensize(my_pensize)
                t.ll.pensize(my_pensize)
                t.el.pencolor(count % 21, count % 60, 255 - count % 10)
                t.ll.pencolor(i * 255, 255 - count % 255, count % 50)
                t.el.circle(count / t.phi, -my_angle)
                f.save_thumb()
                t.ll.circle(count / t.phi, my_angle)
                t.el.penup()
                t.ll.penup()
                t.el.fd(count)
                t.ll.fd(count)
                t.el.pendown()
                t.ll.pendown()
                f.save_thumb()
            stage_video()
    finalize()



#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Majestic Extended Mandala.
def majestic_mandala_extended():
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Hued Gradiant Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    Lg.logger.info('##########################################################')
    t.set_up_el()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        rand_hue = random.randint(10, 155)
        my_length = 500
        my_pensize = 66
        for r in range(3):
            t.el.speed(0)
            turtle.bgcolor(0,25,0)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.seth(my_angle)
            t.el.pendown()
            count = 0
            t.el.speed(0)
            t.el.pencolor(0, 255,0)
            turtle.bgcolor(0,0,0)
            a.report_angle_status()
            Lg.logger.info('The featured angle is  ' + str(my_angle))
            Lg.logger.info('The soundtrack selected for this project is  ' + str(au.my_track))
            Lg.logger.info('Starting First Pass at  ' + Tm.my_time)
            t.el.seth(my_angle)
            for count in range(my_length):
                t.el.pensize(count /my_pensize)
                t.el.pencolor(count % 255, 255 - count % 127, rand_hue)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Second Pass at  '  + Tm.my_time)
            t.el.seth(my_angle)
            t.el.speed(0)
            turtle.bgcolor(0,25,0)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.pendown()
            count = 0
            for count in range(my_length):
                t.el.pensize(count / my_pensize)
                t.el.pencolor(255 - count % 127, 255 - count % 127, rand_hue)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Third Pass at  ' + Tm.my_time)
            t.el.seth(my_angle)
            t.el.speed(0)
            turtle.bgcolor(25, 0, 0)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.pendown()
            count = 0
            for count in range(my_length):
                t.el.pensize(count /my_pensize)
                t.el.pencolor(rand_hue, 255 - count% 127, 255 - count% 255)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.fd(count /t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Fourth Pass at  '  +  Tm.my_time)
            t.el.seth(my_angle)
            t.el.speed(0)
            turtle.bgcolor(0,0,25)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.pendown()
            count = 0
            for count in range(my_length):
                t.el.pensize(count /my_pensize)
                t.el.pencolor(count % 127, rand_hue, 255 - count % 72)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Fifth Pass at  '  + Tm.my_time)
            t.el.seth(my_angle)
            t.el.speed(0)
            turtle.bgcolor(25, 0, 25)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.pendown()
            count = 0
            for count in range(my_length):
                t.el.pensize(count /my_pensize)
                t.el.pencolor(255 - count %255, count % 127, count % 255)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Sixth Pass at  ' + Tm.my_time)
            t.el.seth(my_angle)
            t.el.speed(0)
            turtle.bgcolor(25, 25, 25)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.pendown()
            count = 0
            for count in range(my_length):
                t.el.pensize(count /my_pensize)
                t.el.pencolor(count % 72, count% 255, rand_hue)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.fd(count /t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Seventh Pass at  '  +  Tm.my_time)
            t.el.seth(my_angle)
            t.el.speed(0)
            turtle.bgcolor(0, 25, 25)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.pendown()
            count = 0
            for count in range(my_length):
                t.el.pensize(count /my_pensize)
                t.el.pencolor( rand_hue, count % 255, count % 255)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Eighth Pass at  '  +  Tm.my_time)
            t.el.seth(my_angle)
            t.el.speed(0)
            turtle.bgcolor(10, 35, 25)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.pendown()
            count = 0
            for count in range(my_length):
                t.el.pensize(count /my_pensize)
                t.el.pencolor( rand_hue, 255 - count % 200, count % 200)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Ninth Pass at  '  +  Tm.my_time)
            t.el.seth(my_angle)
            t.el.speed(0)
            turtle.bgcolor(25, 0, 25)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.pendown()
            count = 0
            for count in range(my_length):
                t.el.pensize(count /my_pensize)
                t.el.pencolor( count % 100, 255 - count % 100, rand_hue)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.fd(count + pi)
                f.save_thumb()
            Lg.logger.info('Starting Tenth Pass at  '  +  Tm.my_time)
            t.el.seth(my_angle)
            t.el.speed(0)
            turtle.bgcolor(0, 0, 0)
            t.el.penup()
            t.el.setpos(0,0)
            t.el.pendown()
            count = 0
            for count in range(my_length):
                t.el.pensize(count /my_pensize)
                t.el.pencolor( count % 150, rand_hue, count % 150)
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.fd(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.fd(count + pi)
                f.save_thumb()     
    stage_reverse_video()
    finalize()


#module_43
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def sirius_mandala():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Hued Gradiant Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        for count in range(500):
            if count < 400:
                t.el.color( 0, count % 255, 255) #Blue/Coral
            else:
                t.el.color(count % 255, 255, 0) # Green/Yellow
                
            t.el.fd(count / t.phi)
            f.save_thumb()
            t.el.pensize(count / 63)
            t.el.circle(count / 10, - my_angle)
            f.save_thumb()
            
                         
            t.me.color(255, 0, count % 255) #Red/Magenta
            t.me.rt(my_angle)
            t.me.fd(count / t.phi)
            f.save_thumb()
            t.me.pensize(count / 72)
            t.me.circle(count / 14, - my_angle)
            f.save_thumb()
           
                
            t.ce.color( 255, 255, 255) #White
            t.ce.rt(my_angle)
            t.ce.fd(count / t.phi)
            f.save_thumb()
            t.ce.pensize(count / 81)
            t.ce.circle(count / 18, - my_angle)
            f.save_thumb()
 
    stage_reverse_video()
    finalize()






#module_44
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wall_show():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Wall Show'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        turtle.bgcolor(30,255,60)
        Lg.logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        Lg.logger.info('The featured angle is     ' + str(my_angle))
        Lg.logger.info(('The value of t.rand_num is   ')  + str(t.rand_num))
        Lg.logger.info(('The value of t.rand_pick is   ')  + str(t.rand_pick))
        Lg.logger.info('......................................................................................')
        for count in range(255):
            R =  0
            G =  150
            B =  255
            t.el.color( R + count, G - count % 130, B - count)
            t.el.fd(count * t.phi)
            t.el.left(my_angle)
            t.el.pensize(count /36)
            t.el.color(count, t.rand_num, 255 - count)
            t.el.right(my_angle)
            t.el.circle(count / 3, my_angle, 6)
            t.ce.color( B - count, G - count % 150, R + count )
            t.ce.fd(count * t.phi)
            t.ce.right(my_angle)
            t.ce.fd(count * t.phi)
            t.ce.pensize(count / 27)
            t.ce.color(255 - count, count, t.rand_pick)
            # count_it()
            turtle.bgcolor(30, 256 - count, 60)
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        Tm.end_time()
    Lg.logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    Lg.logger.info('************************************************************************')
    reset_all()





#module_45
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wall_show_extended():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Wall Show Extended'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    for a.i  in range( len(a.i_angle)):
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        count = 0
        turtle.bgcolor(30,255,60)
        Lg.logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        Lg.logger.info('The featured angle is     ' + str(my_angle))
        Lg.logger.info(('The value of t.rand_num is   ')  + str(t.rand_num))
        Lg.logger.info(('The value of t.rand_pick is   ')  + str(t.rand_pick))
        Lg.logger.info('......................................................................................')
        for count in range(250):
            R =  0
            G =  150
            B =  255
            t.el.color( R + count, G - count % 130, B - count)
            t.el.fd(count * t.phi)
            t.el.left(my_angle)
            t.el.pensize(count /36)
            t.el.color(count, t.rand_num, 255 - count)
            t.el.right(my_angle)
            t.el.circle(count / 3, my_angle, 6)
            t.ce.color( B - count, G - count % 150, R + count )
            t.ce.fd(count * t.phi)
            t.ce.right(my_angle)
            t.ce.fd(count + t.phi)
            t.ce.pensize(count / 27)
            t.ce.color(255 - count, count, t.rand_pick)
            # count_it()
            turtle.bgcolor(30, 256 - count, 60)
            f.save_thumb()
        t.el.penup()
        t.ce.penup()
        t.el.setpos(0,0)
        t.ce.setpos(0,0)
        t.el.pendown()
        t.ce.pendown()
        t.el.speed(0)
        t.ce.speed(0)
        count = 0
        for count in range(503):
            R =  255
            G =  150
            B =  0
#             Lg.logger.info(str(t.el.color))
            t.el.color(R - count % 255, G - count % 130, B + count %255)
            t.el.fd(count * t.phi)
            t.el.left(my_angle)
            t.el.pensize(count /36)
            t.el.color(R - count, t.rand_num, count)
            t.el.right(my_angle)
            t.el.circle(count / 3, my_angle, 6)
            t.ce.color(R - count % 255, G - count % 150, B + count % 255 )
            t.ce.fd(count * t.phi)
            t.ce.right(my_angle)
            t.ce.fd(count * t.phi)
            t.ce.pensize(count / 27)
            t.ce.color(R - count % 255, t.rand_num, t.rand_pick)
            # # count += 1
            # count_it()
            f.save_thumb()
        t.el.penup()
        t.ce.penup()
        t.el.setpos(0,0)
        t.ce.setpos(0,0)
        t.el.pendown()
        t.ce.pendown()
        t.el.speed(0)
        t.ce.speed(0)
        count = 0
        for count in range(758):
            R =  150
            G =  0
            B =  255
            t.el.color(R - count % 145, count, B - count % 255)
            t.el.fd(count * t.phi)
            t.el.left(my_angle)
            t.el.pensize(count /36)
            t.el.color(count, t.rand_num, B - count % 255)
            t.el.right(my_angle)
            t.el.circle(count / 3, my_angle, 6)
            t.ce.color( R - count % 100, B - count % 255, t.rand_pick)
            t.ce.fd(count * t.phi)
            t.ce.right(my_angle)
            t.ce.fd(count * t.phi)
            t.ce.pensize(count / 27)
            t.ce.color(R - count % 150, count % 255, t.rand_pick)
            # # count += 1
            # count_it()
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        Tm.end_time()
    Lg.logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    Lg.logger.info('************************************************************************')
    reset_all()





#module_46
#===========================================================================
#Code for Black Seed of Life
def black_seed():
    Lg.logger.info('##########################################################')
    global my_project, my_angle, my_title, my_mandala_name, str_angles
    my_mandala_name = 'Black Seed Mandala'
    startup_script()
    make_folder()
    t.my_angles, t.my_splash = str_angles, f'{my_project} with {au.my_track}'
    t.set_up_el()
    t.set_up_ce()
    for a.i  in range( len(a.i_angle)):
        Lg.logger.info('===============================================================================')
        my_angle = math.trunc(float(a.i_angle_auto[a.i]))
        Tm.set_time()
        Lg.logger.info(f'Current angle to be drawn is {my_angle} @ {Tm.my_time}')
        t.my_title = f'{my_mandala_name}: {my_angle} Degrees Angle and {au.my_track}'
        turtle.title(t.my_title)
        t.el.speed(30)
        t.el.pensize(36)
        t.ce.speed(30)
        t.ce.pensize(54)
        t.ce.pencolor(255,255,255)
        length = 234
        my_image = 'TBD'
#         my_angle = 135 # 60 is default
        my_base = int(3600/ my_angle) # for loop integrity of the number of loops of the ce pen
        t.el.speed(30)
        t.el.pensize(36)
        t.ce.speed(30)
        t.ce.pensize(54)
        t.ce.pencolor(255,255,255)
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
                t.ce.left(my_angle)
                t.ce.circle(length)
                count = 0
            for count in range(254):
                if x == 0:
                    b = count, count % 18, count % 33
                elif x == 1:
                    b = count % 33, count, count % 18
                else:
                    b = count % 18, count % 33, count
                    t.el.pencolor(b)
#                 Lg.logger.info(f'Base is: {my_base}')
#                 Lg.logger.info(f'count  : {Tm.iterable_time}')
#                 Lg.logger.info(f'Pen color:  {b}')
#                 Lg.logger.info(f'x = {x}')
                t.el.left(my_angle)
                t.el.circle(length)
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
                    t.el.pencolor(b)
#                     Lg.logger.info('count  :' + str(Tm.iterable_time))
#                     Lg.logger.info('Pen color:  ' + str(b))
#                     Lg.logger.info(' x = ' + str(x))
                    t.el.left(my_angle)
                    t.el.circle(length)
                    f.save_thumb()
        t.el.reset()
        t.set_up_el()
        set_el_home()
        t.ce.reset()
        t.set_up_ce()
        set_ce_home()
    stage_reverse_video()
    finalize()
    
'''#  module_47
#+++++++++++MODULE DARK MANDALA EXTENDED+++++++++++++++++++++++++++++++++++++++++++++++++++++
def dark_mandala_extended():  #Work on some more
    global my_project
    my_project = my_project
    my_project = 'A Dark Mandala Extended v.' + Tm.project_time + my_key
    startup_script()
    Lg.logger.info('Located @ line 3711 - 3888,   47th module of 48')
    t.my_venv()
     # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    my_title = str('This Show Features Dark Mandalas Extended with   ' + str(str_angles) + '  ' + 'angles')
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.get_special_5_min_track()
#         au.pick_medium_track()
        make_folder()
        turtle.bgcolor(255, 255,100)
        my_iteration = 255 # 300 is default; use lower number for testing
        t.bg_count = 0
        Lg.logger.info("The pick_dark pen is:  ", t.hue_dict ['pick_dark']  )
        Lg.logger.info("The pick_indigo pen is':   ", t.hue_dict ['pick_indigo']  )
        Lg.logger.info("The pick_magenta pen is':   ", t.hue_dict ['pick_magenta']  )
        t.bg_fade_dark_to_yellow()
        for count in range(my_iteration):  # First Loop of 3
            h.pick_magenta() #pen t.me
            h.pick_dark()  # pen t.lz
            h.pick_indigo() # pen t.li

            t.lz.right(my_angle / 2) # Dark pen
            t.lz.pensize(count / 54)
            t.lz.circle(count / 3, my_angle, 6)
            t.lz.penup()
            t.lz.backward(count / t.phi + count)
            t.lz.pendown()

            t.li.right(my_angle) # Indigo pen
            t.li.pensize(count / 54)
            t.li.backward(count / t.phi)

            t.lz.right(my_angle / 2) # Dark pen
            t.lz.fd(count  / 2)

            t.li.right(my_angle)  # Indigo pen
            t.li.fd(count )

            t.lz.penup()  #Dark pen
            t.lz.right(my_angle)
            t.lz.fd(count/9)
            t.lz.pendown()
            t.lz.fd(count * t.phi)

            t.li.left(my_angle)
            t.li.backward(count / t.phi) # Indigo pen
            t.li.circle(count /3, - my_angle, 9)

            #make dots
            t.me.pensize(count/24) # Magenta pen
            t.me.left(my_angle / 2)
            t.me.dot(count /24)
            t.me.penup()
            t.me.backward(count)
            t.me.pendown()
            t.me.fd(count / 60)

            t.iterate_dark_to_yellow()
            f.save_thumb()
            # count_it_bg()
        Lg.logger.info('The value of Tm.iterable_time is   ' + str(Tm.iterable_time))
        count = 0
        t.bg_count = 0
        t.lb.setpos(0,0)
        t.lg.setpos(0,0)
        t.el.setpos(0,0)
        t.bg_fade_yellow_to_dark()
        while count  <= 255: # Second Loop of 3

            h.pick_blue() #pen t.lb
            h.pick_green()  # pen t.lg
            h.pick_light() # pen t.el

            t.el.right(my_angle / 2) # Light pen
            t.el.pensize(count / 54)
            t.el.circle(count / 3, my_angle, 6)
            t.el.penup()
            t.el.backward(count / t.phi  + count)
            t.el.pendown()

            t.lg.right(my_angle) # Green pen
            t.lg.pensize(count / 54)
            t.lg.backward(count / t.phi)

            t.el.right(my_angle / 2) # Light pen
            t.el.fd(count  / 2)

            t.lg.right(my_angle)  # Green pen
            t.lg.fd(count )

            t.el.penup()  #Light pen
            t.el.right(my_angle)
            t.el.fd(count/9)
            t.el.pendown()
            t.el.fd(count * t.phi)

            t.lg.left(my_angle)
            t.lg.backward(count / t.phi) # Green pen
            t.lg.circle(count /3, - my_angle, 9)
            #make dots
            t.lb.pensize(count/24)   # Blue pen
            t.lb.left(my_angle / 2)
            t.lb.dot(count /24)
            t.lb.penup()
            t.lb.backward(count)
            t.lb.pendown()
            t.lb.fd(count / 60)
            t.iterate_yellow_to_dark()
            f.save_thumb()
            #count_three()
            Lg.logger.info('The value of t.bg_count is ' + str(t.bg_count))
            Lg.logger.info('The value of t.bg_count_2 is ' + str(t.bg_count_2))
            Lg.logger.info('The value of t.bg_count_3 is ' + str(t.bg_count_3))
            Lg.logger.info('The value of count is  ' + str(count))
        Lg.logger.info('The value of Tm.iterable_time is   ' + str(Tm.iterable_time))
        count = 0
        t.bg_count = 0
        t.lz.penup()
        t.lz.setpos(0,0)
        t.lz.pendown()
        t.go.setpos(0,0)
        t.lu.setpos(0,0)
        t.bg_fade_dark_to_yellow()
        while count  <= 255: # Third (Final) Loop

            h.pick_dark() #pen t.lz
            h.pick_gold()  # pen t.au
            h.pick_red() # pen t.lu

            t.lu.right(my_angle / 2) # Red pen
            t.lu.pensize(count / 54)
            t.lu.circle(count / 3, my_angle, 6)
            t.lu.penup()
            t.lu.backward(count / t.phi + count)
            t.lu.pendown()

            t.lz.right(my_angle) # Dark pen
            t.lz.pensize(count / 54)
            t.lz.backward(count / t.phi)

            t.lu.right(my_angle / 2) # Red pen
            t.lu.fd(count  / 2)

            t.lz.right(my_angle)  # Dark pen
            t.lz.fd(count )

            t.lu.penup()  #Red pen
            t.lu.right(my_angle)
            t.lu.fd(count/9)
            t.lu.pendown()
            t.lu.fd(count * t.phi)

            t.lz.left(my_angle)
            t.lz.backward(count / t.phi) # Dark pen
            t.lz.circle(count /3, - my_angle, 9)
            #make dots
            t.go.pensize(count/24)
            t.go.left(my_angle / 2) # Gold pen
            t.go.dot(count /24)
            t.go.penup()
            t.go.backward(count)
            t.go.pendown()
            t.go.fd(count / 60)
            t.iterate_dark_to_yellow()
            Lg.logger.info('The value of t.bg_count is ' + str(t.bg_count))
            Lg.logger.info('The value of t.bg_count_2 is ' + str(t.bg_count_2))
            Lg.logger.info('The value of t.bg_count_3 is ' + str(t.bg_count_3))
            Lg.logger.info('The value of count is  ' + str(count))
            f.save_thumb()
            #count_three()
        Lg.logger.info('The value of Tm.iterable_time is   ' + str(Tm.iterable_time))
        stage_video()
    finalize()
'''



#  module_48
#**************************************************************************************************************
  # First Published to YouTube on 11/21/2021
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def awesome_mandala_old():
    global my_project
    my_project = my_project
    my_project = 'Awesome Mandala v.' + Tm.project_time + my_key
    startup_script()
    Lg.logger.info('Located @ line 3864 - 3920, 48th module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        make_folder()
        turtle.bgcolor(0,0,0)
        Lg.logger.info(str('The featured angle is     ') + str(my_angle))
        R = 0
        G = 0
        B = random.randrange(10, 100, 3)
        L = random.randrange(100, 255, 3)
        M = 255
        N = 110
        X = 10
        Y = 255
        Z = 255
        turtle.bgcolor(10, 255, 255)
        h.pick_gold() #Pen t.au
        t.go.left(my_angle/2)
        t.lm.left(my_angle/2)
        for count in range(354):  # 450 is default, use any number
            h.pick_gold() #Pen au
            if count <= 255:
                turtle.bgcolor(X, Y - count, Z - count)
            else:
                turtle.bgcolor(X, 0, 0)
            t.go.pensize(count/120)
            t.go.left(my_angle)
            t.go.fd(count) # /t.phi
            t.lm.pensize(count / 120)
            t.lm.rt(my_angle)
            if count <= 252:
                t.lm.pencolor(L, M - count, M - count)
            else:
                t.lm.pencolor(L, 3, X)
            t.lm.circle(count, - my_angle, 6)
            f.save_thumb()
            Lg.logger.info('The Value of color B is    ' + str(B))
            Lg.logger.info('The Value of color L is    ' + str(L))
        stage_video()
    finalize()

#  module_49
#***************************
   
#nomega
''''''***************************************************************************************************************************************'
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
# awesome_mandala() # Needs overhaul!
# colorful_mandala_extended() # Tested and verified on 1/3/2023; 'Located @ line 260 - 385,  3rd module of 48', created on 11/6/2022
# glorious_mandala_extended()  #Created 11/13/2022 Located @ line 2990- 3111, 32nd module of 48.  # Output duration is 6 minutes; last ran on 5/19/2023; created number box for single angle selection
# awesome_mandala_extended() # Completed major update of format to start with angle selection to prevent faulty looping, by prioritizing angle selection.
# joyous_mandala() # Runs for 12 minutes
# stupendous_mandala() # module_21 Reworked and tested 1/16/2023. First to use the t.fade function, extends the loop count beyond the 255 limit imposed by RGB. Row 1652 - 1101, number 17 of 48.
    #Derived from pretty_awesome_mandala. Created 1/8/2022. added print to file 3/1/2022Features a more prominent center than it's parent.  Works well.
# courage_mandala() # module_22 #Tested and verified on 1/12/2023; Located @ line 1937 -2546, 24th module of 48' 4 of 48, Published to YouTube on 11/2/2021
# brave_mandala_extended() #Completed major update of format to start with angle selection to prevent faulty looping, by prioritizing angle selection.Located @ line 1645 -1736, 20th module of 48
# bold_mandala()  # module_9 Modified, tested and verified on 1/8/2023; Located @ line 713 - 782, 9th module of 48', Updated to automate video creation  Implemented 'phi Offset' Angle on 4/28/2022.
# sirius_mandala() # module_33  Located @2335 - 2408. Developed June 2022, Added 6/28/2022. 33rd module of 48. Makes beautiful diagrams.
# reversing_awesome_mandala()  # last run on 7/25/2023
# Plain_mandala() last run on 9/6/2023

# dark_mandala() #module_7 Tested and verified 1/4/2023;  Revised 7/30/2023
# pretty_awesome_mandala() # module_19; Tested and verified 1/10/2023; Located @ line 1331- 1380, 18th module of 48. Derived from awesome_mandala. # Processed 90 degrees to MP4 on 12/15/2021

# Fantastic_Mandala() Implemented many upgrades, ran multiple times 8/8 - 8/13 2023 and loaded to YouTube
# glorious_mandala() # module_18 Tested and verified 1/10/2023; Created 4/6/2022, based on stupendous mandala. Located @ line 3153- 3219, 41st module of 48. 2 minute duration video.
# breathing_yin_yang()
'Run Date: 09/11 - 9/12/2023'
# ribbons_mandala()  #(Edited from Mandala_160_09292020); converted to mult-angles on 1/20/2022; updated and run on 9/6/2023
'Run date: 09/18/2023 - 9/22/2023'
# mighty_awesome_mandala() # Ran with many improvements 9/22/2023; Tested and verified 01/11/2023; Loaded to YouTube channel; Based on pretty awesome mandala
'Run Date: 9/22/23 - 9/26/2023'
# hued_gradiant_mandala()  #module_9 Row 647 - 733, 9 of 48
'Run Date: 09/26/2023 - '
brave_mandala() #module_19 Located @ line 1386 -1449, Derived from awesome_mandala; 18 of 48




# black_seed()   # module_35 Needs more work

# cloverleaf() # module_33 31 of 48, Located at line  2247 - 2304. Created 3/6/2022.


# Work on cloverleaf_extended()


'======================================================================================================================================================='


#

# # awesome_mandala_old()

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
# hued_polygonial() # module_5; Tested and verified 1/4/2023; Rows 465 - 515,   5th module of 48. Features Blue and Red Hues. Modified 12/17/2021 Updated to automate video creation#


# iridescent_polygram()  # module_8; Tested and verified 1/4/2023; Row 645 - 723, 8 of 48; Modified 1/2/2022 Updated to automate video creation

# animated_abstraction()  #  module_9 10 of 48, Thumbs created 11/21/2021
# animated_hued_polygram()  # module_13  Located @ line 929 - 989, number 13 of 48, created 11/14/2021; added print to file 3/1/2022
# awesome_mandala()  #  Tested and verified on 1/7/2023. module_15 15 of 48, Located at lines 2052 - 2109. Processed to mp4 and published to YouTube on 11/21/2021. modified 11/20/2021, This is exceptional.
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
# Lg.logger.info('All files have been moved to their final home')
# f.sync_mandala_folders()  # Sync video and script folders backups
# Lg.logger.info('Folders and files have been synced and backed up')
# logger.warning('Program is terminating')
# turtle.bye()  # End the program;  Default is to leave uncommentedpip