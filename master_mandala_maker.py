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
    Memory: 32 GB RAM; OEM integrated Mesa Intel HD Graphics 4600; In May 2023,
    upgraded to PowerColor AMD Radeon RX 550 Red Dragon Low Profile Single Fan 4GB GDDR5 PCIe 3.0 Graphics Card

    Modules are imported either from the standard python package or from PyPy through Thonny packages management, and include
    the following: Turtle, MoviePy, PyAutogui, PyDub, NatSort, Numpy, Random, OpenCV, DateTime, TimeIt, OS,  Sys, Logging,  gc, 
    DirSync, Pillow, Shutil, PathLib, Glob, Imagio, Functools, Math, Mutagen.
    
    All screenshot apps, including PyautoGui and Pyscreenshot running on Linux need Scrot, which is installed
    from the 'apt' repository (Ubuntu). To run, Scrot requires support from the desktop manager. Wayland, which
    Ubuntu adopted in 2019, has no support for Scrot. Only the legacy X11 desktop display manager used by Linux Mint
    continues to provide functionality for Scrot.
    
    In addition to the above-listed imported modules from Pypy,
    the the author has developed and is actively maintaining the following custom Python modules:
        1. master_mandala_maker.py; primary module, initiates and runs code for the animations.
        2. my_angles.py; processes angle selections
        3. my_hues.py; selects custom color hues
        4. my_splash_screen.py; starts the show; ends the show
        5  File_scripts.py; repository for file manipulations, creations, deletions, sorting, video processing
        6. audio_clips.py; repository of links to audio tracks on the local server and filters audio clips by duration
        7. Timer.py; provides time/date functionality
        8. _A ColorHueTester.py; the only independent module. It outputs a given hue, based on RGB color hue format.
            Screenshot of image is saved to a file.
        9. My_logger.py; provides both file and streaming logger functionality, and replaces more limited print() function.    

        Maintained at Git Repository (Currently Private).
        Link: https://github.com/elemenel/mandala-py
