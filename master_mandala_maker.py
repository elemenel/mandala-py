'''
MASTER MANDALA MAKER (master_mandala_maker.py); developer: Leon Hatton, elementalsystems1@gmail.com
    Primary Python IDE is Thonny, currently version 4.0.1 on Python 3.10.
    
    Default  platform is Linux. Currently using Kubuntu, which I think has a good balance between performance and
    ease of use.
    
    Imported from PyPy through Thonny are the following:
    Turtle, MoviePy, PyAutogui, NatSort, Numpy, Random, CV2, DateTime, TimeIt, OS,  Sys, Logging,  gc, \
    DirSync, Pillow, Shutil, PathLib, Glob, Imagio, Functools, Math, Mutagen. PyAutoGui  running on Linux needs scrot,
    which is installed from apt(Ubuntu).
    
    In addition to the above-listed imported modules from Pypy,
    the the author has developed and is actively maintaining the following custom Python modules:
        1. master_mandala_maker.py; primary module, initiates and runs code for the animations.
        2. My_template.py; sets up the enviroment
        3. my_angles.py; processes angle selections
        4. my_hues.py; selects custom color hues
        5. my_splash_screen.py; starts the show; ends the show (not being used due to issues with sort)
        6. File_scripts.py; repository for file manipulations, creations, deletions, sorting, video processing
        7. audio_clips.py; repository of links to audio tracks on the local server and filters audio clips by duration
        8. Timer.py; provides time/date functionality
        9. _A ColorHueTester.py; the only independent module. It outputs a given hue, based on RGB color hue format.
            Screenshot of image is saved to a file.
        
        Maintained at Git Repository (Private).
        Link: https://github.com/elemenel/mandala-py
'''




import turtle
import time
from timeit import default_timer as timer
import random
import My_template as t # Set up environment
import my_angles as a  #Processes angle selections
import my_hues as h # Aids in color selections
import my_splash_screen as s
# from PIL import Image #module for converting python output to image
import numpy as np # Processes the video
import cv2 # For screenshots
import pyautogui # For screenshots
from datetime import datetime
from Timer import Timer
import Timer as Tm
import FileScripts as f  # Processes file manipulations
import os
import sys
import audio_clips as au # Processes the audio tracks
import gc
from select import select
import logging
# import logreset
# from functools import lru_cache

if sys.platform.startswith('linux'):
    my_path = '/media/elemen/Inland SSD1'
else:
    my_path = 'M:'

t.my_venv()   #Initializes mandala drawing environments

count = 0

my_project = str('The Novanno Angles')

def startup_script():
    global my_filename
    global logger
    global formatter, fileHandler, consoleHandler, my_project
    my_filename = f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + '_' + t.my_key +  '.log'
    logger = logging.getLogger(my_project) # Initialize global logger
    fileHandler = logging.FileHandler(my_filename)
    fileHandler.setLevel(logging.INFO)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    logger.setLevel(logging.INFO)
    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)
#     formatter = logging.Formatter( '%(asctime)s  |  %(name)s%; (levelname)s:  |  %(message)s  |',   datefmt='%m/%d/%Y %I:%M:%S%p')
#     consoleHandler.setFormatter(formatter)
#     fileHandler.setFormatter(formatter)
    logger.info('Starting  ' + my_project + ' @  ' + str( Tm.my_time))
    logger.info('This is ' + my_project + ' code')

def make_folder():
    logger.info('Setting up directories and files for video production  @  '+ str(Tm.my_time))
    t.my_angle = a.i_angle_auto[a.i]
    t.my_str = my_project + '    featuring   ' + str(round( t.my_angle)) + '    Degree Angles,   with   '  + str(au.my_track)
    s.title_screen()
    t.folder_name = my_project + '_' + str(t.my_angle) + '_' + str(au.my_track)
    logger.info('Folder name is   ' + str(t.folder_name))
    f.make_png_folder()
    os.chdir(f.loc_thumb + t.folder_name)
    turtle.title(t.my_str)
    logger.info('Presenting  ' + t.my_str)


def stage_video():
    f.save_final_thumb()
    logger.info(' Starting video creation @ ' + str(Tm.my_time) + '.........')
    turtle.setup(5,5)
    f.set_vid_env()
    logger.info('Starting merger of video and audio clips @  ' + str(Tm.my_time) + '..........')
    f.sync_av()
    logger.info('Making of mandala completed @  ' + str(Tm.my_time))
    logger.info('Stopping  ' + t.my_str + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('****************************************************************************')
    reset_all()
    
    
    

def finalize():
    logger.info('************************************************************************')
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('Finalizing scripts to sync all files and folders')
    logger.info('Minimizing turtle screen to observe screen and read shell output')
    turtle.setup(5,5) # Minimized turtle window to observe screen and read shell output
    logger.info('Moving files to appropriate folders')
    f.move_all() # Moves files to appropriate locations
    logger.info('Video .mp4 files have been moved to /Videos/')
    logger.info('Image .png files have been moved to /Thumbs/Output/')
    logger.info('Image .jpg files have been moved to /home/elemen/Pictures/Mandala Final Thumbs/')
    logger.info('Pics have been moved to Pictures folder')
    logger.info('================================================================================')
    f.sync_mandala_folders()  # Sync video and script folders backups
    logger.info('Folders and files have been synced and backed up')
    logger.warning('Shutting down this module and resetting logger')
    logger.handlers.clear()
    reset_all()




def reset_all():   #Utility to clear screen and reset to sequence next screen drawing
    turtle.clearscreen()
    t.my_pen.reset()
    t.le.reset()
    t.ce.reset()
    t.lr.reset()
    t.li.reset()
    t.lu.reset()
    t.ld.reset()
    t.la.reset()
    t.lg.reset()
    t.lb.reset()
    t.lc.reset()
    t.lm.reset()
    t.ll.reset()
    t.me.reset()
    t.lz.reset()
    turtle.reset()
    logger.info('Pausing 9 seconds for user option to permanently manually stop the program at  end of sub-routine  before the next one starts.................')
    logger.info('********************************************************************************************************************')
    time.sleep(9)

def count_one():
    t.iterable += 1
    return t.iterable

def count_two():
    t.iterable += 1
    count += 1
    return t.iterable, count

def count_three():
    t.iterable += 1
    count += 1
    t.bg_count += 1
    return t.iterable, count, t.bg_count



#Defines pens and pencolors
# h.pick_red() #Pen lu
# h.pick_indigo() #Pen li
# h.pick_gold() #Pen la
# h.pick_green() #Pen lg
# h.pick_dark() #Pen lz
# h.pick_blue() #Pen lb
# h.pick_random() #Pen me
# h.pick_magenta() #Pen lm
# h.pick_light() # Pen le

global length
length = 255  #Default is 255; any lower number for testing

# Index of modules:


#  module_1
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
def basic_yin_yang(): # **
    global my_project
    t.my_project = my_project
    my_project = 'Animated Yin-Yang v.'  + Tm.project_time
    startup_script()
    logger.info('Starting Animated Yin-Yang module  by Leon Hatton on   ' + str(Tm.my_time))
    logger.info('Located @ line 176 - 206; 1st module of 48')
    t.my_venv()
    t.my_angle = 180
    au.pick_medium_track()
    t.my_str = my_project + '   featuring   ' + str( t.my_angle) + '  ' + '    Degree Angles  with  '  + au.my_track
    turtle.title(t.my_str)
    t.folder_name = my_project + t.my_key 
    f.make_png_folder()
    os.chdir(f.loc_thumb + t.folder_name)
    t.iterable = 0
    turtle.bgcolor('goldenrod') # Has to be a neutral shade like grey to contrast the black and white theme.
    while t.iterable <= (600):  # 600 is default, duration 3.5 minutes. Use lower number for testing. The higher the number, the longer the show.
        t.le.pensize(10)
        t.le.color(0,0,0) # 0,0,0 is default (Black)
        t.le.rt(-t.my_angle + t.phi)
        t.le.circle(250)
        t.le.color(255,255,255) # 255,255,255 is default (White)
        t.le.rt(-t.my_angle)
        t.le.circle(250)
        count_one()
        f.save_thumb()
    stage_video()
    finalize()
    
   


#  module_2
#+++++++++++MODULE 02, Colorful Mandala +++++++++++++++++++++++++++++++++++++++++++++++++++++
def colorful_mandala():  # **
    global my_project
    my_project = t.my_project
    my_project = 'A Colorful Mandala v.'  + Tm.project_time
    startup_script()
    t.my_venv()
    logger.info('Selecting angles to run from my_angles.py')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Colorful Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    logger.info('Located at lines 211 - 265 of master_mandala_maker.py')
    logger.info(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)): # Cycles through each angle in the list
        t.my_venv()
        au.pick_medium_track() # Selects tracks from list under 3.7 minutes durations
        Make_folder()
        turtle.bgcolor(20,10,10)
        t.la.right(t.my_angle/2)
        t.li.left(t.my_angle/2)
        while t.iterable <= 390:
            R =  160
            G =  0
            B =  255
            if R == 0:
                t.la.color(0, t.iterable % 140, B - t.iterable % 199)
                t.li.color( 0, t.iterable %199,  B - t.iterable % 199)
            else:
                t.la.color(R -  t.iterable %160, t.iterable %199, B - t.iterable %199)
                t.li.color( R + t.iterable % 80,  t.iterable %199, B - t.iterable % 250)
            t.la.forward(t.iterable / t.phi)
            t.la.left(t.my_angle)
            t.la.pensize(t.iterable / 84)
            t.la.right(t.my_angle)
            t.la.circle(t.iterable / t.phi, t.my_angle, 6)
            t.li.forward(t.iterable)
            t.li.right(t.my_angle)
            t.li.forward(t.iterable + t.phi)
            t.li.pensize(t.iterable / 54)
            count_one
            f.save_thumb()
#         time.sleep(10)     #For testing only. comment out for normal run.
        stage_video()
    finalize()




