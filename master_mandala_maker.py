#novo_0 This is a marker for Thonny Find and Replace function, to enable quick access to top of each module
# MASTER MANDALA MAKER.PY

import turtle
import time
from timeit import default_timer as timer
import random
import My_template as t # Set up environment
import my_angles as a  #Processes angle selections
import my_hues as h # Aids in color selections
import my_splash_screen as s
from PIL import Image #module for converting python output to image
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
# import gc
from select import select
# from functools import lru_cache

t.my_venv()   #Initializes mandala drawing environments

Tm.time_functions()   #Initializes time functions

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

    time.sleep(2)


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

def my_title():
    my_title = turtle.title(t.my_str)

# MODULES
# Index of modules:


#novo_1
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
def basic_yin_yang():
#     time.sleep(3)
    
    Tm.set_time()
    Tm.start_time()
#     print('Starting basic_yin_yang() by Leon Hatton on   ' + str(Tm.my_time))

    print('Starting basic_yin_yang() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 72 - 114, 1st module of 36')
    t.my_venv()
    t.my_project = 'A Yin-Yang Expression'
  
    t.my_angle = 180
    Tm.start_time()
    au.pick_track()
    t.my_str = t.my_project + '   featuring   ' + str( t.my_angle) + '  ' + '    Degree Angles  with  '  + au.my_track
    turtle.title(t.my_str)
#     s.splash_screen()
    f.folder_name = t.my_project + t.my_key 
    f.make_png_folder()
    os.chdir(f.loc_thumb + f.folder_name)
    time.sleep(3)
    t.iterable = 0
    turtle.bgcolor('goldenrod') # Has to be a neutral shade like grey to contrast the black and white theme.
    while t.iterable <= (400):  #360 is default. Use lower number for testing. The higher the number, the longer the show.
        t.le.pensize(10)
        # s.watermark()
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
    t.reset_all()



#novo_2
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def colorful_mandala():
    Tm.set_time()
    Tm.start_time()
#     print('Starting colorful_mandala by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/colorful_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the colorful_mandala() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 117 - 185,  2nd module of 36')
    print('Ran on:  ' + str(Tm.my_time))
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Colorful Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Colorful Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
        print('The angle for this mandala is    ' + str(t.my_angle) + '    degrees.')
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
        # s.end_screen()
    t.reset_all()
    Tm.end_time()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin


#novo_3
#**************************************************************************************************************
  # Published to YouTube on 11/2/2021
 #This script features three pens: le, me, and lb. They follow separate yet coordinated routes to compose the mandala.
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def jagged_multigram():
    Tm.set_time()
#     print('Starting jagged_multigram() python code by Leon Hatton on  ' + str(Tm.my_time))
    print(str('********************************************************************************************************************'))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/jagged_multigram_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting jagged_multigram() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 191 - 282, 3rd module of 36')
#     f.code_backup()
    t.my_venv() #Calls the template module
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Jagged Multigram'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        my_hue = random.randint(5, 100)
        my_hue_a = random.randint(100, 200)
        turtle.bgcolor(0, 0, 0)
        t.le.speed(0)
        t.me.speed(0)
        t.lb.speed(0)
        t.iterable = 0000
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
        print('The angle for this mandala is    ' + str(t.my_angle) + '    degrees.')
        print('The value of my_hue is' + '   ' + str(my_hue))
        print('The value of my_hue_a is' + '   ' + str(my_hue_a))
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
    Tm.end_time()
    t.reset_all()
    # s.end_screen()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin





#novo_4
#*****************************************************************************************************************************
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def hued_polygonial():  # Uses 2 pens with offset t.phi angle
#     time.sleep(3)
    Tm.set_time()
#     print('Starting hued_polygonial() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/hued_polygonial_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting hued_polygonial() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 285 - 358,   4th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring Hued Polygonial Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    # s.title_screen()
    print(t.my_title)
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        t.my_angle = a.i_angle[a.i]
        print('The offset angle value is  ' + str(t.my_angle * (t.pi/2)))
        au.pick_track()
        t.my_str = ' A Hued Polygonial featuring ' + str(round(t.my_angle)) + ' Degree Angles,    ' + t.my_key + 'with   ' + au.my_track
        f.folder_name = t.my_str + '/'
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
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
        print(t.my_str)
        time.sleep(3)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #  #
        t.my_venv()
    Tm.end_time()
    # s.end_screen()
    t.reset_all()
    #     sys.stdout.close()
    #     sys.stdout=stdoutOrigin