'''
import turtle
import time
import sys
import os
from timeit import default_timer as timer
import random
import pyautogui # For screenshot
import numpy as np # Processes the video
import cv2 # For screenshots
from select import select
from datetime import datetime
import My_template as t
import my_angles as a  #Processes angle selections
import my_hues as h # Defines turtle pen names; Aids in color selections
import my_splash_screen as s
import Timer as Tm
import FileScripts as f  # Processes file manipulations
import audio_clips as au # Processes the audio tracks
import logging
import My_logger as Lg
import subprocess as sp


if sys.platform.startswith('linux'):
    my_path = '/home/champ/Mandala Maker/Modules/'
else:
    my_path = 'D:/'

turtle.setup(1950, 1070)  # This is the default screen size. Choose any size.
turtle.title('The Novonno Healing Mandalas by LeonRHatton') # Placeholder. Is unique to each mandala maker
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
logger.info('Logger Source: MandalaMaker')

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
    
    
# Set up Logger
def startup_script():
    global module_start_time
    module_start_time = Tm.datetime.datetime.now()
    t.my_venv()
#     start = str(Tm.datetime.datetime.fromtimestamp(datetime))
#     end = str(Tm.datetime.datetime.fromtimestamp(datetime))
    my_logfile = f.my_work_dir + '/Logs/' + my_project  +  '.log'
    logger.info('Starting  ' + my_project + ' @  ' + str( Tm.start_time()))
    logger.info('This is ' + my_project + ' code')
    
    
def select_angle():
    global my_angle
    default_angle = 1211
    my_angle = turtle.numinput('Input Angle:', 'Angle, ', 144)
    if my_angle in range(-24, 24, 1):
        my_angle = default_angle
    return my_angle

# Creates working folders and declares variables; gets things rolling
def make_folder():
    logger.info('Setting up directories and files for video production  @  '+ Tm.my_time)
    au.pick_custom_length_track()
    t.my_str = my_project + ' featuring ' + str(au.my_track) 
    s.splash_screen()
    folder_name = my_project
    t.folder_name = folder_name
    logger.info('Folder name is   ' + str(t.folder_name))
    f.make_png_folder()
#     os.chdir(f.loc_thumb + folder_name)
    turtle.title(t.my_str)
    logger.info('Presenting  ' + t.my_str)
    s.watermark()

# Starts video creation process
def stage_video():
    f.save_final_thumb()
    turtle.bye()
    logger.info(' Starting video creation @ ' + Tm.my_time + '.........')
    f.set_vid_env()
    logger.info('Starting merger of video and audio clips @  ' + Tm.my_time + '..........')
    f.sync_av()
    logger.info('Making of mandala completed @  ' + Tm.my_time)
    logger.info('Stopping  ' + t.my_str + ' by Leon Hatton on  ' + Tm.my_time)
    logger.info('****************************************************************************')
    
def stage_reverse_video():
    f.save_final_thumb()
    reset_all()
    turtle.bye()
    logger.info(' Starting video creation @ ' + Tm.my_time + '.........')
    f.set_reverse_vid_env()
    logger.info('Starting merger of video and audio clips @  ' + Tm.my_time + '..........')
    f.sync_av()
    logger.info('Making of mandala completed @  ' + Tm.my_time)
    logger.info('Stopping  ' + t.my_str + ' by Leon Hatton on  ' + Tm.my_time)
    logger.info('****************************************************************************')


# Shuts down module processing and closes Turtle
def finalize():
    global module_end_time
    module_end_time = Tm.datetime.datetime.now()
    difference = module_end_time - module_start_time
    elapsed_time = difference.total_seconds() /3600
    logger.info('Module Run Time: ' + str(elapsed_time) + ' Hours')
    logger.info('************************************************************************')
    logger.info('Stopping  ' + my_project + ' by Leon Hatton on  ' +'@ ' + str( Tm.end_time()))
    logger.info('Finalizing scripts to sync all files and folders')
    logger.info('Moving files to appropriate folders')
    f.move_all() # Moves files to appropriate locations
    logger.info('Video .mp4 files have been moved to /Videos/')
    logger.info('Image .png files have been moved to /Thumbs/')
    logger.info('Image .jpg files have been moved to /Pictures/Mandala Final Thumbs/')
    logger.info('Pics have been moved to Pictures folder')
    logger.info('================================================================================')
    f.sync_mandala_folders()  # Sync video and script folders backups
    logger.info('Folders and files have been synced and backed up')
    logger.warning('Shutting down this module and resetting logger')
    logger.info('MandalaMaker Program shutting down @  ' + str(Tm.end_time()))
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
    t.ld.reset()
    t.go.reset()
    t.lg.reset()
    t.lb.reset()
    t.lc.reset()
    t.lm.reset()
    t.ll.reset()
    t.me.reset()
    t.lz.reset()
    t.ly.reset()
    turtle.reset()
#     logger.info('Pausing 9 seconds for user option to permanently manually stop the program at  end of sub-routine  before the next one starts.................')
    logger.info('All instances of turtle have been reset')
    time.sleep(3)




def all_pens_home():
    # Random Pen
    t.ce.penup()
    t.ce.setpos(0,0)  #1
    t.ce.seth(0)
    t.ce.hideturtle()
    t.ce.pendown()
    # Light Pen
    t.el.penup()
    t.el.setpos(0,0)  #2
    t.el.seth(0)
    t.el.hideturtle()
    t.el.pendown()
    #Gold Pen
    t.go.penup()
    t.go.setpos(0,0)  #3
    t.go.seth(0)
    t.go.hideturtle()
    t.go.pendown()
    # Blue Pen
    t.lb.penup()
    t.lb.setpos(0,0)  #4
    t.lb.seth(0)
    t.lb.hideturtle()
    t.lb.pendown()
    # Pen
    t.lc.penup()
    t.lc.setpos(0,0)  #5
    t.lc.seth(0)
    t.lc.hideturtle()
    t.lc.pendown()
    # Dot Pen
    t.ld.penup()
    t.ld.setpos(0,0)  #6
    t.ld.seth(0)
    t.ld.hideturtle()
    t.ld.pendown()
    #Green Pen
    t.lg.penup()
    t.lg.setpos(0,0)  #7
    t.lg.seth(0)
    t.lg.hideturtle()
    t.lg.pendown()
    # Indigo Pen
    t.li.penup()
    t.li.setpos(0,0)  #8
    t.li.seth(0)
    t.li.hideturtle()
    t.li.pendown()
    # Pen
    t.ll.penup()
    t.ll.setpos(0,0)  #9
    t.ll.seth(0)
    t.ll.hideturtle()
    t.ll.pendown()
    # Pen
    t.lm.penup()
    t.lm.setpos(0,0)  #10
    t.lm.seth(0)
    t.lm.hideturtle()
    t.lm.pendown()
    # Orange Pen
    t.lq.penup()
    t.lq.setpos(0,0)  #11
    t.lq.seth(0)
    t.lq.hideturtle()
    t.lq.pendown()
    # Random_a Pen
    t.lr.penup()
    t.lr.setpos(0,0)  #12
    t.lr.seth(0)
    t.lr.hideturtle()
    t.lr.pendown()
    #  Red Pen
    t.lu.penup()
    t.lu.setpos(0,0)  #13
    t.lu.seth(0)
    t.lu.hideturtle()
    t.lu.pendown()
    # Yellow Pen
    t.ly.penup()
    t.ly.setpos(0,0)  #14
    t.ly.seth(0)
    t.ly.hideturtle()
    t.ly.pendown()
    # Dark Pen
    t.lz.penup()
    t.lz.setpos(0,0)  #15
    t.lz.seth(0)
    t.lz.hideturtle()
    t.lz.pendown()
    #Magenta Pen
    t.me.penup()
    t.me.setpos(0,0)  #16
    t.me.seth(0)
    t.me.hideturtle()
    t.me.pendown()
    
  
    

# Using zip function to bind angle and audio file variables for parallel processing


def colorful_mandala_script():
    loc_pen.pensize(count / 103)
    loc_pen_a.pensize(count / 103)
    loc_pen.left(my_angle)
    loc_pen.forward(count / phi)
    loc_pen_a.forward(count)
    loc_pen_a.right(my_angle / 2)
    loc_pen_a.forward(count / pi)
    loc_pen_a.right(my_angle)
    loc_pen_a.forward(count / pi)
    loc_pen.left(my_angle)
    loc_pen.circle(count / phi, - my_angle, 3)
    loc_pen.forward(count / pi)
    
def colorful_mandala_wheels():
    loc_pen.speed(0)
    loc_pen_a.speed(0)
    loc_pen.pensize(count / 103)
    loc_pen_a.pensize(count / 103)
    loc_pen.circle(count / 1, my_angle)
    loc_pen_a.circle(count / 2, - my_angle)

           


global length
length = 255  #Default is 255; any lower number for testing

# Index of modules:

#Group A : Yin-Yang Series (Three Modules)

#  Group A module_1
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Basic Yin-Yang outputs to 10 minute duration when default settings are applied. Runtime over three days!
# Can re-use the thumbnail pgn output and the no_video poutput to create new videos
def basic_yin_yang(): # **
    global my_project
    global my_angle
    my_angle = 180
    my_project = 'Animated Yin-Yang v.'  + Tm.project_time + my_key 
    startup_script()
    au.pick_medium_track()
    make_folder()
    logger.info('Located @ line 377 - 415; 1st module of 48')
    au.pick_medium_track()
    count = 0
    t.el.hideturtle()
    turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
    for count  in range (5): # Default is 5
        for count in range(1800):  # 1800 is default, duration 10 minutes. Use lower number for testing. The higher the number, the longer the show.
            t.el.pensize(10)
            t.el.color(0,0,0) # 0,0,0 is default (Black)
            t.el.rt(-my_angle + t.phi)
            t.el.circle(250)
            f.save_thumb()
            t.el.pensize(10)
            t.el.color(255,255,255) # 255,255,255 is default (White)
            t.el.rt(-my_angle)
            t.el.circle(250)
            f.save_thumb()
            
        count = 0
        for count in range (1800): # Default is 1800
            t.el.pensize(10)
            t.el.color(0,0,0) # 0,0,0 is default (Black)
            t.el.left(-my_angle + t.phi)
            t.el.circle(250)
            f.save_thumb()
            t.el.color(255,255,255) # 255,255,255 is default (White)
            t.el.left(-my_angle)
            t.el.circle(250)
            f.save_thumb()
    stage_video()
    finalize()


#  Group A module_2
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
def basic_yin_yang_extended(): # **
    global my_project
    my_project = 'Animated Yin-Yang Extended v.'  + Tm.project_time + my_key
    startup_script()
    logger.info('Starting Animated Yin-Yang Extended module  by Leon Hatton on   ' + str(Tm.my_time))
    logger.info('Located @ line 311 - 445;  2nd module of 50')
    my_angle = 180
    au.get_special_track()
    t.my_str = my_project + '   featuring   the Basic Yin-Yang Animated Mandala with   '  + au.my_track
    turtle.title(t.my_str)
    folder_name = my_project + my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + folder_name)
    count = 0
    my_count =  600
    t.el.hideturtle()
    turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
    for count in range(my_count ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        t.el.pensize(10)
        t.el.color(0,0,0) # 0,0,0 is default (Black)
        t.el.rt(-my_angle + phi)
        t.el.circle(250)
        t.el.pensize(10)
        t.el.color(255, 255, 255) # 255,255,255 is default (White)
        t.el.rt(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        logger.info('The value of count is  '+ str(count))
        logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(0, 0, 0)
    count = 0
    for count in range (my_count):
        t.el.pensize(10)
        t.el.color(255,255,255) # 0,0,0 is default (Black)
        t.el.left(-my_angle + phi)
        t.el.circle(250)
        t.el.color(50,255,50) # 255,255,255 is default (White)
        t.el.left(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        logger.info('The value of count is  '+ str(count))
        logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(255,255,255)    
    for count in range(my_count ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        t.el.pensize(10)
        t.el.color(0,0,0) # 0,0,0 is default (Black)
        t.el.rt(-my_angle + phi)
        t.el.circle(250)
        t.el.pensize(10)
        t.el.color(255,50,125) # 255,255,255 is default (White)
        t.el.rt(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        logger.info('The value of count is  '+ str(count))
        logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(252, 148, 10)
    count = 0
    for count in range (my_count):
        turtle.bgcolor(252 - count % 200, 148 + count% 100, 10)
        t.el.pensize(10)
        t.el.color(125,125,125) # 0,0,0 is default (Black)
        t.el.left(-my_angle + phi)
        t.el.circle(250)
        t.el.color(150,150,255) # 255,255,255 is default (White)
        t.el.left(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        logger.info('The value of count is  '+ str(count))
        logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    count = 0
    turtle.bgcolor(125, 125, 125) # Has to be a neutral shade like grey to contrast the black and white theme.
    for count in range(my_count ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
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
        logger.info('The value of count is  '+ str(count))
        logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(0, 0, 0)
    count = 0
    for count in range (my_count):
        t.el.pensize(10)
        t.el.color(255,255,255) # 0,0,0 is default (Black)
        t.el.left(-my_angle + phi)
        t.el.circle(250)
        t.el.color(50,255,50) # 255,255,255 is default (White)
        t.el.left(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        logger.info('The value of count is  '+ str(count))
        logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(255,255,255)    
    for count in range(my_count ):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        t.el.pensize(10)
        t.el.color(0,0,0) # 0,0,0 is default (Black)
        t.el.rt(-my_angle + phi)
        t.el.circle(250)
        t.el.pensize(10)
        t.el.color(255,50,125) # 255,255,255 is default (White)
        t.el.rt(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        logger.info('The value of count is  '+ str(count))
        logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    turtle.bgcolor(252, 148, 10)
    count = 0
    for count in range (my_count):
        turtle.bgcolor(252 - count % 60, 148, 10 + count % 200)
        t.el.pensize(10)
        t.el.color(125,125,125) # 0,0,0 is default (Black)
        t.el.left(-my_angle + phi)
        t.el.circle(250)
        t.el.color(150,150,255) # 255,255,255 is default (White)
        t.el.left(-my_angle)
        t.el.circle(250)
        f.save_thumb()
        logger.info('The value of count is  '+ str(count))
        logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))    
    stage_video()
    finalize()


#  Group A module_3
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
def occilating_yin_yang(): # **
    global my_project
    my_project = my_project
    my_project = 'Occillating Yin-Yang v.'  + Tm.project_time + my_key
    startup_script()
    logger.info('Starting Occillating Yin-Yang module  by Leon Hatton on   ' + str(Tm.my_time))
    logger.info('Located @ line 312 - 363;  2nd module of 49')
    t.my_venv()
    my_angle = 180
    au.get_special_track()
    t.my_str = my_project + '   featuring   the Occillating Yin-Yang Animated Mandala with   '  + au.my_track
    turtle.title(t.my_str)
    folder_name = my_project + my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + folder_name)
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
            logger.info('The value of count is  '+ str(count))
            logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
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
            logger.info('The value of count is  '+ str(count))
            logger.info('The value of Tm.iterable_time is  '+ str(Tm.iterable_time))
    stage_video()
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
    global my_angle
#     logger.info('Selecting angles to run from my_angles.py')
    logger.info('Selecting angle from input box')
    select_angle()  # To run this against more than one angle, comment this
    logger.info('Current angle to be drawn is ' + str(my_angle))
    au.pick_custom_length_track()
    global my_project
    my_project = 'Mystical Mandala by Leon Hatton v.'  + Tm.project_time
    logger.info('Current angle to be drawn is  ' + str(my_angle))
    startup_script()
    logger.info('Located @ line 601- 802, 4th module of 50')
    make_folder()
    R = random.randrange(127, 255, 1)
    G = 0
    B = 255
    logger.info('The value of hue /R/ is   ' + str(R))
    L = random.randrange(10, 150, 1)
    logger.info('The value of hue /L/ is   ' + str(L))
    M = 0
    N = 0
    X = 255
    Y = 255
    Z = 10
    count = 0
    my_length = 5 # Default is 5
    my_pensize = 250 # Default is 150
    my_count = 1250 #Default is 1200
    logger.info('Starting main script at ' + str(Tm.my_time))
    logger.info('Starting first pass....')
    initialize_loc_pen()
#         loc_pen.left(my_angle * 3)
    
    start = Tm.date_time
    for count in range(my_count):
        turtle.bgcolor(0,0,0)
        loc_pen.pensize(count / my_pensize)
        loc_pen.pencolor(count % 255,  B - count % 150, count % 50)
        loc_pen.rt(my_angle)
        loc_pen.circle(count / my_length / t.phi, my_angle)
        f.save_thumb()
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
    end = Tm.date_time
    logger.info('Elapsed Time: ' + str(end - start))        
#             logger.info('Loop count is ' + str(count)) # For testing; comment out for production
#         loc_pen.reset() # Clears screen
    initialize_loc_pen()
    R = random.randrange(1, 150, 1)
    G = 0
    B = 255
    logger.info('The value of hue /R/ is   ' + str(R))
    L = random.randrange(150, 255, 1)
    logger.info('The value of hue /L/ is   ' + str(L))
    M = 0
    N = 0
    X = 255
    Y = 255
    Z = 10
    logger.info('Starting second pass @ ' + str(Tm.my_time))
    count = 0
    for count in range(my_count): # Second pass
        turtle.bgcolor(0,0,0)
        loc_pen.pensize(count / my_pensize)
        loc_pen.pencolor(B - count % 150, count % 50, count % 255)
        loc_pen.rt(my_angle)
        loc_pen.circle(count / my_length / t.phi, my_angle)
        f.save_thumb()
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
    count = 0
#         loc_pen.reset() # Clears screen
    initialize_loc_pen()
    R = random.randrange(10, 255, 1)
    G = 0
    B = 255
    logger.info('The value of hue /R/ is   ' + str(R))
    L = random.randrange(10, 255, 1)
    logger.info('The value of hue /L/ is   ' + str(L))
    logger.info('**************************************')
    logger.info('Starting third pass @ ' + str(Tm.my_time))
    for count in range(my_count + 3): # Third pass
        turtle.bgcolor(0,0,0)
        loc_pen.pensize(count / my_pensize)
        loc_pen.pencolor(count % 50, count % 255,  B - count % 150 )
        loc_pen.rt(my_angle)
        loc_pen.circle(count / my_length / t.phi, my_angle)
        f.save_thumb()
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
    count = 0
    loc_pen.reset()
    initialize_loc_pen()
    R = random.randrange(25, 150, 1)
    G = 0
    B = 255
    logger.info('The value of hue /R/ is   ' + str(R))
    L= random.randrange(10, 255, 1)
    logger.info('The value of hue /L/ is   ' + str(L))
    logger.info('**************************************')
    logger.info('Starting fourth pass @ ' + str(Tm.my_time))
    for count in range(my_count + 4): # Fourth pass
        turtle.bgcolor(0,0,0)
        loc_pen.pensize(count / my_pensize)
        loc_pen.pencolor(R,  B - count % 150, count % 50)
        loc_pen.rt(my_angle)
        loc_pen.circle(count / my_length / t.phi, my_angle)
        f.save_thumb()
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
    count = 0
#         loc_pen.reset() # Clears screen
    initialize_loc_pen()
    R = random.randrange(200, 250, 1)
    G = 0
    B = 255
    logger.info('The value of hue /R/ is   ' + str(R))
    L = random.randrange(10, 255, 1)
    logger.info('The value of hue /L/ is   ' + str(L))
    logger.info('**************************************')
    logger.info('Starting fifth pass @ ' + str(Tm.my_time))
    for count in range(my_count + 5): # Fifth pass
        turtle.bgcolor(0,0,0)
        loc_pen.pensize(count / my_pensize)
        loc_pen.pencolor(count % 255,  L, B - count % 255)
        loc_pen.rt(my_angle)
        loc_pen.circle(count / my_length / t.phi, my_angle)
        f.save_thumb()
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
    count = 0
#         loc_pen.reset() Clears screen
    initialize_loc_pen()
    R = random.randrange(101, 220, 1)
    G = 0
    B = 255
    logger.info('The value of hue /R/ is   ' + str(R))
    L = random.randrange(10, 255, 1)
    logger.info('The value of hue /L/ is   ' + str(L))
    logger.info('**************************************')
    logger.info('Starting sixth pass @ ' + str(Tm.my_time))
    for count in range(my_count + 6): # Sixth pass
        turtle.bgcolor(0,0,0)
        loc_pen.pensize(count / my_pensize)
        loc_pen.pencolor(count % 255,  B - count % 150, R)
        loc_pen.rt(my_angle)
        loc_pen.circle(count / my_length / t.phi, my_angle)
        f.save_thumb()
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
        loc_pen.rt(my_angle)
        loc_pen.forward(count / my_length)
        f.save_thumb()
    loc_pen.reset()
    stage_video()
    finalize()

    

#  Group B Module_5
#+++++++++++MODULE 02, Simple Mandala +++++++++++++++++++++++++++++++++++++++++++++++++++++
#Typical duration is 18 minutes
def simple_mandala():
    global my_angle
    logger.info('Selecting angle from input box')
    select_angle()  # To run this against more than one angle, comment this
    logger.info('Current angle to be drawn is ' + str(my_angle))
    au.pick_custom_length_track()
    global my_project
    my_project = 'A Simple Mandala v.'  + Tm.project_time # + my_key
    startup_script()
    make_folder()
    count = 0
    my_count = 2550 # default is 1800
    my_pensize = 3 # default is 3
    my_length = 5 #default is 2
    logger.info('Starting First Loop @ ' + Tm.my_time)
    start = Tm.date_time
    logger.info('Start time for this loop is ' + str(start))
    t.el.pensize(my_pensize)
    t.lu.pensize(my_pensize)
    turtle.bgcolor(0,0,0)
    for count in range( my_count):
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
        if count == my_count:
            f.save_final_thumb()
    end = Tm.date_time    
    logger.info('End Time for this loop is  ' + str(end))
    logger.info('Elapsed Time:'+ str(end - start))
    count = 0
    all_pens_home()
    logger.info('Starting Second Loop @ ' + Tm.my_time)
    t.ly.pensize(my_pensize)
    t.lq.pensize(my_pensize)
    for count in range(my_count):
        h.pick_yellow()
        h.pick_orange()
        t.ly.rt(my_angle)
        t.ly.fd(count /  my_length)
        f.save_thumb()
        t.lq.rt(-my_angle)
        t.lq.fd(count / my_length )
        f.save_thumb()
        if count == my_count:
            f.save_final_thumb()
    count = 0
    all_pens_home()
    t.el.pensize(my_pensize)
    t.lu.pensize(my_pensize)
    logger.info('Starting Third Loop @ ' + Tm.my_time)
    for count in range(my_count):
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
        if count == my_count:
            f.save_final_thumb()
    count = 0
    all_pens_home()
    t.ly.pensize(my_pensize) # Yellow Pen
    t.lg.pensize(my_pensize) # Green pen
    logger.info('Starting Fourth Loop @ ' + Tm.my_time)
    for count in range(my_count):
        h.pick_green()
        h.pick_yellow()
        t.lg.rt(my_angle)
        t.lg.fd(count / my_length)
        f.save_thumb()
        t.ly.rt(-my_angle)
        t.ly.fd(count / my_length)
        f.save_thumb()
        if count == my_count:
            f.save_final_thumb()
    count = 0
    all_pens_home()
    t.lb.pensize(my_pensize)
    t.go.pensize(my_pensize)
    logger.info('Starting Fifth Loop @ ' + Tm.my_time)
    for count in range(my_count):
        h.pick_blue()
        h.pick_gold()
        t.lb.rt(my_angle)
        t.lb.fd(count / my_length)
        f.save_thumb()
        t.go.rt(-my_angle)
        t.go.fd(count /  my_length)
        f.save_thumb()
        if count == my_count:
            f.save_final_thumb()
    count = 0
    all_pens_home()
    t.el.pensize(my_pensize)
    t.lu.pensize(my_pensize)
    logger.info('Starting Sixth Loop @ ' + Tm.my_time)
    for count in range(my_count):
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
        if count == my_count:
            f.save_final_thumb()
    count = 0
    all_pens_home()
    t.li.pensize(my_pensize)
    t.lr.pensize(my_pensize)
    logger.info('Starting Seventh Loop @ ' + Tm.my_time)
    for count in range( my_count):
        h.pick_indigo()
        h.pick_random_a()
        t.li.rt(my_angle)
        t.li.fd(count / my_length)
        f.save_thumb()
        t.lr.rt(-my_angle)
        t.lr.fd(count /  my_length)
        f.save_thumb()
        if count == my_count:
            f.save_final_thumb()
    count = 0
    all_pens_home()
    t.el.pensize(my_pensize)
    t.lz.pensize(my_pensize)
    logger.info('Starting Eighth Loop @ ' + Tm.my_time)
    for count in range( my_count):
        h.pick_light()
        h.pick_dark()
        t.el.rt(my_angle)
        t.el.fd(count / my_length)
        f.save_thumb()
        t.lz.rt(-my_angle)
        t.lz.fd(count /  my_length)
        f.save_thumb()
        if count == my_count:
            f.save_final_thumb()
    stage_reverse_video() #Comment out if reversal not wanted
#     stage_video() # Comment out if reversal is wanted
    finalize()

# def select_multiple_angles():
#     # Create a set of angles
#     global my_angle
#     select_angles = {972, 1439.984, 526.1538, 135, 1449, 1352}
#     angles_list = [angle for angle in select_angles]
#     for angle in angles_list:
#         my_angle = angle
#         simple_mandala()
# select_multiple_angles()        


#  Group B Module_6
#+++++++++++MODULE Colorful Mandala_Extended+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module has a duration of approximately 5.42 minutes when range and pensize defaults are applied,
# and so will randomly select from the pool of medium clips.
def colorful_mandala_extended():
    global my_angle
    logger.info('Selecting angle from input box')
    select_angle()  # To run this against more than one angle, comment this out
    logger.info('Current angle to be drawn is ' + str(my_angle))
    # select random track from runtime generated list
    au.pick_medium_track() # This script duration is ~5.4 min
    global my_project
    my_project = 'A Colorful Mandala Extended v.' + Tm.project_time # + my_key
    startup_script()
    logger.info('Located @ line 936 - 1064,  6th module of 48')
    logger.info('Ran on:  ' + str(Tm.my_time))
    make_folder()
    count = 0
    turtle.bgcolor(0,0,0)
    my_count = 650 # Default is 650
    my_pensize = 150 # Default is 150
    logger.info('Starting creation of sequential screenshots')
    logger.info('Starting First Loop of 5 @ ' + Tm.my_time)
    for count in range(my_count):
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
        t.go.forward(count / 2)
        f.save_thumb()
        t.go.pensize(count / my_pensize)
        t.go.circle(count / 2, my_angle, 6)
        f.save_thumb()
        t.li.forward(count / 2)
        f.save_thumb()
        t.li.right(my_angle)
        t.li.forward(count)
        t.li.pensize(count / my_pensize)
        f.save_thumb()
        if count == my_count:
            f.save_final_thumb()
#         logger.info('This is loop # ' + str(count) + ' of first pass') # For testing; comment out for production
    # Start second pass
    logger.info('Starting Second Loop of 5 @ ' + Tm.my_time)
    count = 244
    count = 0
    all_pens_home()
    for count in range(my_count):
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
        t.go.forward(count / 2)
        f.save_thumb()
        t.go.circle(count /2, my_angle, 6)
        f.save_thumb()
        t.li.forward(count / 2)
        f.save_thumb()
        t.li.right(my_angle)
        t.li.forward(count)
        f.save_thumb()
        if count == my_count:
            f.save_final_thumb()
    logger.info('Starting Third Loop of 5 @ ' + Tm.my_time)
    count = 0
    all_pens_home()
    for count in range(my_count):
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
        t.go.forward(count / 2)
        f.save_thumb()
        t.go.circle(count / 2, my_angle, 6)
        f.save_thumb()
        t.li.forward(count / 2)
        f.save_thumb()
        t.li.right(my_angle)
        t.li.forward(count)
        f.save_thumb()
        if count == my_count:
            f.save_final_thumb()
    logger.info('Starting Fourth Loop of 5 @ ' + Tm.my_time )
    count = 0
    all_pens_home()
    for count in range(my_count):
        t.go.pensize(count / my_pensize)
        t.li.pensize(count / my_pensize)
        h.pick_gold() # Pen t.go
        h.pick_indigo() # Pen t.li
        t.go.forward(count / 2)
        f.save_thumb()
        t.go.circle(count / 2, my_angle, 6)
        f.save_thumb()
        t.li.forward(count / 2)
        f.save_thumb()
        t.li.right(my_angle)
        t.li.forward(count)
        f.save_thumb()
        if count == my_count:
            f.save_final_thumb()
    logger.info('Starting Fifth Loop of 5 @ ' + Tm.my_time )
    count = 0
    all_pens_home()
    for count in range(my_count):
        t.el.pensize(count / my_pensize)
        t.lz.pensize(count / my_pensize)
        h.pick_dark() # Pen t.lz
        h.pick_light() # Pen t.el
        t.el.forward(count / 2)
        f.save_thumb()
        t.el.circle(count / 2, my_angle, 6)
        f.save_thumb()
        t.lz.forward(count / 2)
        f.save_thumb()
        t.lz.right(my_angle)
        t.lz.forward(count)
        f.save_thumb()
        if count == my_count:
            f.save_final_thumb()
    stage_video()
    finalize()




#  Group B Module_7
#+++++++++++MODULE Glorious Mandala_Extended+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module has a duration of approximately six minutes when range and pensize defaults are applied,
# and so will randomly select from the pool of medium clips, typically 6 minutes or greater.
def glorious_mandala_extended():  # Based on Awesome Manadala
    global my_angle
    logger.info('Selecting Angle from Input Box')
    select_angle()
    logger.info('Current Angle to be drawn is  ' + str(my_angle))
    #Select random track from runtime generated list
    au.pick_medium_track()
    global my_project
    my_project = 'Glorious Mandala Extended v.' + Tm.project_time # + my_key
    startup_script()
    logger.info('Located @ line 1106- 1501, 7th module of 48.')
    logger.info('Run time: ' + str(Tm.my_time))
    make_folder()    
    R = 255
    B = random.randrange(112,155, 1)
    logger.info('The value of hue /B/ is   ' + str(B))
    L = random.randrange(10, 150, 1)
    logger.info('The value of hue /L/ is   ' + str(L))
    E = random.randrange(150, 255, 1)
    logger.info('The value of hue /E/ is   ' + str(L))
    pensize_a = 45
    pensize_b = 120
    count = 0
    my_count = 360  # 360 is default, use lower number for testing.
    turtle.bgcolor(10,40,60)
    # First Pass
    logger.info('Starting creation of sequential screenshots')
    logger.info('Starting First Loop of 8 @ ' + Tm.my_time)
    for count in range (my_count): 
        if count <= 255:
            t.el.pencolor(L, count  %102, count %102)
            t.li.pencolor(B, R-count, count %51)
            t.li.forward(count / 2)
            t.li.left(my_angle) 
            f.save_thumb()
            t.el.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.li.penup()
            t.li.forward(count)
            t.li.left(my_angle)
            t.li.pendown()
            f.save_thumb()
            t.li.forward(count)
            f.save_thumb()
            t.el.forward(count)
            t.el.left(- my_angle)
            t.li.pensize(count/pensize_a)
            t.el.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
        else:
            h.pick_indigo() # Pen li
            h.pick_light() # Pen el
            t.li.forward(count/2)
            t.li.left(my_angle)
            f.save_thumb()
            t.el.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.li.penup()
            t.li.forward(count)
            t.li.left(my_angle)
            t.li.pendown()
            f.save_thumb()
            t.li.forward(count)
            f.save_thumb()
            t.el.forward(count)
            t.el.rt(my_angle)
            t.li.pensize(count/pensize_a)
            t.el.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
#     logger.info('Completing First Loop # ' + str(count) + ' @ ' + Tm.my_time) # For testing only. Default is to leave commented
    # Second Pass
    count = 0
    all_pens_home()
    logger.info('Starting Second Loop of 8 @ ' + Tm.my_time)
    for count in range (my_count): # 360 is default, use lower number for testing.
        if count <= 255:
            t.lg.pencolor(count %102,count %102, L)
            t.go.pencolor(count %51, R - count %102, E)
            t.lg.forward(count/2)
            t.lg.left(my_angle) 
            f.save_thumb()
            t.go.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.lg.penup()
            t.lg.forward(count)
            t.lg.left(my_angle)
            f.save_thumb()
            t.lg.pendown()
            t.lg.forward(count)
            f.save_thumb()
            t.go.forward(count)
            t.go.rt(my_angle)
            t.lg.pensize(count/pensize_a)
            t.go.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
        else:
            h.pick_green() # Pen lg
            h.pick_gold() # Pen go
            t.lg.forward(count/2)
            t.lg.left(my_angle)
            f.save_thumb()
            t.go.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.lg.penup()
            t.lg.forward(count)
            t.lg.left(my_angle)
            f.save_thumb()
            t.lg.pendown()
            t.lg.forward(count)
            f.save_thumb()
            t.go.forward(count)
            t.go.rt(my_angle)
            t.lg.pensize(count/pensize_a)
            t.go.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
    #  Third Pass
    count = 0
    all_pens_home()
    logger.info('Starting Third Loop of 8 @ ' + Tm.my_time)
    for count in range (my_count): 
        if count <= 255:
            t.ly.pencolor(L, count %51, B)
            t.lz.pencolor(B, R-count, count %102)
            t.lz.forward(count/2)
            t.lz.left(my_angle) 
            f.save_thumb()
            t.ly.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.lz.penup()
            t.lz.forward(count)
            t.lz.left(my_angle)
            t.lz.pendown()
            f.save_thumb()
            t.lz.forward(count)
            f.save_thumb()
            t.ly.forward(count)
            t.ly.rt(my_angle)
            t.lz.pensize(count/pensize_a)
            t.ly.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
        else:
            h.pick_dark() # Pen lz
            h.pick_yellow() # Pen ly
            t.lz.forward(count/2)
            t.lz.left(my_angle)
            f.save_thumb()
            t.ly.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.lz.penup()
            t.lz.forward(count)
            t.lz.left(my_angle)
            t.lz.pendown()
            f.save_thumb()
            t.lz.forward(count)
            f.save_thumb()
            t.ly.forward(count)
            t.ly.rt(my_angle)
            t.lz.pensize(count/pensize_a)
            t.ly.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
    # Fourth Pass
    count = 0
    all_pens_home()
    logger.info('Starting Fourth Loop of 8 @ ' + Tm.my_time)
    for count in range (my_count): # 360 is default, use lower number for testing.
        if count <= 255:
            t.lb.pencolor(E, count %51, count %102)
            t.ce.pencolor(count %51, R-count %102, L)
            t.lb.forward(count/2)
            t.lb.left(my_angle) 
            f.save_thumb()
            t.ce.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.lb.penup()
            t.lb.forward(count)
            t.lb.left(my_angle)
            f.save_thumb()
            t.lb.pendown()
            t.lb.forward(count)
            f.save_thumb()
            t.ce.forward(count)
            t.ce.rt(my_angle)
            t.lb.pensize(count/pensize_a)
            t.ce.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
        else:
            h.pick_blue() # Pen lb
            h.pick_random() # Pen ce
            t.lb.forward(count/2)
            t.lb.left(my_angle) 
            f.save_thumb()
            t.ce.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.lb.penup()
            t.lb.forward(count)
            t.lb.left(my_angle)
            f.save_thumb()
            t.lb.pendown()
            t.lb.forward(count)
            f.save_thumb()
            t.ce.forward(count)
            t.ce.rt(my_angle)
            t.lb.pensize(count/pensize_a)
            t.ce.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
    # Fifth Pass        
    logger.info('Starting Fifth Loop of 8 @ ' + Tm.my_time)
    count = 0
    all_pens_home()
    for count in range (my_count): 
        if count <= 255:
            t.me.pencolor(L, count %102, count %51)
            t.lr.pencolor(B, R-count %51, count %204)
            t.lr.forward(count/2)
            t.lr.left(my_angle)
            f.save_thumb()
            t.me.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.lr.penup()
            t.lr.forward(count)
            t.lr.left(my_angle)
            t.lr.pendown()
            f.save_thumb()
            t.lr.forward(count)
            f.save_thumb()
            t.me.forward(count)
            t.me.rt(my_angle)
            t.lr.pensize(count/pensize_a)
            t.me.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
        else:
            h.pick_random_a() # Pen lr
            h.pick_magenta() # Pen me
            t.lr.forward(count/2)
            t.lr.left(my_angle)
            f.save_thumb()
            t.me.circle(count/t.phi,-my_angle) # Light Pen
            f.save_thumb()
            t.lr.penup()
            t.lr.forward(count)
            t.lr.left(my_angle)
            t.lr.pendown()
            f.save_thumb()
            t.lr.forward(count)
            f.save_thumb()
            t.me.forward(count)
            t.me.rt(my_angle)
            t.lr.pensize(count/pensize_a)
            t.me.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
    # Sixth Pass
    count = 0
    all_pens_home()
    logger.info('Starting Sixth Loop of 8 @ ' + Tm.my_time)
    for count in range (my_count): # 360 is default, use lower number for testing.
        if count <= 255:
            t.lu.pencolor(count %102,count %51, L)
            t.lq.pencolor(count %51, R-count %102, E)
            t.lu.forward(count/2)
            t.lu.left(my_angle)
            f.save_thumb()
            t.lq.circle(count/t.phi,-my_angle) # Gold Pen
            f.save_thumb()
            t.lu.penup()
            t.lu.forward(count)
            t.lu.left(my_angle)
            f.save_thumb()
            t.lu.pendown()
            t.lu.forward(count)
            f.save_thumb()
            t.lq.forward(count)
            t.lq.rt(my_angle)
            t.lu.pensize(count/pensize_a)
            t.lq.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
        else:
            h.pick_red() # Pen lu
            h.pick_orange() # Pen lq
            t.lu.forward(count/2)
            t.lu.left(my_angle)
            f.save_thumb()
            t.lq.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.lu.penup()
            t.lu.forward(count)
            t.lu.left(my_angle)
            f.save_thumb()
            t.lu.pendown()
            t.lu.forward(count)
            f.save_thumb()
            t.lq.forward(count)
            t.lq.rt(my_angle)
            t.lu.pensize(count/pensize_a)
            t.lq.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
    # Seventh Pass        
    logger.info('Starting Seventh Loop of 8 @ ' + Tm.my_time)
    all_pens_home()
    count = 0
    for count in range (my_count): 
        if count <= 255:
            t.go.pencolor(L, count %51, count %102)
            t.li.pencolor(R-count %51, E, count %102)
            t.li.forward(count/2)
            t.li.left(my_angle)
            f.save_thumb()
            t.go.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.li.penup()
            t.li.forward(count)
            t.li.left(my_angle)
            t.li.pendown()
            f.save_thumb()
            t.li.forward(count)
            f.save_thumb()
            t.go.forward(count)
            t.go.rt(my_angle)
            t.li.pensize(count/pensize_a)
            t.go.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
        else:
            h.pick_indigo() # Pen li
            h.pick_gold() # Pen go
            t.li.forward(count/2)
            t.li.left(my_angle)
            f.save_thumb()
            t.go.circle(count/t.phi,-my_angle) # Light Pen
            f.save_thumb()
            t.li.penup()
            t.li.forward(count)
            t.li.left(my_angle)
            t.li.pendown()
            f.save_thumb()
            t.li.forward(count)
            f.save_thumb()
            t.go.forward(count)
            t.go.rt(my_angle)
            t.li.pensize(count/pensize_a)
            t.go.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
    # Eighth Pass
    count = 0
    all_pens_home()
    logger.info('Starting Eigth Loop of 8 @ ' + Tm.my_time)
    for count in range (my_count): # 360 is default, use lower number for testing.
        if count <= 255:
            t.el.pencolor(count %102,count %51, L)
            t.lz.pencolor(count %51, R-count %51, B)
            t.el.forward(count/2)
            t.el.left(my_angle)
            f.save_thumb()
            t.lz.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.el.penup()
            t.el.forward(count)
            t.el.left(my_angle)
            f.save_thumb()
            t.el.pendown()
            t.el.forward(count)
            f.save_thumb()
            t.lz.forward(count)
            t.lz.rt(my_angle)
            t.el.pensize(count/pensize_a)
            t.lz.pensize(count/pensize_b)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
        else:
            h.pick_light() # Pen el
            h.pick_dark() # Pen lz
            t.el.forward(count/2)
            t.el.left(my_angle)
            f.save_thumb()
            t.lz.circle(count/t.phi,-my_angle) 
            f.save_thumb()
            t.el.penup()
            t.el.forward(count)
            t.el.left(my_angle)
            f.save_thumb()
            t.el.pendown()
            t.el.forward(count)
            f.save_thumb()
            t.lz.forward(count)
            t.lz.rt(my_angle)
            t.el.pensize(count/pensize_a)
            t.lz.pensize(count/pensize_b)
            f.save_thumb()            
    stage_video()
    finalize()
    
    
    
    
#  Group B Module_9
#+++++++++++MODULE Bold Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''This project can select and run a sequence of angles as a single video. It will select and retain a single audio track
for the duration of the video track.'''    
def reversing_simple_mandala():
    global my_angle
    global my_title
    a.pick_angles()
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    global my_project
    my_project = 'A Reversing Simple Mandala v.'+ Tm.project_time
    my_title = my_project + ' with ' + str(str_angles) + ' angles'
    startup_script()
    make_folder()
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        my_angle = a.i_angle_auto[a.i]
        logger.info('Current angle to be drawn is ' + str(my_angle))
