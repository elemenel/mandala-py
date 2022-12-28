'''
MASTER MANDALA MAKER (master_mandala_maker.py) author: Leon Hatton
    Dependent upon, in addition to the imported modules from Pypy,
    the following custom modules developed by the author:
        My_template; sets up the enviroment
        my_angles; processes angle selections
        my_hues; selects custom color hues
        my_splash_screen; starts the show; ends the show (not being used due to issues with sort)
        File_scripts; repository for file manipulations, creations, deletions, sorting
        audio_clips; repository of links to audio tracks on the local server
        Timer; provides time/date functionality
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

# global open_shell_out_path
# open_shell_out_path = f.my_work_dir + '/Logs/_log.txt'

if sys.platform.startswith('linux'):
    my_path = '/media/elemen/Inland SSD1'
else:
    my_path = 'M:'

t.my_venv()   #Initializes mandala drawing environments

# Tm.time_functions()   #Initializes time functions

my_project = str('The Novanno Angles')




# my_log_file = f.my_work_dir + '/Make_Mandalas/Logs/' + my_project  + '_' + str(t.file_key) + '_log.txt', 'a', encoding="utf-8"
# 
# Printing to file and to console together
def log_file_console():
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
#     log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/mandalas.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
# log_file_console()




def reset_all():   #Utility to clear screen and reset to sequence next screen drawing
    turtle.clearscreen()
    t.my_pen.reset()
    t.le.reset()
    t.me.reset()
    t.lb.reset()
    t.la.reset()
    t.lg.reset()
    t.ld.reset()
    t.lr.reset()
    t.lc.reset()
    t.ll.reset()
    t.lu.reset()
    t.lm.reset()
    t.li.reset()
    t.lz.reset()
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.info('Pausing 9 seconds for user to manually stop the program at the end of a sub-routine and before the next one starts.................')
#     logging.shutdown()
    time.sleep(9)


turtle.bgcolor(0, 0, 10)

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

length = 255  #Default is 252; any lower number for testing

def my_project():
    my_project = t.my_project
    return my_project

def my_title():
    my_title = turtle.title(t.my_str)

# MODULES
# Index of modules:


#  module_1
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
def basic_yin_yang():
    Tm.set_time()
    Tm.start_time()
    log.info('Starting basic_yin_yang() by Leon Hatton on   ' + str(Tm.my_time))
    log.info('Located @ line 78 - 112, 1st module of 38')
    t.my_venv()
    t.my_project = 'A Yin-Yang Expression'
    t.my_angle = 180
    Tm.start_time()
    au.pick_short_track()
    t.my_str = t.my_project + '   featuring   ' + str( t.my_angle) + '  ' + '    Degree Angles  with  '  + au.my_track
    turtle.title(t.my_str)
    t.folder_name = t.my_project + t.my_key 
    f.make_png_folder()
    os.chdir(f.loc_thumb + t.folder_name)
    time.sleep(3)
    t.iterable = 0
    turtle.bgcolor('goldenrod') # Has to be a neutral shade like grey to contrast the black and white theme.
    while t.iterable <= (600):  #360 is default. Use lower number for testing. The higher the number, the longer the show.
        t.le.pensize(10)
        t.le.color(0,0,0) # 0,0,0 is default (Black)
        t.le.left(-t.my_angle + t.phi)
        t.le.circle(250)
        t.le.color(255,255,255) # 255,255,255 is default (White)
        t.le.left(-t.my_angle)
        t.le.circle(250)
        t.iterable += 1
        f.save_thumb()
    f.save_final_thumb()
    turtle.setup(5,5)
    f.set_vid_env()
    f.sync_av()
    reset_all()



#  module_2
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def colorful_mandala():
    global my_project
    my_project = t.my_project
    my_project = 'A Colorful Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 116 - 186,  2nd module of 46')
    log.info('Ran on:  ' + str(Tm.my_time))
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Colorful Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    log.info(t.my_title)
    # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        log.info('The angle for this mandala is    ' + str(t.my_angle) + '    degrees.')
        t.iterable = 0
        t.li.pensize(1)
        turtle.bgcolor(50,10,10)
        t.la.right(t.my_angle/2)
        t.li.left(t.my_angle/2)
        while t.iterable <= 255:
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
            f.save_thumb()
            t.iterable += 1
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#  module_3
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def colorful_mandala_extended():
    global my_project
    my_project = t.my_project
    my_project = 'A Colorful Mandala Extended'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 190 - 298,  3rd module of 46')
    log.info('Ran on:  ' + str(Tm.my_time))
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto 
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Colorful Extended Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    log.info(t.my_title)
    # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Colorful Mandala Extended'
        au.pick_medium_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
        log.info('The angle for this mandala is    ' + str(t.my_angle) + '    degrees.')
        t.iterable = 0
        t.li.pensize(1)
        turtle.bgcolor(50,10,10)
        t.la.right(t.my_angle/2)
        t.li.left(t.my_angle/2)
        while t.iterable <= 255:
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
            f.save_thumb()
            t.iterable += 1
        # Start second pass
        log.info('Starting second pass')
        t.iterable = 255
        count = 0
        t.la.penup()
        t.li.penup()
        t.la.setpos(0,0)
        t.li.setpos(0,0)
        t.la.pendown()
        t.li.pendown()
        t.li.speed(0)
        t.la.speed(0)
        while t.iterable <= 495:
            R =  0
            G =  140
            B =  255
            if R == 0:
                t.la.color( B - count, count, G - count % 140)
                t.li.color( R + count, 0, B - count)
            else:
                t.la.color( count, G - count %140, B - count %100)
                t.li.color( count, G - count %140, B - count)
            t.la.forward(count * t.phi)
            t.la.left(t.my_angle)
            t.la.pensize(count / 54)
            t.la.right(t.my_angle)
            t.la.circle(count + t.phi, t.my_angle, 6)
            t.li.forward(count + t.phi)
            t.li.right(t.my_angle)
            t.li.forward(count)
            t.li.pensize(count / 45)
            count += 1
            t.iterable += 1
            f.save_thumb()

        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
        # s.end_screen()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()


#  module_4
#**************************************************************************************************************
  # Published to YouTube on 11/2/2021
 #This script features three pens: le, me, and lb. They follow separate yet coordinated routes to compose the mandala.
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def jagged_multigram():
    global my_project
    my_project = t.my_project
    my_project = 'Jagged Multigram'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 301 - 393, 4th module of 46')
    t.my_venv() #Calls the template module
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        my_hue = random.randint(5, 100)
        my_hue_a = random.randint(100, 200)
        turtle.bgcolor(0, 0, 0)
        t.le.speed(0)
        t.me.speed(0)
        t.lb.speed(0)
        t.iterable = 0000
        turtle.title(t.my_str)
        log.info('The angle for this mandala is    ' + str(t.my_angle) + '    degrees.')
        log.info('The value of my_hue is' + '   ' + str(my_hue))
        log.info('The value of my_hue_a is' + '   ' + str(my_hue_a))
        t.iterable = 1
        turtle.bgcolor(0, 0, 0)
        t.le.left(t.my_angle/2)
        t.lb.left(t.my_angle/2)
        t.me.left(t.my_angle/2)
        while t.iterable <= 359: #250 is default. Use lower number for testing. Loops limited by maximum color value of 255.
            R =  my_hue  #Pen le color
            G =  255  #Pen le color
            B =  0  #Pen le color
            L = 255  #Pen me color
            M = my_hue_a  #Pen me color
            N = 0  #Pen me color
            D = 0  #Pen lb color
            E = my_hue  #Pen lb color
            F = 255  #Pen lb color
            t.le.color( R , G - t.iterable % 252, B + t.iterable % 252)
            t.me.color( L - t.iterable % 252, M, N + t.iterable % 252)
            t.lb.color( D + t.iterable % 252, E, F - t.iterable % 252)
            t.le.left(t.my_angle)
            t.me.left(t.my_angle)
            t.lb.left( t.my_angle / t.phi)
            t.le.forward( t.iterable * 1.5 )
            t.me.forward( t.iterable  * t.phi )
            t.lb.forward( t.iterable  * 2)
            t.le.rt(t.my_angle)
            t.me.left( - t.my_angle)
            t.lb.rt( t.my_angle)
            t.me.forward(t.iterable  / 4)
            t.le.forward(t.iterable  / 3)
            t.lb.forward(t.iterable  / 5)
            t.le.circle(t.iterable / 63,  t.my_angle, 5)
            t.me.circle(t.iterable / 72,  t.my_angle)
            t.lb.circle(t.iterable / 54, t.my_angle)
            t.me.pensize(t.iterable  / 50 %25)
            t.le.pensize(t.iterable  / 50 %33)
            t.lb.pensize(t.iterable  / 50 %14)
            turtle.bgcolor(0, 0, t.iterable %252)
            f.save_thumb()
            t.iterable += 1
        turtle.bgcolor(5,9,5)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()





#  module_5
#*****************************************************************************************************************************
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def hued_polygonial():  # Uses 2 pens with offset t.phi angle
    global my_project
    t.my_project = my_project
    my_project = 'Hued Polygonial'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 399 - 472,   5th module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring Hued Polygonial Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    # s.title_screen()
    log.info(t.my_title)
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        t.my_angle = a.i_angle[a.i]
        log.info('The offset angle value is  ' + str(t.my_angle * (t.pi/2)))
        au.pick_short_track()
        t.my_str = my_project +  ' featuring ' + str(round(t.my_angle)) + ' Degree Angles,    ' + t.my_key + 'with   ' + au.my_track
        t.folder_name = t.my_str + '/'
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        h.pick_gold()
        t.la.rt(t.my_angle / 2)
        h.pick_blue()
        t.lb.rt(t.my_angle / 2)
        t.iterable = 0
        t.lb.speed(0)
        t.la.speed(0)
        turtle.bgcolor(a.i + 25 % 100, a.i + 20 %110, a.i + 50 % 250)
        while t.iterable <= 255:    #255 is default. Use lower number for testing.
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
            f.save_thumb()
            t.iterable += 1
        log.info(t.my_str)
        time.sleep(3)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #  #
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#  module_6
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Fantastic_Mandala():  # Uses 2 pens with offset t.phi angle
    global my_project
    t.my_project = my_project
    my_project = 'Fantastic Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 477 - 542,   6th module of 46')
    t.my_venv() # Initializes turtle canvas screen environment
    # Select which set of angles to run using list comprehension method
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        log.info('Presenting' + t.my_str)
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
            t.li.pensize(t.iterable / 18)  #li is the purple hue
            t.le.pensize(t.iterable / 12)
            h.pick_light()
            h.pick_gold()
            h.pick_indigo()
            t.la.right(t.my_angle)
            t.la.fd(t.iterable + t.phi)
            t.le.fd(t.iterable * t.pi/2)
            t.le.circle(t.iterable, t.my_angle) # le is a random light hue.
            t.li.circle(t.iterable, -t.my_angle * t.phi) # This is the offset angle
            f.save_thumb()
            t.iterable += 1
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #  #
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#  module_7
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''#NEEDS SOME REWORKING def dark_mandala(): #Needs work
    global my_project
    t.my_project = my_project
    my_project = 'A Dark Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 547 - 635,   7th module of 46')
    t.my_venv()
     # Select which set of angles to run using list comprehension method
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0, 0,100)
        print ("The pick_random pen is:   ",  h.dict ['pick_random']  )
        print ("The pick_dark pen is:  ", h.dict ['pick_dark']  )
        print ("The pick_indigo pen is':   ", h.dict ['pick_indigo']  )
        print ("The pick_dot pen is':   ", h.dict ['pick_dot']  )
        for t.iterable in range(300):
            if t.iterable > 255:
                t.lz.pencolor(200, 50, 10)
                t.my_pen.color(10, 10, 30)
                turtle.bgcolor(255, 255, 100)
                # s.watermark()
            else:
                turtle.bgcolor(t.iterable, t.iterable, 100)
            h.pick_magenta() #pen t.me
            h.pick_dark()  # pen t.lz
            h.pick_indigo() # pen t.li
#             t.lz.left(t.my_angle)
            for i in range(6):
                t.li.right(t.my_angle)
                t.me.right(t.my_angle)
                t.me.pensize(t.iterable/24)
                t.li.pensize(t.iterable / 54)
                t.lz.pensize(t.iterable / 54)
#             t.lz.circle(t.iterable, t.my_angle)
                t.lz.penup()
                t.lz.backward(t.iterable / t.phi + i)
                t.lz.pendown()
                t.li.forward(t.iterable * t.phi)
                t.lz.right(t.my_angle)
                t.lz.forward(t.iterable + i)
                t.li.right(t.my_angle)
                t.li.forward(t.iterable * t.phi)
#             t.lz.penup()
                t.lz.right(t.my_angle)
                t.me.forward(t.iterable/9)
#             t.lz.pendown()
                t.lz.forward(t.iterable * t.phi)
                t.li.forward(t.iterable * t.phi)
#             t.lz.circle(t.iterable / 2, t.my_angle)

#                 t.li.circle(t.iterable /2, - t.my_angle)
            #make dots
#             t.me.left(t.my_angle)
#             t.me.dot(t.iterable / 6)
#             t.me.penup()
#             t.me.backward(t.iterable)
#             t.me.pendown()
#             t.me.forward(t.iterable / 60)
            f.save_thumb()
        log.info(t.my_str)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #  #
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
'''