#  module_3
#+++++++++++MODULE Colorful Mandala_Extended+++++++++++++++++++++++++++++++++++++++++++++++++++++
def colorful_mandala_extended():  # **
    global my_project
    my_project = t.my_project
    my_project = 'A Colorful Mandala Extended v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 265 - 383,  3rd module of 48')
    logger.info('Ran on:  ' + str(Tm.my_time))
    t.my_venv()
    # Select which set of angles to run
    logger.info('Selecting which angles to run from my_angles.py')
    a.i_angle = a.i_angle_auto 
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Colorful Extended Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    logger.info(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()
        t.iterable = 0
        t.li.pensize(1)
        turtle.bgcolor(20,10,10)
        t.la.right(t.my_angle/2)
        t.li.left(t.my_angle/2)
        logger.info('Starting creation of sequential screenshots')
        logger.info('Starting First Loop of 3')
        while t.iterable <= 244:
            R =  0
            G =  140
            B =  255
            if G == 0:
                t.la.color( t.iterable, t.iterable, B - t.iterable)
                t.li.color( t.iterable, 0, B - t.iterable)
            else:
                t.la.color( t.iterable, G - t.iterable %140, B - t.iterable %100)
                t.li.color( t.iterable, G - t.iterable %140, B - t.iterable)
            t.la.forward(t.iterable * t.phi)
            t.la.left(t.my_angle)
            t.la.pensize(t.iterable / 36)
            t.la.right(t.my_angle)
            t.la.circle(t.iterable + t.phi, t.my_angle, 6)
            t.li.forward(t.iterable * t.phi)
            t.li.right(t.my_angle)
            t.li.forward(t.iterable + t.phi)
            t.li.pensize(t.iterable / 27)
            count_one()
            f.save_thumb()
        # Start second pass
        logger.info('Starting Second Loop of 3')
        t.iterable = 244
        count = 0
        t.la.penup()
        t.li.penup()
        t.la.setpos(0,0)
        t.li.setpos(0,0)
        t.la.pendown()
        t.li.pendown()
        t.li.speed(0)
        t.la.speed(0)
        while t.iterable <= 505:
            R =  0
            G =  140
            B =  255
            if R == 240:
                t.la.color( 240, count %100, B - count %250)
                t.li.color( 240, G -count % 140, B - count % 240)
            else:
                t.la.color( count %240, G - count %140, B - count %100)
                t.li.color( count %100, G - count %140, B - count % 240)
            t.la.forward(count * t.phi)
            t.la.left(t.my_angle)
            t.la.pensize(count / 54)
            t.la.right(t.my_angle)
            t.la.circle(count + t.phi, t.my_angle, 6)
            t.li.forward(count + t.phi)
            t.li.right(t.my_angle)
            t.li.forward(count)
            t.li.pensize(count / 45)
            count_two()
            f.save_thumb()
          # Start second pass
        logger.info('Starting Third Loop of 3')
        t.iterable = 505
        count = 0
        t.la.penup()
        t.li.penup()
        t.la.setpos(0,0)
        t.li.setpos(0,0)
        t.la.pendown()
        t.li.pendown()
        t.li.speed(0)
        t.la.speed(0)
        while t.iterable <= 755:
            R =  255
            G =  140
            B = 0
            if B == 240:
                t.la.color( R - count, G + count %140, 240)
                t.li.color( R - count, G - count%140, 240)
            else:
                t.la.color( R - count, G - count %140, count %100)
                t.li.color(R - count %100, G - count %140,  count % 240)
            t.la.forward(count * t.phi)
            t.la.left(t.my_angle)
            t.la.pensize(count / 45)
            t.la.right(t.my_angle)
            t.la.circle(count + t.phi, t.my_angle, 6)
            t.li.forward(count + t.phi)
            t.li.right(t.my_angle)
            t.li.forward(count)
            t.li.pensize(count /36)
            count_two()
            f.save_thumb()    
        stage_video()
    finalize()




#  module_4
#**************************************************************************************************************
  # Published to YouTube on 11/2/2021
 #This script features three pens: le, me, and lb. They follow separate yet coordinated routes to compose the mandala.
#+++++++++++MODULE  Jagged Multigram+++++++++++++++++++++++++++++++++++++++++++++++++++++
def jagged_multigram():  # **
    global my_project
    t.my_project = my_project
    my_project = 'Jagged Multigram v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 388 - 499, 4th module of 48')
    t.my_venv() #Calls the template module
    logger.info('Selecting which angles to run from my_angles.py')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Jagged Multigram Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    logger.info(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()
        my_hue = random.randint(5, 100)
        my_hue_a = random.randint(100, 200)
        t.le.speed(0)
        t.me.speed(0)
        t.lb.speed(0)
        turtle.title(t.my_str)
        logger.info('The angle for this mandala is    ' + str(t.my_angle) + '    degrees.')
        logger.info('The value of my_hue is' + '   ' + str(my_hue))
        logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
        t.iterable = 0
        t.bg_count = 0
        my_length = 255
        while t.iterable <= my_length: #250 is default. Use lower number for testing. Loops limited by maximum color value of 255.
            h.bg_fade_dark_to_yellow()
            R =  my_hue  #Pen le color
            G =  my_length  #Pen le color
            B =  0  #Pen le color
            L = my_length  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = my_length  #Pen lb color
            t.le.color( R , G - t.iterable ,  t.iterable )
            t.me.color( L - t.iterable, M,  t.iterable )
            t.lb.color( D + t.iterable, E, F - t.iterable)
            t.le.left(t.my_angle)
            t.me.left(t.my_angle)
            t.lb.left( t.my_angle / t.phi)
            t.le.forward( t.iterable * 3 )
            t.me.forward( t.iterable  * 2 + t.phi )
            t.lb.forward( t.iterable  * 2.5)
            t.le.rt(t.my_angle)
            t.me.left( - t.my_angle)
            t.lb.rt( t.my_angle)
            t.me.forward(t.iterable  / 2)
            t.le.forward(t.iterable  / 1.5)
            t.lb.forward(t.iterable  / 2.5)
            t.le.circle(t.iterable / 63,  t.my_angle, 5)
            t.me.circle(t.iterable / 72,  t.my_angle)
            t.lb.circle(t.iterable / 54, t.my_angle)
            t.me.pensize(t.iterable  / 45)
            t.le.pensize(t.iterable  / 50 )
            t.lb.pensize(t.iterable  / 50)
            t.iterable += 1
            t.bg_count += 1
            f.save_thumb()
        count = 0
        t.bg_count = 0
        t.le.penup()
        t.me.penup()
        t.lb.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.lb.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        t.lb.pendown()
        while count <= my_length: #255 is default. Use lower number for testing. Loops limited by maximum color value of 255.
            h.bg_fade_yellow_to_dark()
            R =  my_hue  #Pen le color
            G =  my_length  #Pen le color
            B =  0  #Pen le color
            L = my_length  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = my_length  #Pen lb color
            logger.info('The value of my_hue is' + '   ' + str(my_hue))
            logger.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
            t.le.color( R , G - count ,  count )
            t.me.color( L - count, M,  count )
            t.lb.color( D + count, E, F - count)
            t.le.left(t.my_angle)
            t.me.left(t.my_angle)
            t.lb.left( t.my_angle / t.phi)
            t.le.forward( count * 3 )
            t.me.forward( count  * 2 + t.phi )
            t.lb.forward( count  * 2.5)
            t.le.rt(t.my_angle)
            t.me.left( - t.my_angle)
            t.lb.rt( t.my_angle)
            t.me.forward(count  / 2)
            t.le.forward(count  / 1.5)
            t.lb.forward(count  / 2.5)
            t.le.circle(count / 63,  t.my_angle, 5)
            t.me.circle(count / 72,  t.my_angle)
            t.lb.circle(count / 54, t.my_angle)
            t.me.pensize(count  / 45)
            t.le.pensize(count  / 50 )
            t.lb.pensize(count  / 50)
            count_three()
            f.save_thumb()    
        stage_video()
    finalize()




#  module_5
#*****************************************************************************************************************************
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def hued_polygonial():  # Uses 2 pens with offset t.phi angle
    global my_project
    t.my_project = my_project
    my_project = 'Hued Polygonial v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 513 - 561, 5th module of 48')
    t.my_venv()
    t.my_title = str('This Show Features Hued Polygonial Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    logger.info(t.my_title)
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()
        logger.info('The offset angle value is  ' + str(t.my_angle * (t.pi/2)))
        h.pick_gold()
        t.la.rt(t.my_angle / 2)
        h.pick_blue()
        t.lb.rt(t.my_angle / 2)
        t.iterable = 0
        t.lb.speed(0)
        t.la.speed(0)
        turtle.bgcolor(a.i + 25 % 100, a.i + 20 %110, a.i + 50 % 250)
        t.bg_count = 0
        while t.iterable <= 255:    #255 is default. Use lower number for testing.
            h.bg_fade_skyblue_to_dark()
            t.lb.pensize(t.iterable / 9)
            t.la.pensize(t.iterable /18)
            R = random.randrange(50, 100, 6)
            G = 0
            B = 255
            V = 0
            W = random.randrange(0, 81, 7)
            X =  255
            t.lb.color( R + t.iterable % 100,  t.iterable,  B - t.iterable)
#             t.la.color( X - t.iterable, V + t.iterable, W)
            h.pick_gold()
            t.la.left(t.my_angle * t.phi)
            t.la.fd(t.iterable * t.phi)
            t.lb.left(t.my_angle)
            t.lb.circle(t.iterable + t.phi, t.my_angle)
            turtle.bgcolor(255 - t.iterable, 255 - t.iterable, 30)
            count_two()
            f.save_thumb()
        stage_video()
    finalize()




#  module_6
#+++++++++++MODULE FANTASTIC MANDALA+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Fantastic_Mandala():  #  On 4/28/2022, assigned an 'Offset Angle' to second turtle pen as the current angle times t.phi, looks good as a balance.
    global my_project
    t.my_project = my_project
    my_project = 'Fantastic Mandala v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 506 - 549,   6th module of 48')
    t.my_venv() # Initializes turtle canvas screen environment
    logger.info('Selecting which angles to run from my_angles.py')
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring   ' + my_project + '   with  ' +  str(str_angles) + '  ' + 'angles')
    s.title_screen()
    logger.info(t.my_title)
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()
        h.pick_light()
        h.pick_gold()
        h.pick_indigo()
        t.la.rt(t.my_angle / 2)
        t.li.rt(t.my_angle / 2)
        t.iterable = 0
        t.li.speed(0)
        t.la.speed(0)
        turtle.bgcolor(10, 0, 10)
        while t.iterable <= length:    #255 is default. Use lower number for testing. 300 for audio clip add.
            t.la.pensize(t.iterable / 24) #la is the gold hue
            t.li.pensize(t.iterable / 30)  #li is the purple hue
            t.le.pensize(t.iterable / 36)
            h.pick_light()
            h.pick_gold()
            h.pick_indigo()
            t.la.right(t.my_angle)
            t.la.fd(t.iterable + t.phi)
            t.le.fd(t.iterable * t.pi/2)
            t.le.circle(t.iterable, t.my_angle, 6) # le is a random light hue.
            t.li.circle(t.iterable, -t.my_angle * t.phi) # This is the offset angle
            t.iterable += 1
            f.save_thumb()
        stage_video()
    finalize()




#  module_7
#+++++++++++MODULE DARK MANDALA+++++++++++++++++++++++++++++++++++++++++++++++++++++
def dark_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'A Dark Mandala v. ' + Tm.project_time
    startup_script()
    logger.info('Located @ line 614 - 677,   7th module of 48')
    t.my_venv()
    make_folder()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()
        turtle.bgcolor(0, 0,100)
        print ("The pick_random pen is:   ",  h.hue_dict ['pick_random']  )
        print ("The pick_dark pen is:  ", h.hue_dict ['pick_dark']  )
        print ("The pick_indigo pen is':   ", h.hue_dict ['pick_indigo']  )
        print ("The pick_dot pen is':   ", h.hue_dict ['pick_dot']  )
        t.bg_count = 0
        while t.iterable <= 300:
            h.bg_fade_dark_to_green_to_dark()
            if t.iterable <= 255:
                t.lz.pencolor(200, 50, 10)
                t.my_pen.color(10, 10, 30)
            else:
                h.pick_magenta() #pen t.me
                h.pick_dark()  # pen t.lz
                h.pick_indigo() # pen t.li
            for i in range(2):
                t.li.right(t.my_angle / 2)
                t.me.right(t.my_angle)
                t.me.pensize(t.iterable/24)
                t.li.pensize(t.iterable / 54)
                t.lz.right(t.my_angle / 2)
                t.lz.pensize(t.iterable / 54)
                t.lz.circle(t.iterable / 4, t.my_angle, 6)
                t.lz.penup()
                t.lz.backward(t.iterable / t.phi + i)
                t.lz.pendown()
                t.li.forward(t.iterable / t.phi)
                t.lz.right(t.my_angle / 2)
                t.lz.forward(t.iterable  / 2)
                t.li.right(t.my_angle)
                t.li.forward(t.iterable )
                t.lz.penup()
                t.lz.right(t.my_angle)
                t.me.forward(t.iterable/9)
                t.lz.pendown()
                t.lz.forward(t.iterable * t.phi)
                t.li.forward(t.iterable / t.phi)
                t.li.circle(t.iterable /3, - t.my_angle)
            #make dots
            t.me.left(t.my_angle / 2)
            t.me.dot(t.iterable /24)
            t.me.penup()
            t.me.backward(t.iterable)
            t.me.pendown()
            t.me.forward(t.iterable / 60)
            count_two()
            f.save_thumb()
        stage_video()
    finalize()




#  module_8
#+++++++++++MODULE 8 - Iridescent Polygram+++++++++++++++++++++++++++++++++++++++++++++++++++++
def iridescent_polygram():  # Uses 2 pens with offset t.phi angle
    global my_project
    t.my_project = my_project
    my_project = 'Iridescent Polygram v.' + Tm.project_time
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
        t.le.right(t.my_angle /2)
        t.me.right(t.my_angle / 2)
        for t.iterable in range (255):  #255 is default. Use lower number for testing.
            turtle.bgcolor(50 - t.iterable %49, 10 + t.iterable %200, 255 - t.iterable)
            t.le.pensize(t.iterable / 49)
            t.me.pensize(t.iterable / 72)
            t.le.right(t.my_angle)
            t.le.forward(t.iterable + t.phi)
            t.me.left(t.my_angle * t.phi)  # This is the offset angle
            t.me.pencolor(random.randint(100,200), random.randint(0,75) + t.iterable %150,  random.randint(175,255) - t.iterable %150)
            t.le.pencolor(random.randint(0,128) + t.iterable %126, random.randint(150,255)- t.iterable %126, random.randint(100, 200))
            t.le.circle( t.iterable - t.pi, -t.my_angle, 8)
            t.me.circle(t.iterable / t.pi, t.my_angle * t.phi) # This is the offset angle
            t.le.pencolor(255,255,random.randint(100, 200))
            t.me.pencolor(255,random.randint(100, 200), 255)
            t.le.dot(t.iterable / t.phi / 18)
            t.me.dot(t.iterable / t.phi / 9)
            f.save_thumb()
        stage_video()
    finalize()