#         au.pick_custom_length_track()
        turtle.title('A Reversing Simple Mandala: ' + str(my_angle) + '  Angle ' + ' and  ' + str(au.my_track))
#         logger.info('Selecting angle from input box')
#         logger.info('Current angle to be drawn is ' + str(my_angle))
        count = 0
        my_count = 1785 # default is 1785
        my_pensize = 3 # default is 3
        my_length = 2 #default is 2
        logger.info('Starting First Loop @ ' + Tm.my_time)
        start = Tm.date_time
        logger.info('Start time for this loop is ' + str(start))
        t.me.pensize(my_pensize)
        t.lq.pensize(my_pensize)
        turtle.bgcolor(0,0,0)
        for count in range(my_count):
            h.pick_red()  # Pen t.lu
            h.pick_light() # Pen t.el
            t.lu.rt(my_angle)
            t.lu.fd(count /  my_length)
            f.save_thumb()
            t.el.rt(-my_angle)
            t.el.fd(count / my_length )
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
        count = 0
        all_pens_home()
        t.lg.pensize(my_pensize) # Yellow Pen
        t.ly.pensize(my_pensize) # Green pen
        logger.info('Starting Second Loop @ ' + Tm.my_time)
        for count in range(my_count):
            h.pick_green() #Pen t.lg
            h.pick_yellow() # Pen t.ly
            t.lg.rt(my_angle)
            t.lg.fd(count / my_length)
            f.save_thumb()
            t.ly.rt(-my_angle)
            t.ly.fd(count / my_length)
            f.save_thumb()
            if count == my_count:
                f.save_final_thumb()
#         count = 0
#         all_pens_home()
#         t.lb.pensize(my_pensize)
#         t.go.pensize(my_pensize)
#         logger.info('Starting Third Loop @ ' + Tm.my_time)
#         for count in range(my_count):
#             h.pick_blue() #Pen t.lb
#             h.pick_gold()  # Pent.go
#             t.lb.rt(my_angle)
#             t.lb.fd(count / my_length)
#             f.save_thumb()
#             t.go.rt(-my_angle)
#             t.go.fd(count /  my_length)
#             f.save_thumb()
#             if count == my_count:
#                 f.save_final_thumb()
#         count = 0
#         all_pens_home()
#         t.li.pensize(my_pensize)
#         t.lr.pensize(my_pensize)      
#         logger.info('Starting Fourth Loop @ ' + Tm.my_time)
#         for count in range( my_count):
#             h.pick_indigo() # Pen t.li
#             h.pick_random_a() # Pen t.lr
#             t.li.rt(my_angle)
#             t.li.fd(count / my_length)
#             f.save_thumb()
#             t.lr.rt(-my_angle)
#             t.lr.fd(count /  my_length)
#             f.save_thumb()
#             if count == my_count:
#                 f.save_final_thumb()
#         count = 0
#         all_pens_home()
#         t.el.pensize(my_pensize)
#         t.lz.pensize(my_pensize)
#         logger.info('Starting Fifth Loop @ ' + Tm.my_time)
#         for count in range( my_count):
#             h.pick_light() # Pen t.el
#             h.pick_dark() #  Pen t.lz
#             t.el.rt(my_angle)
#             t.el.fd(count / my_length)
#             f.save_thumb()
#             t.lz.rt(-my_angle)
#             t.lz.fd(count /  my_length)
#             f.save_thumb()
#             if count == my_count:
#                 f.save_final_thumb()
    stage_reverse_video() #Comment out if reversal not wanted
#     stage_video()
    finalize()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#  Group B Module_8