#  module_8
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def iridescent_polygram():  # Uses 2 pens with offset t.phi angle
    global my_project
    t.my_project = my_project
    my_project = 'Iridescent Polygram'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 639 - 705,   8th module of 46')
    t.my_venv()
    # Select which set of angles to run;  Favorite angles: 144/5P, 210/12P, 834/TightSpiral,2394/20P,1350/Square
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Iridescent Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    # s.title_screen()
    log.info(t.my_title)
    Tm.start_time()
    for a.i  in range(len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        log.info('Featuring' + t.my_str)
#             s.splash_screen()
        # s.watermark()
        turtle.bgcolor(50, 10, 255)
        t.le.left(t.my_angle*2)
        t.me.rt(t.my_angle*2)
        for t.iterable in range (150):  #255 is default. Use lower number for testing.
            turtle.bgcolor(50 - t.iterable %49, 10 + t.iterable %200, 255 - t.iterable)
            t.le.pensize(t.iterable /9)
            t.me.pensize(t.iterable / 18)
            t.le.right(t.my_angle)
            t.le.forward(t.iterable + t.phi)
            t.me.left(t.my_angle * t.phi)  # This is the offset angle
            t.me.pencolor(random.randint(100,200), random.randint(0,75) + t.iterable %150,  random.randint(175,255) - t.iterable %150)
            t.le.pencolor(random.randint(0,128) + t.iterable %126, random.randint(150,255)- t.iterable %126, random.randint(100, 200))
            t.le.circle( t.iterable - t.pi, -t.my_angle)
            t.me.circle(t.iterable / t.pi, t.my_angle * t.phi, 7) # This is the offset angle
            t.le.pencolor(255,255,random.randint(100, 200))
            t.me.pencolor(255,random.randint(100, 200), 255)
            t.le.dot(t.iterable / t.phi / 18)
            t.me.dot(t.iterable / t.phi / 9)
            f.save_thumb()
        time.sleep(3)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #  #
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()


#  module_9
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def bold_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Bold Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 709 - 775, 8th module of 46')
    t.my_venv()
#     
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '  featuring ' + str( t.my_angle) + ' Degree Angles, with   '  + au.my_track
        log.info('Presenting  ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        t.la.speed(0)
        for t.iterable in range (255):      #255 is default. Use lower number for testing. 300 for audio.
            turtle.bgcolor(255- t.iterable, t.iterable %25, 255 - t.iterable)
            h.pick_indigo() #Indigo hues
            h.pick_gold() #Gold hues
            t.la.left(t.my_angle / 3) #Gold pen
            t.la.penup()
            t.la.setpos(0,0)
            t.la.pendown()
            t.la.pensize(t.iterable / 45)
            t.la.circle(t.iterable, t.my_angle, 5)
            t.li.pensize(t.iterable / 25)  #Indigo pen
            t.li.left(t.my_angle / 5)
            t.li.forward(t.iterable * t.phi)
            t.li.right(t.my_angle)
            t.li.forward(t.iterable)
#             time.sleep(10) #for testing only; comment out to run code
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
# s.end_screen()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    



#  module_10
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''# NEEDS SOME TWEAKING def hued_gradiant():  # Uses 2 pens with offset t.phi angle
    global my_project
    t.my_project = my_project
    my_project = 'Hued Gradiant'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 778 - 860, 10th module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' +  str(round(t.my_angle)) + ' and  ' + str(round (t.my_angle * t.phi)) +'    Degree Angles,   with   '  + au.my_track
        log.info('Presenting   ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        log.info('The offset angle value is  ' + str(t.my_angle * t.phi))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    
'''



#  module_11
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def animated_abstraction():
    global my_project
    t.my_project = my_project
    my_project = 'Animated Abstract'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 862 - 938,   11th module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info('Presenting   ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
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
            f.save_thumb()
            t.iterable += 2
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
   




#  module_12
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gradiant_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Gradiant Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 943 - 1001, 12th module of 46')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info('Presenting   ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
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
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
        reset_all()
        Tm.end_time()
        # s.end_screen()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    



#  module_13
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def growing_yin_yang(): #Published to YouTube 11/11/2021
    global my_project
    t.my_project = my_project
    my_project = 'Growing Animated Yin-Yang'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1007 - 1047, 13th module of 46')
    t.my_venv()
    Tm.start_time()
    au.pick_short_track()
    t.my_angle =180
    t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
    log.info('Presenting   ' + t.my_str)
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
    f.save_final_thumb()
    turtle.setup(5,5)
    f.set_vid_env()
    f.sync_av()
    reset_all()
    Tm.end_time()
    # s.end_screen()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    



#  module_14
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Uses 2 pens with offset t.phi angle
def hued_polygram():
    global my_project
    t.my_project = my_project
    my_project = 'Animated Hued Polygram'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1051 - 1113, 14th module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
     # s.title_screen()
    Tm.start_time()
    for a.i  in range(len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info('Presenting   ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
        turtle.bgcolor(10,100,255)
        log.info(str('The featured angle is     ') + str(t.my_angle))
        for t.iterable in range(length):
            turtle.bgcolor(255 - t.iterable, 50,  255 - t.iterable)
            h.pick_light()
            t.le.right(t.my_angle)
            t.le.forward(t.iterable * t.pi)
            h.pick_indigo()
            t.li.left(-t.my_angle)
            t.li.forward(t.iterable * t.pi)
            h.pick_gold()
            t.la.forward(t.iterable + t.phi)
            h.pick_dot()
            t.ld.dot(t.iterable /36 * t.phi)
            t.la.circle(t.iterable / 9, t.my_angle, 10)
            t.le.pensize(t.iterable / 15)
            t.li.pensize(t.iterable / 18)
            t.la.pensize(t.iterable / 33)
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    



#  module_15
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
'''# def pretty_polygonial(): # NEEDS WORK
    global my_project
    t.my_project = my_project
    my_project = 'Pretty Polygonial'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1118 - 1187, 15th module of 46')
    au.pick_short_track()
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
            au.pick_short_track()
            t.my_str = my_project + ' featuring '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key  + '-' + au.my_track
            t.folder_name = my_project + t.my_key
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            os.chdir(f.loc_thumb + t.folder_name)
            turtle.title(t.my_str)
            turtle.bgcolor(0,0,0)
            log.info(str('The featured angle is     ') + str(t.my_angle))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
        
'''



#  module_16
#**************************************************************************************************************
  # First Published to YouTube on 11/21/2021
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def awesome_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Awesome Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1192 - 1266, 16th module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info('Presenting   ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle))
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
        log.info('The Value of color B is    ' + str(B))
        log.info('The Value of color L is    ' + str(L))
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    
    


#  module_17
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def awesome_mandala_extended():
    global my_project
    t.my_project = my_project
    my_project = 'Awesome Mandala Extended'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1270 - 1398, 17th module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track() # Randomly selects a track from dymaically created medium_clips list
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info('Presenting   ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle))
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
        h.pick_gold() #Pen la
        while t.iterable <= 255:  # First pass
            h.pick_gold() #Pen la
            if t.iterable <= 255:
                turtle.bgcolor(X, Y - t.iterable, Z - t.iterable)
            else:
                turtle.bgcolor(X, 0, 0)
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
            f.save_thumb()
            t.iterable += 1
            
        log.info('The Value of color B is    ' + str(B))
        log.info('The Value of color L is    ' + str(L))
        h.pick_magenta #Pen me
        t.me.penup()
        t.lm.penup()
        t.me.home()
        t.lm.home()
        t.me.pendown()
        t.lm.pendown()
        t.la.pendown()
        t.me.speed(0)
        t.lm.speed(0)
        count = 0
        while t.iterable <= 501:  # 450 is default, use any number Second pass
            h.pick_magenta() #Pen me
            turtle.bgcolor(X, 0, 0)
            t.me.pensize(count/27)
            t.me.forward(count * t.phi)
            t.me.left(t.my_angle)
            t.lm.pensize(count /45)
            t.lm.rt(t.my_angle)
            if count <= 255:
                t.lm.pencolor(R + count, M - count, B)
            else:
                t.lm.pencolor(M, M, X)
            t.lm.circle(count / t.phi, - t.my_angle, 9)
            count += 1
            t.iterable += 1
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
        while t.iterable <= 740:  # 450 is default, use any number Third pass
            h.pick_indigo() #Pen li
            h.pick_gold()  #Pen la
            turtle.bgcolor(X, 0, 0)
            t.li.pensize(count/27)
            t.li.left(t.my_angle)
            t.li.forward(count * t.phi)
            t.lm.pensize(count /45)
            t.lm.rt(t.my_angle)
            t.la.pensize(count/54)
            t.la.left(t.my_angle)
            t.la.backward(count)
            if count <= 255:
                t.lm.pencolor(R + count, M - count, B)
            else:
                t.lm.pencolor(M, M, X)
            t.lm.circle(count / t.phi, - t.my_angle, 9)
            count += 1
            t.iterable += 1
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
        
    
    

#  module_18
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_awesome_mandala():  # Based on Awesome Manadala
    global my_project
    t.my_project = my_project
    my_project = 'Pretty Awesome Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1403- 1474, 18th module of 46')
   
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info('Presenting   ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle))
        R = 0
        G = 255
        B = random.randrange(10, 200, 1)
        log.info('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 200, 1)
        log.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        turtle.bgcolor(10, 255, 255)
        t.le.left(t.my_angle/2)
        t.me.rt(t.my_angle/2)
        for t.iterable in range(253): # 255 is default, use lower number for testing
            if t.iterable <= 255:
                turtle.bgcolor(X- t.iterable, Y - t.iterable, Z)
            else:
                turtle.bgcolor(0, 0, 10)
            t.le.pensize(t.iterable/27)
            t.le.left(t.my_angle)
            t.le.pencolor(R + t.iterable, B, G - t.iterable)
            t.le.forward(t.iterable /6)
            t.me.pensize(3)
            t.me.rt(t.my_angle)
            t.me.pencolor(L, M + t.iterable, N + t.iterable)
            t.me.circle(t.iterable / t.phi, - t.my_angle)
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    
    
    

#  module_19
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def mighty_awesome_mandala():  # Based on pretty_awesome Manadala
    global my_project
    t.my_project = my_project
    my_project = 'Mighty Awesome Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1478- 1607, 19th module of 46')
#     
    t.my_venv()
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
        log.info('Presenting   ' + t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        log.info(str('The featured angle is     ') + str(t.my_angle))
        R = random.randrange(10, 200, 1)
        G = 0
        B = 255
        log.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(10, 200, 1)
        log.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        t.me.left(t.my_angle / 2)
        t.le.left(- t.my_angle / 2)
        t.iterable = 0
        while t.iterable <= 230:
            turtle.bgcolor(X- t.iterable, Y - t.iterable, Z)
            t.le.pensize(t.iterable/48)
            t.le.rt(t.my_angle)
            t.le.pencolor(R, G + t.iterable, B - t.iterable % 100)
            t.le.forward(t.iterable)
            t.me.pensize(t.iterable/24)
            t.me.rt(t.my_angle)
            t.me.pencolor(L, M + t.iterable, X - t.iterable)
            t.me.circle(t.iterable + t.phi, - t.my_angle)
            f.save_thumb()
            t.iterable += 1
        count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        R = random.randrange(1, 150, 1)
        G = 0
        B = 255
        log.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(150, 255, 1)
        log.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        while t.iterable <= 460: # Second pass
            t.le.pensize(count/24)
            t.le.rt(t.my_angle)
            t.le.pencolor(B - count % 100, count, L)
            t.le.forward(count)
            t.me.pensize(count/6)
            t.me.rt(t.my_angle)
            t.me.pencolor(X - count, M + count, R)
            t.me.circle(count + t.phi, - t.my_angle)
            f.save_thumb()
            t.iterable += 1
            count += 1
        count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        R = random.randrange(10, 200, 1)
        G = 0
        B = 255
        log.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(10, 200, 1)
        log.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        while t.iterable <= 690: # Third pass
            t.le.pensize(count/24)
            t.le.rt(t.my_angle)
            t.le.pencolor(count % 100, count, R)
            t.le.forward(count)
            t.me.pensize(count/12)
            t.me.rt(t.my_angle)
            t.me.pencolor(count, L, R)
            t.me.circle(count + t.phi, - t.my_angle)
            f.save_thumb()
            t.iterable += 1
            count += 1
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    
    


#  module_20
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def mystical_mandala():  # Based on pretty_awesome Manadala
    global my_project
    t.my_project = my_project
    my_project = 'Mystical Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1694- 1832, 20th module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        log.info(au.my_audio_clip)
        log.info('The selected track is ' + str(au.my_track))
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info('Presenting  ' + str(t.my_str))
        t.folder_name = my_project + t.my_key
        log.info('The folder name is   ' + str(t.folder_name))
        f.make_png_folder()
        log.info('Starting make_png_folder()....................')
#         log.info('New folder:  ' + str(f.png_folder) + '  has been created')
#         log.info(str(f.png_folder) +'  has been emptied. The folder is now ready for new content.')
        
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        log.info(str('The featured angle is     ') + str(t.my_angle))
        R = random.randrange(10, 200, 1)
        G = 0
        B = 255
        log.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(10, 200, 1)
        log.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        t.iterable = 0
        log.info('Starting first pass')
        while t.iterable <= 250:
            turtle.bgcolor(X- t.iterable, Y - t.iterable, Z)
            t.le.pensize(t.iterable/48)
            t.le.rt(t.my_angle)
            t.le.pencolor(R, G + t.iterable, B - t.iterable % 50)
            t.le.forward(t.iterable * t.phi)
            t.le.rt(t.my_angle)
            t.le.forward(t.iterable / t.phi)
            t.me.pensize(t.iterable/42)
            t.me.rt(t.my_angle)
            t.me.pencolor(L, M + t.iterable, X - t.iterable)
            t.me.circle(t.iterable + t.phi, - t.my_angle, 6)
            t.me.rt(t.my_angle)
            t.me.backward(t.iterable  * t.phi)
            f.save_thumb()
            t.iterable += 1
        count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        R = random.randrange(1, 150, 1)
        G = 0
        B = 255
        log.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(150, 255, 1)
        log.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        log.info('Starting second pass')
        while t.iterable <= 502: # Second pass
            t.le.pensize(count/48)
            t.le.rt(t.my_angle)
            t.le.pencolor(B - count % 50, count, L)
            t.le.forward(count * t.phi)
            t.le.rt(t.my_angle)
            t.le.forward(count / t.phi)
            t.me.pensize(count/42)
            t.me.rt(t.my_angle)
            t.me.pencolor(X - count, M + count, R)
            t.me.circle(count + t.phi, - t.my_angle, 6)
            t.me.rt(t.my_angle)
            t.me.backward(count * t.phi)
            f.save_thumb()
            t.iterable += 1
            count += 1
        count = 0
        t.le.penup()
        t.me.penup()
        t.le.setpos(0,0)
        t.me.setpos(0,0)
        t.le.pendown()
        t.me.pendown()
        R = random.randrange(150, 255, 1)
        G = 0
        B = 255
        log.info('The value of hue /R/ is   ' + str(G))
        L = random.randrange(10, 255, 1)
        log.info('The value of hue /L/ is   ' + str(L))
        log.info('**************************************')
        log.info('Starting third pass')
        while t.iterable <= 756: # Third pass
            t.le.pensize(count/48)
            t.le.rt(t.my_angle)
            t.le.pencolor(count % 25, count, R)
            t.le.forward(count * t.phi)
            t.le.rt(t.my_angle)
            t.le.forward(count / t.phi)
            t.me.pensize(count/42)
            t.me.rt(t.my_angle)
            t.me.pencolor(count, L, R)
            t.me.circle(count + t.phi, - t.my_angle, 6)
            t.me.rt(t.my_angle)
            t.me.backward(count * t.phi)
            f.save_thumb()
            t.iterable += 1
            count += 1
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        log.info('Stopping  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
        reset_all()
        t.my_venv()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    





#  module_21
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def stupendous_mandala():  # Based on Awesome Manadala
    global my_project
    t.my_project = my_project
    my_project = 'Stupendous Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1757- 1843, 21st module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        log.info('===============================================================================')
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info('The soundtrack being used for this show is:   ' + au.my_track)
        log.info('The featured angle is     ' + str(t.my_angle))
        R = 255
        G = 255
        B = random.randrange(150, 255, 20)
        log.info('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 150, 25)
        log.info('The value of hue /L/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        turtle.bgcolor(10, 255, 255)
#             t.le.rt(t.my_angle /2)
        t.me.rt(t.my_angle)
        for t.iterable in range(300): # 255 is default, use lower number for testing; 300 for audio sync.
            h.pick_red()
            if t.iterable <= 255:
                turtle.bgcolor(X- t.iterable, Y - t.iterable, Z)
                t.me.pencolor(L, M + t.iterable, N + t.iterable)
                t.lu.pencolor(R - t.iterable, B, G - t.iterable)
            else:
                turtle.bgcolor(0, 0, 10)
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
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
            #  #
        t.my_venv()
        Tm.end_time()
# s.end_screen()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#  module_22
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def multi_hued_polygram():
    global my_project
    t.my_project = my_project
    my_project = 'Multi-Hued Polygram'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1848- 1914, 22nd module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        t.iterable = 0
        t.le.right(t.my_angle / 2)
        t.le.speed(0)
        t.la.speed(0)
        N =  random.randint(1, 100)
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
            t.la.circle(t.iterable + t.phi, t.my_angle, 6)
#             t.le.circle(t.iterable * t.phi, -t.my_angle)
            t.le.right(t.my_angle)
            t.le.forward(t.iterable * t.phi)
            if t.iterable <= 255:
                turtle.bgcolor(G - t.iterable, B - t.iterable, N)
            else:
                turtle.bgcolor(L, M, N)
            f.save_thumb()
            t.iterable += 1
#             gc.collect()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
     # s.end_screen()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#novo_23
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Brave Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1386 -1449, 23rd module of 46')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle))
        R = random.randrange(150, 250, 10)
        log.info('The value of color R :   ' + str(R))
        G = 0
        B = 255
        L = random.randrange(10, 200, 1)
        log.info('The value of color L :   ' + str(L))
        M = 255
        N = 255
        X = 255
        Y = 255
        Z = 10
        t.le.left(t.my_angle/2)
        t.me.rt(t.my_angle/2)
        for t.iterable in range(255): #255 is default, use lower number for testing
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
            f.save_thumb()   #Screenshot as a png set set up mp4
        f.save_final_thumb() #Saves completed image as a jpeg and a png
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
       # s.end_screen()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#novo_24
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala_extended():
    global my_project
    t.my_project = my_project
    my_project = 'Brave Mandala Extended'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1994 -2100, 24th module of 46')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_extended_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info('Presenting  ' + str(t.my_str))
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle))
        R = random.randrange(175, 255, 10)
        log.info('The value of color R :   ' + str(R))
        G = 0
        B = 255
        L = random.randrange(10, 200, 1)
        log.info('The value of color L :   ' + str(L))
        M = 255
        N = 255
        X = 255
        Y = 255
        Z = 10
        t.iterable = 0
        while t.iterable <= 250: # First Pass
            turtle.bgcolor(X - t.iterable, Y - t.iterable, Z)
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
            turtle.bgcolor(5, 5,10)
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
        while t.iterable <= 760: # Third Pass
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
            f.save_thumb()    #Screenshot as a png set set up mp4    
        f.save_final_thumb() #Saves completed image as a jpeg and a png
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#novo_24
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala_decimated():
    global my_project
    t.my_project = my_project
    x = 3
    my_project = 'Angle-Fractioned Brave Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 2068 -2194, 24th module of 46')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_extended_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle/x) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle) + ',' + '  fractional =  ' + str(x) + ',' + '  fractional angle = ' + str(t.my_angle/x))
        R = random.randrange(175, 255, 10)
        log.info('The value of color R :   ' + str(R))
        G = 0
        B = 255
        L = random.randrange(10, 200, 1)
        log.info('The value of color L :   ' + str(L))
        M = 255
        N = 255
        X = 255
        Y = 255
        Z = 10
        t.iterable = 0
        while t.iterable <= 255: # First Pass
            turtle.bgcolor(X - t.iterable, Y - t.iterable, Z)
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
        while t.iterable <= 510: # Second Pass
#             log.info('The value of t.iterable is ' + str(t.iterable))
#             log.info('The value of count is  ' + str(count))
            turtle.bgcolor(5, 5,10)
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
        while t.iterable <= 765: # Third Pass
            log.info('The value of t.iterable is ' + str(t.iterable))
            log.info('The value of count is  ' + str(count))
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
            f.save_thumb()    #Screenshot as a png set set up mp4    
        f.save_final_thumb() #Saves completed image as a jpeg and a png
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()


#novo_25
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def color_shifting_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Color Shifting Animation'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1498 - 1563, 25th module of 46')
#     Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle))
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
        for t.iterable in range (360): # 360 is default for audio clip add, use lower number for testing
            t.le.pensize(t.iterable/ 90)
            t.le.dot(3)
            t.le.color( R - t.iterable %60,  G - t.iterable %140, B + t.iterable %200)
            t.le.left(t.my_angle)
            t.le.circle(t.iterable / t.phi, t.my_angle, 36 )
            if t.iterable <= 55:
                turtle.bgcolor(A + t.iterable, H + t.iterable, C)
            else:
                turtle.bgcolor(56, 56, C)
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    f.save_final_thumb()
    # s.end_screen()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()





#novo_26
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gold_red_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Gold-Red Animation'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1801 - 1852, 26th module of 46')
#     
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#novo_27
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gold_red_mandala_extended():
    global my_project
    t.my_project = my_project
    my_project = 'Gold-Red Animation Extended'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1853 - 1963, 27th module of 46')
    
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
        log.info(str('The featured angle is     ') + str(t.my_angle))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#novo_28
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Hued_freedom_star():
    global my_project
    t.my_project = my_project
    my_project = 'Hued Freedom Star'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1634 - 1715, 28th module of 46')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        log.info(str('The featured angle is     ') + str(t.my_angle))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()



#novo_29
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def blue_orange_mandala_144():
    global my_project
    t.my_project = my_project
    my_project = 'Blue-Orange Animation'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1720 - 1784, 29th module of 46')
    t.my_venv()
    Tm.start_time()
    au.pick_short_track()
    t.my_angle = 144
    t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
    t.folder_name = my_project + t.my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + t.folder_name)
    turtle.title(t.my_str)
    log.info(str('The featured angle is     ') + str(t.my_angle))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    
    


#novo_30
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def ribbons_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Ribbons Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1848 - 1923, 30th module of 46')    
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        log.info(str('The featured angle is     ') + str(round(t.my_angle)))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#novo_31
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def circular_mandala_205():
    global my_project
    t.my_project = my_project
    my_project = 'Circular Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1790 - 1853, 31st module of 46')
    t.my_venv()
    Tm.start_time()
    au.pick_short_track()
    t.my_angle = a.i_angle[a.i]
    t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
    t.folder_name = my_project + t.my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + t.folder_name)
    turtle.title(t.my_str)
    log.info(str('The featured angle is     ') + str(round(t.my_angle)))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#novo_32
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def occillating_polygon(): # Needs work
    global my_project
    t.my_project = my_project
    my_project = 'Occilating Polygon'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 1958 - 1929, 32nd module of 46')
    Tm.start_time()
     
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle))
        t.iterable = 0
        t.le.pensize(1)
        log.info('The Angle is   ' + str(t.my_angle))
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

                log.info('Value of iterable: ' + str(t.iterable))
                log.info('Value of Undobufferentries:  ' + str(t.le.undobufferentries()))
            f.save_final_undo()

    f.set_vid_env()
    f.sync_av()
    Tm.end_time()
    reset_all()
    t.my_venv()

    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#novo_33
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def arc_star():
    global my_project
    t.my_project = my_project
    my_project = 'Arc-Star'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 2088 - 2180, 33rd module of 46')
    log.info('Ran on:  ' + str(Tm.my_time))
    Tm.start_time()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle))
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
        au.pick_short_track()
        f.sync_av()
        reset_all()
        Tm.end_time()
#     s.end_screen()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()


#novo_34
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def home_star():
    global my_project
    t.my_project = my_project
    my_project = 'Home Star'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 2010 - 2085, 34th module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(10, 50 ,0)
        log.info(str('The featured angle is  ') + str(t.my_angle))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    
    


#novo_35
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#Deals best with whole number angles
def use_abs():
    global my_project
    t.my_project = my_project
    my_project = 'Absolute Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 2268- 2328, 35th module of 46')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info(str('The featured angle is     ') + str(t.my_angle))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
   
   


#novo_36
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Six-Pointed Mandalas or doubles.
def double_take():
    global my_project
    t.my_project = my_project
    my_project = 'Double Take'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 3083 - 3138, 36th module of 46')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
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
        log.info('The value of color R is    ' + str(R))
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
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        Tm.end_time()
#     s.end_screen()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#novo_37
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Cloverleaf Cross Mandala.
def cloverleaf():
    global my_project
    t.my_project = my_project
    my_project = 'Cloverleaf'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 3141 - 3195, 37th module of 46')
    # Select which set of angles to run
    a.i_angle =a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()


    

#novo_38
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Cloverleaf Extended Cross Mandala.
def cloverleaf_extended():
    global my_project
    t.my_project = my_project
    my_project = 'Cloverleaf Extended'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 3141 - 3268, 38th module of 46')
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
        log.info('Presenting  ' + str(t.my_str))
        t.folder_name = my_project + t.my_key
        log.info('The folder name is   ' + str(t.folder_name))
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        log.info('Starting First Pass at  ' + str(Tm.my_time))
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
            
        log.info('Starting Second Pass at  ' + str(Tm.my_time))
        t.le.pensize(5) # Second Pass
        t.le.speed(0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
        log.info('The value of t.iterable is   ' + str(t.iterable))
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
        log.info('Starting Third Pass at  ' + str(Tm.my_time))
        t.le.pensize(3) # Third Pass
        t.le.speed(0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
        log.info('The value of t.iterable is   ' + str(t.iterable))
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
        log.info('Starting Fourth Pass at  ' + str(Tm.my_time)) 
        t.le.pensize(2) # Fourth Pass
        t.le.speed(0)
        t.le.pencolor(0, 255,0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
#         t.le.left(t.my_angle)
        log.info('The value of t.iterable is   ' + str(t.iterable))
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
        log.info('The value of t.iterable is   ' + str(t.iterable))    
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()





#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Majestic Extended Mandala.
def majestic_mandala_extended():
    global my_project
    t.my_project = my_project
    my_project = 'Majestic Mandala Extended'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 3331 - 3467, 39th module of 46')
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
        log.info('Starting First Pass....')
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
            
        log.info('Starting Second Pass...')    
        t.le.pensize(5) # Second Pass
        t.le.speed(0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
        log.info('The value of t.iterable is   ' + str(t.iterable))
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
        log.info('Starting Third Pass....')    
        t.le.pensize(3) # Third Pass
        t.le.speed(0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
        log.info('The value of t.iterable is   ' + str(t.iterable))
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
        log.info('Starting Fourth Pass...')   
        t.le.pensize(2) # Fourth Pass
        t.le.speed(0)
        turtle.bgcolor(0,0,0)
        t.le.penup()
        t.le.setpos(0,0)
        t.le.pendown()
        count = 0
#         t.le.left(t.my_angle)
        log.info('The value of t.iterable is   ' + str(t.iterable))
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
        log.info('The value of t.iterable is   ' + str(t.iterable))    
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()




#novo_41
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def glorious_mandala():  # Based on Awesome Manadala
    global my_project
    t.my_project = my_project
    my_project = 'Glorious Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 3471 - 3551, 41st module of 46')
    t.my_venv()
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        log.info('===============================================================================')
        t.my_venv()
        Tm.start_time()
        t.my_angle =  a.i_angle[a.i]
        au.pick_short_track()
        t.my_str = my_project + '    featuring ' + str(round(t.my_angle)) + '  Degree Angles  with   ' + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info('The soundtrack being used for this show is: ' + str(au.my_track))
        log.info('The featured angle is     ' + str(t.my_angle))
        R = 255
        G = 255
        B = random.randrange(112,155, 1)
        log.info('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 150, 1)
        log.info('The value of hue /L/ is   ' + str(L))
        E = random.randrange(150, 255, 1)
        log.info('The value of hue /E/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        turtle.bgcolor(10, 255, 255)
        for t.iterable in range(252): # 359 is default, use lower number for testing.
            if t.iterable <= 255:
                turtle.bgcolor(X- t.iterable, Y - t.iterable, Z)
                t.me.pencolor(L, M + t.iterable, N + t.iterable)
                t.le.pencolor(R - t.iterable, G - t.iterable, Z + t.iterable %100)
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
            f.save_thumb()
        
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
        Tm.end_time()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    
    


#novo_42
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def glorious_mandala_extended():  # Based on Awesome Manadala
    global my_project
    t.my_project = my_project
    my_project = 'Glorious Mandala Extended'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 3391- 3317, 42nd module of 38.')
    t.my_venv()
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        log.info('===============================================================================')
        t.my_venv()
        Tm.start_time()
        t.my_angle =  a.i_angle[a.i]
        au.pick_medium_track()
        t.my_str = my_project + '    featuring ' + str(round(t.my_angle)) + '  Degree Angles  with   ' + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info('The soundtrack being used for this show is: ' + str(au.my_track))
        log.info('The featured angle is     ' + str(t.my_angle))
        R = 255
        G = 255
        B = random.randrange(112,155, 1)
        log.info('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 150, 1)
        log.info('The value of hue /L/ is   ' + str(L))
        E = random.randrange(150, 255, 1)
        log.info('The value of hue /E/ is   ' + str(L))
        M = 0
        N = 0
        X = 255
        Y = 255
        Z = 10
        t.iterable = 0
        turtle.bgcolor(10, 255, 255)  # First Pass
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
        log.info('Starting Second Pass....')    
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
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
        Tm.end_time()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    



#novo_43
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Independence_mandala():
    global my_project
    t.my_project = my_project
    my_project = 'Independence Mandala'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 3521- 3590, 43rd module of 46')
    t.my_venv()
    a.i_angle = a.i_angle_auto # Select set of angles to use from the -my_angles- module.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using list comprehension
    # s.title_screen() # Commented out to facilitate accurate a/v processing of the .png images
    t.my_title = str('Featuring Independence Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    log.info(str(t.my_title))
    for a.i  in range( len(a.i_angle)):
        log.info('===============================================================================')
        t.my_venv()
        Tm.start_time()
        t.my_angle =  a.i_angle[a.i]
        au. pick_short_track()
        t.my_str = my_project + '  featuring '+ str(round(t.my_angle)) + '  Degree Angles   ' + 'with  ' + '-' + au.my_track
        t.folder_name = my_project + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(10,0,10)
        log.info('The soundtrack being used for this show is: ' + str(au.my_track))
        log.info('The featured angle is     ' + str(t.my_angle))
        log.info('..........................................................................................................................................................................................')
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
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    




#novo_44
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wall_show():
    global my_project
    t.my_project = my_project
    my_project = 'Wall Show'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 3595- 3665 44th module of 46')
    
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using list comprehension
    for a.i  in range( len(a.i_angle)):
        log.info('======================================================================')
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info(t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        log.info(t.folder_name)
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        t.iterable = 0
        turtle.bgcolor(30,255,60)
        log.info('The soundtrack being used for this show is: ' + str(au.my_track))
        log.info('The featured angle is     ' + str(t.my_angle))
        log.info(('The value of t.rand_num is   ')  + str(t.rand_num))
        log.info(('The value of t.rand_pick is   ')  + str(t.rand_pick))
        log.info('......................................................................................')
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()
    




#novo_45
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wall_show_extended():
    global my_project
    t.my_project = my_project
    my_project = 'Wall Show Extended'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 3771- 3895, 45th module of 46')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using list comprehension
    for a.i  in range( len(a.i_angle)):
        log.info('======================================================================')
        t.my_venv()
        Tm.start_time()
        au.pick_medium_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info(t.my_str)
        t.folder_name = my_project + t.my_key
        f.make_png_folder()
        log.info(t.folder_name)
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        t.iterable = 0
        turtle.bgcolor(30,255,60)
        log.info('The soundtrack being used for this show is: ' + str(au.my_track))
        log.info('The featured angle is     ' + str(t.my_angle))
        log.info(('The value of t.rand_num is   ')  + str(t.rand_num))
        log.info(('The value of t.rand_pick is   ')  + str(t.rand_pick))
        log.info('......................................................................................')
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
#             log.info(str(t.le.color))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()    





#novo_46
#===========================================================================
#Code for Black Seed of Life
def black_seed():
    global my_project
    t.my_project = my_project
    my_project = 'Black Seed'
    log=logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    log.addHandler(logging.FileHandler(filename=f.my_work_dir + '/Make_Mandalas/Logs/' + my_project + str(t.my_key) + '.log'))
    log.info('Starting master_mandala_maker at  ' + str(Tm.my_time))
    log.info('Starting  ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('This is ' + my_project + ' code')
    log.info('Located @ line 3803- 3917, 46th module of 46')
    
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
        log.info('===============================================================================')
        t.my_venv()
        Tm.start_time()
        au.pick_short_track()
#         t.my_angle = a.i_angle[a.i]
        t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        log.info(t.my_str)
        t.folder_name = my_project + t.my_key
        log.info(t.folder_name)
        f.make_png_folder()
        os.chdir(f.loc_thumb + t.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        log.info('The soundtrack being used for this show is: ' + str(au.my_track))  
        log.info('The featured angle is     ' + str(t.my_angle))
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
                log.info('Base is:  ' + str(my_base))
                log.info('t.iterable  :' + str(t.iterable))
                log.info('Pen color:  ' + str(b))
                log.info(' x = ' + str(x))
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
                    log.info('t.iterable  :' + str(t.iterable))
                    log.info('Pen color:  ' + str(b))
                    log.info(' x = ' + str(x))
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
    log.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    log.info('************************************************************************')
    reset_all()



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
mystical_mandala()
# glorious_mandala_extended()  #Created 11/13/2022 Located @ line 2990- 3111, 32nd module of 38.  # 2.43 minutes
awesome_mandala_extended() #Created 11/7/2022 'Located @ line 1242 - 1342, 3.57 minutes
# colorful_mandala_extended() #'Located @ line 187 - 256,  3rd module of 38', created on 11/6/2022 # 2.46 minutes
# wall_show_extended() #Located @ line 3266- 3393, 34th module of 41.
brave_mandala_extended() #Located @ line 1645 -1736, 20th module of 38
brave_mandala_decimated()
'''
Run long_clips
'''
# cloverleaf_extended() #Located @ line 2648 - 2770, 31st module of 38' Created 11/ 17/2022
majestic_mandala_extended()  # Created 11/17/2022; Located @ line 3300 - 3442, 39th module of 46' Derived from cloverleaf_extended; employs lines instead of circles

'''Run short clips
'''

'===================================================================================================================================================================='
#  This second group of modules specifies a single angle; has no looping lists of angles

# basic_yin_yang()  # ( novo_1)  Located @ line 73 - 109, 1st module of 38. An animated rendition of the yin-yang grat.phic. My original; currently
                    # the most popular one on YouTube. Added the working do_video on 1/14/2022 which converts the png files/
                    #to gif, mp4, and avi files. Successfully automated video (.avi) creation 1/20/2022.
                    #Successfully lengthened and added long audio clips on 8/17/2022.


# growing_yin_yang() #novo_3 12 of 38, Published to YouTube 11/11/2021, Need to work on further as of 4/3/2022


# circular_mandala_205()  # novo_4 25 of 38; Added 12/9/2021 (Edited from Mandala_160_09292020) Processed to mp4 12/9/2021
'======================================================================================================================================================================='
# This third group of modules specifies a list of angles to loop

colorful_mandala() # Row 101 - 151, #2 of 38 Updated to automate video creation
#  
# jagged_multigram() # novo_6 #Row 150, 3 of 38, Published to YouTube on 11/2/2021 Updated to automate video creation
# 
# Fantastic_Mandala() # novo_8  Row 328 - 384, 5 of 38 # Works well. Updated to automate video creation Implemented 't.phi Offset' Angle on 4/28/2022.
# 
bold_mandala()  # novo_8 Row 593 - 643, 8 of 38, Updated to automate video creation  Implemented 't.phi Offset' Angle on 4/28/2022.
# animated_abstraction()  #  novo_9 10 of 38, Thumbs created 11/21/2021
# hued_polygram()  # novo_13  Located @ line 929 - 989, number 13 of 38, created 11/14/2021; added print to file 3/1/2022
awesome_mandala()  #  novo_15 15 of 38, Located at lines 1073 - 1118. Processed to mp4 and published to YouTube on 11/21/2021. modified 11/20/2021, This is exceptional.
# 
glorious_mandala() # novo_18 Created 4/6/2022, based on stupendous mandala. Located @ line 2337- 2419, 32nd module of 38.
pretty_awesome_mandala() # novo_19 Row 997 - 1054, Number 16 of 38. Derived from awesome_mandala. # Processed 90 degrees to MP4 on 12/15/2021
mighty_awesome_mandala()
# 
stupendous_mandala() # novo_18 Row 1034 - 1101, number 17 of 38. Derived from pretty_awesome_mandala. Created 1/8/2022. added print to file 3/1/2022Features a more prominent center than it's parent.  Works well.
brave_mandala() #novo_19 Located @ line 1386 -1449, Derived from awesome_mandala; 18 of 38
color_shifting_mandala() # novo_20 Rows 1274 - 1327, 19 of 38 work on
Hued_freedom_star() # novo_26 Row 1358 - 1428, 22 of 38; Added 12/4/2021
# arc_star() #novo_28 27 of 38; Located at lines 1586 - 1654. Added 01/06/2022. Derived from a Thought Matrix arc-star wriiten by me in 2020.\
#                       # Employs first use of automated creation of angle lists using numpy arange.
# home_star() #novo_ 28 of 38; Located at lines 2007 - 2078.  Added 01/06/2022. Derived from a Thought Matrix arc-star scripted by me in 2020.\
# ribbons_mandala()  #novo_30  24 of 38; Located at rows 1572 - 1635. Added 12/8/2021 (Edited from Mandala_160_09292020); converted to mult-angles on 1/20/2022
# use_abs() # novo_31 29 of 38; Located at line 1890. Uses the abs() function to draw the sides and points such that it continues until the point of origin is reached.
# double_take() # novo_32 30 of 38; Located at line 1843 - 1881. Facilitates the creation of a hexagram by using 2 pens drawn\
#                    # with same angles in opposite directions. Using specific angle array named a.i.angle_double.
# cloverleaf() # novo_33 31 of 38, Located at line  2247 - 2304. Created 3/6/2022.
wall_show() # novo_34 of 38. Located @ line 2408- 2474. Working on a suitable product to frame and display on a wall. Began development August 2022.
Independence_mandala() # novo_33  Located @2335 - 2408. Developed June 2022, Added 6/28/2022. 33rd module of 38. Makes beautiful diagrams.

'===================================================================================================================================================='
# This set of modules require tweaking and modification

# # # #     #NEEDS Work -- Too Slow!# gold_red_mandala_extended() # Created 11/18/2022; 'Located @ line 1856 - 1961, 21st module of 38')  # 4:12 minutes
# #     #NEEDS Work -- Too slow!# gold_red_mandala()  # novo_25 Located @ line 1801 - 1852, 21st module of 38 Added 12/3/2021; processed to mp4 12/16/2021(added 3 degrees)
#NEEDS SOME REWORKINGdark_mandala() #novo_6 Row 435, 6 of 38, Revised 4/30/2022
# NEEDS A BIT OF TWEAKING iridescent_polygram()  # novo_7 Row 516 - 577, 7 of 38 Modified 1/2/2022 Updated to automate video creation
# NEEDS SOME TWEAKING blue_orange_mandala_144() #novo_23  23 of 38; Located at rows 1510 - 1568. Added 12/7/2021 (Edited from Mandala_160_09292020) Processed to mp4 12/7/2021
# Work on  hued_polygonial() # novo_7 Rows 293 - 361,   4th module of 38. Features Blue and Red Hues. Modified 12/17/2021 Updated to automate video creation
          # On 4/28/2022, assigned an 'Offset Angle' to second turtle pen as the current angle times t.phi, looks good as a balance.
          # Base angle + it's t.phi offset. Nice.
# NEEDS TWEAKING hued_gradiant()  #novo_9 Row 647 - 733, 9 of 38
# NEEDS TWEAKING gradiant_mandala() #  novo_14 Row  785 - 852, 11 of 38. Last run date: 2/1/2022
# pretty_polygonial()   # novo_16   Row 856, 14 of 38, modified 11/19/2021  nEEDS WORK!
# Work on some more  multi_hued_polygram() # novo_23 Row  1125 - 1180, 20 of 38
# black_seed()   # novo_35 Needs more work
# occillating_polygon() # novo_27 NEED WORK ON THE UNDO FUNCTION Located @ line 1891 - 1968, 26th module of 38; Added 12/28/2021  Is first attempt to use undo function as way to create occillation
'======================================================================================================================================================================================================='
# Finalizing scripts to sync all files and folders
turtle.setup(550,550) # Minimized turtle window to observe screen and read shell output
f.move_all() # Moves files to appropriate locations
f.sync_mandala_folders()  # Sync video and script folders backups
turtle.bye()  # End the program;  Default is to leave uncommented.