#novo_5
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Fantastic_Mandala():  # Uses 2 pens with offset t.phi angle
#     time.sleep(3)
    Tm.set_time()
#     print('Starting Fantastic_Mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open(my_path + /Logs/Fantastic_Mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting Fantastic_Mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 362 - 433,   5th module of 36')
    t.my_venv() # Initializes turtle canvas screen environment
    # Select which set of angles to run using list comprehension method
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Fantastic Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
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
        print(t.my_str)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #  #
        t.my_venv()
    Tm.end_time()
    # s.end_screen()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin




#novo_6
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#NEEDS SOME REWORKING def dark_mandala(): #Needs work
#     time.sleep(3)
    Tm.set_time()
#     print('Starting dark_mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open(my_path + /Logs/dark_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting dark_mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 432 - 509,   6th module of 36')
    t.my_venv()
     # Select which set of angles to run using list comprehension method
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Dark Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
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
        print(t.my_str)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #  #
        t.my_venv()
    Tm.end_time()
    # s.end_screen()
    t.reset_all()
#         sys.stdout.close()
#         sys.stdout=stdoutOrigin



#novo_7
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def iridescent_polygram():  # Uses 2 pens with offset t.phi angle
#     time.sleep(3)
    Tm.set_time()
#     print('Starting iridescent_polygram() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/iridescent_polygram_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting iridescent_polygram() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 513 - 578,   7th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run;  Favorite angles: 144/5P, 210/12P, 834/TightSpiral,2394/20P,1350/Square
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Iridescent Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    # s.title_screen()
    print(t.my_title)
    Tm.start_time()
    for a.i  in range(len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'An Iridescent Polygram'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
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
        print(t.my_str)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #  #
        t.my_venv()
    Tm.end_time()
    # s.end_screen()
    t.reset_all()
#         sys.stdout.close()
#         sys.stdout=stdoutOrigin



#novo_8
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def bold_mandala():
    #     time.sleep(3)
    Tm.set_time()
#     print('Starting  bold_mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/bold_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting  bold_mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 594 - 660, 8th module of 36')
    t.my_venv()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Bold Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '  featuring ' + str( t.my_angle) + ' Degree Angles, with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
        turtle.bgcolor(0,0,0)
        t.la.speed(0)
        for t.iterable in range (255):      #255 is default. Use lower number for testing. 300 for audio.
            turtle.bgcolor(255- t.iterable, t.iterable, t.iterable)
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
        print(t.my_str)

#             turtle.bgcolor(2,9,3)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        #  #  #
        t.my_venv()
# s.end_screen()
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin
#


#novo_9
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# NEEDS SOME TWEAKING def hued_gradiant():  # Uses 2 pens with offset t.phi angle
#     time.sleep(3)
    Tm.set_time()
#     print('Starting  hued_gradiant() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/hued_gradiant_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting  hued_gradiant() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 655 - 745, 9th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Hued Gradiant Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' +  str(round(t.my_angle)) + ' and  ' + str(round (t.my_angle * t.phi)) +'    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        print('The offset angle value is  ' + str(t.my_angle * t.phi))
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
    # s.end_screen()
    t.reset_all()
    Tm.end_time()
 #     sys.stdout.close()
#     sys.stdout=stdoutOrigin
    #


#novo_10
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def animated_abstraction():
    Tm.set_time()
#     print('Starting animated_abstraction() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open(my_path + '/Logs/animated _abstraction_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting animated_abstraction() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 752 - 832,   10th module of 36')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'Animated Abstract Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
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
            t.iterable = t.iterable + 2
        print(t.my_str)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
    Tm.end_time()
    # s.end_screen()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin




#novo_11
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gradiant_mandala():
#     time.sleep(3)
    Tm.set_time()
#     print('Starting gradiamt_mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/gradiant_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting gradiant_mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 827 - 898, 11th module of 36')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Gradiant Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
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
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin





#novo_12
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def growing_yin_yang(): #Published to YouTube 11/11/2021
    Tm.set_time()
    print('Starting growing_yin_yang() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open(f.my_path + '/Logs/growing_yin_yang_' + str(t.file_key) + '_log.txt', 'w')
#     print('Starting growing_yin_yang() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 930 - 981, 12th module of 36')
    t.my_venv()
    Tm.start_time()
    t.my_project = 'A Growing Yin-Yang'
    au.pick_track()
    t.my_angle =180
    t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
    f.folder_name = t.my_project + t.my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + f.folder_name)
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
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin



#novo_13
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Uses 2 pens with offset t.phi angle
def hued_polygram():
    Tm.set_time()
#     print('Starting hued_polygram() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/hued_polygram_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting hued_polygram() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('novo_13, Located @ line 961 - 1021, 13th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
     # s.title_screen()
    Tm.start_time()
    for a.i  in range(len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Hued Polygram'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
        turtle.bgcolor(10,100,10)
        print(str('The featured angle is     ') + str(t.my_angle))
        for t.iterable in range(length):
            turtle.bgcolor(100, 10 + t.iterable %245, t.iterable)
            h.pick_indigo()
            t.li.left(-t.my_angle)
            t.li.forward(t.iterable * t.phi)
            h.pick_light()
            t.le.right(t.my_angle)
            t.le.forward(t.iterable / t.pi)
            h.pick_gold()
            t.la.forward(t.iterable)
            h.pick_dot()
            t.ld.dot(t.iterable /36 * t.phi)
            t.la.circle(t.iterable / 9, t.my_angle, 10)
            t.le.pensize(t.iterable / 27)
            t.li.pensize(t.iterable / 18)
            t.la.pensize(t.iterable / 33)
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
    #  #
        t.my_venv()
    # s.end_screen()
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin




#novo_14
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_polygonial(): # NEEDS WORK
    time.sleep(3)
    Tm.set_time()
    print('Starting pretty_polygonial() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/pretty_polygonial_' + str(t.file_key) + '_log.txt', 'w')
#     print('Starting pretty_polygonial() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 1028 - 1096, 14th module of 36')
#     f.code_backup()
    au.pick_track()
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
            au.pick_track()
            t.my_str = ' A Pretty Polygram Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key  + '-' + au.my_track
            f.folder_name = t.my_str + '/'
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            os.chdir(f.loc_thumb + f.folder_name)
            turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
            turtle.bgcolor(0,0,0)
            print(str('The featured angle is     ') + str(t.my_angle))
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
            #  #
            t.my_venv()
        # s.end_screen()
        Tm.end_time()
        t.reset_all()
#         sys.stdout.close()
#         sys.stdout=stdoutOrigin




#novo_15
#**************************************************************************************************************
  # First Published to YouTube on 11/21/2021
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def awesome_mandala():
#     print("Press any key to configure or wait 5 seconds...")
#     timeout = 5
#     rlist, wlist, xlist = select([sys.stdin], [], [], timeout)
#     if rlist:
#         print("Press any Key to continue...")
#     else:
#        print("Timed out..")

    Tm.set_time()
#     print('Starting awesome_mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/awesome_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting awesome_mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 1067 - 1147, 15th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'An Awesome Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        print(str('The featured angle is     ') + str(t.my_angle))
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
        print('The Value of color B is    ' + str(B))
        print('The Value of color L is    ' + str(L))
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        t.my_venv()
    Tm.end_time()
# s.end_screen()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin




#novo_16
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_awesome_mandala():  # Based on Awesome Manadala
    Tm.set_time()
#     print('Starting pretty_awesome_mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/pretty_awesome_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting pretty_awesome_mandala() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 1191- 1264, 16th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Pretty Awesome Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
        turtle.bgcolor(0,0,0)
        print(str('The featured angle is     ') + str(t.my_angle))
        R = 0
        G = 255
        B = random.randrange(10, 200, 1)
        print('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 200, 1)
        print('The value of hue /L/ is   ' + str(L))
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
    # s.end_screen()
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin





#novo_17
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def stupendous_mandala():  # Based on Awesome Manadala
#     time.sleep(3)
    Tm.set_time()
#     print('Starting stupendous_mandala() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/stupendous_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Starting stupendous_mandala by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 1270- 1351, 17th module of 36.')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        print('===============================================================================')
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Stupendous Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        print('The soundtrack being used for this show is:   ' + au.my_track)
        print('The featured angle is     ' + str(t.my_angle))
        R = 255
        G = 255
        B = random.randrange(150, 255, 20)
        print('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 150, 25)
        print('The value of hue /L/ is   ' + str(L))
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
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')




#novo_18
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def multi_hued_polygram():
    Tm.set_time()
#     print('Starting multi_hued_polygram() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open(my_path +'/Logs/multi_hued_polygram_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting multi_hued_polygram() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 1376- 1446, 18th module of 36')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Multi-Hued Polygram'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark() # Be sure to customize to correctly id the music track
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
    Tm.end_time()
    t.reset_all()
        #     sys.stdout.close()
#     sys.stdout=stdoutOrigin



#novo_19
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def brave_mandala():
#     time.sleep(3)
    Tm.set_time()
#     print('Starting brave_mandala() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/brave_mandala' + str(t.file_key) + '_log.txt', 'w')
    print('Starting brave_mandala() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 1459 -1531, 19th module of 36')
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Brave Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        print(str('The featured angle is     ') + str(t.my_angle))
        R = random.randrange(150, 250, 10)
        print('The value of color R :   ' + str(R))
        G = 0
        B = 255
        L = random.randrange(10, 200, 1)
        print('The value of color L :   ' + str(L))
        M = 255
        N = 255
        X = 255
        Y = 255
        Z = 10
        t.le.left(t.my_angle/2)
        t.me.rt(t.my_angle/2)
        for t.iterable in range(255): #255 is default, use lower number for testing
            turtle.bgcolor(X - t.iterable, Y - t.iterable, Z)
            t.le.pensize(t.iterable/81)
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
    Tm.end_time()
    t.reset_all()
    #  f.pause_option()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin



#novo_20
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def color_shifting_mandala():
    Tm.set_time()
    print('Starting color_shifting_mandala() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/color_shifting_mandala_' + str(t.file_key) + '_log.txt', 'w')
#     print('Starting color_shifting_mandala() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 1498 - 1563, 20th module of 36')
#     f.code_backup()
   # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Color Shifting Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        print(str('The featured angle is     ') + str(t.my_angle))
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
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin





#novo_21
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gold_red_mandala():
    Tm.set_time()
#     print('Starting gold_red_mandala() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/gold_red_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting gold_red_mandala() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 1570 - 1627, 21st module of 36')
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Gold Red Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        print(str('The featured angle is     ') + str(t.my_angle))
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
    # s.end_screen()
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin



#novo_22
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Hued_freedom_star():
    Tm.set_time()
#     print('Starting  Hued_freedom_star by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/Hued_freedom_star_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting  Hued_freedom_star by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 1634 - 1715, 22nd module of 36')
    Tm.start_time()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Hued Freedom Star'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        print(str('The featured angle is     ') + str(t.my_angle))
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
    t.reset_all()
    # s.end_screen()
    Tm.end_time()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin



#novo_23
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def blue_orange_mandala_144():
    Tm.set_time()
#     print('Starting blue_orange_mandala by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/blue_orange_mandala_144_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting blue_orange_mandala by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 1720 - 1784, 23rd module of 36')
    t.my_venv()
    Tm.start_time()
    t.my_project = 'A Blue Orange Mandala'
    au.pick_track()
    t.my_angle = 144
    t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
    f.folder_name = t.my_project + t.my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + f.folder_name)
    turtle.title(t.my_str)
    print(str('The featured angle is     ') + str(t.my_angle))
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
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin


#novo_24
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def ribbons_mandala():
    Tm.set_time()
    Tm.start_time()
#     print('Starting ribbons_mandala() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/ribbons_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting ribbons_mandala() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 1848 - 1923, 24th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Ribbon Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        print(str('The featured angle is     ') + str(round(t.my_angle)))
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
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin




#novo_25
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def circular_mandala_205():
    Tm.set_time()
#     print('Starting circular_mandala_205 on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/circular_mandala_205_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting circular_mandala on   ' + str(Tm.my_time))
    print('Located @ line 1790 - 1853, 25th module of 36')
    t.my_venv()
    Tm.start_time()
    t.my_project = 'A Circular Mandala'
    au.pick_track()
    t.my_angle = a.i_angle[a.i]
    t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
    f.folder_name = t.my_project + t.my_key
    f.make_png_folder()
    os.chdir(f.loc_thumb + f.folder_name)
    turtle.title(t.my_str)
    print(str('The featured angle is     ') + str(round(t.my_angle)))
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
    t.reset_all()
#     s.end_screen()
    Tm.end_time()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin




#novo_26
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def occillating_polygon(): # Needs work
    Tm.set_time()
    # stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/occillating_polygon_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the occillating polygon() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1958 - 1929, 26th module of 36')
    Tm.start_time()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'An Occillating Polygon'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        print(str('The featured angle is     ') + str(t.my_angle))
        t.iterable = 0
        t.le.pensize(1)
        print('The Angle is   ' + str(t.my_angle))
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

                print('Value of iterable: ' + str(t.iterable))
                print('Value of Undobufferentries:  ' + str(t.le.undobufferentries()))
            f.save_final_undo()

    f.set_vid_env()
    f.sync_av()
    Tm.end_time()
    reset_all()
    t.my_venv()

    t.reset_all()
#     s.end_screen()
    Tm.end_time()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin




#novo_27
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def arc_star():
    Tm.set_time()
#     print('Starting arc_star() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/arc_star_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting arc_star() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2088 - 2180, 27th module of 36')
    print('Ran on:  ' + str(Tm.my_time))
    Tm.start_time()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'An Arc Star Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        print(str('The featured angle is     ') + str(t.my_angle))
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
        au.pick_track()
        f.sync_av()
        reset_all()
        Tm.end_time()
#     s.end_screen()
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin


#novo_28
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def home_star():
    Tm.set_time()
#     print('Starting home_star() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/home_star_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting home_star() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2010 - 2085, 28th module of 36')
    Tm.start_time()
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
   #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Home Star Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(10, 50 ,0)
        print(str('The featured angle is  ') + str(t.my_angle))
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
    Tm.end_time()
#     s.end_screen()
    t.reset_all()
#     #  f.pause_option()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin


#novo_29
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#Deals best with whole number angles
def use_abs():
    Tm.set_time()
    print('Starting use_abs() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2268- 2328, 29th module of 36')
    Tm.start_time()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Use of Abs() Function'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        print(str('The featured angle is     ') + str(t.my_angle))
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
    Tm.end_time()
    t.reset_all()
    #  #  f.pause_option()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin



#novo_30
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Six-Pointed Mandalas or doubles.
def double_take():
    Tm.set_time()
#     print('Starting double_take() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/double_take_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting double_take() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2232 - 2396, 30th module of 36')
    Tm.start_time()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Double Pinned Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        R = random.randrange(155,255, 5)
        G = 255
        B = 0
        print('The value of color R is    ' + str(R))
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
    t.reset_all()
    Tm.end_time()
    #  #  f.pause_option()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin



#novo_31
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Cloverleaf Cross Mandala.
def cloverleaf():
    Tm.set_time()
    print('Starting cloverleaf() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/cloverleaf' + str(t.file_key) + '_log.txt', 'w')
#     print('Starting cloverleaf() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2400 - 2462, 31st module of 36')
    Tm.start_time()
    f.code_backup()
    # Select which set of angles to run
    a.i_angle =a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    #     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Cloverleaf Mandala'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
#             t.le.left(t.my_angle/2)
        t.le.pensize(10)
        t.le.speed(0)
        t.le.pencolor(0, 255,0)
        turtle.bgcolor(0,0,0)
        for t.iterable in range(300):
            if t.iterable <= 255:
                t.le.pencolor(0 + t.iterable, 255 - t.iterable, 0 + t.iterable)
            else:
                t.le.pencolor(255, 0, 255)
            t.le.circle(t.phi + t.iterable, t.my_angle)
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
#     s.end_screen()
    t.reset_all()
    Tm.end_time()
#     f.pause_option()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin



#novo_32
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def glorious_mandala():  # Based on Awesome Manadala
    Tm.set_time()
    Tm.start_time()
#     time.sleep(3)
#     print('Starting glorious_mandala by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open(my_path + /Logs/glorious_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Starting glorious_mandala by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2251- 22334, 32nd module of 36.')
#     f.code_backup()
    t.my_venv()
    
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        print('===============================================================================')
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Glorious Mandala'
        t.my_angle =  a.i_angle[a.i]
        au.pick_track()
        t.my_str = t.my_project + '    featuring ' + str(round(t.my_angle)) + '  Degree Angles  with   ' + au.my_track
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        print('The soundtrack being used for this show is: ' + str(au.my_track))
        print('The featured angle is     ' + str(t.my_angle))
        R = 255
        G = 255
        B = random.randrange(112,155, 1)
        print('The value of hue /B/ is   ' + str(B))
        L = random.randrange(10, 150, 1)
        print('The value of hue /L/ is   ' + str(L))
        E = random.randrange(150, 255, 1)
        print('The value of hue /E/ is   ' + str(L))
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
#     s.end_screen()
    Tm.end_time()
    t.reset_all()
#  #  f.pause_option()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin




#novo_33
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Independence_mandala():
    Tm.set_time()
    Tm.start_time()
#     print('Starting Independence_mandala() by Leon Hatton on   ' + str(Tm.my_time))
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Starting Independence_Mandala Python module by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2344- 2408, 33rd module of 36.')
    t.my_venv()
    a.i_angle = a.i_angle_auto # Select set of angles to use from the -my_angles- module.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using list comprehension
    # s.title_screen() # Commented out to facilitate accurate a/v processing of the .png images
    t.my_title = str('Featuring Independence Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(str(t.my_title))
    for a.i  in range( len(a.i_angle)):
        print('===============================================================================')
        t.my_venv()
        Tm.start_time()
        t.my_project = 'An Independence Mandala'
        t.my_angle =  a.i_angle[a.i]
        au. pick_track()
        t.my_str = t.my_project + '  featuring '+ str(round(t.my_angle)) + '  Degree Angles   ' + 'with  ' + '-' + au.my_track
        f.folder_name = t.my_project + t.my_key
#         f.output_to_file() #Starts saving shell output to a file; optional, comment out for default
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
       #             s.splash_screen()  # Commented out to facilitate accurate a/v processing of the .png images
        # s.watermark() # Commented out to facilitate accurate a/v processing of the .png images
        turtle.bgcolor(10,0,10)
        print('The soundtrack being used for this show is: ' + str(au.my_track))
        print('The featured angle is     ' + str(t.my_angle))
        print('..........................................................................................................................................................................................')
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
#         f.restore_default_shell() #Use to restore default shell output
        reset_all()
    #  #
    t.my_venv()
    Tm.end_time()
#     s.end_screen() # Commented out to facilitate accurate a/v processing of the .png images
    t.reset_all()
    #  #  f.pause_option()
   




#novo_34
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def wall_show():
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    Tm.set_time()
    Tm.start_time()
#     print('Starting Independence_mandala() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/Independence_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting Wall Shows by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2632- 2702, 34th module of 36.')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using list comprehension
    for a.i  in range( len(a.i_angle)):
        print('======================================================================')
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Wall Show'
        au.pick_track()
        t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        print(t.my_str)
        f.folder_name = t.my_project + t.my_key
        f.make_png_folder()
        print(f.folder_name)
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        t.iterable = 0
        turtle.bgcolor(30,255,60)
        print('The soundtrack being used for this show is: ' + str(au.my_track))
        print('The featured angle is     ' + str(t.my_angle))
        print(('The value of t.rand_num is   ')  + str(t.rand_num))
        print(('The value of t.rand_pick is   ')  + str(t.rand_pick))
        print('......................................................................................')
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
        time.sleep(6)
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        reset_all()
        Tm.end_time()
    t.reset_all()
    Tm.end_time()
    #  #  f.pause_option()



#novo_35
#===========================================================================
#Code for Black Seed of Life
def black_seed():
    Tm.set_time()
    start = timer()
#     time.sleep(3)
#     print('Starting black seed mandala by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/glorious_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Starting black_seed_mandala by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2679- 2768, 34th module of 36.')
#     f.code_backup()
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
        print('===============================================================================')
        t.my_venv()
        Tm.start_time()
        t.my_project = 'A Black Seed Mandala'
        au.pick_track()
#         t.my_angle = a.i_angle[a.i]
        t.my_str = t.my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + au.my_track
        print(t.my_str)
        f.folder_name = t.my_project + t.my_key
        print(f.folder_name)
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name)
        turtle.title(t.my_str)
        turtle.bgcolor(0,0,0)
        print('The soundtrack being used for this show is: ' + str(au.my_track))  
        print('The featured angle is     ' + str(t.my_angle))
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
                print('Base is:  ' + str(my_base))
                print('t.iterable  :' + str(t.iterable))
                print('Pen color:  ' + str(b))
                print(' x = ' + str(x))
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
                    print('t.iterable  :' + str(t.iterable))
                    print('Pen color:  ' + str(b))
                    print(' x = ' + str(x))
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
#     s.end_screen()
    Tm.end_time()
    end = timer()
    print(end - start)
    t.reset_all()
    #  #  f.pause_option()
    #     sys.stdout.close()
    #     sys.stdout=stdoutOrig



#nomega
print('********************************************************************************************')
""" List of modules. To run, uncomment the row. A word of caution: Computer memory and speed take a hit with the 250+ looping, image creation,
 and video creation associated with each image file. No load testing has been made at this time. Also, because of the looping screenshots a dedicated,
 always on monitor is needed. The screenshot code will capture anything that is on the monitor screen while it is running. Power-saving and screensaver
 apps should be disabled while this code is running.
'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
"""
# Sync vbideo and script folders backups
f.sync_mandala_folders()

#  This first group of modules specifies a single angle; has no looping lists of angles
# basic_yin_yang()  # ( novo_1)  Located @ line 71 - 111, 1st module of 36. An animated rendition of the yin-yang grat.phic. My original; currently
                    # the most popular one on YouTube. Added the working do_video on 1/14/2022 which converts the png files/
                    #to gif, mp4, and avi files. Successfully automated video (.avi) creation 1/20/2022. Successfully lengthened and added long audio clips on 8/17/2022.

# NEEDS SOME TWEAKING blue_orange_mandala_144() #novo_23  23 of 36; Located at rows 1510 - 1568. Added 12/7/2021 (Edited from Mandala_160_09292020)\
                            # Processed to mp4 12/7/2021
# growing_yin_yang() #novo_3 12 of 36, Published to YouTube 11/11/2021, Need to work on further as of 4/3/2022


# circular_mandala_205()  # novo_4 25 of 36; Added 12/9/2021 (Edited from Mandala_160_09292020) Processed to mp4 12/9/2021
# '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# This group of modules specifies a list of angles to loop
#
# colorful_mandala() #novo_5 Row 101 - 151, #2 of 36 Updated to automate video creation
# jagged_multigram() # novo_6 #Row 150, 3 of 36, Published to YouTube on 11/2/2021 Updated to automate video creation
# ===Work on  hued_polygonial() # novo_7 Rows 293 - 361,   4th module of 36. Features Blue and Red Hues. Modified 12/17/2021 Updated to automate video creation
          # On 4/28/2022, assigned an 'Offset Angle' to second turtle pen as the current angle times t.phi, looks good as a balance.
          # Base angle + it's t.phi offset. Nice.
# #'**********************************************************************************************************************'
# Fantastic_Mandala() # novo_8  Row 328 - 384, 5 of 36 # Works well. Updated to automate video creation Implemented 't.phi Offset' Angle on 4/28/2022.
# # #'**********************************************************************************************************************'
#NEEDS SOME REWORKINGdark_mandala() #novo_6 Row 435, 6 of 36, Revised 4/30/2022
# NEEDS A BIT OF TWEAKING iridescent_polygram()  # novo_7 Row 516 - 577, 7 of 36 Modified 1/2/2022 Updated to automate video creation
# bold_mandala()  # novo_8 Row 593 - 643, 8 of 36, Updated to automate video creation  Implemented 't.phi Offset' Angle on 4/28/2022.
# NEEDS TWEAKING hued_gradiant()  #novo_9 Row 647 - 733, 9 of 36
# animated_abstraction()  #  novo_9 10 of 36, Thumbs created 11/21/2021
#  NEEDS TWEAKING gradiant_mandala() #  novo_14 Row  785 - 852, 11 of 36. Last run date: 2/1/2022
hued_polygram()  # novo_13  Row 799, number 13 of 36, created 11/14/2021; added print to file 3/1/2022
#               pretty_polygonial()   # novo_16   Row 856, 14 of 36, modified 11/19/2021  nEEDS WORK!

# awesome_mandala()  #  novo_15 15 of 36, Located at lines 1073 - 1118. Processed to mp4 and published to YouTube on 11/21/2021.\
#                                 # modified 11/20/2021, This is exceptional.
# #                                 # I might expand on it with other modules and angles. added print to file 3/1/2022\
#                                   # Altered code to randomnize gold color using h.pick_gold().
#
# glorious_mandala() # novo_18 Created 4/6/2022, based on stupendous mandala. Located @ line 2337- 2419, 32nd module of 36.
# pretty_awesome_mandala() # novo_19 Row 997 - 1054, Number 16 of 36. Derived from awesome_mandala.\
#                             # Processed 90 degrees to MP4 on 12/15/2021
# #'**********************************************************************************************************************'
stupendous_mandala() # novo_18 Row 1034 - 1101, number 17 of 36. Derived from pretty_awesome_mandala. Created 1/8/2022. added print to file 3/1/2022
#                         #Features a more prominent center than it's parent.  Works well.
# #'**********************************************************************************************************************'
brave_mandala() #novo_19 Row 1116, Derived from awesome_mandala; 18 of 36
color_shifting_mandala() # novo_20 Rows 1274 - 1327, 19 of 36 work on
multi_hued_polygram() # novo_23 Row  1125 - 1180, 20 of 36
gold_red_mandala()  # novo_25 Rows 1303 - 1353; 21 of 36 Added 12/3/2021; processed to mp4 12/16/2021(added 3 degrees)
Hued_freedom_star() # novo_26 Row 1358 - 1428, 22 of 36; Added 12/4/2021
# # #
                  # occillating_polygon() # novo_27 NEED WORK ON THE UNDO FUNCTION Located @ line 1891 - 1968, 26th module of 36; Added 12/28/2021  Is first attempt to use undo function as way to create occillation
# arc_star() #novo_28 27 of 36; Located at lines 1586 - 1654. Added 01/06/2022. Derived from a Thought Matrix arc-star wriiten by me in 2020.\
#                        # Employs first use of automated creation of angle lists using numpy arange.
#
home_star() #novo_ 28 of 36; Located at lines 2007 - 2078.  Added 01/06/2022. Derived from a Thought Matrix arc-star scripted by me in 2020.\
#                        # Employs first use of automated creation of angle lists using numpy arange. Called home_star because the turtle\
#                        # pen is picked up and dropped down at the center of the screen(0,0).
# ribbons_mandala()  #novo_30  24 of 36; Located at rows 1572 - 1635. Added 12/8/2021 (Edited from Mandala_160_09292020);\
#                         #converted to mult-angles on 1/20/2022
# use_abs() # novo_31 29 of 36; Located at line 1890. Uses the abs() function to draw the sides and points such that\
#                         #it continues until the point of origin is reached.
# double_take() # novo_32 30 of 36; Located at line 1843 - 1881. Facilitates the creation of a hexagram by using 2 pens drawn\
#                     # with same angles in opposite directions. Using specific angle array named a.i.angle_double.
cloverleaf() # novo_33 31 of 36, Located at line  2247 - 2304. Created 3/6/2022.
wall_show() # novo_34 of 36. Located at 2592 - 2659. Working on a suitable product to frame and display on a wall. Began development August 2022.
Independence_mandala() # novo_33  Located @2335 - 2408. Developed June 2022, Added 6/28/2022. 33rd module of 36. Makes beautiful diagrams.
# black_seed()   # novo_35 Needs more work

#****************************************************************************************************************************************************************
turtle.setup(550,550)
f.move_all()
f.sync_mandala_folders()
turtle.exitonclick()  # Waits for mouse click to end the program;  Default is to leave uncommented.