#+++++++++++MODULE Bold Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''This project can select and run a sequence of angles as a single video. It will select and retain a single audio track
for the duration.'''
def bold_mandala():
    global my_angle
#     logger.info('Selecting angle from input box') # To run this against more than one angle, comment this
#     select_angle()  # To run this against more than one angle, comment this
    # Select which set of angles to run
#     a.pick_angles()
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    global my_project
    my_project = 'A Bold Mandala v.'+ Tm.project_time + '  with  ' + '  ' +str(str_angles) + ' angles'
    startup_script()
    make_folder()
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        my_angle = a.i_angle_auto[a.i]
        logger.info('Current angle to be drawn is ' + str(my_angle))
#         au.pick_custom_length_track()
        turtle.title('A Bold Mandala: ' + str(my_angle) + '  Angle ' + ' and  ' + str(au.my_track))
        my_pensize = 30
        turtle.bgcolor(0,0,0)
        my_range = 25
        count = 0
    #     my_count = count
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
            t.go.forward(count)
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
            t.lb.forward(count)
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
            t.ly.forward(count)
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
            t.me.forward(count)
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
            t.lr.forward(count)
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
            t.el.forward(count)
            f.save_thumb()
            turtle.bgcolor(0, 255 - count, 255 - count)
            f.save_thumb()
#     stage_video() # Ends with completed mandala; comment out if reversal is specified
    stage_reverse_video() #Ends with blank screen; commit out if full image is needed at the end
    finalize()

def strong_mandala():
    global my_angle
    logger.info('Selecting angle from input box')
    select_angle()  # To run this against more than one angle, comment this out
    logger.info('Current angle to be drawn is ' + str(my_angle))
#     au.get_special_track()
    au.pick_custom_length_track()
    global my_project
    my_project = 'A Strong Mandala v.'  + Tm.project_time 
    startup_script()
    make_folder()
    my_range = 1275
    count = 0
    for count in range(my_range):
        turtle.bgcolor(25, 10, 10)
        R =  0
        G =  0
        B =  90
        t.el.color(count % 255 , G, B )
        t.el.pensize(2)
        t.el.forward(count / 3 )
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
    logger.info('Angle being drawn is ' + str(my_angle *3))
    for count in range(my_range):
        turtle.bgcolor(25, 10, 10)
        R =  0
        G =  0
        B =  90
        t.el.color(count % 255 , G, B )
        t.el.pensize(2)
        t.el.forward(count / 3 )
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


#  Group B Module_8
#+++++++++++MODULE Awesome Mandala_Extended+++++++++++++++++++++++++++++++++++++++++++++++++++++
# This module has a duration of approximately 18 minutes when range and pensize defaults are applied,
# and so will randomly select from the pool of long clips.
def awesome_mandala_extended():
    global my_angle
    logger.info('Selecting angle from input box')
    select_angle()
    logger.info('Current Angle to be Drawn is ' + str(my_angle))
    #Select random music track from runtime generated list
    au.pick_medium_track()            
    global my_project
    my_project = 'Awesome Mandala Extended v.' + Tm.project_time # + t.my_key
    startup_script()
    logger.info('Located @ line 1083 - 1178, 7th module of 48')
    logger.info('Ran on  ' + str(Tm.my_time))    
    make_folder() # line 168
    turtle.bgcolor(0,0,0)
    R = 0
    G = 0
    B = random.randrange(10, 100, 3)
    L = random.randrange(100, 255, 3)
    logger.info('The Value of color B is    ' + str(B))
    logger.info('The Value of color L is    ' + str(L))
    M = 255
    N = 110
    X = 10
    Y = 255
    Z = 255
    my_pensize = 2500 # Default is 2500
    my_count = 2500 # Default is 2500 for 18 minutes
    forward_count = 5 # Default is 5 
    circ_rad = 12 # Default is 12
    logger.info('My pensize = '+ str(my_pensize)+'; Default is 6000')
    logger.info('Loop Count = '+ str(my_count)+'; Default is 6000')
    logger.info('Forward Count  = '+ str(forward_count)+'; Default is 18')
    logger.info('Circ_rad = ' + str(circ_rad)+'; Default is 45')
    count = 0
    all_pens_home()
    logger.info('Starting First Pass @ ' + Tm.my_time)
    for count in range(my_count):  # First pass
        h.pick_red() #Pen lu
        t.lu.pensize(count / my_pensize)
        t.lu.forward(count / forward_count * t.phi)
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
        f.save_thumb()
#         logger.info('Completed loop # ' + str(count)) # Uncomment for testing purposes only
        if count == my_count:
            logger.info('Completed Loop # '+ str(count) + '  of First Pass @ ' + Tm.my_time)
            f.save_final_thumb()
    all_pens_home()
    count = 0
    logger.info('Starting Second Pass @ ' + Tm.my_time)
    for count in range( my_count):
        h.pick_green() #Pen lg
        turtle.bgcolor(X, 0, 0)
        t.lg.pensize(count / my_pensize)
        t.lg.forward(count / forward_count * t.phi)
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
        if count == my_count:
            logger.info('Completed Loop # '+ str(count) + 'of Second Pass @ ' + Tm.my_time)
            f.save_final_thumb()
    all_pens_home()
    count = 0
    logger.info:('Starting Third Pass @ ' + Tm.my_time)
    for count in range(my_count):  # 3000 is default, use any number Third pass
        h.pick_indigo() #Pen li
        h.pick_gold()  #Pen go
        t.li.pensize(count / my_pensize)
        t.li.rt(my_angle)
        t.li.forward(count / forward_count * t.phi)
        f.save_thumb()
        t.go.pensize(count / my_pensize)
        t.go.rt(my_angle)
        t.go.circle(count / circ_rad, - my_angle, 9)
        f.save_thumb()
        if count == my_count:
            logger.info('Completed Loop # '+ str(count) + 'of Third Pass @ ' + Tm.my_time)
            f.save_final_thumb()
    all_pens_home()
    count = 0
    logger.info:('Starting Fourth Pass @ ' + Tm.my_time)
    for count in range(my_count):  # 3000 is default, use any number Third pass
        h.pick_blue() #Pen lb
        h.pick_random()  #Pen ce
        t.lb.pensize(count / my_pensize)
        t.lb.rt(my_angle)
        t.lb.forward(count / forward_count * t.phi)
        f.save_thumb()
        t.ce.pensize(count / my_pensize)
        t.ce.rt(my_angle)
        t.ce.circle(count / circ_rad, - my_angle, 9)
        f.save_thumb()
        if count == my_count:
            logger.info('Completed Loop # '+ str(count) + 'of Fourth Pass @ ' + Tm.my_time)
            f.save_final_thumb()
    all_pens_home()
    count = 0
    logger.info:('Starting Fifth Pass @ ' + Tm.my_time)
    for count in range(my_count):  # 3000 is default, use any number Third pass
        h.pick_magenta() #Pen me
        h.pick_orange()  #Pen lq
        t.me.pensize(count / my_pensize)
        t.me.rt(my_angle)
        t.me.forward(count / forward_count * t.phi)
        f.save_thumb()
        t.lq.pensize(count / my_pensize)
        t.lq.rt(my_angle)
        t.lq.circle(count / circ_rad, - my_angle, 9)
        f.save_thumb()
        if count == my_count:
            logger.info('Completed Loop # '+ str(count) + 'of Fifth Pass @ ' + Tm.my_time)
            f.save_final_thumb()
    all_pens_home()
    count = 0
    logger.info:('Starting Sixth Pass @ ' + Tm.my_time)
    for count in range(my_count):  # 3000 is default, use any number Third pass
        h.pick_light() #Pen el
        h.pick_random_a()  #Pen lr
        t.el.pensize(count / my_pensize)
        t.el.rt(my_angle)
        t.el.forward(count / forward_count * t.phi)
        f.save_thumb()
        t.lr.pensize(count / my_pensize)
        t.lr.rt(my_angle)
        t.lr.circle(count / circ_rad, - my_angle, 9)
        f.save_thumb()
        if count == my_count:
            logger.info('Completed Loop # '+ str(count) + 'of Sixth Pass @ ' + Tm.my_time)
            f.save_final_thumb()
    stage_video()
    finalize()


#  Group B Module_9
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Uses pens go(gold) and lb(blue); Based on Mystical Mandala
def joyous_mandala():
    global my_angle
    logger.info('Selecting angle from input box')
    select_angle()
    logger.info('Current Angle to be Drawn is ' + str(my_angle))
    #Select music track from runtime generated list
    au.pick_custom_length_track()          
    global my_project
    my_project = 'Joyous Mandala v.' + Tm.project_time # + t.my_key
    startup_script()
    logger.info('Located @ line 1713 - 1792, 7th module of 48')
    logger.info('Ran on  ' + str(Tm.my_time))    
    make_folder() # line 168
    count = 0
    my_length = 5
    logger.info('The value of my_length is: ' + str(my_length))
    my_pensize = 360
    logger.info('The value of my_pensize is: ' +str(my_pensize))
    my_count = 1800
    logger.info('The valu of my_count is: ' + str(my_count))
    logger.info('Starting main script at ' + str(Tm.my_time))
    for my_loops in range(1,3):
        logger.info('Starting first pass of  loop  ' + str(my_loops)  + '@ ' + str(Tm.my_time))
        turtle.bgcolor(0, 0, my_loops * 18)
        all_pens_home()
        for count in range(my_count):
            h.pick_gold()
            t.lb.pencolor(my_loops * 80, my_range - count % 255, count % 255)
            t.go.pensize(count / my_pensize / my_loops)
            t.lb.pensize(count / my_pensize / my_loops)
            t.lb.left(my_angle)
            t.go.rt(my_angle)
            t.lb.forward(count / my_length)
            f.save_thumb()
            t.go.forward(count / my_length)
            f.save_thumb()
            t.lb.left(my_angle / 2)
            t.go.rt(my_angle / 2)
            t.lb.forward(count / my_length / 2)
            f.save_thumb()
            t.go.forward(count / my_length / 2)
            f.save_thumb()
            t.go.circle(count / my_length / t.phi, my_angle)
            f.save_thumb()
            t.lb.circle(count / my_length / t.phi, -my_angle)
            f.save_thumb()
        all_pens_home()
        logger.info('Starting second pass of  loop  ' + str(my_loops)  + '@ ' + str(Tm.my_time))
        count = 0
        turtle.bgcolor(my_loops * 50, my_loops * 45, my_loops * 20)
        for count in range(my_count):
            '''Second pass'''
            if my_loops == 2:
                h.pick_magenta()
                t.go.pencolor(my_loops * 80, my_loops * count % 255, my_range - count % 152)
                t.go.pensize(count / my_pensize / my_loops)
                t.me.pensize(count / my_pensize / my_loops)
                t.me.rt(my_angle)        
                t.go.left(my_angle)
                t.me.forward(count / my_length)
                f.save_thumb()
                t.go.forward(count / my_length)
                f.save_thumb()
                t.me.rt(my_angle / 2)
                t.go.left(my_angle / 2)
                t.me.forward(count / my_length / 2)
                f.save_thumb()
                t.go.forward(count / my_length / 2)
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
                t.lg.forward(count / my_length)
                f.save_thumb()
                t.go.forward(count / my_length)
                f.save_thumb()
                t.lg.rt(my_angle / 2)
                t.go.left(my_angle / 2)
                t.lg.forward(count / my_length / 2)
                f.save_thumb()
                t.go.forward(count / my_length / 2)
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
def stupendous_mandala():
    global my_angle
    logger.info('Selecting Angle from Input Box')
    select_angle()
    logger.info('Current Angle to be Drawn is ' + str(my_angle))
    logger.info('Selecting track from runtime-generated list')
    au.pick_custom_length_track()           
    global my_project
    global log
    my_project = my_project
    my_project = 'Stupendous Mandala v.' + Tm.project_time # + my_key
    startup_script()
    logger.info('Located @ line 1775- 1966, 21st module of 48')
    logger.info('Run Time: ' + str(Tm.my_time))
    make_folder()
    logger.info('The soundtrack being used for this show is:   ' + str(au.my_track))
    turtle.bgcolor(10, 10, 20)
    my_range = 2040 # Make it a multiple of 255 to sync end of cycle to 255 RGB modulo functions            
    count = 0
    all_pens_home() # Brings all pens, whether used or unused in this module, to 0,0 (Home) and setheader to angle.
    my_random = random.randint(150,255) # Varies the pencolor where used
    my_pensize = 200 # Divisor. Greater the number, the shorter the line drawn
    my_pensize_a = 150 # Divisor. Greater the number, the shorter the line drawn
    my_length = 8 # Divisor. Greater the number, the shorter the line drawn
    my_circle = 6 # Divisor. Greater the number, the shorter the line drawn
    my_length_bk = 5 # Divisor. Greater the number, the shorter the line drawn
    for count in range(my_range): # First Pass
        t.lu.pencolor(my_random, 255, count % 150) # Pen t.lu (Pen 1)
        t.me.pencolor(255-count % 255, count % 255, count % 255) #Pen t.me  (Pen 2)
        t.el.pencolor(count % 255, count % 127, my_random - count % 150) #Pen t.el  (Pen 3)
        
        t.lu.pensize(count / my_pensize)
        t.me.pensize(count / my_pensize_a)
        t.el.pensize(count /my_pensize)
       
        t.me.left(my_angle)  # Pen 2
        t.el.circle(count / my_circle, - my_angle, 3)  # Pen 3
        f.save_thumb()    
        t.el.forward(count / my_length)  # Pen 3
        f.save_thumb()
        t.lu.backward(count / my_length_bk)  # Pen 1
        f.save_thumb()
        t.lu.right(my_angle / 2)  # Pen 1
        t.lu.forward(count / my_length)
        f.save_thumb()
        t.me.left(my_angle)  #Pen 2
        t.me.forward(count / my_length)  #Pen 2
        f.save_thumb()
        t.lu.rt(my_angle)  # Pen 1
        t.lu.forward(count / my_length)  # Pen 1
        f.save_thumb()
    all_pens_home()
    count = 0
    for count in range(my_range): # Second Pass
        t.li.pencolor(count % 255, my_random, 255) #Pen t.li (Pen 1)
        t.lg.pencolor(25, count % 255, count % 127) #Pen t.lg (Pen 2)
        t.go.pencolor(count % 127, count % 255, 255 -count % 255) # Pen t.go (Pen 3)

        t.li.pensize(count / my_pensize) # (Pen 1)
        t.lg.pensize(count / my_pensize_a) # (Pen 2)
        t.go.pensize(count / my_pensize) #  (Pen 3)

        t.lg.left(my_angle) #Pen 2
        t.go.circle(count / my_circle, - my_angle, 3) # Pen 3
        f.save_thumb()
        t.go.forward(count / my_length) # Pen 3
        f.save_thumb()
        t.li.backward(count / my_length_bk) # Pen 1
        f.save_thumb()
        t.li.right(my_angle / 2) # Pen 1
        t.li.forward(count / my_length) # Pen 1
        f.save_thumb()
        t.lg.left(my_angle) # Pen 2
        t.lg.forward(count / my_length) # Pen  2
        f.save_thumb()
        t.li.rt(my_angle)   #Pen 1
        t.li.forward(count / my_length) # Pen 1
        f.save_thumb()
    count = 0
    all_pens_home()
    for count in range(my_range): # Third Pass
        t.lu.pencolor(127 - count % 127, 255-count% 255, count % 255) # Pen t.lu (Pen 1)
        t.me.pencolor(count % 255, my_random, 255 - count% 255) #Pen t.me  (Pen 2)
        t.el.pencolor(255- count % 255, count % 255, 255) #Pen t.el  (Pen 3)
        
        t.lu.pensize(count / my_pensize)
        t.me.pensize(count /my_pensize_a)
        t.el.pensize(count / my_pensize)
       
        t.me.left(my_angle)  # Pen 2
        t.el.circle(count / my_circle, - my_angle, 3)  # Pen 3
        f.save_thumb()    
        t.el.forward(count / my_length)  # Pen 3
        f.save_thumb()
        t.lu.backward(count / my_length_bk)  # Pen 1
        f.save_thumb()
        t.lu.right(my_angle / 2)  # Pen 1
        t.lu.forward(count / my_length)
        f.save_thumb()
        t.me.left(my_angle)  #Pen 2
        t.me.forward(count / my_length)  #Pen 2
        f.save_thumb()
        t.lu.rt(my_angle)  # Pen 1
        t.lu.forward(count / my_length)  # Pen 1
        f.save_thumb()
    all_pens_home()
    count = 0
    for count in range(my_range): # Fourth Pass
        h.pick_indigo() #Pen t.li (Pen 1)
        t.lg.pencolor(count % 255, 255 - count % 255, 255 - count % 255) #Pen t.lg (Pen 2)
        t.go.pencolor(count % 127, count % 255, 255 - count % 255) # Pen t.go (Pen 3)

        t.li.pensize(count / my_pensize) # (Pen 1)
        t.lg.pensize(count / my_pensize_a) # (Pen 2)
        t.go.pensize(count / my_pensize) #  (Pen 3)

        t.lg.left(my_angle) #Pen 2
        t.go.circle(count  / my_circle, - my_angle, 3) # Pen 3
        f.save_thumb()
        t.go.forward(count / my_length) # Pen 3
        f.save_thumb()
        t.li.backward(count/ my_length_bk) # Pen 1
        f.save_thumb()
        t.li.right(my_angle / 2) # Pen 1
        t.li.forward(count / my_length) # Pen 1
        f.save_thumb()
        t.lg.left(my_angle) # Pen 2
        t.lg.forward(count / my_length) # Pen  2
        f.save_thumb()
        t.li.rt(my_angle)   #Pen 1
        t.li.forward(count / my_length) # Pen 1
        f.save_thumb()    
    stage_video()
    finalize()




#  Group B Module_11
#**************************************************************************************************************
#This script features pens: el, me, go, ly, ce, lu, lg, and lb.
#They follow separate yet coordinated routes to compose the mandala.
#Duration at 18 minutes for length value of 600.
#+++++++++++MODULE  Courage Mandala+++++++++++++++++++++++++++++++++++++++++++++++++++++
def courage_mandala():
    global my_angle
    logger.info('Selecting Angle from Input Box')
    select_angle()
    logger.info('Current Angle to be Drawn is ' + str(my_angle))
    logger.info('Selecting track from runtime-generated list')
    au.pick_custom_length_track()
    global my_project
    global log
    my_project = 'Courage Mandala v.' + Tm.project_time 
    startup_script()
    logger.info('Located @ line 1938 - 2553, 10th module of 48')
    make_folder()
    logger.info('The soundtrack being used for this show is:   ' + str(au.my_track))
    my_hue = random.randint(5, 100)
    my_hue_a = random.randint(100, 200)
    logger.info('The value of my_hue is' + '   ' + str(my_hue))
    logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
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
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.me.forward( count + t.phi )
        f.save_thumb()
        t.lb.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.me.left( - my_angle)
        t.lb.rt( my_angle)
        t.me.forward(count / fd_03)
        f.save_thumb()
        t.lb.forward(count  / fd_04)
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
        logger.info('The value of my_hue is' + '   ' + str(my_hue))
        logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
        t.el.color( G - count %255 ,  count %255, R )
#         t.me.color( L - count %255, M,  E)
        t.lb.color(F - count %255, E, D + count %255)
        t.el.left(my_angle)
        t.me.left(my_angle)
        t.lb.left( my_angle / t.phi)
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.me.forward( count + t.phi )
        f.save_thumb()
        t.lb.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.me.left( - my_angle)
        t.lb.rt( my_angle)
        t.me.forward(count /fd_03)
        f.save_thumb()
        t.lb.forward(count  / fd_04)
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
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.me.forward( count + t.phi )
        f.save_thumb()
        t.lg.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.me.left( - my_angle)
        t.lg.rt( my_angle)
        t.me.forward(count / fd_03)
        f.save_thumb()
        t.lg.forward(count  / fd_04)
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
#         logger.info('The value of my_hue is' + '   ' + str(my_hue))
#         logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
#         t.el.color( G - count %255 ,  count %255, R )
# #         t.me.color( L - count %255, M,  E)
#         t.lb.color(F - count %255, E, D + count %255)
#         t.el.left(my_angle)
#         t.me.left(my_angle)
#         t.lb.left( my_angle / t.phi)
#         t.el.forward( count / fd_01)
#         f.save_thumb()
#         t.me.forward( count + t.phi )
#         f.save_thumb()
#         t.lb.forward( count / fd_02)
#         f.save_thumb()
#         t.el.rt(my_angle)
#         t.me.left( - my_angle)
#         t.lb.rt( my_angle)
#         t.me.forward(count /fd_03)
#         f.save_thumb()
#         t.lb.forward(count  / fd_04)
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
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.me.forward( count + t.phi )
        f.save_thumb()
        t.go.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.me.left( - my_angle)
        t.go.rt( my_angle)
        t.me.forward(count / fd_03)
        f.save_thumb()
        t.go.forward(count  / fd_04)
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
        logger.info('The value of my_hue is' + '   ' + str(my_hue))
        logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
        t.el.color( G - count %255 ,  count %255, R )
        t.me.color( L - count %255, M,  E)
#         t.ly.color(F - count %255, E, D + count %255)
        t.el.left(my_angle)
        t.me.left(my_angle)
        t.ly.left( my_angle / t.phi)
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.me.forward( count + t.phi )
        f.save_thumb()
        t.ly.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.me.left( - my_angle)
        t.ly.rt( my_angle)
        t.me.forward(count / fd_03)
        f.save_thumb()
        t.ly.forward(count  / fd_04)
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
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.me.forward( count + t.phi )
        f.save_thumb()
        t.lu.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.me.left( - my_angle)
        t.lu.rt( my_angle)
        t.me.forward(count / fd_03)
        f.save_thumb()
        t.lu.forward(count  / fd_04)
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
        logger.info('The value of my_hue is' + '   ' + str(my_hue))
        logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
        t.el.color( G - count %255 ,  count %255, R )
        t.me.color( L - count %255, M,  E)
#         t.lq.color(F - count %255, E, D + count %255)
        t.el.left(my_angle)
        t.me.left(my_angle)
        t.lq.left( my_angle / t.phi)
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.me.forward( count + t.phi )
        f.save_thumb()
        t.lq.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.me.left( - my_angle)
        t.lu.rt( my_angle)
        t.me.forward(count / fd_03)
        f.save_thumb()
        t.lq.forward(count  / fd_04)
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
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.me.forward( count + t.phi )
        f.save_thumb()
        t.lb.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.me.left( - my_angle)
        t.lb.rt( my_angle)
        t.me.forward(count / fd_03)
        f.save_thumb()
        t.lb.forward(count  / fd_04)
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
        logger.info('The value of my_hue is' + '   ' + str(my_hue))
        logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
        t.el.color( G - count %255 ,  count %255, R )
#         t.li.color( L - count %255, M,  E)
        t.lb.color(F - count %255, E, D + count %255)
        t.el.left(my_angle)
        t.li.left(my_angle)
        t.lb.left( my_angle / t.phi)
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.li.forward( count + t.phi )
        f.save_thumb()
        t.lb.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.li.left( - my_angle)
        t.lb.rt( my_angle)
        t.li.forward(count / fd_03)
        f.save_thumb()
        t.lb.forward(count  / fd_04)
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
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.me.forward( count + t.phi )
        f.save_thumb()
        t.lz.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.me.left( - my_angle)
        t.lz.rt( my_angle)
        t.me.forward(count / fd_03)
        f.save_thumb()
        t.lz.forward(count  / fd_04)
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
        logger.info('The value of my_hue is' + '   ' + str(my_hue))
        logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
        t.el.color( G - count %255 ,  count %255, R )
#             t.ce.color( L - count %255, M,  E)
        t.lb.color(F - count %255, E, D + count %255)
        t.el.left(my_angle)
        t.ce.left(my_angle)
        t.lb.left( my_angle / t.phi)
        t.el.forward( count / fd_01)
        f.save_thumb()
        t.ce.forward( count + t.phi )
        f.save_thumb()
        t.lb.forward( count / fd_02)
        f.save_thumb()
        t.el.rt(my_angle)
        t.ce.left( - my_angle)
        t.lb.rt( my_angle)
        t.ce.forward(count / fd_03)
        f.save_thumb()
        t.lb.forward(count  / fd_04)
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
    global my_angle
    logger.info('Selecting Angle from Input Box')
    select_angle()
    logger.info('Current Angle to be Drawn is ' + str(my_angle))
    logger.info('Selecting track from runtime-generated list')
    au.pick_custom_length_track()
    global my_project
    global log
    my_project = 'Brave Mandala v.' + Tm.project_time 
    startup_script()
    logger.info('Located @ line 2592 - 2800, 11th module of 48')
    logger.info('The soundtrack being used for this show is:   ' + str(au.my_track))
    make_folder()
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
        logger.info('The value of color L :   ' + str(L))
        M = 255
        N = 255
        X = 255
        Y = 255
        Z =  random.randrange(175, 255, 10)
        logger.info('The value of color Z :   ' + str(Z))
        my_pensize = 36
        my_count = 500
        t.el.seth(my_angle)
        t.me.seth(my_angle)
        logger.info('Starting 1st Loop...')
        for count in range( my_count):  # First Pass
            t.el.pensize(count / my_pensize)
            t.el.left(my_angle)
            t.el.forward(count / t.phi)
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
        logger.info('Starting 2nd Loop...')
        for count in range( my_count + 3): # Second Pass
            t.el.pensize(count/ my_pensize)
            t.el.left(my_angle)
            t.el.forward(count / t.phi)
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
        logger.info('Starting 3rd Loop...')
        for  count  in range(my_count + 6):  #Third Pass
            t.el.pensize(count /  my_pensize)
            t.el.left(my_angle)
            t.el.forward(count / t.phi)
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
        logger.info('Starting 4th Loop...')
        for count in range( my_count + 12): # Fourth Pass
            t.el.pensize(count / my_pensize)
            t.el.left(my_angle)
            t.el.forward(count / t.phi)
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
        logger.info('Starting 5th Loop...')
        for count in range( my_count + 18): # Fifth Pass
            t.el.pensize(count / my_pensize)
            t.el.left(my_angle)
            t.el.forward(count / t.phi)
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
        logger.info('Starting 6th Loop...')
        for count  in range(my_count + 24):  # Sixth Pass
            t.el.pensize(count / my_pensize)
            t.el.left(my_angle)
            t.el.forward(count / t.phi)
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
        logger.info('Starting 7th Loop...')
        for count  in range(my_count + 30): # Seventh Pass
            h.pick_light() #Pen el
            h.pick_magenta() # Pen me
            t.el.pensize(count / my_pensize)
            t.el.left(my_angle)
            t.el.forward(count / t.phi)
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
    global my_project
    my_project = my_project
    my_project = 'Hued Polygonial v.' + Tm.project_time # + my_key
    startup_script()
    logger.info('Located @ line 541 - 591, 5th module of 48')
    t.my_venv()
     # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    my_title = str('This Show Features Hued Polygonial Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    logger.info(my_title)
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()
        logger.info('The offset angle value is  ' + str(my_angle * (t.pi/2)))
        t.bg_fade_skyblue_to_dark()
        h.pick_gold()
        t.go.rt(my_angle / 2)
        h.pick_blue()
        t.lb.rt(my_angle / 2)
        count = 0
        t.lb.speed(0)
        t.go.speed(0)
        t.bg_count = 0
        for count in range(900):    #255 is default. Use lower number for testing.
            t.bg_fade_skyblue_to_dark()
            t.lb.pensize(count / 200)
            t.go.pensize(count /250)
            h.pick_blue()
            h.pick_gold()
            t.go.left(my_angle / t.phi)
            t.go.fd(count / t.phi)
            t.lb.left(my_angle)
            t.lb.circle(count / 3, my_angle, 3)
            # count_it_bg()
            f.save_thumb()
        stage_video()
    finalize()




#  module_6
#+++++++++++MODULE FANTASTIC MANDALA+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Fantastic_Mandala():  #  On 4/28/2022, assigned an 'Offset Angle' to second turtle pen as the current angle times phi, looks good as a balance.
    global my_project
    my_project = my_project
    my_project = 'Fantastic Mandala v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1467 - 1513,   6th module of 48')
    t.my_venv() # Initializes turtle canvas screen environment
    logger.info('Selecting which angles to run from my_angles.py')
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    my_title = str('Featuring   ' + my_project + '   with  ' +  str(str_angles) + '  ' + 'angles')
    s.title_screen()
    logger.info(my_title)
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()
#         h.pick_light()
        h.pick_gold()
#         h.pick_indigo()
        count = 0
        t.li.speed(0)
        t.go.speed(0)
        t.el.speed(0)
        t.li.seth(my_angle)
        t.el.seth(my_angle)
        t.go.seth(my_angle)
        turtle.bgcolor(0,0,0)
        for count in range(6000):
            t.li.pensize(count / 1000)
            t.li.pencolor(count % 255, 255, 255 - count % 255)
            t.li.forward(count / 20)
            t.li.right(my_angle)
            h.pick_gold()
            t.go.pensize(count / 7200)
            t.go.circle(count / 90, my_angle)
            t.el.pensize(count / 300)
            t.el.right(my_angle)
            t.el.pencolor(0, count % 255, 255)
            t.el.forward(count  / 45)
            f.save_thumb()
            # For testing purposes only; comment out for production run
            logger.info('Ending Loop Count ' + str(count))
        stage_video()
    finalize()




#  module_7
#+++++++++++MODULE DARK MANDALA+++++++++++++++++++++++++++++++++++++++++++++++++++++
def dark_mandala():
    global my_project
    my_project = my_project
    my_project = 'A Dark Mandala v. ' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 614 - 677,   7th module of 48')
    t.my_venv()
     # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    my_title = str('This Show Features Dark Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()

#         logger.info("The pick_random pen is:   ",  t.hue_dict ['pick_random']  )
#         logger.info("The pick_dark pen is:  ", t.hue_dict ['pick_dark']  )
#         logger.info("The pick_indigo pen is':   ", t.hue_dict ['pick_indigo']  )
#         logger.info("The pick_dot pen is':   ", t.hue_dict ['pick_dot']  )
        t.bg_count = 0
        for count in range(500):
            t.lz.pensize(count / 36)
            t.me.pensize(count /84)
            t.li.pensize(count / 24)
            t.bg_fade_dark_to_green()
            if count <= 100:
                t.lz.pencolor(200, 50, 255- count % 50)
                t.me.pencolor(255 - count % 50, 10, 30)
                t.li.pencolor(count % 50, 10, 100)
            else:
                h.pick_magenta() #pen t.me
                h.pick_dark()  # pen t.lz
                h.pick_indigo() # pen t.li
#             t.li.right(my_angle / 2)
#             t.lz.right(my_angle / 2)

            t.lz.circle(count / 9, my_angle, 3)
            t.lz.penup()
            t.lz.right(my_angle)
            t.lz.backward(count )
            t.lz.pendown()

            t.li.forward(count / pi)
            t.lz.right(my_angle / 2)
            t.lz.forward(count / 2)
            t.li.right(my_angle)
            t.li.forward(count / 24 )
#             t.lz.penup()
#             t.lz.right(my_angle)
#
#             t.lz.pendown()
#             t.lz.forward(count / 5)
            t.li.forward(count / t.phi)
            t.li.circle(count / 12, - my_angle)
        #make dots
            t.me.left(my_angle / 2)
            t.me.forward(count / 6)
            t.me.dot(count /100)
            t.me.penup()
            t.me.backward(count / 3)
            t.me.pendown()
            t.me.forward(count / 6)
            t.me.dot(3)

            f.save_thumb()
            # count_it_bg()
        stage_video()
    finalize()




#  module_8
#+++++++++++MODULE 8 - Iridescent Polygram+++++++++++++++++++++++++++++++++++++++++++++++++++++
def iridescent_polygram():  # Uses 2 pens with offset phi angle
    global my_project
    my_project = my_project
    my_project = 'Iridescent Polygram v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 682 -  718,  8th module of 48')
    t.my_venv()
    # Select which set of angles to run;  Favorite angles: 144/5P, 210/12P, 834/TightSpiral,2394/20P,1350/Square
    make_folder()
    for a.i  in range(len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        make_folder()
        turtle.bgcolor(50, 10, 255)
        t.el.right(my_angle /2)
        t.me.right(my_angle / 2)
        while  count in range (0, 255):  #255 is default. Use lower number for testing.
            t.bg_fade_yellow_to_dark()
            t.el.pensize(count / 49)
            t.me.pensize(count / 72)
            t.el.right(my_angle)
            t.el.forward(count + t.phi)
            t.me.left(my_angle * t.phi)  # This is the offset angle
            t.me.pencolor(random.randint(100,200), random.randint(0,75) + count %150,  random.randint(175,255) - count %150)
            t.el.pencolor(random.randint(0,128) + count %126, random.randint(150,255)- count %126, random.randint(100, 200))
            t.el.circle( count - pi, -my_angle, 8)
            t.me.circle(count / pi, my_angle * t.phi) # This is the offset angle
            t.el.pencolor(255,255,random.randint(100, 200))
            t.me.pencolor(255,random.randint(100, 200), 255)
            t.el.dot(count / t.phi / 18)
            t.me.dot(count / t.phi / 9)
            f.save_thumb()
            # count_it_bg()
        stage_video()
    finalize()









'''
#  module_10
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# NEEDS SOME TWEAKING def hued_gradiant():  # Uses 2 pens with offset phi angle
    global my_project
    my_project = my_project
    my_project = 'Hued Gradiant v.' + Tm.project_time + my_key
    log=logging.getLogger()
    startup_script()
    logging.info('Located @ line 778 - 860, 10th module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' +  str(round(my_angle)) + ' and  ' + str(round (my_angle * phi)) +'    Degree Angles,   with   '  + au.my_track
        logging.info('Presenting   ' + t.my_str)
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        logging.info('The offset angle value is  ' + str(my_angle * t.phi))
        turtle.bgcolor(0,0,10)
        t.el.pensize(1)
        t.me.pencolor(200, 99, 102)
        t.el.left(my_angle / 2)
        t.me.left(my_angle / 2)
        for count in range(200):
            turtle.bgcolor(5, 10, 40)
            R =  random.randint(100,200)
            G =  0
            B =  255
            L = 255
            M = random.randint(100,200)
            N = 0
            t.el.pencolor( R , G + count %216, B - count %126 )
            h.pick_magenta()
            t.me.pencolor(L - count % 216, M, N + count %246)
            t.el.forward( count * phi)
            t.me.forward( count + t.phi)
            t.el.left(my_angle)
            t.me.left(my_angle * t.phi)  # This is the offset angle
            t.me.forward(count / 2)
            t.el.forward(count / 3)
            t.el.left(my_angle)
            t.me.left(my_angle * t.phi) # This is the offset angle
            t.el.forward(count / 33)
            t.me.circle(count / t.phi, my_angle * t.phi, 6)
            t.el.pencolor(255, 255, random.randint(100,200))
            t.el.dot(9)
            t.el.right(my_angle)
            t.me.right(my_angle * t.phi) # This is the offset angle
            t.el.forward(count / t.phi)
            t.me.forward(count / t.phi)
            t.el.pencolor(random.randint(100,200), 255, 255)
            t.el.dot(9)
            t.me.dot(9)
            t.me.pensize(count / 12)
            t.el.pensize(count / 24)
            # count_it()
            f.save_thumb()
        time.sleep(1)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
    logging.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logging.info('************************************************************************')
    reset_all()
'''




#  module_11
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def animated_abstraction():
    global my_project
    my_project = my_project
    my_project = 'Animated Abstract v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 862 - 938,   11th module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        make_folder()
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
            t.el.forward(100)
            t.el.circle(9, my_angle, 6)
            count += 2
            f.save_thumb()
        stage_video()
    finalize()





#  module_12
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gradiant_mandala():
    global my_project
    my_project = my_project
    my_project = 'Gradiant Mandala v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 945 - 997, 12th module of 48')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        make_folder()
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
            t.el.forward(count)
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
    global my_project
    my_project = my_project
    my_project = 'Growing Animated Yin-Yang v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 981 - 1018, 13th module of 48')
    t.my_venv()
    Tm.start_time()
    au.pick_medium_track()
    my_angle =180
    t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
    logger.info('Presenting   ' + t.my_str)
    folder_name = my_project + my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + folder_name)
    turtle.title(t.my_str)
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
    global my_project
    my_project = my_project
    my_project = 'Animated Hued Polygram v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1028- 1070, 14th module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
     # s.title_screen()
    Tm.start_time()
    for a.i  in range(len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        make_folder()
        logger.info(str('The featured angle is     ') + str(my_angle))
        t.bg_count = 0
        for count in range(500):
            t.bg_fade_dark_to_green_to_dark()
            h.pick_light()
            t.el.right(my_angle)
            t.el.forward(count / pi)
            h.pick_indigo()
            t.li.left(-my_angle)
            t.li.forward(count / pi)
            t.el.rt(my_angle)
            t.el.backward(count / t.phi)
            h.pick_gold()
            t.go.forward(count  + t.phi)
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




#  module_15
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''# def pretty_polygonial(): # NEEDS WORK
    global my_project
    my_project = my_project
    my_project = 'Pretty Polygonial v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1118 - 1187, 15th module of 48')
    au.pick_medium_track()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    my_title = str('This Show Features Pretty Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            my_angle =  a.i_angle[a.i]
            au.pick_medium_track()
            t.my_str = my_project + ' featuring '+ str(round(my_angle)) + '  Degree Angles'  + my_key  + '-' + au.my_track
            folder_name = my_project + my_key
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            os.chdir(f.loc_thumb + folder_name)
            turtle.title(t.my_str)
            turtle.bgcolor(0,0,0)
            logger.info(str('The featured angle is     ') + str(my_angle))
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
\                f.save_thumb()
                # count_it()
            f.save_final_thumb()
            turtle.setup(5,5)
            f.set_vid_env()
            f.sync_av()
            reset_all()
            t.my_venv()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()

'''




#  module_16
#**************************************************************************************************************
  # First Published to YouTube on 11/21/2021
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def awesome_mandala():
    global my_angle
    logger.info('Selecting Angle from Input Box')
    select_angle()
    logger.info('Current Angle to be drawn is ' + str(my_angle))
    au.pick_medium_track()
    global my_project
    my_project = 'Awesome Mandala v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 2052 - 2109, 16th module of 48')
    make_folder()
    count = 0
    my_count = 6400
    my_pensize = 300
    my_length = 15
    for count in range(12):
        R = 0
        G = 0
        B = random.randrange(1, 127, 1)
        L = random.randrange(127, 255, 1)
        M = 255
        N = 110
        X = 10
        Y = 255
        Z = 255
        x = 5
        h.pick_gold() #Pen go
        logger.info('The Value of color B is    ' + str(B))
        logger.info('The Value of color L is    ' + str(L))
        turtle.bgcolor(0,0,15)
        all_pens_home()
        for count in range(my_count):  # 450 is default, use any number
                h.pick_gold() #Pen la
                t.go.pensize(count/my_pensize)
                awesome_mandala_snippet()
                t.go.left(my_angle)
                t.go.forward(count /my_length)
                f.save_thumb()
                if count <= 1500:
#                       t.me.pencolor(B, M - count % 380, L) Renders blue/green tones
                      t.el.pencolor(M, B, count % 255)
                else:
                    h.pick_light()
                t.go.left(my_angle)
                t.go.forward(count/my_length)
                f.save_thumb()
                t.el.pensize(count/my_pensize)
                t.el.rt(my_angle)
                t.el.circle(count /my_length, - my_angle, 6)
                f.save_thumb()
        all_pens_home()        
        awesome_mandala_snippet_a
        for count in range(my_count):  # 450 is default, use any number
            h.pick_gold() #Pen go
            t.go.pensize(count / my_pensize)
            t.go.left(my_angle)
            t.go.forward(count / my_length) 
            f.save_thumb()
            t.lm.pensize(count /my_pensize)
            t.lm.rt(my_angle)
            t.lm.pencolor(L, B, M - count % 250)
            t.lm.left(my_angle / 2)
            t.lm.circle(count / my_length, - my_angle, 2)
            f.save_thumb()
        stage_video()
        finalize()








#  module_18
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_awesome_mandala():  # Based on Awesome Mandala
    global my_project
    my_project = my_project
    my_project = 'Pretty Awesome Mandala v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1312- 1361, 18th module of 48')
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
        logger.info(str('The featured angle is     ') + str(my_angle))
        R = 0
        G = 255
        B = random.randrange(100, 255, 1)
        logger.info('The value of hue /B/ is   ' + str(B))
        L = random.randrange(1, 100, 1)
        logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        turtle.bgcolor(10, 255, 255)
        t.el.left(my_angle/2)
        t.me.rt(my_angle/2)
        t.bg_count = 0
        for count in range(550):      # 255 is default, use lower number for testing
            t.bg_fade_yellow_to_dark()
            t.el.left(my_angle)
            t.el.pencolor(R + count % 180, B, G - count %120)
            t.el.forward(count /12)
            t.me.rt(my_angle)
            t.me.pencolor(L, M + count % 180, N + count % 75)
            t.me.circle(count / t.phi, - my_angle, 3)
            t.el.pensize(count/ 84)
            t.me.pensize(count / 102)
            t.bg_count += 1
            # count_it()
            f.save_thumb()
        stage_video()
    finalize()