#  module_9
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def bold_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Bold Mandala v. ' + Tm.project_time
    startup_script()
    logger.info('Located @ line 723 - 792, 8th module of 48')
    t.my_venv()
    my_pensize = random.randint(18, 48)
    for a.i  in range( len(a.i_angle_auto)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        make_folder()
        turtle.bgcolor(0,0,0)
        t.la.speed(0)
        t.bg_count = 0
        while t.iterable <= 255:      #255 is default. Use lower number for testing. 
            h.bg_fade_dark_to_yellow()
            h.pick_indigo() #Indigo hues
            h.pick_gold() #Gold hues
            t.li.left(t.my_angle / 3) #Indigo pen
            t.li.penup()
            t.li.setpos(0,0)
            t.li.pendown()
            t.li.pensize(t.iterable / my_pensize)
            logger.info('The value of my_pensize is  ' + str(my_pensize))
            t.li.circle(t.iterable, t.my_angle, 3)
            
            t.la.pensize(t.iterable / 21)  #Gold pen
            t.la.left(t.my_angle)
            t.la.backward(t.iterable * t.phi)
            t.la.left(t.my_angle /3)
            t.la.forward(t.iterable)
            t.iterable += 1, t.bg_count += 1
            f.save_thumb()
        count = 0
        t.bg_count = 0
        t.li.penup()
        t.la.penup()
        t.li.setpos(0,0)
        t.la.setpos(0,0)
        t.li.pendown()
        t.la.pendown()
        while count <= 255:    
            h.bg_fade_yellow_to_dark()
            h.pick_indigo() #Indigo hues
            h.pick_gold() #Gold hues
            t.la.left(t.my_angle / 3) #Gold pen
            t.la.penup()
            t.la.setpos(0,0)
            t.la.pendown()
            t.la.pensize(count /my_pensize)
            logger.info('The value of my_pensize is  ' + str(my_pensize))
            t.la.circle(count, t.my_angle, 3)
            
            t.li.pensize(count / 21)  #Indigo pen
            t.li.left(t.my_angle)
            t.li.backward(count * t.phi)
            t.li.left(t.my_angle / 3)
            t.li.forward(count)
            count_three()
            f.save_thumb()
        time.sleep(6)
        stage_video()
    finalize()    

     


'''
#  module_10
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# NEEDS SOME TWEAKING def hued_gradiant():  # Uses 2 pens with offset t.phi angle
    global my_project
    t.my_project = my_project
    my_project = 'Hued Gradiant v.' + Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' +  str(round(t.my_angle)) + ' and  ' + str(round (t.my_angle * t.phi)) +'    Degree Angles,   with   '  + au.my_track
        logging.info('Presenting   ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        logging.info('The offset angle value is  ' + str(t.my_angle * t.phi))
         # s.watermark()
        turtle.bgcolor(0,0,10)
        t.le.pensize(1)
        t.me.pencolor(200, 99, 102)
        t.le.left(t.my_angle / 2)
        t.me.left(t.my_angle / 2)
        while t.iterable <= 200:
            turtle.bgcolor(5, 10, 40)
            R =  random.randint(100,200)
            G =  0
            B =  255
            L = 255
            M = random.randint(100,200)
            N = 0
            t.le.pencolor( R , G + t.iterable %216, B - t.iterable %126 )
            h.pick_magenta()
            t.me.pencolor(L - t.iterable % 216, M, N + t.iterable %246)
            t.le.forward( t.iterable * t.phi)
            t.me.forward( t.iterable + t.phi)
            t.le.left(t.my_angle)
            t.me.left(t.my_angle * t.phi)  # This is the offset angle
            t.me.forward(t.iterable / 2)
            t.le.forward(t.iterable / 3)
            t.le.left(t.my_angle)
            t.me.left(t.my_angle * t.phi) # This is the offset angle
            t.le.forward(t.iterable / 33)
            t.me.circle(t.iterable / t.phi, t.my_angle * t.phi, 6)
            t.le.pencolor(255, 255, random.randint(100,200))
            t.le.dot(9)
            t.le.right(t.my_angle)
            t.me.right(t.my_angle * t.phi) # This is the offset angle
            t.le.forward(t.iterable / t.phi)
            t.me.forward(t.iterable / t.phi)
            t.le.pencolor(random.randint(100,200), 255, 255)
            t.le.dot(9)
            t.me.dot(9)
            t.me.pensize(t.iterable / 12)
            t.le.pensize(t.iterable / 24)
            t.iterable += 1
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
    t.my_project = my_project
    my_project = 'Animated Abstract v.' + Tm.project_time
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
        t.le.pensize(1)
        t.me.pencolor(200, 99, 102)
        t.iterable = 0
        while t.iterable <= length:  # 255 is default. Use lower number for testing.
            t.le.setpos(0,0)
            turtle.bgcolor(t.iterable %200, t.iterable % 250, t.iterable % 50)
            R = 0
            G = 20
            B = 255
            t.le.color( R + t.iterable %150, G + t.iterable %150,   B - t.iterable %100)
            t.le.pensize(5)
            t.le.setposition(-700, 300)
            t.le.circle(t.iterable/3, t.my_angle, 7)
            t.le.backward(100)
            t.le.circle(9, t.my_angle, 6)
            t.le.pencolor('green')
            t.le.dot(18)
            t.le.penup()
            t.le.setpos(0,0)
            t.le.pendown()
            t.le.pencolor(R + t.iterable, G + t.iterable % 190, B - t.iterable)
            t.le.pensize(t.iterable % 20 + t.phi /18 )
            t.le.circle(150, -t.my_angle, 4)
            t.le.penup()
            t.le.setposition(700, 300)
            t.le.pendown()
            t.le.pensize(5)
            t.le.color( R + t.iterable %250, G + t.iterable %190,   B - t.iterable %200)
            t.le.circle(t.iterable/3, t.my_angle, 7)
            t.le.forward(100)
            t.le.circle(9, t.my_angle, 6)
            t.iterable += 2
            f.save_thumb()
        stage_video()
    finalize()
   




#  module_12
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gradiant_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Gradiant Mandala v.' + Tm.project_time
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
        t.le.pensize(1)
        t.me.pencolor(200, 99, 102)
        t.le.left(t.my_angle / 2)
        t.me.rt(t.my_angle / 2)
        for t.iterable in range(252):  #250 is default. Use lower number for testing, 300 for audio add.
            t.le.pensize(t.iterable/18)
            t.le.right(t.my_angle)
            R = 0
            G = 255
            B = 255
            t.le.color(R + t.iterable, G - t.iterable, B - t.iterable)
            t.le.forward(t.iterable)
            turtle.bgcolor(20, t.iterable, t.iterable)
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
    t.my_project = my_project
    my_project = 'Growing Animated Yin-Yang v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 981 - 1018, 13th module of 48')
    t.my_venv()
    Tm.start_time()
    au.pick_medium_track()
    t.my_angle =180
    t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
    logger.info('Presenting   ' + t.my_str)
    t.folder_name = my_project + t.my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + t.folder_name)
    turtle.title(t.my_str)
    turtle.bgcolor('aqua') # Has to be a neutral shade like grey to contrast the black and white theme.
    for t.iterable in range(400):  #360 is default. Use lower number for testing. The higher the number, the longer the show.
        t.le.pensize(t.iterable / 18)
        t.le.color(0,0,0)
        t.le.left(-t.my_angle - t.phi)
        t.le.circle(t.iterable / 2)
        t.le.color(255,255,255)
        t.le.left(t.my_angle)
        t.le.circle(t.iterable / 2)
        f.save_thumb()
    stage_video()
    finalize()
    



#  module_14
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Uses 2 pens with offset t.phi angle
def animated_hued_polygram():
    global my_project
    t.my_project = my_project
    my_project = 'Animated Hued Polygram v.' + Tm.project_time
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
        logger.info(str('The featured angle is     ') + str(t.my_angle))
        t.bg_count = 0
        while t.iterable <= 500:
            h.bg_fade_dark_to_green_to_dark()
            h.pick_light()
            t.le.right(t.my_angle)
            t.le.forward(t.iterable / t.pi)
            h.pick_indigo()
            t.li.left(-t.my_angle)
            t.li.forward(t.iterable / t.pi)
            t.le.rt(t.my_angle)
            t.le.backward(t.iterable / t.phi)
            h.pick_gold()
            t.la.forward(t.iterable  + t.phi)
            h.pick_dot()
            t.ld.dot(t.iterable /48 * t.phi)
            t.la.circle(t.iterable / 6, t.my_angle, 3)
            t.le.pensize(t.iterable / 15)
            t.li.pensize(t.iterable / 18)
            t.la.pensize(t.iterable / 33)
            t.iterable += 1
            t.bg_count += 1
            f.save_thumb()
        stage_video()
    finalize()
    



#  module_15
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''# def pretty_polygonial(): # NEEDS WORK
    global my_project
    t.my_project = my_project
    my_project = 'Pretty Polygonial v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 1118 - 1187, 15th module of 48')
    au.pick_medium_track()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Pretty Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            au.pick_medium_track()
            t.my_str = my_project + ' featuring '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key  + '-' + au.my_track
            t.folder_name = my_project + t.my_key
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            os.chdir(f.loc_thumb + t.folder_name)
            turtle.title(t.my_str)
            turtle.bgcolor(0,0,0)
            logger.info(str('The featured angle is     ') + str(t.my_angle))
            t.iterable = 0
            t.la.pensize(1)
            t.lg.pensize(1)
            t.lm.pensize(3)
            while t.iterable <= 300: # 255 is default. Use lower number for testing
                h.pick_gold()
                h.pick_green()
                h.pick_random()
                h.pick_magenta()
                t.lr.dot(t.iterable / 9)
                t.la.pensize(t.iterable / 144)
                t.la.left(t.my_angle)
                t.la.fd(t.iterable * t.phi)
                t.lg.pensize(t.iterable / 36)
                t.lg.left(t.my_angle)
                t.lg.fd(t.iterable * t.phi)
                t.lm.pensize(t.iterable / 54)
                t.lm.left(t.my_angle)
                t.lm.dot(t.iterable / t.phi / 18)
                t.lm.fd(t.iterable + t.pi)
                t.lg.left(t.my_angle)
                t.lg.circle(-t.iterable /9, t.my_angle, 9)
                t.lm.circle(t.iterable /6 ,t.my_angle, 9)
                f.save_thumb()
                t.iterable += 1
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
    global my_project
    t.my_project = my_project
    my_project = 'Awesome Mandala v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 1148 - 1189, 16th module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()
        logger.info(str('The featured angle is     ') + str(t.my_angle))
        R = 0
        G = 0
        B = random.randrange(1, 100, 2)
        L = random.randrange(100, 200, 2)
        M = 255
        N = 110
        X = 10
        Y = 255
        Z = 255
        h.pick_gold() #Pen la
        t.la.rt(t.my_angle)
        t.lm.rt(t.my_angle)
        t.bg_count = 0
        logger.info('The Value of color B is    ' + str(B))
        logger.info('The Value of color L is    ' + str(L))
        while t.iterable <= 600:  # 450 is default, use any number
            h.pick_gold() #Pen la
            h.bg_fade_skyblue_to_dark()
            t.la.pensize(t.iterable/150)
            t.la.left(t.my_angle)
            t.la.forward(t.iterable / 2) # /t.phi
            t.lm.pensize(t.iterable / 150)
            t.lm.rt(t.my_angle)
            t.lm.pencolor(L, M - t.iterable % 180, B)
            t.lm.circle(t.iterable / 2, - t.my_angle, 3)
            t.iterable += 1
            t.bg_count += 1
            f.save_thumb()
        stage_video()
    finalize()
    
    


#  module_17
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def awesome_mandala_extended():
    global my_project
    t.my_project = my_project
    my_project = 'Awesome Mandala Extended v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 1184 - 1306, 17th module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track() # Randomly selects a track from dymaically created medium_clips list
        make_folder()
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(t.my_angle))
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
        t.iterable = 0
        t.bg_count = 0
        h.pick_gold() #Pen la
        while t.iterable <= 255:  # First pass
            h.pick_gold() #Pen la
            h.bg_fade_skyblue_to_dark()
            t.la.pensize(t.iterable/60)
            t.la.forward(t.iterable * t.phi)
            t.la.rt(t.my_angle)
            t.lm.pensize(t.iterable / 120)
            t.lm.rt(t.my_angle)
            if t.iterable <= 255:
                t.lm.pencolor(L, M - t.iterable, M - t.iterable)
            else:
                t.lm.pencolor(L, 3, X)
            t.lm.circle(t.iterable / t.phi, - t.my_angle, 9)
            s.watermark()
            t.bg_count += 1
            t.iterable += 1
            f.save_thumb()
        logger.info('The Value of color B is    ' + str(B))
        logger.info('The Value of color L is    ' + str(L))
        h.pick_magenta #Pen me
        t.me.penup()
        t.lm.penup()
        t.la.penup()
        t.me.setpos(0 ,0)
        t.lm.setpos(0, 0)
        t.la.setpos(0, 0)
        t.me.pendown()
        t.lm.pendown()
        t.la.pendown()
        t.me.speed(0)
        t.lm.speed(0)
        t.la.speed(0)
        count = 0
        t.bg_count = 0
        while t.iterable <= 510:  # 450 is default, use any number Second pass
            h.bg_fade_dark_to_skyblue()
            h.pick_magenta() #Pen me
            turtle.bgcolor(X, 0, 0)
            t.me.pensize(count/27)
            t.me.forward(count * t.phi)
            t.me.left(t.my_angle)
            t.lm.pensize(count /45)
            t.lm.rt(t.my_angle)
            s.watermark()
            if count <= 255:
                t.lm.pencolor(R + count, M - count, B)
            else:
                t.lm.pencolor(M, M, X)
            t.lm.circle(count / t.phi, - t.my_angle, 9)
            count += 1
            t.iterable += 1
            t.bg_count += 1
            f.save_thumb()
        h.pick_indigo() #Pen li
        t.li.penup()
        t.lm.penup()
        t.la.penup()
        t.lm.home()
        t.li.home()
        t.la.home()
        t.li.pendown()
        t.lm.pendown()
        t.la.pendown()
        t.li.speed(0)
        t.lm.speed(0)
        t.la.speed(0)
        count = 0
        t.bg_count = 0
        while t.iterable <= 740:  # 450 is default, use any number Third pass
            h.bg_fade_skyblue_to_dark()
            h.pick_indigo() #Pen li
            h.pick_gold()  #Pen la
            t.li.pensize(count/27)
            t.li.left(t.my_angle)
            t.li.forward(count * t.phi)
            t.lm.pensize(count /45)
            t.lm.rt(t.my_angle)
#             t.la.pensize(count/54)
#             t.la.left(t.my_angle)
#             t.la.backward(count)
            if count <= 255:
                t.lm.pencolor(R + count, M - count, B)
            else:
                t.lm.pencolor(M, M, X)
            t.lm.circle(count / t.phi, - t.my_angle, 9)
            count += 1
            t.iterable += 1
            t.bg_count += 1
            f.save_thumb()
        stage_video()
    finalize()
        
    
    

#  module_18
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_awesome_mandala():  # Based on Awesome Mandala
    global my_project
    t.my_project = my_project
    my_project = 'Pretty Awesome Mandala v.' + Tm.project_time
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
        logger.info(str('The featured angle is     ') + str(t.my_angle))
        R = 0
        G = 255
        B = random.randrange(10, 200, 1)
        logger.info('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 200, 1)
        logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        turtle.bgcolor(10, 255, 255)
        t.le.left(t.my_angle/2)
        t.me.rt(t.my_angle/2)
        t.bg_count = 0
        while t.iterable <= 550:      # 255 is default, use lower number for testing
            h.bg_fade_yellow_to_dark()
            t.le.left(t.my_angle)
            t.le.pencolor(R + t.iterable % 200, B, G - t.iterable %200)
            t.le.forward(t.iterable /12)
            t.me.rt(t.my_angle)
            t.me.pencolor(L, M + t.iterable % 180, N + t.iterable % 75)
            t.me.circle(t.iterable / t.phi, - t.my_angle, 3)
            t.le.pensize(t.iterable/ 56)
            t.me.pensize(t.iterable / 75)
            t.bg_count += 1
            t.iterable += 1
            f.save_thumb()
        stage_video()
    finalize()
    
    
    

#  module_19
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def mighty_awesome_mandala():  # Based on pretty_awesome Mandala
    global my_project
    t.my_project = my_project
    my_project = 'Mighty Awesome Mandala v.' + Tm.project_time
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
        logger.info(str('The featured angle is     ') + str(t.my_angle))
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
        t.me.left(t.my_angle * 2)
        t.le.left(- t.my_angle * 2)
        t.iterable = 0
        t.bg_count = 0
        while t.iterable <= 255:
            h.bg_fade_skyblue_to_dark()
            t.le.rt(t.my_angle)
            t.le.pencolor(R, G + t.iterable, B - t.iterable % 100)
            t.le.forward(t.iterable)
            t.me.rt(t.my_angle)
            t.me.pencolor(L, M + t.iterable, X - t.iterable %50)
            t.me.circle(t.iterable + t.phi, - t.my_angle)
            t.le.pensize(t.iterable/48)
            t.me.pensize(t.iterable / 48)
            t.iterable += 1
            t.bg_count += 1
            f.save_thumb()
        count = 0
        t.bg_count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.me.left(t.my_angle * 2)
        t.le.left(- t.my_angle * 2)
        t.le.pendown()
        t.me.pendown()
        R = random.randrange(1, 150, 1)
        G = 0
        B = 255
        logger.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(75, 255, 1)
        logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        while t.iterable <= 510: # Second pass
            h.bg_fade_dark_to_skyblue()
            t.le.rt(t.my_angle)
            t.le.pencolor(B - count % 100, count, L)
            t.le.forward(count)
            t.me.rt(t.my_angle)
            t.me.pencolor(X - count, M + count % 50, R)
            t.me.circle(count + t.phi, - t.my_angle)
            t.le.pensize(count / 48)
            t.me.pensize(count / 48)
            t.iterable += 1
            t.bg_count += 1
            count += 1
            f.save_thumb()
        count = 0
        t.bg_count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.me.left(t.my_angle * 2)
        t.le.left(- t.my_angle * 2)
        t.le.pendown()
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
        while t.iterable <= 765: # Third pass
            h.bg_fade_skyblue_to_dark()
            t.le.rt(t.my_angle)
            t.le.pencolor(count % 100, count, R)
            t.le.forward(count)
            t.me.rt(t.my_angle)
            t.me.pencolor(count % 50, L, R)
            t.me.circle(count + t.phi, - t.my_angle)
            t.le.pensize(count / 48)
            t.me.pensize(count / 48)
            t.iterable += 1
            t.bg_count += 1
            count += 1
            f.save_thumb()
        stage_video()
    finalize()
    
    


#  module_20
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def mystical_mandala():  # Based on pretty_awesome Mandala
    global my_project
    t.my_project = my_project
    my_project = 'Mystical Mandala by Leon Hatton v.'  + Tm.project_time
    startup_script()
    logger.info('Located @ line 1508- 1631, 20th module of 48')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
#     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.pick_medium_track()
        make_folder()
        logger.info(str('The featured angle is     ') + str(t.my_angle))
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
        t.iterable = 0
        t.bg_count = 0
        logger.info('Starting main script at ' + str(Tm.my_time))
        logger.info('Starting first pass....')
        while t.iterable <= 250:
            h.bg_fade_green_to_dark()
            t.le.pensize(t.iterable / 48)
            t.le.pencolor(R, G + t.iterable, B - t.iterable % 50)
            t.le.rt(t.my_angle)
            t.le.forward(t.iterable + t.phi)
            t.le.rt(t.my_angle)
            t.le.forward(t.iterable / t.phi)
            t.me.pensize(t.iterable/42)
            t.me.rt(t.my_angle)
            t.me.pencolor(L, M + t.iterable, X - t.iterable)
            t.me.circle(t.iterable + t.phi, - t.my_angle)
            t.me.left(t.my_angle)
            t.me.backward(t.iterable)
            t.iterable += 1
            t.bg_count +=1  
            f.save_thumb()
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        R = random.randrange(1, 150, 1)
        G = 0
        B = 255
        logger.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(150, 255, 1)
        logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        logger.info('Starting second pass....')
        logger.info('Local iterator  created to restrict maximum count at 255')
        t.bg_count = 0
        count = 0
        while t.iterable <= 502: # Second pass
            h.bg_fade_dark_to_green()
            t.le.pensize(count /36)
            t.le.pencolor(B - count % 50, count, L)
            t.le.rt(t.my_angle)
            t.le.forward(count + t.phi)
            t.le.rt(t.my_angle)
            t.le.forward(count / t.phi)
            t.me.pensize(count / 36)
            t.me.rt(t.my_angle)
            t.me.pencolor(X - count, M + count, R)
            t.me.circle(count + t.phi, - t.my_angle)
            t.me.left(t.my_angle)
            t.me.backward(count)
            t.iterable += 1
            t.bg_count += 1
            count += 1
            f.save_thumb()
        count = 0
        t.bg_count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        R = random.randrange(150, 255, 1)
        G = 0
        B = 255
        logger.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(10, 255, 1)
        logger.info('The value of hue /L/ is   ' + str(L))
        logger.info('**************************************')
        logger.info('Starting third pass....')
        while t.iterable <= 756: # Third pass
            h.bg_fade_green_to_dark()
            t.le.pensize(count /36)
            t.le.pencolor(count % 25, count, R)
            t.le.rt(t.my_angle)
            t.le.forward(count + t.phi)
            t.le.rt(t.my_angle)
            t.le.forward(count / t.phi)
            t.me.pensize(count /36)
            t.me.rt(t.my_angle)
            t.me.pencolor(count, L, R)
            t.me.circle(count + t.phi, - t.my_angle)
            t.me.left(t.my_angle)
            t.me.backward(count )
            t.iterable += 1
            count += 1
            t.bg_count += 1
            f.save_thumb()
        stage_video()
    finalize()





#  module_21
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def stupendous_mandala():  # Based on Awesome Manadala
    global my_project
    global log
    t.my_project = my_project
    my_project = 'Stupendous Mandala v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 1852- 1919, 21st module of 48')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        logger.info('===============================================================================')
        t.my_venv()
        logger.info('Picking random short track')
        au.pick_medium_track()
        make_folder()
        turtle.bgcolor(0,0,0)
        logger.info('The soundtrack being used for this show is:   ' + au.my_track)
        logger.info('The featured angle is     ' + str(t.my_angle))
        R = 255
        G = 255
        B = random.randrange(150, 255, 20)
        logger.info('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 150, 25)
        logger.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        turtle.bgcolor(10, 255, 255)
#             t.le.rt(t.my_angle /2)
        t.me.rt(t.my_angle)
        t.bg_count = 0
        while t.iterable <= 300: # 255 is default, use lower number for testing; 300 for audio sync.
            h.bg_fade_skyblue_to_dark()
            h.pick_red()
            if t.iterable <= 255:
                t.me.pencolor(L, M + t.iterable, N + t.iterable)
                t.lu.pencolor(R - t.iterable, B, G - t.iterable)
            else:
                t.me.pencolor(t.iterable - 100, 55, 25)
                t.me.pensize(4)
#                     t.me.pencolor(L, t.iterable - 75, t.iterable - 112)
                t.lu.pencolor(t.iterable - 75, t.iterable - 112, B)
#                 t.le.left(t.my_angle)
            t.me.circle(t.iterable / t.phi, - t.my_angle, 9)
            t.me.forward(t.iterable / t.phi)
            t.lu.backward(t.iterable / t.phi)
            t.lu.right(t.my_angle / 2)
            t.lu.pensize(t.iterable /45)
            t.le.pensize(t.iterable /81)
            t.le.left(t.my_angle)
            t.le.forward(t.iterable)
            t.me.pensize(t.iterable / 24)
            t.me.rt(t.my_angle)
            t.me.forward(t.iterable / 6)
            t.iterable + = 1
            t.bg_count += 1
            f.save_thumb()
        stage_video()
    finalize()    
        
        




#  module_22
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def multi_hued_polygram():
    global my_project
    t.my_project = my_project
    my_project = 'Multi-Hued Polygram v.' + Tm.project_time
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
        t.iterable = 0
        t.le.right(t.my_angle / 2)
        t.le.speed(0)
        t.la.speed(0)
        N =  random.randint(1, 100)
        t.bg_count = 0
        while t.iterable <= 500: #Determines size of graphic on the screen by the count of loops
            h.pick_green()
            h.pick_gold()
            R =  0
            G =  255
            B =  255
            L =  0
            M =  0
            t.la.pensize(t.iterable /120)
            t.le.pensize(t.iterable / 64)
            t.le.color( R + t.iterable %255, G - t.iterable %255, B - t.iterable %255)
            t.le.right(t.my_angle)
            t.le.forward(t.iterable + t.phi)
            t.la.circle(t.iterable + t.phi, t.my_angle, 3)
#             t.le.circle(t.iterable * t.phi, -t.my_angle)
            t.le.right(t.my_angle)
            t.le.forward(t.iterable * t.phi)
            h.bg_fade_dark_to_green()
            t.bg_count += 1
            t.iterable += 1
            f.save_thumb()
#             gc.collect()
        stage_video()
    finalize()    




#module_23
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Brave Mandala v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 1807 -1856, 23rd module of 48')
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
        logger.info(str('The featured angle is     ') + str(t.my_angle))
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
        t.le.left(t.my_angle/2)
        t.me.rt(t.my_angle/2)
        t.bg_count = 0
        while t.iterable <= 255: #255 is default, use lower number for testing
            turtle.bgcolor(X - t.iterable, Y - t.iterable, Z)
            t.le.pensize(t.iterable/56)
            t.le.left(t.my_angle)
            t.le.forward(t.iterable)
            t.le.pencolor(R, G + t.iterable, B - t.iterable)
            t.me.pensize(t.iterable /18)
            t.me.pencolor(R, Y - t.iterable, L)
            t.me.circle(t.iterable / t.phi, t.my_angle)
            t.le.rt(t.my_angle)
            t.le.pencolor(L, M - t.iterable, N - t.iterable)
            t.le.circle(t.iterable * 1.26, - t.my_angle)
            t.iterable += 1
            t.bg_count += 1
            f.save_thumb()   #Screenshot as a png set set up mp4
        stage_video()
    finalize()




#module_24
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala_extended():
    global my_project
    t.my_project = my_project
    my_project = 'Brave Mandala Extended v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 1994 -2100, 24th module of 48')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_extended_track()
        make_folder()
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(t.my_angle))
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
        t.iterable = 0
        t.bg_count = 0
        while t.iterable <= 250: # First Pass
            h.bg_fade_dark_to_yellow()
            t.le.pensize(t.iterable/45)
            t.le.left(t.my_angle)
            t.le.forward(t.iterable)
            t.le.pencolor(G + t.iterable, B - t.iterable, R)
            t.me.pensize(t.iterable /18)
            t.me.pencolor(Y - t.iterable, R, L)
            t.me.circle(t.iterable / t.phi, t.my_angle)
            t.le.rt(t.my_angle)
            t.le.pencolor(L, M - t.iterable, N - t.iterable)
            t.le.circle(t.iterable * t.phi, - t.my_angle)
            t.iterable += 1
            f.save_thumb()  #Screenshot as a png set set up mp4
        count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        t.le.speed(0)
        t.me.speed(0)
        while t.iterable <= 505: # Second Pass
            h.bg_fade_yellow_to_dark()
            t.le.pensize(count/72)
            t.le.left(t.my_angle)
            t.le.forward(count)
            t.le.pencolor(R, G + count, B - count)
            t.me.pensize(count/27)
            t.me.pencolor(R, Y - count, L)
            t.me.circle(count / t.phi, t.my_angle)
            t.le.rt(t.my_angle)
            t.le.pencolor(Z + count % 230, M - count, N)
            t.le.circle(count, - t.my_angle)
            t.iterable += 1
            count += 1
            f.save_thumb()    #Screenshot as a png set set up mp4
        count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        t.le.speed(0)
        t.me.speed(0)
        t.bg_count = 0
        while t.iterable <= 760: # Third Pass
            h.bg_fade_yellow_to_dark()
            t.le.pensize(count/72)
            t.le.left(t.my_angle)
            t.le.forward(count)
            t.le.pencolor(R, G + count, B - count)
            t.me.pensize(count/27)
            t.me.pencolor(R, Y - count, L)
            t.me.circle(count / t.phi, t.my_angle)
            t.le.rt(t.my_angle)
            t.le.pencolor(L, M - count, N - count)
            t.le.circle(count, - t.my_angle)
            t.iterable += 1
            count += 1
            t.bg_count += 1
            f.save_thumb()    #Screenshot as a png set set up mp4    
        stage_video()
    finalize()




#module_24
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala_decimated():
    global my_project
    t.my_project = my_project
    x = 3
    my_project = 'Angle-Fractioned Brave Mandala v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 2068 -2194, 24th module of 48')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_extended_track()
        make_folder()
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(t.my_angle) + ',' + '  fractional =  ' + str(x) + ',' + '  fractional angle = ' + str(t.my_angle/x))
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
        t.iterable = 0
        t.bg_count = 0
        while t.iterable <= 255: # First Pass
            h.bg_fade_dark_to_green()
            t.le.pensize(t.iterable/45)
            t.le.left(t.my_angle/x)
            t.le.forward(t.iterable)
            t.le.pencolor(G + t.iterable, B - t.iterable, R)
            t.me.pensize(t.iterable /18)
            t.me.pencolor(Y - t.iterable, R, L)
            t.me.circle(t.iterable / t.phi, t.my_angle/x)
            t.le.rt(t.my_angle/x)
            t.le.pencolor(L, M - t.iterable, N - t.iterable)
            t.le.circle(t.iterable * 1.26, - t.my_angle/x)
            t.iterable += 1
            t.bg_count += 1
            f.save_thumb()  #Screenshot as a png set set up mp4
        count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        t.le.speed(0)
        t.me.speed(0)
        t.bgbg_count = 0
        while t.iterable <= 510: # Second Pass
            h.bg_fade_green_to_dark()
            t.le.pensize(count/56)
            t.le.left(t.my_angle/ x)
            t.le.forward(count)
            t.le.pencolor(R, G + count, B - count)
            t.me.pensize(count/18)
            t.me.pencolor(R, Y - count, L)
            t.me.circle(count / t.phi, t.my_angle/x)
            t.le.rt(t.my_angle/x)
            t.le.pencolor(Z + count % 225, M - count, N)
            t.le.circle(count, - t.my_angle/x)
            t.iterable += 1
            count += 1
            t.bg_count += 1
            f.save_thumb()    #Screenshot as a png set set up mp4
        count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        t.le.speed(0)
        t.me.speed(0)
        t.bg_count = 0
        while t.iterable <= 765: # Third Pass
            logger.info('The value of t.iterable is ' + str(t.iterable))
            logger.info('The value of count is  ' + str(count))
            t.le.pensize(count/56)
            t.le.left(t.my_angle/x)
            t.le.forward(count)
            t.le.pencolor(R, G + count, B - count)
            t.me.pensize(count/27)
            t.me.pencolor(R, Y - count, L)
            t.me.circle(count / t.phi, t.my_angle/x)
            t.le.rt(t.my_angle / x)
            t.le.pencolor(L, M - count, N - count)
            t.le.circle(count, - t.my_angle/x)
            t.iterable += 1
            count += 1
            t.bg_count += 1
            f.save_thumb()    #Screenshot as a png set set up mp4    
        stage_video()
    finalize()
    
    


#module_25
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def color_shifting_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Color Shifting Animation v.' + Tm.project_time
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
        logger.info(str('The featured angle is     ') + str(t.my_angle))
        t.iterable = 0
        R = 255
        G = 150
        B = 18
        A = 0
        H = 0
        C = 255
        turtle.bgcolor(A,H,C)
        time.sleep(4)
        t.le.left(t.my_angle/2)
        t.bg_count = 0
        while  t.iterable <= 360: # 360 is default for audio clip add, use lower number for testing
            t.le.pensize(t.iterable/ 90)
            t.le.dot(3)
            t.le.color( R - t.iterable %60,  G - t.iterable %140, B + t.iterable %200)
            t.le.left(t.my_angle)
            t.le.circle(t.iterable / t.phi, t.my_angle, 3)
            h.bg_fade_skyblue_to_dark()
            t.bg_count += 1
            f.save_thumb()
        stage_video()
    finalize()





#module_26
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gold_red_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Gold-Red Animation' + Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(t.my_angle))
        turtle.bgcolor("indigo")
        for t.iterable in range(300): #252 is default, use lower number for testing; 300 for audio clip add
            h.pick_gold()
            h.pick_red()
            h.pick_light()
            t.la.pensize(t.iterable / 27)
            t.la.circle(t.iterable *t.phi, - t.my_angle)
            t.lu.pensize(t.iterable/18)
            t.lu.backward(t.iterable *t.pi)
            t.lu.right(t.my_angle)
            t.le.dot(5)
            t.le.left(t.my_angle)
            t.le.forward(t.iterable/2)
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
    t.my_project = my_project
    my_project = 'Gold-Red Animation Extended' + Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(t.my_angle))
        turtle.bgcolor("indigo")
        while t.iterable <= (250): # First Pass 
            h.pick_gold()
            h.pick_red()
            h.pick_light()
            t.la.pensize(t.iterable / 27)
            t.la.circle(t.iterable *t.phi, - t.my_angle)
            t.lu.pensize(t.iterable/18)
            t.lu.backward(t.iterable *t.pi)
            t.lu.right(t.my_angle)
            t.le.dot(5)
            t.le.left(t.my_angle)
            t.le.forward(t.iterable/2)
            f.save_thumb()
            t.iterable += 1
            
        t.la.penup()
        t.lu.penup()
        t.le.penup()
        t.la.setpos(0,0)
        t.lu.setpos(0,0)
        t.le.setpos(0,0)
        t.la.pendown()
        t.lu.pendown()
        t.le.pendown()
        t.la.speed(0)
        t.lu.speed(0)
        t.le.speed(0)
        count = 0
        while t.iterable <= (505): # Second Pass
            h.pick_gold()
            h.pick_red()
            h.pick_light()
            t.lu.pensize(count / 27)
            t.lu.circle(count *t.phi, - t.my_angle)
            t.la.pensize(count/18)
            t.la.backward(count *t.pi)
            t.la.right(t.my_angle)
            t.le.dot(5)
            t.le.left(t.my_angle)
            t.le.forward(count/2)
            f.save_thumb()
            t.iterable += 1
            count += 1
            
        t.la.penup()
        t.lu.penup()
        t.le.penup()
        t.la.setpos(0,0)
        t.lu.setpos(0,0)
        t.le.setpos(0,0)
        t.la.pendown()
        t.lu.pendown()
        t.le.pendown()
        t.la.speed(0)
        t.lu.speed(0)
        t.le.speed(0)   
        count = 0
        while t.iterable <= (755): # Third Pass 
            h.pick_gold()
            h.pick_red()
            h.pick_light()
            t.le.pensize(count / 27)
            t.le.circle(count *t.phi, - t.my_angle)
            t.lu.pensize(count/18)
            t.lu.backward(count *t.pi)
            t.lu.right(t.my_angle)
            t.la.dot(5)
            t.la.left(t.my_angle)
            t.la.forward(count/2)
            f.save_thumb()
            t.iterable += 1
            count += 1
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
    t.my_project = my_project
    my_project = 'Hued Freedom Star' + Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        logger.info(str('The featured angle is     ') + str(t.my_angle))
        t.le.color(122,133,215)
        R = 0
        G = 50
        B = 255
        turtle.bgcolor(R, G, B)
        def white_dot():
            t.le.pencolor(255,255,255)
            t.le.dot(15)
            t.le.pencolor(123,135,216)
        def purple_dot():
            t.le.pencolor(123,135,216)
            t.le.dot(15)
        for t.iterable in range(300): # 720 is default, use lower number for testing
            if t.iterable <= 255:
                turtle.bgcolor(R + t.iterable, G, B)
            else:
                turtle.bgcolor(255, G, B)
            t.le.pensize(t.iterable/50)
            t.le.forward(t.iterable * t.phi ) #+ 63)
            white_dot()
            t.le.rt(t.my_angle)
            t.le.pencolor(123 + t.iterable %100 ,135,216 -t.iterable %200)
            t.le.forward(t.iterable * t.phi)
            white_dot()
            t.le.rt(t.my_angle)
            t.le.circle(t.iterable / t.phi, t.my_angle, 9)
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
    t.my_project = my_project
    my_project = 'Blue-Orange Animation' + Tm.project_time
    startup_script()
    logger.info('Located @ line 1720 - 1784, 29th module of 48')
    t.my_venv()
    Tm.start_time()
    au.pick_medium_track()
    t.my_angle = 144
    t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
    t.folder_name = my_project + t.my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + t.folder_name)
    turtle.title(t.my_str)
    logger.info(str('The featured angle is     ') + str(t.my_angle))
    R = 255
    G = 255
    B = 255
    L = 0
    C = 0
    H = 0
    Z = 255
    t.le.penup()
    t.le.setpos(0, -100)
    t.le.pendown()
    t.le.speed(0)
    t.le.shape("circle")
    t.le.shapesize(1)
    t.le.pensize(1)
    for t.iterable in range(252): #252 is default, use lower number for testing
        turtle.bgcolor(L, C, H + t.iterable)
        t.le.pensize(10)
        t.le.right(t.my_angle)
        t.le.color(L, C, H + t.iterable % 150)
        t.le.forward(t.iterable  + t.phi)
        f.save_thumb()
        for g in range(12):
            R = 0 + t.iterable % 150
            Y = 100
            B = 255 - t.iterable % 150
            t.le.left(t.my_angle)
            t.le.color(R, Y, B)
            t.le.pensize(2)
            t.le.forward(500)
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
    t.my_project = my_project
    my_project = 'Ribbons Mandala' + Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        logger.info(str('The featured angle is     ') + str(round(t.my_angle)))
        R = 255
        G = 255
        B = 255
        L = 0
        C = 0
        H = 0
        Z = 255
        turtle.bgcolor(L, C, H)
        t.le.penup()
        t.le.setpos(0,  -25)
        t.le.pendown()
        t.le.shape("circle")
        t.le.shapesize(1)
        t.le.pensize(1)
        t.le.speed(0)
        for t.iterable in range(300): # 200 is default, use lower number for testing
            turtle.bgcolor(L, C, H + t.iterable % 150)
            t.le.pensize(10)
            t.le.right(t.my_angle)
            t.le.color(L, C, H + t.iterable %150 )
            t.le.forward(t.iterable  + t.phi)
            f.save_thumb()
            for g in range(10):
                R = 101 + t.iterable %133
                Y = 101 - t.iterable %100
                B = 25 - t.iterable %20
                t.le.left(t.my_angle)
                t.le.color(R, Y, B)
                t.le.pensize(2)
                t.le.circle(81, t.my_angle, 9)
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
    t.my_project = my_project
    my_project = 'Circular Mandala' + Tm.project_time
    startup_script()
    logger.info('Located @ line 1790 - 1853, 31st module of 48')
    t.my_venv()
    Tm.start_time()
    au.pick_medium_track()
    t.my_angle = a.i_angle[a.i]
    t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
    t.folder_name = my_project + t.my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + t.folder_name)
    turtle.title(t.my_str)
    logger.info(str('The featured angle is     ') + str(round(t.my_angle)))
    R = 255
    G = 255
    B = 255
    L = 0
    C = 0
    H = 0
    Z = 255
    turtle.color(R, G, B)
    turtle.bgcolor(L, C, H)
    t.le.penup()
    t.le.setpos(0, -150)
    t.le.pendown()
    t.le.speed(0)
    t.le.shape("circle")
    t.le.shapesize(1)
    t.le.pensize(1)
    t.le.hideturtle()
    t.le.color(R, G, B)
    for t.iterable in range(200): #200 is default, use lower number for testing
        turtle.bgcolor(L, C, H + t.iterable %299)
        t.le.pensize(10)
        t.le.right(t.my_angle)
        t.le.color(L +t.iterable, C + t.iterable %80, H)
        t.le.forward(t.iterable  * t.phi)
        f.save_thumb()
        for g in range(4):
            R = 101 + t.iterable %133
            Y = 101 - t.iterable %130
            B = 25 + t.iterable %100
            t.le.left(t.my_angle)
            t.le.color(R, G - t.iterable, B)
            t.le.pensize(2)
            t.le.circle(175, t.my_angle, 11)
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
    t.my_project = my_project
    my_project = 'Occilating Polygon' + Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(t.my_angle))
        t.iterable = 0
        t.le.pensize(1)
        logger.info('The Angle is   ' + str(t.my_angle))
        while t.iterable <= 149:
            # Default is 149; can use lower number for testing
            R = random.randrange(10,100)
            G = 255  #  random.randrange(171, 255)
            B =  0
            t.le.color( R + t.iterable, G - t.iterable, B + t.iterable)
            turtle.bgcolor(155 - t.iterable, 155 - t.iterable, 10)
            h.pick_red()
            t.lu.dot(t.iterable / 6)
            t.lu.left( - t.my_angle /2)
            t.lu.forward(t.iterable/2 +t.phi)
            t.lu.circle(t.iterable * t.phi, t.my_angle, 6)
            t.lu.rt(t.my_angle)
            t.le.left(t.my_angle)
            t.le.circle( t.iterable * 3, t.my_angle)
            t.lu.dot(t.iterable / 6)
            t.le.pensize(t.iterable / 27)
            t.iterable += 1
            f.save_thumb()
        f.save_final_thumb()
            # The Undo routine which animates the shrinking
        for t.iterable in range(3500): # Default is 1200; can use lower number for testing
            while t.le.undobufferentries():
                t.le.undo()
                t.lu.undo()
                f.save_undo()

                logger.info('Value of iterable: ' + str(t.iterable))
                logger.info('Value of Undobufferentries:  ' + str(t.le.undobufferentries()))
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
    t.my_project = my_project
    my_project = 'Arc-Star' + Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(t.my_angle))
        turtle.title(t.my_str)
        t.iterable = 0
        t.le.pensize(1)
        t.iterable = 0
        t.le.pensize(3)
#             t.le.right(t.my_angle * 2 )
        while t.iterable <= 300:
            if t.iterable <= 255:
                turtle.bgcolor(25, 50, t.iterable)
            else:
                turtle.bgcolor(25,50,255)
            R =  0
            G =  0
            B =  90
            if t.iterable <= 255:
                t.le.color( R + t.iterable , G + t.iterable, B )
            else:
                t.le.color(255, 255, B)
            t.le.left(t.my_angle)
            t.le.penup()
            t.le.forward( t.iterable / t.phi )
            t.le.pendown()
            t.le.pensize(6)
            t.le.fd(t.iterable /t.phi)
            t.le.rt(t.my_angle)
            R = 0
            G = 230
            B = 255
            t.le.color( t.iterable %255, G - t.iterable %54, B - t.iterable %255 )
            t.le.penup()
            t.le.fd(75)
            t.le.pensize(3)
            t.le.circle(24, t.my_angle, 10)
            t.le.pendown()
            t.le.backward(t.iterable)
            t.le.pensize(t.iterable / 72)
            t.le.penup()
            t.le.setposition(0, 0)
            t.le.pendown()
            t.le.color(R + t.iterable %50, t.iterable %75, 0)
            t.le.circle(t.iterable + t.phi, t.my_angle, 5)
            t.iterable += 1
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
    t.my_project = my_project
    my_project = 'Home Star' + Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(10, 50 ,0)
        logger.info(str('The featured angle is  ') + str(t.my_angle))
        t.iterable = 0
        t.le.pensize(1)
        t.iterable = 0
        t.le.pensize(3)
        while t.iterable <= 359: #359 is default
            turtle.bgcolor(10 + t.iterable % 240, 50 + t.iterable % 200, t.iterable %255)
            R = 150
            G = 230
            B = 0
            t.le.color(t.iterable % 104, G - t.iterable %200, t.iterable %254 )
            t.le.left(t.my_angle)
            t.le.penup()
            t.le.fd(t.iterable / t.phi )
            t.le.pendown()
            t.le.pensize(6)
            t.le.fd(t.iterable / t.phi)
            t.le.rt(t.my_angle)
            t.le.penup()
            t.le.fd(27)
            t.le.pensize(3)
            t.le.pendown()
            t.le.circle(12, t.my_angle, 9)
            t.le.backward(t.iterable + t.phi)
            t.le.pensize(t.iterable / 72)
            t.le.penup()
            t.le.setposition(0, 0)
            t.le.pendown()
            t.le.circle(t.iterable, t.my_angle, 5)
            t.iterable += 1
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
    t.my_project = my_project
    my_project = 'Absolute Mandala' + Tm.project_time
    startup_script()
    logger.info('Located @ line 2268- 2328, 35th module of 48')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info(str('The featured angle is     ') + str(t.my_angle))
        turtle.title(t.my_str)
        t.iterable = 0
        t.le.pensize(1)
        t.iterable = 0
        t.le.pensize(3)
        t.le.color('brown', 'green')
        t.le.begin_fill()
        while True:
            t.le.left(t.my_angle)
            t.le.forward(250)
            f.save_thumb()
            if abs(t.le.pos()) < 1:
                break
        t.le.end_fill()
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
    t.my_project = my_project
    my_project = 'Double Take v.' +Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        R = random.randrange(155,255, 5)
        G = 255
        B = 0
        logger.info('The value of color R is    ' + str(R))
        for t.iterable in range(359):
            t.le.pensize(4)
            t.li.pensize(4)
            t.le.left(t.my_angle)
            t.le.color(R, G - t.iterable %255, B + t.iterable %255)
            t.le.forward(t.iterable * t.phi)
            t.li.color(R, G - t.iterable %250, B + t.iterable %250)
            t.li.right(t.my_angle)
            t.li.forward(t.iterable * t.phi)
            f.save_thumb()
        stage_video()
    finalize()   
    




#module_37
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Cloverleaf Cross Mandala.
def cloverleaf():
    global my_project
    t.my_project = my_project
    my_project = 'Cloverleaf v.' +Tm.project_time
    startup_script()
    logger.info('Located @ line 3141 - 3195, 37th module of 48')
    # Select which set of angles to run
    a.i_angle =a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
#             t.le.left(t.my_angle/2)
        t.le.pensize(1)
        t.le.speed(0)
        t.le.pencolor(0, 255,0)
        turtle.bgcolor(0,0,0)
        for t.iterable in range(300):
            if t.iterable <= 255:
                t.le.pencolor(0 + t.iterable, 255 - t.iterable, 0 + t.iterable)
            else:
                t.le.pencolor(255, 0, 255)
            t.le.pensize(t.iterable / 45)    
            t.le.circle(t.iterable, t.my_angle)
            t.le.penup()
            t.le.forward(t.iterable)
            t.le.pendown()
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
    global my_project
    t.my_project = my_project
    my_project = 'Cloverleaf Extended v.' +Tm.project_time
    startup_script()
    logger.info('Located @ line 3141 - 3268, 38th module of 48')
    # Select which set of angles to run
    a.i_angle =a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_extended_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        logger.info('Presenting  ' + str(t.my_str))
        t.folder_name = my_project + t.my_key
        logger.info('The folder name is   ' + str(t.folder_name))
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        logger.info('Starting First Pass at  ' + str(Tm.my_time))
        t.le.pensize(5) #First Pass
        t.le.speed(0)
        t.le.pencolor(0, 255,0)
        turtle.bgcolor(0,0,0)
        
        while t.iterable <= 300:
            if t.iterable <= 251:
                t.le.pencolor(0 + t.iterable, 255 - t.iterable, 0 + t.iterable)
            else:
                t.le.pencolor(255, 0, 255)
            t.le.circle(t.iterable, t.my_angle)
            t.le.penup()
            
            t.le.forward(t.iterable)
            t.le.pendown()
            f.save_thumb()
            t.iterable += 1
            
        logger.info('Starting Second Pass at  ' + str(Tm.my_time))
        t.le.pensize(5) # Second Pass
        t.le.speed(0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
        logger.info('The value of t.iterable is   ' + str(t.iterable))
        while t.iterable <= 605:
            if count <= 253:
                t.le.pencolor(255 - count, 255 - count, count)
            else:
                t.le.pencolor(0, 0, 255)
            t.le.circle(count, t.my_angle)
            t.le.penup()
            
            t.le.forward(count)
            t.le.pendown()
            f.save_thumb()
            count += 1
            t.iterable += 1
        logger.info('Starting Third Pass at  ' + str(Tm.my_time))
        t.le.pensize(3) # Third Pass
        t.le.speed(0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
        logger.info('The value of t.iterable is   ' + str(t.iterable))
        while t.iterable <= 910:
            if count <= 254:
                t.le.pencolor(count, 255 - count, 255 - count)
            else:
                t.le.pencolor(255, 0, 0)
            t.le.circle(count, t.my_angle)
            t.le.penup()
            
            t.le.forward(count)
            t.le.pendown()
            f.save_thumb()
            count += 1
            t.iterable += 1
        logger.info('Starting Fourth Pass at  ' + str(Tm.my_time)) 
        t.le.pensize(2) # Fourth Pass
        t.le.speed(0)
        t.le.pencolor(0, 255,0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
#         t.le.left(t.my_angle)
        logger.info('The value of t.iterable is   ' + str(t.iterable))
        while t.iterable <= 1215:
            if count <= 255:
                t.le.pencolor(255 - count, count, 255- count)
            else:
                t.le.pencolor(0, 255, 0)
            t.le.circle(count, t.my_angle)
            t.le.penup()
            
            t.le.forward(count)
            t.le.pendown()
            f.save_thumb()
            count += 1
            t.iterable += 1
        logger.info('The value of t.iterable is   ' + str(t.iterable))    
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()





#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Majestic Extended Mandala.
def majestic_mandala_extended():
    global my_project
    t.my_project = my_project
    my_project = 'Majestic Mandala Extended v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 3074 - 3204, 39th module of 48')
    # Select which set of angles to run
    a.i_angle =a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_extended_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        
        t.le.pensize(5) #First Pass
        t.le.speed(0)
        t.le.pencolor(0, 255,0)
        turtle.bgcolor(0,0,0)
        logger.info('Starting First Pass....')
        while t.iterable <= 300:
            if t.iterable <= 251:
                t.le.pencolor(t.iterable, 255 - t.iterable, t.iterable)
            else:
                t.le.pencolor(255, 0, 255)
            t.le.left(t.my_angle)
            t.le.forward(t.iterable * t.phi)
            t.le.penup()
            t.le.left(t.my_angle)
            t.le.forward(t.iterable)
            t.le.pendown()
            t.le.left(t.my_angle)
            t.le.forward(t.iterable + t.pi)
            f.save_thumb()
            t.iterable += 1
            
        logger.info('Starting Second Pass...')    
        t.le.pensize(5) # Second Pass
        t.le.speed(0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
        logger.info('The value of t.iterable is   ' + str(t.iterable))
        while t.iterable <= 605:
            if count <= 253:
                t.le.pencolor(255 - count, 255 - count, count)
            else:
                t.le.pencolor(0, 0, 255)
            t.le.left(t.my_angle)
            t.le.forward(count * t.phi)
            t.le.penup()
            t.le.left(t.my_angle)
            t.le.forward(count)
            t.le.pendown()
            t.le.left(t.my_angle)            
            t.le.forward(count + t.pi)
            
            f.save_thumb()
            count += 1
            t.iterable += 1
        logger.info('Starting Third Pass....')    
        t.le.pensize(3) # Third Pass
        t.le.speed(0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
        logger.info('The value of t.iterable is   ' + str(t.iterable))
        while t.iterable <= 910:
            if count <= 254:
                t.le.pencolor(count, 255 - count, 255 - count)
            else:
                t.le.pencolor(255, 0, 0)
            t.le.left(t.my_angle)
            t.le.forward(count * t.phi)
            t.le.penup()
            t.le.left(t.my_angle)
            t.le.forward(count)
            t.le.pendown()
            t.le.left(t.my_angle)
            t.le.forward(count + t.pi)
            f.save_thumb()
            count += 1
            t.iterable += 1
        logger.info('Starting Fourth Pass...')   
        t.le.pensize(2) # Fourth Pass
        t.le.speed(0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
#         t.le.left(t.my_angle)
        logger.info('The value of t.iterable is   ' + str(t.iterable))
        while t.iterable <= 1215:
            if count <= 255:
                t.le.pencolor(count, count, 255 - count)
            else:
                t.le.pencolor(255, 255, 0)
            t.le.left(t.my_angle)
            t.le.forward(count * t.phi)
            t.le.penup()
            t.le.left(t.my_angle)
            t.le.forward(count)
            t.le.pendown()
            t.le.left(t.my_angle)
            t.le.forward(count + t.pi)
            f.save_thumb()
            count += 1
            t.iterable += 1
        logger.info('The value of t.iterable is   ' + str(t.iterable))    
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#module_41
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def glorious_mandala():  # Based on Awesome Manadala
    global my_project
    t.my_project = my_project
    my_project = 'Glorious Mandala v.' + Tm.project_time
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
        t.my_angle =  a.i_angle[a.i]
        au.pick_medium_track()
        make_folder()
        turtle.bgcolor(0,0,0)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        logger.info('The featured angle is     ' + str(t.my_angle))
        R = 255
        G = 255
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        turtle.bgcolor(10, 255, 0)
        t.la.right(t.my_angle * 2)
        t.lb.right(t.my_angle * 2)
        while  t.iterable <= 600: # 359 is default, use lower number for testing.
            h.bg_fade_green_to_dark()
            if t.iterable <= 255:
                t.lb.pencolor(L, M + t.iterable % 50, N + t.iterable)
                t.la.pencolor(R - t.iterable, G - t.iterable, Z + t.iterable %100)
            else:
                h.pick_gold()
                h.pick_blue()
            t.la.left(t.my_angle)
            t.la.forward(t.iterable / 9)
            t.lb.circle(t.iterable / 6, - t.my_angle, 6)
            t.la.left(t.my_angle)
            t.la.penup()
            t.lb.penup()
            t.la.right(t.my_angle)
            t.la.forward(t.iterable / 6)
            t.lb.rt(t.my_angle)
            t.la.pendown()
            t.lb.pendown()
            t.la.forward(t.iterable / t.phi)
            t.lb.forward(t.iterable / t.phi)
            t.la.left(t.my_angle)
            t.la.backward(t.iterable / 6)
            t.la.pensize(t.iterable / 110)
            t.lb.pensize(t.iterable / 112)
            t.iterable += 1
            t.bg_count += 1
            f.save_thumb()
        stage_video()
    finalize()
    
    


#module_42
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def glorious_mandala_extended():  # Based on Awesome Manadala
    global my_project
    t.my_project = my_project
    my_project = 'Glorious Mandala Extended v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 3391- 3317, 42nd module of 48.')
    t.my_venv()
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        logger.info('===============================================================================')
        t.my_venv()
        Tm.start_time()
        t.my_angle =  a.i_angle[a.i]
        au.pick_medium_track()
        t.my_str = my_project + '    featuring ' + str(round(t.my_angle)) + '  Degree Angles  with   ' + au.my_track
        logger.info('Presenting  ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        logger.info('The featured angle is     ' + str(t.my_angle))
        R = 255
        G = 255
        B = random.randrange(112,155, 1)
        logger.info('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 150, 1)
        logger.info('The value of hue /L/ is   ' + str(L))
        E = random.randrange(150, 255, 1)
        logger.info('The value of hue /E/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        t.iterable = 0
        turtle.bgcolor(10, 255, 255)  # First Pass
        logger.info('Starting First Pass.....')
        while t.iterable < 252: # 359 is default, use lower number for testing.
            if t.iterable <= 255:
                turtle.bgcolor(X- t.iterable, Y - t.iterable, Z)
                t.me.pencolor(L, M + t.iterable, N + t.iterable)
                t.le.pencolor(B - t.iterable % 100, G - t.iterable, Z + t.iterable %200)
            else:
                turtle.bgcolor(0, 0, 10)
                h.pick_random()
                h.pick_light()
            t.le.left(t.my_angle)
            t.le.forward(t.iterable /2)
            t.me.circle(t.iterable, - t.my_angle, 6)
            t.le.pensize(t.iterable /27)
            t.le.left(t.my_angle)
            t.le.penup()
            t.me.penup()
            t.le.forward(t.iterable)
            t.me.pensize(t.iterable /36)
            t.me.rt(t.my_angle)
            t.le.pendown()
            t.me.pendown()
            t.le.forward(t.iterable / t.phi)
            t.me.forward(t.iterable / t.phi)
            t.iterable += 1
            f.save_thumb()
        logger.info('Starting Second Pass....')    
        # Second Pass
        count = 0
        t.me.penup()
        t.le.penup()
        t.me.setpos(0,0)
        t.le.setpos(0,0)
        t.me.pendown()
        t.le.pendown()
        t.me.speed(0)
        t.le.speed(0)
        logger.info('Starting Third Pass.....')
        while t.iterable < 490: # 359 is default, use lower number for testing.
            turtle.bgcolor(0,0,10)
            if count <= 155:
                t.me.pencolor(M + count, N + count, L)
                t.le.pencolor(Z + count %100, R - count, G)
            else:
                h.pick_random()
                h.pick_light()
            t.le.left(t.my_angle)
            t.le.forward(count /2)
            t.me.circle(count, - t.my_angle, 6)
            t.le.pensize(count /49)
            t.le.left(t.my_angle)
            t.le.penup()
            t.me.penup()
            t.le.forward(count)
            t.me.pensize(count /144)
            t.me.rt(t.my_angle)
            t.le.pendown()
            t.me.pendown()
            t.le.forward(count / t.phi)
            t.me.forward(count / t.phi)
            count += 1
            t.iterable += 1
            f.save_thumb()
        stage_video()
    finalize()   
   
    



#module_43
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Independence_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Independence Mandala v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 3521- 3590, 43rd module of 48')
    t.my_venv()
    a.i_angle = a.i_angle_auto # Select set of angles to use from the -my_angles- module.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using list comprehension
    # s.title_screen() # Commented out to facilitate accurate a/v processing of the .png images
    t.my_title = str('Featuring Independence Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    logger.info(str(t.my_title))
    for a.i  in range( len(a.i_angle)):
        logger.info('===============================================================================')
        t.my_venv()
        logger.info(Tm.start_time())
        t.my_angle =  a.i_angle[a.i]
        au. pick_medium_track()
        t.my_str = my_project + '  featuring '+ str(round(t.my_angle)) + '  Degree Angles   ' + 'with  ' + '-' + au.my_track
        logger.info('Presenting  ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(10,0,10)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        logger.info('The featured angle is     ' + str(t.my_angle))
        logger.info('..........................................................................................................................................................................................')
        while t.iterable <= 300:
            t.le.color( 0, 0, 255) #Blue
            t.le.left(t.my_angle)
            t.le.forward(t.iterable + t.phi)
            t.le.pensize(t.iterable / 27)
            t.me.color(255,0,0) #Red
            t.me.right(t.my_angle)
            t.me.forward(t.iterable * t.phi)
            t.me.pensize(t.iterable / 45)
            t.ce.color( 255, 255, 255) #White
            t.ce.forward(t.iterable * t.phi)
            t.ce.right(t.my_angle)
            t.ce.pensize(t.iterable /36)
            t.ce.forward(t.iterable /2)
            t.iterable += 1
#             time.sleep(9) #for testing only. Comment out normally
            f.save_thumb()
        stage_video()
    finalize()  
   
    




#module_44
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wall_show():
    global my_project
    t.my_project = my_project
    my_project = 'Wall Show v.' + Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        logger.info(t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        logger.info(t.folder_name)
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        t.iterable = 0
        turtle.bgcolor(30,255,60)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        logger.info('The featured angle is     ' + str(t.my_angle))
        logger.info(('The value of t.rand_num is   ')  + str(t.rand_num))
        logger.info(('The value of t.rand_pick is   ')  + str(t.rand_pick))
        logger.info('......................................................................................')
        while t.iterable <= 255:
            R =  0
            G =  150
            B =  255
            t.le.color( R + t.iterable, G - t.iterable % 130, B - t.iterable)
            t.le.forward(t.iterable * t.phi)
            t.le.left(t.my_angle)
            t.le.pensize(t.iterable /36)
            t.le.color(t.iterable, t.rand_num, 255 - t.iterable)
            t.le.right(t.my_angle)
            t.le.circle(t.iterable / 3, t.my_angle, 6)
            t.ce.color( B - t.iterable, G - t.iterable % 150, R + t.iterable )
            t.ce.forward(t.iterable * t.phi)
            t.ce.right(t.my_angle)
            t.ce.forward(t.iterable * t.phi)
            t.ce.pensize(t.iterable / 27)
            t.ce.color(255 - t.iterable, t.iterable, t.rand_pick)
            t.iterable += 1
            turtle.bgcolor(30, 256 - t.iterable, 60)
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
    t.my_project = my_project
    my_project = 'Wall Show Extended v.' + Tm.project_time
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
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        logger.info(t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        logger.info(t.folder_name)
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        t.iterable = 0
        turtle.bgcolor(30,255,60)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))
        logger.info('The featured angle is     ' + str(t.my_angle))
        logger.info(('The value of t.rand_num is   ')  + str(t.rand_num))
        logger.info(('The value of t.rand_pick is   ')  + str(t.rand_pick))
        logger.info('......................................................................................')
        while t.iterable <= 250:
            R =  0
            G =  150
            B =  255
            t.le.color( R + t.iterable, G - t.iterable % 130, B - t.iterable)
            t.le.forward(t.iterable * t.phi)
            t.le.left(t.my_angle)
            t.le.pensize(t.iterable /36)
            t.le.color(t.iterable, t.rand_num, 255 - t.iterable)
            t.le.right(t.my_angle)
            t.le.circle(t.iterable / 3, t.my_angle, 6)
            t.ce.color( B - t.iterable, G - t.iterable % 150, R + t.iterable )
            t.ce.forward(t.iterable * t.phi)
            t.ce.right(t.my_angle)
            t.ce.forward(t.iterable + t.phi)
            t.ce.pensize(t.iterable / 27)
            t.ce.color(255 - t.iterable, t.iterable, t.rand_pick)
            t.iterable += 1
            turtle.bgcolor(30, 256 - t.iterable, 60)
            f.save_thumb()
        t.le.penup()
        t.ce.penup()
        t.le.setpos(0,0)
        t.ce.setpos(0,0)
        t.le.pendown()
        t.ce.pendown()
        t.le.speed(0)
        t.ce.speed(0)
        count = 0    
        while t.iterable <= 503:
            R =  255
            G =  150
            B =  0
#             logger.info(str(t.le.color))
            t.le.color(R - count % 255, G - count % 130, B + count %255)
            t.le.forward(count * t.phi)
            t.le.left(t.my_angle)
            t.le.pensize(count /36)
            t.le.color(R - count, t.rand_num, count)
            t.le.right(t.my_angle)
            t.le.circle(count / 3, t.my_angle, 6)
            t.ce.color(R - count % 255, G - count % 150, B + count % 255 )
            t.ce.forward(count * t.phi)
            t.ce.right(t.my_angle)
            t.ce.forward(count * t.phi)
            t.ce.pensize(count / 27)
            t.ce.color(R - count % 255, t.rand_num, t.rand_pick)
            count += 1
            t.iterable += 1
            f.save_thumb()
        t.le.penup()
        t.ce.penup()
        t.le.setpos(0,0)
        t.ce.setpos(0,0)
        t.le.pendown()
        t.ce.pendown()
        t.le.speed(0)
        t.ce.speed(0)
        count = 0
        while t.iterable <= 758:
            R =  150
            G =  0
            B =  255
            t.le.color(R - count % 145, count, B - count % 255)
            t.le.forward(count * t.phi)
            t.le.left(t.my_angle)
            t.le.pensize(count /36)
            t.le.color(count, t.rand_num, B - count % 255)
            t.le.right(t.my_angle)
            t.le.circle(count / 3, t.my_angle, 6)
            t.ce.color( R - count % 100, B - count % 255, t.rand_pick)
            t.ce.forward(count * t.phi)
            t.ce.right(t.my_angle)
            t.ce.forward(count * t.phi)
            t.ce.pensize(count / 27)
            t.ce.color(R - count % 150, count % 255, t.rand_pick)
            count += 1
            t.iterable += 1
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
    t.my_project = my_project
    my_project = 'Black Seed v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 3803- 3917, 46th module of 48')
    t.my_venv()
    t.le.speed(30)
    t.le.pensize(36)
    t.ce.speed(30)
    t.ce.pensize(54)
    t.ce.pencolor(255,255,255)
    length = 234
    my_image = 'TBD'
    t.my_angle = 135 # 60 is default
    my_base = int(3600/ t.my_angle) # for loop integrity of the number of loops of the ce pen
#     a.i_angle = a.i_angle_auto # Select set of angles to use.
#     str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   
    # s.title_screen()
    for a.i  in range( length):
        logger.info('===============================================================================')
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
#         t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        logger.info(t.my_str)
        t.folder_name = my_project + t.my_key
        logger.info(t.folder_name)
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        logger.info('The soundtrack being used for this show is: ' + str(au.my_track))  
        logger.info('The featured angle is     ' + str(t.my_angle))
        t.le.speed(30)
        t.le.pensize(36)
        t.ce.speed(30)
        t.ce.pensize(54)
        t.ce.pencolor(255,255,255)
        global b
        t.iterable = 0
        for x in range(3): # 3 is default
            if x == 0:
                 b = t.iterable , t.iterable % 18, t.iterable % 63
            elif x == 1:
                 b = t.iterable % 63, t.iterable, t.iterable % 18
            else:
                b = t.iterable % 18, t.iterable % 63, t.iterable

            for i in range(my_base):
                t.ce.left(t.my_angle)
                t.ce.circle(length)
                t.iterable = 0
            while t.iterable <= 254:
                if x == 0:
                    b = t.iterable, t.iterable % 18, t.iterable % 33
                elif x == 1:
                    b = t.iterable % 33, t.iterable, t.iterable % 18
                else:
                    b = t.iterable % 18, t.iterable % 33, t.iterable
                    t.le.pencolor(b)
                logger.info('Base is:  ' + str(my_base))
                logger.info('t.iterable  :' + str(t.iterable))
                logger.info('Pen color:  ' + str(b))
                logger.info(' x = ' + str(x))
                t.le.left(t.my_angle)
                t.le.circle(length)
                f.save_thumb()
                t.iterable += 1

                del t.iterable
                gc.collect()
                t.iterable = 255
                while t.iterable >= 2:
                    if x == 0:
                        b = t.iterable , t.iterable % 33, t.iterable % 18
                    elif x == 1:
                        b = t.iterable % 18, t.iterable, t.iterable % 33
                    else:
                        b = t.iterable % 33, t.iterable % 18, t.iterable
                    t.le.pencolor(b)
                    logger.info('t.iterable  :' + str(t.iterable))
                    logger.info('Pen color:  ' + str(b))
                    logger.info(' x = ' + str(x))
                    t.le.left(t.my_angle)
                    t.le.circle(length)
                    f.save_thumb()
                    t.iterable -= 1
                f.save_final_thumb()
                turtle.setup(5,5)
                f.set_vid_env()
                f.sync_av()
                reset_all()
                Tm.end_time()
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('************************************************************************')
    reset_all()




#  module_47
#+++++++++++MODULE DARK MANDALA EXTENDED+++++++++++++++++++++++++++++++++++++++++++++++++++++
def dark_mandala_extended():
    global my_project
    t.my_project = my_project
    my_project = 'A Dark Mandala Extended v.' + Tm.project_time
    startup_script()
    logger.info('Located @ line 3662 - 3828,   47th module of 48')
    t.my_venv()
     # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        au.get_special_5_min_track()
#         au.pick_medium_track()
        make_folder()
        turtle.bgcolor(255, 255,100)
        my_iteration =280 # 300 is default; use lower number for testing
        t.bg_count = 0
        print ("The pick_dark pen is:  ", h.hue_dict ['pick_dark']  )
        print ("The pick_indigo pen is':   ", h.hue_dict ['pick_indigo']  )
        print ("The pick_magenta pen is':   ", h.hue_dict ['pick_magenta']  )
        while t.iterable <= my_iteration:  # First Loop of 3
            h.bg_fade_dark_to_yellow()
            h.pick_magenta() #pen t.me
            h.pick_dark()  # pen t.lz
            h.pick_indigo() # pen t.li
            
            t.lz.right(t.my_angle / 2) # Dark pen
            t.lz.pensize(t.iterable / 54)
            t.lz.circle(t.iterable / 3, t.my_angle, 6)
            t.lz.penup()
            t.lz.backward(t.iterable / t.phi + t.iterable)
            t.lz.pendown()
            
            t.li.right(t.my_angle) # Indigo pen
            t.li.pensize(t.iterable / 54)
            t.li.backward(t.iterable / t.phi)
            
            t.lz.right(t.my_angle / 2) # Dark pen
            t.lz.forward(t.iterable  / 2)
            
            t.li.right(t.my_angle)  # Indigo pen
            t.li.forward(t.iterable )
            
            t.lz.penup()  #Dark pen
            t.lz.right(t.my_angle)
            t.lz.forward(t.iterable/9)
            t.lz.pendown()
            t.lz.forward(t.iterable * t.phi)
            
            t.li.backward(t.iterable / t.phi) # Indigo pen
            t.li.circle(t.iterable /3, - t.my_angle, 9)
            #make dots
            t.me.pensize(t.iterable/24) # Magenta pen
            t.me.left(t.my_angle / 2)
            t.me.dot(t.iterable /24)
            t.me.penup()
            t.me.backward(t.iterable)
            t.me.pendown()
            t.me.forward(t.iterable / 60)
            f.save_thumb()
            t.iterable += 1
            t.bg_count += 1
        logger.info('The value of t.iterable is   ' + str(t.iterable))
        count = 0
        t.bg_count = 0
        t.lb.setpos(0,0)
        t.lg.setpos(0,0)
        t.le.setpos(0,0)
        while   count  <= my_iteration: # Second Loop of 3
            h.bg_fade_yellow_to_dark()
            h.pick_blue() #pen t.lb
            h.pick_green()  # pen t.lg
            h.pick_light() # pen t.le
            
            t.le.right(t.my_angle / 2) # Light pen
            t.le.pensize(count / 54)
            t.le.circle(count / 3, t.my_angle, 6)
            t.le.penup()
            t.le.backward(count / t.phi  + count)
            t.le.pendown()
            
            t.lg.right(t.my_angle) # Green pen
            t.lg.pensize(count / 54)
            t.lg.backward(count / t.phi)
            
            t.le.right(t.my_angle / 2) # Light pen
            t.le.forward(count  / 2)
            
            t.lg.right(t.my_angle)  # Green pen
            t.lg.forward(count )
            
            t.le.penup()  #Light pen
            t.le.right(t.my_angle)
            t.le.forward(count/9)
            t.le.pendown()
            t.le.forward(count * t.phi)
            
            t.lg.backward(count / t.phi) # Green pen
            t.lg.circle(count /3, - t.my_angle, 9)
            #make dots
            t.lb.pensize(count/24)   # Blue pen 
            t.lb.left(t.my_angle / 2)
            t.lb.dot(count /24)
            t.lb.penup()
            t.lb.backward(count)
            t.lb.pendown()
            t.lb.forward(count / 60)
            count += 1
            t.iterable += 1
            t.bg_count += 1
            f.save_thumb()
        logger.info('The value of t.iterable is   ' + str(t.iterable))    
        count = 0
        t.bg_count = 0
        t.lz.penup()
        t.lz.setpos(0,0)
        t.lz.pendown()
        t.la.setpos(0,0)
        t.lu.setpos(0,0)
        while count  <= my_iteration: # Third (Final) Loop
            h.bg_fade_dark_to_yellow()
            h.pick_dark() #pen t.lz
            h.pick_gold()  # pen t.la
            h.pick_red() # pen t.lu
           
            t.lu.right(t.my_angle / 2) # Red pen
            t.lu.pensize(count / 54)
            t.lu.circle(count / 3, t.my_angle, 6)
            t.lu.penup()
            t.lu.backward(count / t.phi + count)
            t.lu.pendown()
            
            t.lz.right(t.my_angle) # Dark pen
            t.lz.pensize(count / 54)
            t.lz.backward(count / t.phi)
            
            t.lu.right(t.my_angle / 2) # Red pen
            t.lu.forward(count  / 2)
            
            t.lz.right(t.my_angle)  # Dark pen
            t.lz.forward(count )
            
            t.lu.penup()  #Red pen
            t.lu.right(t.my_angle)
            t.lu.forward(count/9)
            t.lu.pendown()
            t.lu.forward(count * t.phi)
            
            t.lz.backward(count / t.phi) # Dark pen
            t.lz.circle(count /3, - t.my_angle, 9)
            #make dots
            t.la.pensize(count/24)    
            t.la.left(t.my_angle / 2) # Gold pen
            t.la.dot(count /24)
            t.la.penup()
            t.la.backward(count)
            t.la.pendown()
            t.la.forward(count / 60)
            t.iterable += 1
            count += 1
            t.bg_count += 1
            f.save_thumb()
        logger.info('The value of t.iterable is   ' + str(t.iterable))    
        stage_video()
    finalize()




#  module_48
#**************************************************************************************************************
  # First Published to YouTube on 11/21/2021
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def awesome_mandala_old():
    global my_project
    t.my_project = my_project
    my_project = 'Awesome Mandala v.' + Tm.project_time
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
        logger.info(str('The featured angle is     ') + str(t.my_angle))
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
        h.pick_gold() #Pen la
        t.la.left(t.my_angle/2)
        t.lm.left(t.my_angle/2)
        for t.iterable in range(354):  # 450 is default, use any number
            h.pick_gold() #Pen la
            if t.iterable <= 255:
                turtle.bgcolor(X, Y - t.iterable, Z - t.iterable)
            else:
                turtle.bgcolor(X, 0, 0)
            t.la.pensize(t.iterable/120)
            t.la.left(t.my_angle)
            t.la.forward(t.iterable) # /t.phi
            t.lm.pensize(t.iterable / 120)
            t.lm.rt(t.my_angle)
            if t.iterable <= 252:
                t.lm.pencolor(L, M - t.iterable, M - t.iterable)
            else:
                t.lm.pencolor(L, 3, X)
            t.lm.circle(t.iterable, - t.my_angle, 6)
            f.save_thumb()
            logger.info('The Value of color B is    ' + str(B))
            logger.info('The Value of color L is    ' + str(L))
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
#  This first group of modules are extended versions of their parent script, as indicated by their name. The are set to also empoly the list of extended music clips.
'''
Run medium_clips
'''
mystical_mandala() #Working ok as of 1/1 2023, still an issue with the log file all rolling up into a single one per run, which is ok.
# glorious_mandala_extended()  #Created 11/13/2022 Located @ line 2990- 3111, 32nd module of 48.  # 2.43 minutes

# awesome_mandala()
# awesome_mandala_extended() #Created 11/7/2022 'Located @ line 1242 - 1342, 3.57 minutes
# awesome_mandala_old()
colorful_mandala_extended() # Tested and verified on 1/3/2023; 'Located @ line 260 - 385,  3rd module of 48', created on 11/6/2022 
# wall_show_extended() #Located @ line 3266- 3393, 34th module of 41.
# brave_mandala_extended() #Located @ line 1645 -1736, 20th module of 48
# brave_mandala_decimated()
dark_mandala_extended() # Tested and verified on 1/6/2023; Created 1/4/2023; Located at lines 3717 - 3873; 47th module of 48.

'''
Run long_clips
'''
# cloverleaf_extended() #Located @ line 2648 - 2770, 31st module of 48' Created 11/ 17/2022
# majestic_mandala_extended()  # Created 11/17/2022; Located @ line 3300 - 3442, 39th module of 48' Derived from cloverleaf_extended; employs lines instead of circles

'''Run short clips
'''

'===================================================================================================================================================================='
#  This second group of modules specifies a single angle; has no looping lists of angles

# basic_yin_yang()  # ( module_1)   Tested and verified on 1/3/2023; Located @ line 165 - 195, 1st module of 48. An animated rendition of the ancient chinese yin-yang graphic. My original; currently
                    # the most popular one on YouTube. Added the working do_video on 1/14/2022 which converts the png files/
                    #to gif, mp4, and avi files. Successfully automated video (.avi) creation 1/20/2022.
                    #Successfully lengthened and added long audio clips on 8/17/2022.


# growing_yin_yang() #module_3 12 of 48, Published to YouTube 11/11/2021, Need to work on further as of 4/3/2022


# circular_mandala_205()  # module_4 25 of 48; Added 12/9/2021 (Edited from Mandala_160_09292020) Processed to mp4 12/9/2021
'======================================================================================================================================================================='
# This third group of modules specifies a list of angles to loop

colorful_mandala() # module_2; Tested and verified on 1/3/2023; Row 200 - 254, #2 of 48 
jagged_multigram() # module_4 #Tested and verified on 1/4/2023; Located @ line 397 - 466, 4th module of 48' 4 of 48, Published to YouTube on 11/2/2021
hued_polygonial() # module_5; Tested and verified 1/4/2023; Rows 465 - 515,   5th module of 48. Features Blue and Red Hues. Modified 12/17/2021 Updated to automate video creation# 
Fantastic_Mandala() # module_6 Tested and verified 1/4/2023; Located @ line 520 - 576,   6th module of 48. Works well. Updated to automate video creation Implemented 't.phi Offset' Angle on 4/28/2022.
dark_mandala() #module_7 Tested and verified 1/4/2023; Rows 568 - 640, 7 of 48, Revised 1/4/2023
iridescent_polygram()  # module_8; Tested and verified 1/4/2023; Row 645 - 723, 8 of 48; Modified 1/2/2022 Updated to automate video creation
bold_mandala()  # module_9 Modified, tested and verified on 1/8/2023; Located @ line 713 - 782, 9th module of 48', Updated to automate video creation  Implemented 't.phi Offset' Angle on 4/28/2022.
# animated_abstraction()  #  module_9 10 of 48, Thumbs created 11/21/2021
# animated_hued_polygram()  # module_13  Located @ line 929 - 989, number 13 of 48, created 11/14/2021; added print to file 3/1/2022
awesome_mandala()  #  Tested and verified on 1/7/2023. module_15 15 of 48, Located at lines 1135 - 1189. Processed to mp4 and published to YouTube on 11/21/2021. modified 11/20/2021, This is exceptional.
 
glorious_mandala() # module_18 Tested and verified 1/10/2023; Created 4/6/2022, based on stupendous mandala. Located @ line 3153- 3219, 41st module of 48.
pretty_awesome_mandala() # module_19; Tested and verified 1/10/2023; Located @ line 1331- 1380, 18th module of 48. Derived from awesome_mandala. # Processed 90 degrees to MP4 on 12/15/2021
mighty_awesome_mandala() # Tested and verified 01/11/2023; Located @ line 1385- 1497, 19th module of 48; Based on pretty awesome mandala
# 
# stupendous_mandala() # module_18 Row 1034 - 1101, number 17 of 48. Derived from pretty_awesome_mandala. Created 1/8/2022. added print to file 3/1/2022Features a more prominent center than it's parent.  Works well.
# brave_mandala() #module_19 Located @ line 1386 -1449, Derived from awesome_mandala; 18 of 48
# color_shifting_mandala() # module_20 Rows 1274 - 1327, 19 of 48 work on
# Hued_freedom_star() # module_26 Row 1358 - 1428, 22 of 48; Added 12/4/2021
# arc_star() #module_28 27 of 48; Located at lines 1586 - 1654. Added 01/06/2022. Derived from a Thought Matrix arc-star wriiten by me in 2020.\
#                       # Employs first use of automated creation of angle lists using numpy arange.
# home_star() #module_ 28 of 48; Located at lines 2007 - 2078.  Added 01/06/2022. Derived from a Thought Matrix arc-star scripted by me in 2020.\
# ribbons_mandala()  #module_30  24 of 48; Located at rows 1572 - 1635. Added 12/8/2021 (Edited from Mandala_160_09292020); converted to mult-angles on 1/20/2022
# use_abs() # module_31 29 of 48; Located at line 1890. Uses the abs() function to draw the sides and points such that it continues until the point of origin is reached.
# double_take() # module_32 30 of 48; Located at line 1843 - 1881. Facilitates the creation of a hexagram by using 2 pens drawn\
#                    # with same angles in opposite directions. Using specific angle array named a.i.angle_double.
# cloverleaf() # module_33 31 of 48, Located at line  2247 - 2304. Created 3/6/2022.
# wall_show() # module_34 of 48. Located @ line 2408- 2474. Working on a suitable product to frame and display on a wall. Began development August 2022.
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
turtle.setup(550,550) # Minimized turtle window to observe screen and read shell output
f.move_all() # Moves files to appropriate locations
logger.info('All files have been moved to their final home')
f.sync_mandala_folders()  # Sync video and script folders backups
logger.info('Folders and files have been synced and backed up')
logger.warning('Program is terminating')
turtle.bye()  # End the program;  Default is to leave uncommented.