#  module_19
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def mighty_awesome_mandala():  # Based on pretty_awesome Mandala
    global my_project
    my_project = my_project
    my_project = 'Mighty Awesome Mandala v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1366- 1484, 19th module of 48')
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
        logger.info(str('The featured angle is     ') + str(my_angle))
        R = random.randrange(10, 200, 1)
        G = 0
        B = 255
        logger.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(10, 200, 1)
        logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        count = 0
        t.bg_count = 0
        t.el.seth(my_angle / 2)
        t.me.seth(my_angle / 2)
        for count in range(255):
            t.bg_fade_skyblue_to_dark()
            t.el.pencolor(R, G + count, B - count % 100)
            t.el.forward(count)
            t.el.rt(my_angle)
            t.me.pencolor(L, M + count, X - count %255)
            t.me.circle(count + t.phi, - my_angle)
            t.me.rt(my_angle)
            t.el.pensize(count/24)
            t.me.pensize(count / 24)
            # count_it_bg()
            f.save_thumb()
        count = 0
        t.bg_count = 0
        t.el.penup()
        t.me.penup()
        t.el.setpos(0,0)
        t.me.setpos(0,0)
        t.me.left(my_angle * 2)
        t.el.left(- my_angle * 2)
        t.el.pendown()
        t.me.pendown()
        R = random.randrange(1, 150, 1)
        G = 0
        B = 255
        logger.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(175, 255, 1)
        logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        for count in range(510): # Second pass
            t.bg_fade_dark_to_skyblue()
            t.el.pencolor(B - count % 100, count, L)
            t.el.forward(count)
            t.el.rt(my_angle)
            t.me.pencolor(X - count, M + count % 50, R)
            t.me.circle(count + t.phi, - my_angle)
            t.me.rt(my_angle)
            t.el.pensize(count / 24)
            t.me.pensize(count / 24)
            count_three()
            f.save_thumb()
        count = 0
        t.bg_count = 0
        t.el.penup()
        t.me.penup()
        t.el.setpos(0,0)
        t.me.setpos(0,0)
        t.me.left(my_angle * 2)
        t.el.left(- my_angle * 2)
        t.el.pendown()
        t.me.pendown()
        R = random.randrange(100, 200, 1)
        G = 0
        B = 255
        logger.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(10, 200, 1)
        logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        for count in range(765): # Third pass
            t.bg_fade_skyblue_to_dark()
            t.el.pencolor(count % 84, count, R)
            t.el.forward(count)
            t.el.rt(my_angle)
            t.me.pencolor(count % 50, L, R)
            t.me.circle(count + t.phi, - my_angle)
            t.me.rt(my_angle)
            t.el.pensize(count / 24)
            t.me.pensize(count / 24)
            count_three()
            f.save_thumb()
        stage_video()
    finalize()













#  module_22
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def multi_hued_polygram():
    global my_project
    my_project = my_project
    my_project = 'Multi-Hued Polygram v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1742- 1789, 22nd module of 48')
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
        count = 0
        t.el.right(t.my_angle / 2)
        t.el.speed(0)
        t.go.speed(0)
        N =  random.randint(1, 100)
        t.bg_count = 0
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
            t.el.forward(count + t.phi)
            t.go.circle(count + t.phi, t.my_angle, 3)
#             t.el.circle(count * t.phi, -t.my_angle)
            t.el.right(t.my_angle)
            t.el.forward(count * t.phi)
            t.bg_fade_dark_to_green()
            t.bg_count += 1
            # count_it()
            f.save_thumb()
#             gc.collect()
        stage_video()
    finalize()



'''
#module_23
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala(): # Uses pens le, me
    global my_project
    my_project = my_project
    my_project = 'Brave Mandala v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1802 -1851, 23rd module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
#     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(my_angle))
        R = random.randrange(150, 250, 10)
        logger.info('The value of color R :   ' + str(R))
        G = 0
        B = 255
        L = random.randrange(10, 200, 1)
        logger.info('The value of color L :   ' + str(L))
        M = 255
        N = 255
        X = 255
        Y = 255
        Z = 10
        t.loop_count = 764
        t.bg_count = 0
        for count in range(t.loop_count): #255 is default, use lower number for testing
            t.bg_fade_yellow_to_dark()
            if count <= t.loop_count / 2:
                t.el.pencolor(R, G + count % 255, B - count % 255)
                t.el.pensize(count/168)
                t.el.forward(count)
                t.el.left(my_angle)
                t.me.pensize(count /168)
                t.me.pencolor(R, Y - count % 255, L)
                t.me.circle(count, my_angle, 3)
                t.el.rt(my_angle)
                t.el.pencolor(L, M - count % 255, N - count % 255)
                t.el.circle(count * 1.26, - my_angle, 2)
                t.me.backward(count / 18)
                t.iterate_yellow_to_dark()
                # count_it_bg()
                f.save_thumb()
            else:




     stage_video()
    finalize()
'''




            
            
            
            
            
            
            
   




#module_24
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala_decimated():
    global my_project
    my_project = my_project
    x = 3
    my_project = 'Angle-Fractioned Brave Mandala v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 2068 -2194, 24th module of 48')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_long_track()
        make_folder()
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(my_angle) + ',' + '  fractional =  ' + str(x) + ',' + '  fractional angle = ' + str(my_angle/x))
        R = random.randrange(175, 255, 10)
        logger.info('The value of color R :   ' + str(R))
        G = 0
        B = 255
        L = random.randrange(10, 200, 1)
        logger.info('The value of color L :   ' + str(L))
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
            t.el.forward(count)
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
            t.el.forward(count)
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
            logger.info('The value of Tm.iterable_time is ' + str(Tm.iterable_time))
            logger.info('The value of count is  ' + str(count))
            t.el.pensize(count/56)
            t.el.left(my_angle/x)
            t.el.forward(count)
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
        stage_video()
    finalize()




#module_25
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def color_shifting_mandala():
    global my_project
    my_project = my_project
    my_project = 'Color Shifting Animation v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1498 - 1563, 25th module of 48')
#     Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        make_folder()
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(my_angle))
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
        stage_video()
    finalize()





#module_26
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gold_red_mandala():
    global my_project
    my_project = my_project
    my_project = 'Gold-Red Animation' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1801 - 1852, 26th module of 48')
#
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(my_angle))
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
            t.el.forward(count/2)
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
            #  #
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#module_27
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gold_red_mandala_extended():
    global my_project
    my_project = my_project
    my_project = 'Gold-Red Animation Extended' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1853 - 1963, 27th module of 48')

    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(my_angle))
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
            t.el.forward(count/2)
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
            t.el.forward(count/2)
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
            t.go.forward(count/2)
            f.save_thumb()
            # count_it()
            # # count += 1
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#module_28
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Hued_freedom_star():
    global my_project
    my_project = my_project
    my_project = 'Hued Freedom Star' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1634 - 1715, 28th module of 48')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        logger.info(str('The featured angle is     ') + str(my_angle))
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
            t.el.forward(count * t.phi ) #+ 63)
            white_dot()
            t.el.rt(my_angle)
            t.el.pencolor(123 + count %100 ,135,216 -count %200)
            t.el.forward(count * t.phi)
            white_dot()
            t.el.rt(my_angle)
            t.el.circle(count / t.phi, my_angle, 9)
            white_dot()
            f.save_thumb()
            for i in range(2):
                purple_dot()
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
     # s.end_screen()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()



#module_29
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def blue_orange_mandala_144():
    global my_project
    my_project = my_project
    my_project = 'Blue-Orange Animation' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1720 - 1784, 29th module of 48')
    t.my_venv()
    Tm.start_time()
    au.pick_medium_track()
    my_angle = 144
    t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
    folder_name = my_project + my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + folder_name)
    turtle.title(t.my_str)
    logger.info(str('The featured angle is     ') + str(my_angle))
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
        t.el.forward(count  + t.phi)
        f.save_thumb()
        for g in range(12):
            R = 0 + count % 150
            Y = 100
            B = 255 - count % 150
            t.el.left(my_angle)
            t.el.color(R, Y, B)
            t.el.pensize(2)
            t.el.forward(500)
#             f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #
        t.my_venv()
#     s.end_screen()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#module_30
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def ribbons_mandala():
    global my_project
    my_project = my_project
    my_project = 'Ribbons Mandala' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1848 - 1923, 30th module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        logger.info(str('The featured angle is     ') + str(round(my_angle)))
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
        t.el.shape("circle")
        t.el.shapesize(1)
        t.el.pensize(1)
        t.el.speed(0)
        for count in range(300): # 200 is default, use lower number for testing
            turtle.bgcolor(L, C, H + count % 150)
            t.el.pensize(10)
            t.el.right(my_angle)
            t.el.color(L, C, H + count %150 )
            t.el.forward(count  + t.phi)
            f.save_thumb()
            for g in range(10):
                R = 101 + count %133
                Y = 101 - count %100
                B = 25 - count %20
                t.el.left(my_angle)
                t.el.color(R, Y, B)
                t.el.pensize(2)
                t.el.circle(81, my_angle, 9)
                f.save_thumb()
        f.save_thumb()
        reset_all()
        Tm.end_time()
        f.set_vid_env()
        f.sync_av()
        reset_all()
  #     s.end_screen()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#module_31
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def circular_mandala_205():
    global my_project
    my_project = my_project
    my_project = 'Circular Mandala' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1790 - 1853, 31st module of 48')
    t.my_venv()
    Tm.start_time()
    au.pick_medium_track()
    my_angle = a.i_angle[a.i]
    t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
    folder_name = my_project + my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + folder_name)
    turtle.title(t.my_str)
    logger.info(str('The featured angle is     ') + str(round(my_angle)))
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
        t.el.forward(count  * t.phi)
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
    reset_all()
#     s.end_screen()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#module_32
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def occillating_polygon(): # Needs work
    global my_project
    my_project = my_project
    my_project = 'Occilating Polygon' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 1958 - 1929, 32nd module of 48')
    Tm.start_time()

    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(my_angle))
        count = 0
        t.el.pensize(1)
        logger.info('The Angle is   ' + str(my_angle))
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
            t.lu.forward(count/2 +t.phi)
            t.lu.circle(count * t.phi, my_angle, 6)
            t.lu.rt(my_angle)
            t.el.left(my_angle)
            t.el.circle( count * 3, my_angle)
            t.lu.dot(count / 6)
            t.el.pensize(count / 27)
            # count_it()
            f.save_thumb()
        f.save_final_thumb()
            # The Undo routine which animates the shrinking
        for count in range(3500): # Default is 1200; can use lower number for testing
            while t.el.undobufferentries():
                t.el.undo()
                t.lu.undo()
                f.save_undo()

                logger.info('Value of iterable: ' + str(Tm.iterable_time))
                logger.info('Value of Undobufferentries:  ' + str(t.el.undobufferentries()))
            f.save_final_undo()

    f.set_vid_env()
    f.sync_av()
    Tm.end_time()
    reset_all()
    t.my_venv()

    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#module_33
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def arc_star():
    global my_project
    my_project = my_project
    my_project = 'Arc-Star' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 2088 - 2180, 33rd module of 48')
    logger.info('Ran on:  ' + str(Tm.my_time))
    Tm.start_time()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(my_angle))
        turtle.title(t.my_str)
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
            t.el.forward( count / t.phi )
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
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        au.pick_medium_track()
        f.sync_av()
        reset_all()
        Tm.end_time()
#     s.end_screen()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()


#module_34
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def home_star():
    global my_project
    my_project = my_project
    my_project = 'Home Star' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 2010 - 2085, 34th module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(10, 50 ,0)
        logger.info(str('The featured angle is  ') + str(my_angle))
        count = 0
        t.el.pensize(1)
        # count = 0
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
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#module_35
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#Deals best with whole number angles
def use_abs():
    global my_project
    my_project = my_project
    my_project = 'Absolute Mandala' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 2268- 2328, 35th module of 48')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(my_angle))
        turtle.title(t.my_str)
        count = 0
        t.el.pensize(1)
        # count = 0
        t.el.pensize(3)
        t.el.color('brown', 'green')
        t.el.begin_fill()
        while True:
            t.el.left(my_angle)
            t.el.forward(250)
            f.save_thumb()
            if abs(t.el.pos()) < 1:
                break
        t.el.end_fill()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        Tm.end_time()
#     s.end_screen()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#module_36
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Six-Pointed Mandalas or doubles.
def double_take():
    global my_project
    my_project = my_project
    my_project = 'Double Take v.' +Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 3083 - 3138, 36th module of 48')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        R = random.randrange(155,255, 5)
        G = 255
        B = 0
        logger.info('The value of color R is    ' + str(R))
        for count in range(359):
            t.el.pensize(4)
            t.li.pensize(4)
            t.el.left(my_angle)
            t.el.color(R, G - count %255, B + count %255)
            t.el.forward(count * t.phi)
            t.li.color(R, G - count %250, B + count %250)
            t.li.right(my_angle)
            t.li.forward(count * t.phi)
            f.save_thumb()
        stage_video()
    finalize()





#module_37
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Cloverleaf Cross Mandala.
def cloverleaf():
    global my_project
    my_project = my_project
    my_project = 'Cloverleaf v.' +Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 3901 - 3948, 37th module of 48')
    # Select which set of angles to run
    a.i_angle =a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        folder_name = my_project + my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
#             t.el.left(my_angle/2)
        t.el.pensize(1)
        t.el.speed(0)
        t.el.pencolor(0, 255,0)
        turtle.bgcolor(0,0,0)
        for count in range(600):
            if count <= 255:
                t.el.pencolor(0 + count, 255 - count, 0 + count)
            else:
                t.el.pencolor(255, 0, 255)
            t.el.pensize(count / 45)
            t.el.circle(count, my_angle)
            t.el.penup()
            t.el.forward(count)
            t.el.pendown()
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        Tm.end_time()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#module_38
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Cloverleaf Extended Cross Mandala.
def cloverleaf_extended():
    a.pick_angles()
    for a.angle  in range( len(a.my_angles)):
        global my_project
        my_project = my_project
        my_project = 'Cloverleaf Extended v.' + Tm.project_time
        startup_script()
        logger.info('Located @ line 3953 - 4203, 39th module of 48')
        logger.info('===========================================================')
        t.my_venv()
        make_folder() #Line 94   
        logger.info('Starting First Pass at  ' + str(Tm.my_time))
        t.ld.speed(0)
        t.ld.pencolor(0, 255,0)
        turtle.bgcolor(0,0,0)
        count = 0
        global my_pensize
        my_pensize = count / 56
        global my_count
        my_count = 396 # 400 is default; use any number for testing, etc
        logger.info(' The program will loop  ' + str(my_count) + '  times')
        for i in range(2):
            t.ld.penup()
            t.ld.setpos(0,0)
            t.ld.seth(my_angle)
            t.ld.pendown()
            for count in range(my_count):
                my_pensize = count / 56
                if i ==  0:
                    t.ld.pencolor(255 - count % 255 , 255 - count % 255 ,  count % 255)  # Fade yellwo to blue
                else:
                    t.ld.pencolor( count % 255, 255, 0)
                t.ld.circle(count / t.phi, my_angle)
                f.save_thumb()
                t.ld.penup()
                t.ld.forward(count / t.phi)
                f.save_thumb()
                t.ld.pendown()
                t.ld.pensize(my_pensize)
                logger.info('t.ld.pensize is  ' + str(my_pensize) + '( for  ' +  str(count))
                f.save_thumb()
        logger.info('Starting Second Pass at  ' + str(Tm.my_time))
        turtle.bgcolor(0,0,0)
        del my_count
        del count
        del t.ld
        gc.collect()
        count = 0
        my_count = 396 # 400 is default; use any number for testing, etc
        t.lm.speed(0)
        turtle.colormode(255)
        for i in range(2):
            t.lm.penup()
            t.lm.setpos(0,0)
            t.lm.seth(my_angle)
            t.lm.pendown()
            for count in range(my_count):
                my_pensize = count / 56
                if i == 0:
                    t.lm.pencolor(count % 255,  255 - count % 255 , 255 - count % 255 )  # Fade aqua to red
                else:
                    t.lm.pencolor(255, 0, count %  255)
                t.lm.pensize(my_pensize)
                t.lm.circle(count / t.phi, my_angle)
                f.save_thumb()
                t.lm.penup()
                t.lm.forward(count / t.phi)
                t.lm.pendown()
                f.save_thumb()
                logger.info('t.lm.pencolor is  ' + str(t.lm.pencolor))
        logger.info('Starting Third Pass at  ' + str(Tm.my_time))
        turtle.bgcolor(0,0,0)
        del count
        del t.lm
        del my_count
        gc.collect()
        count = 0
        my_count = 396 # 400 is default; use any number for testing, etc
        t.lc.speed(0)
        turtle.colormode(255)
        for i in range(2):
             t.lc.penup()
             t.lc.setpos(0,0)
             t.lc.seth(my_angle)
             t.lc.pendown()
             for count in range(my_count):
                 my_pensize = count / 56
                 t.lc.pensize(my_pensize)
                 if i == 0:
                     t.lc.pencolor(count % 25, 255 - count % 250, 255 - count % 100)  # Fade yellow to red
                 else:
                     t.lc.pencolor( 255 - count % 100, count % 25, 126)
                 t.lc.circle(count / t.phi, my_angle)
                 t.lc.penup()
                 t.lc.forward(count / t.phi)
                 t.lc.pendown()
                 f.save_thumb()
        logger.info('Starting Fourth Pass at  ' + str(Tm.my_time))
        turtle.bgcolor(0,0,0)
        del my_count
        del count
        del t.lc
        gc.collect()
        count = 0
        my_count = 396 # 400 is default; use any number for testing, etc
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
            for count in range(my_count):
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
                t.ly.forward(count / t.phi)
                t.lg.pendown()
                t.ly.pendown()
                f.save_thumb()
        logger.info('Starting Fifth Pass at  ' + str(Tm.my_time))
        turtle.bgcolor(0,0,0)
        del my_count
        del count
        del t.ly
        del t.lg
        gc.collect()
        count = 0
        my_count = 396 # 400 is default; use any number for testing, etc
        t.me.speed(0)
        turtle.colormode(255)
        for i in range(2):
            t.me.penup()
            t.me.setpos(0,0)
            t.me.pendown()
            for count in range(my_count):
                my_pensize = count / 56
                t.me.pensize(my_pensize)
                t.me.pencolor(count %100, count % 255, 255 * i)
                t.me.circle(count / t.phi, my_angle)
                f.save_thumb()
                t.me.penup()
                t.me.forward(count / t.phi)
                t.me.pendown()
                f.save_thumb()
        logger.info('Starting Sixth Pass at  ' + str(Tm.my_time))
        turtle.bgcolor(0,0,0)
        del my_count
        del count
        del t.me
        gc.collect()
        count = 0
        my_count = 396 # 400 is default; use any number for testing, etc
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
            for count in range(my_count):
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
                t.lq.forward(count / t.phi)
                t.lb.pendown()
                t.lq.pendown()
                f.save_thumb()
        logger.info('Starting Seventh Pass at  ' + str(Tm.my_time))
        turtle.bgcolor(0,0,0)
        del my_count
        del count
        del t.lb
        del t.lq
        gc.collect()
        count = 0
        turtle.colormode(255)
        my_count = 396 # 400 is default; use any number for testing, etc
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
            for count in range(my_count):
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
    a.pick_angles()
    for a.i  in range(len(a.i_angle_auto)):
        global my_project
        my_project = my_project
        my_project = 'Majestic Mandala Extended v.' + Tm.project_time
        startup_script()
        logger.info('Located @ line 4120 - 4344, 39th module of 48')
        logger.info('===========================================================')
        t.my_venv()
        make_folder() #Line 94
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
            logger.info('The featured angle is  ' + str(my_angle))
            logger.info('The soundtrack selected for this project is  ' + str(au.my_track))
            logger.info('Starting First Pass at  ' + Tm.my_time)
            t.el.seth(my_angle)
            for count in range(my_length):
                t.el.pensize(count /my_pensize)
                t.el.pencolor(count % 255, 255 - count % 127, rand_hue)
                t.el.left(my_angle)
                t.el.forward(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.forward(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.forward(count + pi)
                f.save_thumb()
            logger.info('Starting Second Pass at  '  + Tm.my_time)
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
                t.el.forward(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.forward(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.forward(count + pi)
                f.save_thumb()
            logger.info('Starting Third Pass at  ' + Tm.my_time)
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
                t.el.forward(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.forward(count /t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.forward(count + pi)
                f.save_thumb()
            logger.info('Starting Fourth Pass at  '  +  Tm.my_time)
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
                t.el.forward(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.forward(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.forward(count + pi)
                f.save_thumb()
            logger.info('Starting Fifth Pass at  '  + Tm.my_time)
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
                t.el.forward(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.forward(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.forward(count + pi)
                f.save_thumb()
            logger.info('Starting Sixth Pass at  ' + Tm.my_time)
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
                t.el.forward(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.forward(count /t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.forward(count + pi)
                f.save_thumb()
            logger.info('Starting Seventh Pass at  '  +  Tm.my_time)
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
                t.el.forward(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.forward(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.forward(count + pi)
                f.save_thumb()
            logger.info('Starting Eighth Pass at  '  +  Tm.my_time)
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
                t.el.forward(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.forward(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.forward(count + pi)
                f.save_thumb()
            logger.info('Starting Ninth Pass at  '  +  Tm.my_time)
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
                t.el.forward(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.forward(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.forward(count + pi)
                f.save_thumb()
            logger.info('Starting Tenth Pass at  '  +  Tm.my_time)
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
                t.el.forward(count / t.phi)
                f.save_thumb()
                t.el.penup()
                t.el.left(my_angle)
                t.el.forward(count / t.phi)
                t.el.pendown()
                t.el.left(my_angle)
                t.el.forward(count + pi)
                f.save_thumb()     
#         stage_video()
#     finalize()    




#module_41
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def glorious_mandala():  # Based on Awesome Manadala
    global my_project
    my_project = my_project
    my_project = 'Glorious Mandala v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 3153 - 3217, 41st module of 48')
    t.my_venv()
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    B = random.randrange(112,155, 1)
    logger.info('The value of hue /B/ is   ' + str(B))
    L = random.randrange(10, 150, 1)
    logger.info('The value of hue /L/ is   ' + str(L))
    E = random.randrange(150, 255, 1)
    logger.info('Th e value of hue /E/ is   ' + str(L))
    for a.i  in range( len(a.i_angle)):
        logger.info('===============================================================================')
        t.my_venv()
        Tm.start_time()
        my_angle =  a.i_angle[a.i]
        au.pick_medium_track()
        make_folder()
        turtle.bgcolor(0,0,0)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        logger.info('The featured angle is     ' + str(my_angle))
        R = 255
        G = 255
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        turtle.bgcolor(10, 25, 0)
        t.go.seth(my_angle)
        t.lb.seth(my_angle)
        for count in range(1200):
            t.go.pensize(count / 110)
            t.lb.pensize(count / 120)
            if count <= 255:
                t.lb.pencolor(L + count % 50, M + count % 150, E)
                t.go.pencolor(R - count, B, Z + count %100)
            else:
                h.pick_gold()
                h.pick_blue()
            t.go.left(my_angle)
            t.go.forward(count / 15)
            f.save_thumb()
            t.lb.circle(count / 18, - my_angle, 6)
            f.save_thumb()
            t.go.left(my_angle)
            t.go.penup()
            t.lb.penup()
            t.go.right(my_angle)
            t.go.forward(count / 18)
            f.save_thumb()
            t.lb.rt(my_angle)
            t.go.pendown()
            t.lb.pendown()
            t.go.forward(count / t.phi)
            f.save_thumb()
            t.lb.forward(count / t.phi)
            f.save_thumb()
            t.go.backward(count / 18)
            f.save_thumb()
        stage_video()
    finalize()










#module_43
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Independence_mandala():
    global my_project
    my_project = my_project
    my_project = 'Independence Mandala v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 3521- 3590, 43rd module of 48')
    t.my_venv()
    a.i_angle = a.i_angle_auto # Select set of angles to use from the -my_angles- module.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using list comprehension
    # s.title_screen() # Commented out to facilitate accurate a/v processing of the .png images
    my_title = str('Featuring Independence Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    logger.info(str(my_title))
    for a.i  in range( len(a.i_angle)):
        logger.info('===============================================================================')
        t.my_venv()
        logger.info(Tm.start_time())
        my_angle =  a.i_angle[a.i]
        au. pick_medium_track()
        t.my_str = my_project + '  featuring '+ str(round(my_angle)) + '  Degree Angles   ' + 'with  ' + '-' + au.my_track
        logger.info('Presenting  ' + t.my_str)
        folder_name = my_project + my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(10,0,10)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        logger.info('The featured angle is     ' + str(my_angle))
        logger.info('..........................................................................................................................................................................................')
        for count in range(300):
            t.el.color( 0, 0, 255) #Blue
            t.el.left(my_angle)
            t.el.forward(count + t.phi)
            t.el.pensize(count / 27)
            t.me.color(255,0,0) #Red
            t.me.right(my_angle)
            t.me.forward(count * t.phi)
            t.me.pensize(count / 45)
            t.ce.color( 255, 255, 255) #White
            t.ce.forward(count * t.phi)
            t.ce.right(my_angle)
            t.ce.pensize(count /36)
            t.ce.forward(count /2)
            # count_it()
#             time.sleep(9) #for testing only. Comment out normally
            f.save_thumb()
        stage_video()
    finalize()






#module_44
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wall_show():
    global my_project
    my_project = my_project
    my_project = 'Wall Show v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 3595- 3665 44th module of 48')

    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using list comprehension
    for a.i  in range( len(a.i_angle)):
        logger.info('======================================================================')
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        logger.info(t.my_str)
        folder_name = my_project + my_key
        f.make_png_folder()
        logger.info(folder_name)
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        count = 0
        turtle.bgcolor(30,255,60)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        logger.info('The featured angle is     ' + str(my_angle))
        logger.info(('The value of t.rand_num is   ')  + str(t.rand_num))
        logger.info(('The value of t.rand_pick is   ')  + str(t.rand_pick))
        logger.info('......................................................................................')
        for count in range(255):
            R =  0
            G =  150
            B =  255
            t.el.color( R + count, G - count % 130, B - count)
            t.el.forward(count * t.phi)
            t.el.left(my_angle)
            t.el.pensize(count /36)
            t.el.color(count, t.rand_num, 255 - count)
            t.el.right(my_angle)
            t.el.circle(count / 3, my_angle, 6)
            t.ce.color( B - count, G - count % 150, R + count )
            t.ce.forward(count * t.phi)
            t.ce.right(my_angle)
            t.ce.forward(count * t.phi)
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
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()





#module_45
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wall_show_extended():
    global my_project
    my_project = my_project
    my_project = 'Wall Show Extended v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 3771- 3895, 45th module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using list comprehension
    for a.i  in range( len(a.i_angle)):
        logger.info('======================================================================')
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        logger.info(t.my_str)
        folder_name = my_project + my_key
        f.make_png_folder()
        logger.info(folder_name)
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        count = 0
        turtle.bgcolor(30,255,60)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        logger.info('The featured angle is     ' + str(my_angle))
        logger.info(('The value of t.rand_num is   ')  + str(t.rand_num))
        logger.info(('The value of t.rand_pick is   ')  + str(t.rand_pick))
        logger.info('......................................................................................')
        for count in range(250):
            R =  0
            G =  150
            B =  255
            t.el.color( R + count, G - count % 130, B - count)
            t.el.forward(count * t.phi)
            t.el.left(my_angle)
            t.el.pensize(count /36)
            t.el.color(count, t.rand_num, 255 - count)
            t.el.right(my_angle)
            t.el.circle(count / 3, my_angle, 6)
            t.ce.color( B - count, G - count % 150, R + count )
            t.ce.forward(count * t.phi)
            t.ce.right(my_angle)
            t.ce.forward(count + t.phi)
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
#             logger.info(str(t.el.color))
            t.el.color(R - count % 255, G - count % 130, B + count %255)
            t.el.forward(count * t.phi)
            t.el.left(my_angle)
            t.el.pensize(count /36)
            t.el.color(R - count, t.rand_num, count)
            t.el.right(my_angle)
            t.el.circle(count / 3, my_angle, 6)
            t.ce.color(R - count % 255, G - count % 150, B + count % 255 )
            t.ce.forward(count * t.phi)
            t.ce.right(my_angle)
            t.ce.forward(count * t.phi)
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
            t.el.forward(count * t.phi)
            t.el.left(my_angle)
            t.el.pensize(count /36)
            t.el.color(count, t.rand_num, B - count % 255)
            t.el.right(my_angle)
            t.el.circle(count / 3, my_angle, 6)
            t.ce.color( R - count % 100, B - count % 255, t.rand_pick)
            t.ce.forward(count * t.phi)
            t.ce.right(my_angle)
            t.ce.forward(count * t.phi)
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
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()





#module_46
#===========================================================================
#Code for Black Seed of Life
def black_seed():
    global my_project
    my_project = my_project
    my_project = 'Black Seed v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 3803- 3917, 46th module of 48')
    t.my_venv()
    t.el.speed(30)
    t.el.pensize(36)
    t.ce.speed(30)
    t.ce.pensize(54)
    t.ce.pencolor(255,255,255)
    length = 234
    my_image = 'TBD'
    my_angle = 135 # 60 is default
    my_base = int(3600/ my_angle) # for loop integrity of the number of loops of the ce pen
#     a.i_angle = a.i_angle_auto # Select set of angles to use.
#     str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration

    # s.title_screen()
    for a.i  in range( length):
        logger.info('===============================================================================')
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
#         my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( my_angle) + '    Degree Angles,   with   '  + au.my_track
        logger.info(t.my_str)
        folder_name = my_project + my_key
        logger.info(folder_name)
        f.make_png_folder()
        os.chdir(f.loc_thumb + folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        logger.info('The featured angle is     ' + str(my_angle))
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
                logger.info('Base is:  ' + str(my_base))
                logger.info('count  :' + str(Tm.iterable_time))
                logger.info('Pen color:  ' + str(b))
                logger.info(' x = ' + str(x))
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
                    logger.info('count  :' + str(Tm.iterable_time))
                    logger.info('Pen color:  ' + str(b))
                    logger.info(' x = ' + str(x))
                    t.el.left(my_angle)
                    t.el.circle(length)
                    f.save_thumb()
                    count -= 1
                f.save_final_thumb()
                turtle.setup(5,5)
                f.set_vid_env()
                f.sync_av()
                reset_all()
                Tm.end_time()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




'''#  module_47
#+++++++++++MODULE DARK MANDALA EXTENDED+++++++++++++++++++++++++++++++++++++++++++++++++++++
def dark_mandala_extended():  #Work on some more
    global my_project
    my_project = my_project
    my_project = 'A Dark Mandala Extended v.' + Tm.project_time + my_key
    startup_script()
    logger.info('Located @ line 3711 - 3888,   47th module of 48')
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
        logger.info("The pick_dark pen is:  ", t.hue_dict ['pick_dark']  )
        logger.info("The pick_indigo pen is':   ", t.hue_dict ['pick_indigo']  )
        logger.info("The pick_magenta pen is':   ", t.hue_dict ['pick_magenta']  )
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
            t.lz.forward(count  / 2)

            t.li.right(my_angle)  # Indigo pen
            t.li.forward(count )

            t.lz.penup()  #Dark pen
            t.lz.right(my_angle)
            t.lz.forward(count/9)
            t.lz.pendown()
            t.lz.forward(count * t.phi)

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
            t.me.forward(count / 60)

            t.iterate_dark_to_yellow()
            f.save_thumb()
            # count_it_bg()
        logger.info('The value of Tm.iterable_time is   ' + str(Tm.iterable_time))
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
            t.el.forward(count  / 2)

            t.lg.right(my_angle)  # Green pen
            t.lg.forward(count )

            t.el.penup()  #Light pen
            t.el.right(my_angle)
            t.el.forward(count/9)
            t.el.pendown()
            t.el.forward(count * t.phi)

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
            t.lb.forward(count / 60)
            t.iterate_yellow_to_dark()
            f.save_thumb()
            #count_three()
            logger.info('The value of t.bg_count is ' + str(t.bg_count))
            logger.info('The value of t.bg_count_2 is ' + str(t.bg_count_2))
            logger.info('The value of t.bg_count_3 is ' + str(t.bg_count_3))
            logger.info('The value of count is  ' + str(count))
        logger.info('The value of Tm.iterable_time is   ' + str(Tm.iterable_time))
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
            t.lu.forward(count  / 2)

            t.lz.right(my_angle)  # Dark pen
            t.lz.forward(count )

            t.lu.penup()  #Red pen
            t.lu.right(my_angle)
            t.lu.forward(count/9)
            t.lu.pendown()
            t.lu.forward(count * t.phi)

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
            t.go.forward(count / 60)
            t.iterate_dark_to_yellow()
            logger.info('The value of t.bg_count is ' + str(t.bg_count))
            logger.info('The value of t.bg_count_2 is ' + str(t.bg_count_2))
            logger.info('The value of t.bg_count_3 is ' + str(t.bg_count_3))
            logger.info('The value of count is  ' + str(count))
            f.save_thumb()
            #count_three()
        logger.info('The value of Tm.iterable_time is   ' + str(Tm.iterable_time))
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
    logger.info('Located @ line 3864 - 3920, 48th module of 48')
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
        logger.info(str('The featured angle is     ') + str(my_angle))
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
            t.go.forward(count) # /t.phi
            t.lm.pensize(count / 120)
            t.lm.rt(my_angle)
            if count <= 252:
                t.lm.pencolor(L, M - count, M - count)
            else:
                t.lm.pencolor(L, 3, X)
            t.lm.circle(count, - my_angle, 6)
            f.save_thumb()
            logger.info('The Value of color B is    ' + str(B))
            logger.info('The Value of color L is    ' + str(L))
        stage_video()
    finalize()

#  module_49
#**************************************************************************************************************
# The Rainbow Self 
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def the_rainbow_self():
#     global my_angle
#     logger.info('Selecting Angle from Input Box')
#     select_angle()
#     logger.info('Current Angle to be Drawn is ' + str(my_angle))
    logger.info('Selecting track from runtime-generated list')
    au.pick_custom_length_track()
    global my_project
    global log
    my_project = 'The Rainbow Self v.' + Tm.project_time 
    startup_script()
    logger.info('Located @ line 5860 - 6215, 49th module of 49')
    make_folder()
    logger.info('The soundtrack being used for this show is:   ' + str(au.my_track))
    turtle.bgcolor(0,0,0)
    my_range = 90
    my_length = 200
    my_pensize = .5
    t.my_angle = 4
    my_speed = 2

    def crown_chakra():
        #1
        el = turtle.Turtle()
        el.shape('blank')
        el.pencolor(255,255,250)
        el.speed(my_speed)
        el.pensize(my_pensize)
        el.penup()
        el.setpos(0,300)
        el.pendown()
        for i in range(my_range):
            el.left(t.my_angle)
            el.forward(my_length)
            f.save_thumb()
            el.setpos(0,300)
            f.save_thumb()
            el.left(t.my_angle)
            el.forward(my_length / 7)
            f.save_thumb()

    def third_eye():
        #2    
        ed = turtle.Turtle()
        ed.shape('blank')
        ed.pencolor('indigo')
        ed.speed(my_speed)
        ed.pensize(my_pensize)
        ed.penup()
        ed.setpos(0,200)
        ed.pendown()

        for i in range(my_range):
            ed.left(t.my_angle)
            ed.forward(my_length)
            f.save_thumb()
            ed.setpos(0,200)
            f.save_thumb()
            ed.left(t.my_angle)
            ed.forward(my_length / 7)
            f.save_thumb()

    def throat_chakra():
        #3
        ef = turtle.Turtle()
        ef.shape('blank')
        ef.pencolor(0,255,255)
        ef.speed(my_speed)
        ef.pensize(my_pensize)
        ef.penup()
        ef.setpos(0,100)
        ef.pendown()


        for i in range(my_range):
            ef.left(t.my_angle)
            ef.forward(my_length)
            f.save_thumb()
            ef.setpos(0,100)
            f.save_thumb()
            ef.left(t.my_angle)
            ef.forward(my_length / 7)
            f.save_thumb()
            


    def heart_chakra():
        #4
        eg = turtle.Turtle()
        eg.shape('blank')
        eg.pencolor(0,255,0)
        eg.speed(my_speed)
        eg.pensize(my_pensize)
        eg.penup()
        eg.setpos(0,0)
        eg.pendown()


        for i in range(my_range):
            eg.left(t.my_angle)
            eg.forward(my_length)
            f.save_thumb()
            eg.setpos(0,0)
            f.save_thumb()
            eg.left(t.my_angle)
            eg.forward(my_length / 7)
            f.save_thumb()
            

    def solar_plexus_chakra():
        #5
        ee = turtle.Turtle()
        ee.shape('blank')
        ee.pencolor(255, 255, 0)
        ee.speed(my_speed)
        ee.pensize(my_pensize)
        ee.penup()
        ee.setpos(0,-100)
        ee.pendown()


        for i in range(my_range):
            ee.left(t.my_angle)
            ee.forward(my_length)
            f.save_thumb()
            ee.setpos(0,-100)
            f.save_thumb()
            ee.left(t.my_angle)
            ee.forward(my_length / 7)
            f.save_thumb()
        
    def seat_of_soul_chakra():
        #6
        ei = turtle.Turtle()
        ei.shape('blank')
        ei.pencolor('orange')
        ei.speed(my_speed)
        ei.pensize(my_pensize)
        ei.penup()
        ei.setpos(0,-200)
        ei.pendown()

        for i in range(my_range):
            ei.left(t.my_angle)
            ei.forward(my_length)
            f.save_thumb()
            ei.setpos(0,-200)
            f.save_thumb()
            ei.left(t.my_angle)
            ei.forward(my_length / 7)
            f.save_thumb()

    def sacral_chakra():
        #7    
        ej = turtle.Turtle()
        ej.shape('blank')
        ej.pencolor(255, 0,0)
        ej.speed(my_speed)
        ej.pensize(my_pensize)
        ej.penup()
        ej.setpos(0,-300)
        ej.pendown()

        for i in range(my_range):
            ej.left(t.my_angle)
            ej.forward(my_length)
            f.save_thumb()
            ej.setpos(0,-300)
            f.save_thumb()
            ej.left(t.my_angle)
            ej.forward(my_length / 7)
            f.save_thumb()
        
    def play_chakras():
        global my_range
#         global t.my_angle
        global my_length
        for count in range(7):
            if count == 0:
                print(str(count))
                t.my_angle = 40
                my_range = 9
                my_length = 30
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 1:
                t.my_angle = 30
                my_range = 12
                my_length = 60
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 2:
                t.my_angle = 20
                my_range = 18
                my_length = 90
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 3:
                t.my_angle = 10
                my_range = 36
                my_length = 120
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 4:
                t.my_angle = 5
                my_range = 72
                my_length = 70
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 5:
                t.my_angle = 4
                my_range = 90
                my_length = 150
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            elif count == 6:
                t.my_angle = 2
                my_range = 180
                my_length = 180
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            else:
                t.my_angle = 1
                my_range = 360
                my_length = 200
                sacral_chakra()
                seat_of_soul_chakra()
                solar_plexus_chakra()
                heart_chakra()
                throat_chakra()
                third_eye()
                crown_chakra()
            


    play_chakras()
    stage_video()
    finalize()
   
#nomega
'''***************************************************************************************************************************************'
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
reversing_simple_mandala() #Based on simple mandala; has option to include multiple angles;  exclusively uses the pick_hues function to select colors.
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





# cloverleaf() # module_33 31 of 48, Located at line  2247 - 2304. Created 3/6/2022.


# Work on cloverleaf_extended()


'======================================================================================================================================================='
# glorious_mandala() # module_18 Tested and verified 1/10/2023; Created 4/6/2022, based on stupendous mandala. Located @ line 3153- 3219, 41st module of 48. 2 minute duration video.

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
# Fantastic_Mandala() # module_6 Tested and verified 1/4/2023; Located @ line 520 - 576,   6th module of 48. Works well. Updated to automate video creation Implemented 'phi Offset' Angle on 4/28/2022.
# dark_mandala() #module_7 Tested and verified 1/4/2023; Rows 568 - 640, 7 of 48, Revised 1/4/2023
# iridescent_polygram()  # module_8; Tested and verified 1/4/2023; Row 645 - 723, 8 of 48; Modified 1/2/2022 Updated to automate video creation

# animated_abstraction()  #  module_9 10 of 48, Thumbs created 11/21/2021
# animated_hued_polygram()  # module_13  Located @ line 929 - 989, number 13 of 48, created 11/14/2021; added print to file 3/1/2022
# awesome_mandala()  #  Tested and verified on 1/7/2023. module_15 15 of 48, Located at lines 2052 - 2109. Processed to mp4 and published to YouTube on 11/21/2021. modified 11/20/2021, This is exceptional.
#

# pretty_awesome_mandala() # module_19; Tested and verified 1/10/2023; Located @ line 1331- 1380, 18th module of 48. Derived from awesome_mandala. # Processed 90 degrees to MP4 on 12/15/2021
# mighty_awesome_mandala() # Tested and verified 01/11/2023; Located @ line 1385- 1497, 19th module of 48; Based on pretty awesome mandala


# brave_mandala() #module_19 Located @ line 1386 -1449, Derived from awesome_mandala; 18 of 48
# color_shifting_mandala() # module_20 Rows 1274 - 1327, 19 of 48 work on
# Hued_freedom_star() # module_26 Row 1358 - 1428, 22 of 48; Added 12/4/2021
# arc_star() #module_28 27 of 48; Located at lines 1586 - 1654. Added 01/06/2022. Derived from a Thought Matrix arc-star wriiten by me in 2020.\
#                       # Employs first use of automated creation of angle lists using numpy arange.
# home_star() #module_ 28 of 48; Located at lines 2007 - 2078.  Added 01/06/2022. Derived from a Thought Matrix arc-star scripted by me in 2020.\
# ribbons_mandala()  #module_30  24 of 48; Located at rows 1572 - 1635. Added 12/8/2021 (Edited from Mandala_160_09292020); converted to mult-angles on 1/20/2022
# use_abs() # module_31 29 of 48; Located at line 1890. Uses the abs() function to draw the sides and points such that it continues until the point of origin is reached.
# double_take() # module_32 30 of 48; Located at line 1843 - 1881. Facilitates the creation of a hexagram by using 2 pens drawn\
#                    # with same angles in opposite directions. Using specific angle array named a.i.angle_doublewall_show() # module_34 of 48. Located @ line 2408- 2474. Working on a suitable product to frame and display on a wall. Began development August 2022.
# Independence_mandala() # module_33  Located @2335 - 2408. Developed June 2022, Added 6/28/2022. 33rd module of 48. Makes beautiful diagrams.

'===================================================================================================================================================='
# This set of modules require tweaking and modification

# # # #     #NEEDS Work -- Too Slow!# gold_red_mandala_extended() # Created 11/18/2022; 'Located @ line 1856 - 1961, 21st module of 48')  # 4:12 minutes
# #     #NEEDS Work -- Too slow!# gold_red_mandala()  # module_25 Located @ line 1801 - 1852, 21st module of 48 Added 12/3/2021; processed to mp4 12/16/2021(added 3 degrees)


# NEEDS SOME TWEAKING blue_orange_mandala_144() #module_23  23 of 48; Located at rows 1510 - 1568. Added 12/7/2021 (Edited from Mandala_160_09292020) Processed to mp4 12/7/2021

# NEEDS TWEAKING hued_gradiant()  #module_9 Row 647 - 733, 9 of 48
# gradiant_mandala() #  module_14 Row  785 - 852, 11 of 48. Last run date: 2/1/2022
# pretty_polygonial()   # module_16   Row 856, 14 of 48, modified 11/19/2021  nEEDS WORK!
# Work on some more  multi_hued_polygram() # module_23 Row  1125 - 1180, 20 of 48
# black_seed()   # module_35 Needs more work
# occillating_polygon() # module_27 NEED WORK ON THE UNDO FUNCTION Located @ line 1891 - 1968, 26th module of 48; Added 12/28/2021  Is first attempt to use undo function as way to create occillation
'======================================================================================================================================================================================================='
# Finalizing scripts to sync all files and folders
# turtle.setup(550,550) # Minimized turtle window to observe screen and read shell output
# f.move_all() # Moves files to appropriate locations
# logger.info('All files have been moved to their final home')
# f.sync_mandala_folders()  # Sync video and script folders backups
# logger.info('Folders and files have been synced and backed up')
# logger.warning('Program is terminating')
# turtle.bye()  # End the program;  Default is to leave uncommented.

