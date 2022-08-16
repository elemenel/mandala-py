#novo_0 This is a marker for Thonny Find and Replace function, to enable quick access to top of each module
# MASTER MANDALA MAKER.PY

import turtle
import time
import random
import My_template as t # Set up environment
import my_angles as a  #Processes angle selections
import my_hues as h # Aids in color selections
import my_splash_screen as s
from PIL import Image #module for converting python output to image
import numpy as np # Processes the video
import cv2 # For screenshots
import pyautogui
from datetime import datetime
from Timer import Timer
import Timer as Tm
import FileScripts as f  # Processes file manipulations
import os
import sys
import audio_clips as au # Processes the audio tracks
import gc
from select import select

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
h.pick_red() #Pen lu
h.pick_indigo() #Pen li
h.pick_gold() #Pen la
h.pick_green() #Pen lg
h.pick_dark() #Pen lz
h.pick_blue() #Pen lb
h.pick_random() #Pen me
h.pick_magenta() #Pen lm
h.pick_light() # Pen le

length = 255  #Default is 252; any lower number for testing

def my_title():
    my_title = turtle.title(t.my_str)

# MODULES

#novo_1
#+++++++++++MODULE 1, BASIC YIN-YANG+++++++++++++++++++++++++++++++++++++++++++++++++++++
def basic_yin_yang():
#     time.sleep(3)
    Tm.set_time()
#     print('Starting basic_yin_yang() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/basic_yin_yang_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting basic_yin_yang() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 68 - 110, 1st module of 36')
    t.my_venv()

    Tm.start_time()
    au.pick_track()
    t.my_str = 'A Yin-Yang Expression   ' + t.my_key + au.my_track
    t.my_title = str('This show features the basic yin-yang, animated.')
    t.my_angle = 120
    turtle.title(t.my_str)
#     s.splash_screen()
#     f.code_backup()
    f.folder_name = t.my_str
    f.make_png_folder()
    os.chdir(f.loc_thumb + f.folder_name + '/')
    time.sleep(3)
    turtle.bgcolor('grey') # Has to be a neutral shade like grey to contrast the black and white theme.
    for t.iterable in range(600):  #360 is default. Use lower number for testing. The higher the number, the longer the show.
        t.le.pensize(30)
        # s.watermark()
        t.le.color(0,0,0) # 0,0,0 is default (Black)
        t.le.left(-t.my_angle + t.phi)
        t.le.circle(250)
        t.le.color(255,255,255) # 255,255,255 is default (White)
        t.le.left(-t.my_angle)
        t.le.circle(250)
        f.save_thumb()
    f.save_final_thumb()
    turtle.setup(5,5)
    f.set_vid_env()
    f.sync_av()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin


#novo_2
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def colorful_mandala():
    Tm.set_time()
#     print('Starting colorful_mandala by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/colorful_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the colorful_mandala() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 114 - 187,  2nd module of 36')
    print('Ran on:  ' + str(Tm.my_time))
    t.my_venv()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Colorful Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    # s.title_screen()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            t.my_angle = a.i_angle[a.i]
            f.folder_name = 'colorful_mandala' + '_' + t.my_key + '_' +  str(t.my_angle)
            f.make_png_folder()
            au.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            t.my_str = str('A  Colorful  Mandala  featuring   ' + str( t.my_angle) + '  ' + '    Degree Angles,  with  ' + au.my_track)
            turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
            print('The angle for this mandala is    ' + str(t.my_angle) + '    degrees.')
            t.iterable = 0
            t.li.pensize(1)
            turtle.bgcolor(50,10,10)
            t.la.right(t.my_angle/2)
            t.li.left(t.my_angle/2)
            while t.iterable <= length:
                R =  0
                G = 240
                B =  255

                t.la.color( t.iterable, G - t.iterable % 238, B - t.iterable)
                t.la.forward(t.iterable * t.phi)
                t.la.left(t.my_angle)
                t.la.pensize(t.iterable / 63)
                t.la.right(t.my_angle)
                t.la.circle(t.iterable + t.phi, t.my_angle, 6)

                t.li.color( B - t.iterable, R + t.iterable, G - t.iterable % 228 )
                t.li.forward(t.iterable * t.phi)
                t.li.right(t.my_angle)
                t.li.forward(t.iterable + t.phi)
                t.li.pensize(t.iterable / 54)
                f.save_thumb()
                t.iterable += 1
            a.i += 1
            f.save_final_thumb()
            turtle.setup(5,5)
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            #  #  #
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
#     time.sleep(3)
    Tm.set_time()
#     print('Starting jagged_multigram() python code by Leon Hatton on  ' + str(Tm.my_time))
    print(str('********************************************************************************************************************'))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/jagged_multigram_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting jagged_multigram() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 185 - 282, 3rd module of 36')
#     f.code_backup()
    t.my_venv() #Calls the template module
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Jagged Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    # s.title_screen()
    
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_angle = a.i_angle[a.i]
        f.folder_name = 'Jagged_Mandala' + '_' + t.my_key + '_' +  str(t.my_angle)
        f.make_png_folder()
        au.pick_track()
        os.chdir(f.loc_thumb + f.folder_name + '/')
        my_hue = random.randint(5, 100)
        my_hue_a = random.randint(100, 200)
        turtle.bgcolor(0, 0, 0)
        t.le.speed(0)
        t.me.speed(0)
        t.lb.speed(0)
        t.iterable = 0000
        t.my_str = str('A Jagged Mandala  featuring   ' + str(t.my_angle) + '  ' + '    Degree Angles  with   ' + au.my_track)
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
        t.my_venv()
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
        f.folder_name = 'Hued Polygonial Mandala' +'_'+ str(t.my_angle) + '_' + t.my_key
        f.make_png_folder()
        au.pick_track()
        os.chdir(f.loc_thumb + f.folder_name + '/')
        t.my_str = ' A Hued Polygonial featuring ' + str(round(t.my_angle)) + '  Degree Angles   with   '  + au.my_track
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
        h.pick_gold()
        h.pick_blue()
        t.la.rt(t.my_angle / 2)
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
            t.la.color( X - t.iterable, V + t.iterable, W)
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
    #             f.move_all()
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
    t.my_title = 'This Show Features Fantastic Mandalas with   ' + str(str_angles) + ' ' + 'angles'
    print(t.my_title)
#     s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        t.my_angle = a.i_angle[a.i]
        au.pick_track()
        t.my_str = 'A Fantastic Mandala featuring ' + str(round(t.my_angle)) + '  Degree Angles  with    '  + au.my_track
        f.folder_name = 'Fantastic Mandala_ '+ t.my_key + ' -' +  str(t.my_angle)
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name + '/')
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
#             f.move_all()
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
def dark_mandala(): #Needs work
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
    t.my_title = str('This Show Features Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    # s.title_screen()
    print(t.my_title)
#     f.code_backup()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        t.my_angle = a.i_angle[a.i]
        au.pick_track()
        t.my_str = ' A Dark Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles  with   ' + au.my_track
        f.folder_name = 'dark_mandala' + '_' +  str(t.my_angle) + '-' + t.my_key + '-' + au.my_track
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name + '/')
        turtle.title(t.my_str)
        turtle.bgcolor(0, 0,100)
        print ("The pick_random pen is:   ",  h.dict ['pick_random']  )
        print ("The pick_dark pen is:  ", h.dict ['pick_dark']  )
        print ("The pick_indigo pen is':   ", h.dict ['pick_indigo']  )
        print ("The pick_dot pen is':   ", h.dict ['pick_dot']  )
        for t.iterable in range(25):
            if t.iterable > 255:
                t.lz.pencolor(200, 50, 10)
                t.my_pen.color(10, 10, 30)
                turtle.bgcolor(255, 255, 100)
                # s.watermark()
            else:
                turtle.bgcolor(t.iterable, t.iterable, 100)
            h.pick_random() #pen t.me
            h.pick_dark()  # pen t.lz
            h.pick_indigo() # pen t.li
#             t.lz.left(t.my_angle)
            for i in range(6):
                t.li.right(t.my_angle)
                t.li.pensize(t.iterable / 54)
                t.lz.pensize(t.iterable / 54)
#             t.lz.circle(t.iterable, t.my_angle)
                t.lz.penup()
                t.lz.backward(t.iterable / t.phi + i)
                t.lz.pendown()
                t.li.forward(t.iterable * t.phi)
                t.lz.right(t.my_angle / 6)
                t.lz.forward(t.iterable + i)
                t.li.right(t.my_angle / 6)
                t.li.forward(t.iterable * t.phi)
#             t.lz.penup()
                t.lz.right(t.my_angle / 6)
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
        f.move_all()
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
        t.my_angle = a.i_angle[a.i]
        au.pick_track()
        t.my_str = 'An Iridescent Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles  with   ' + au.my_track
        f.folder_name =  'An Iridescent Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name + '/')
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
        turtle.bgcolor(50, 10, 255)
#         t.le.left(t.my_angle / 2)
#         t.me.left(t.my_angle / 2)
        for t.iterable in range (length):  #255 is default. Use lower number for testing.
            turtle.bgcolor(50 - t.iterable %49, 10, 255 - t.iterable)
            t.le.pensize(t.iterable / 36)
            t.me.pensize(t.iterable / 18)
            t.le.right(t.my_angle)
            t.le.forward(t.iterable + t.phi)
            t.me.left(t.my_angle * t.phi)  # This is the offset angle
            t.me.pencolor(random.randint(100,200), random.randint(0,75) + t.iterable %150,  random.randint(175,255) - t.iterable %150)
            t.le.pencolor(random.randint(0,128) + t.iterable %126, random.randint(150,255)- t.iterable %126, random.randint(100, 200))
            t.le.circle( t.iterable, -t.my_angle)
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
#             f.move_all()
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
    print('Located @ line 590 - 657, 8th module of 36')
    t.my_venv()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Bold Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    # s.title_screen()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            Tm.start_time()
            t.my_angle = a.i_angle[a.i]
            au.pick_track()
            my_str = ' A Bold Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key + au.my_track
            t.my_str = my_str
            f.folder_name = t.my_str
            f.make_png_folder()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
            turtle.bgcolor(0,0,0)
            t.la.speed(0)
            t.la.left(t.my_angle /2)
            t.la.penup()
            t.la.setpos(0, 50)
            t.la.pendown()
            for t.iterable in range (255):      #255 is default. Use lower number for testing. 300 for audio.
                if t.iterable <= 234:
                     h.pick_gold()
                else:
                     t.la.pencolor(0, t.iterable, 255 - t.iterable)
                h.pick_blue()
                t.la.left(t.my_angle)
                t.la.circle(t.iterable, t.my_angle, 6)
                turtle.bgcolor(0, 255 - t.iterable, 255 - t.iterable)
                t.la.pensize(t.iterable / 30)
                f.save_thumb()
            print(t.my_str)
            time.sleep(6)
#             turtle.bgcolor(2,9,3)
            f.save_final_thumb()
            turtle.setup(5,5)
            f.set_vid_env()
            f.sync_av()
#             f.move_all()
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
def hued_gradiant():  # Uses 2 pens with offset t.phi angle
#     time.sleep(3)
    Tm.set_time()
#     print('Starting  hued_gradiant() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/hued_gradiant_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting  hued_gradiant() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 632 - 717, 9th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Gradiant Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    # s.title_screen()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            t.my_venv()
            Tm.start_time()
            t.my_angle = a.i_angle[a.i]
            au.pick_track()
            print('The offset angle value is  ' + str(t.my_angle * t.phi))
            my_str = ' A Random Gradiant Hued Mandala featuring '+ str(round(t.my_angle)) + ' and  ' + str(round (t.my_angle * t.phi)) +'  Degree Angles'  + t.my_key  + au.my_track
            t.my_str = my_str
            f.folder_name = t.my_str
            f.make_png_folder()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
            turtle.bgcolor(0,0,10)
            t.le.pensize(1)
            t.me.pencolor(200, 99, 102)
            t.le.left(t.my_angle / 2)
            t.me.left(t.my_angle / 2)
            while t.iterable <= 333:
                turtle.bgcolor(5, 10, 40)
                R =  random.randint(100,200)
                G =  0
                B =  255
                L = 255
                M = random.randint(100,200)
                N = 0
                t.le.pencolor( R , G + t.iterable %216, B - t.iterable %126 )
                t.me.pencolor(L, M, N)
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
                t.me.pencolor(random.randint(100,200), 255, random.randint(100,200))
                t.le.dot(9)
                t.me.dot(9)
                t.le.right(t.my_angle)
                t.me.right(t.my_angle * t.phi) # This is the offset angle
                t.le.forward(t.iterable / t.phi)
                t.me.forward(t.iterable / t.phi)
                t.le.pencolor(random.randint(100,200), 255, 255)
                t.me.pencolor(25, random.randint(100,200), 25)
                t.le.dot(9)
                t.me.dot(9)
                t.me.pensize(t.iterable / 72)
                t.le.pensize(t.iterable /72)
                t.iterable += 1
                f.save_thumb()
            time.sleep(1)
            f.save_final_thumb()
            turtle.setup(5,5)
            f.set_vid_env()
            f.sync_av()
#             f.move_all()
            reset_all()
            #  #
            t.my_venv()
        # s.end_screen()
        t.reset_all()
        Tm.end_time()
    # s.end_screen()
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
    t.my_title = str('This Show Features Animated Abtract Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    # s.title_screen()
    Tm.start_time()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        t.my_angle = a.i_angle[a.i]
        au.pick_track()
        my_str = ' An Animated Abstraction Mandala-auto featuring '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key + au.my_track
        t.my_str = my_str
        f.folder_name =  t.my_str
        f.make_png_folder()
        os.chdir(f.loc_thumb + f.folder_name + '/')
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
        print(my_str)
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
    print('Starting animated_abstraction() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 825 - 901, 11th module of 36')
#     f.code_backup()
    au.pick_track()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Gradiant Star Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        # s.title_screen()
        for a.i  in range( len(a.i_angle)):
            t.my_venv()
            with Timer("Elapsed time to run this code: {} minutes"):
                Tm.start_time()
                t.my_angle =  a.i_angle[a.i]
                au.pick_track()
                my_str = ' A Gradiant Star Mandala featuring     '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key + au.my_track
                t.my_str = my_str
                f.folder_name = t.my_str
                f.make_png_folder()
                os.chdir(f.loc_thumb + f.folder_name + '/')
                turtle.title(t.my_str)
    #             s.splash_screen()
                # s.watermark()
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
                    t.le.rt(t.my_angle * t.phi)
                    t.le.penup()
                    t.le.setpos(0,0)
                    t.le.pendown()
                    t.le.backward(t.iterable / t.pi)
                    t.le.forward(t.iterable)
                    t.me.left(t.my_angle)
                    t.me.circle(t.iterable / t.phi, t.my_angle, 12)
                    t.me.pencolor(175, t.iterable, 102 + t.iterable % 25) #Golden hues
                    t.me.pensize(t.iterable /27)
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
                #  #
                t.my_venv()
#                 f.move_all()
            reset_all()
            t.my_venv()
            Tm.end_time()
        # s.end_screen()
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin





#novo_12
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def growing_yin_yang(): #Published to YouTube 11/11/2021
    time.sleep(3)
    Tm.set_time()
    print('Starting growing_yin_yang() python code by Leon Hatton on  ' + str(Tm.my_time))
    stdoutOrigin=sys.stdout
    sys.stdout = open('/media/elemen/Container/Logs/growing_yin_yang_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting growing_yin_yang() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 880 - 930, 12th module of 36')
#     f.code_backup()
    f.folder_name = 'Growing Yin-Yang'
    f.make_png_folder()
    au.pick_track()
    os.chdir(f.loc_thumb + f.folder_name + '/')
    t.my_venv()
    Tm.start_time()
    t.my_title = 'This show features the growing yin-yang, animated.'
    t.my_angle = 180
    t.my_str = 'A Growing Yin-Yang Expression'  + t.my_key + au.my_track
    Tm.start_time()
    turtle.title(t.my_str)
#     s.splash_screen()
    turtle.bgcolor('grey') # Has to be a neutral shade like grey to contrast the black and white theme.
    for t.iterable in range(300):  #360 is default. Use lower number for testing. The higher the number, the longer the show.
        t.le.pensize(t.iterable / 20)
        t.le.color(0,0,0)
        t.le.left(-t.my_angle - t.pi)
        t.le.circle(t.iterable / 2)
        t.le.color(255,255,255)
        t.le.left(-t.my_angle + t.phi)
        t.le.circle(t.iterable / 2)
        f.save_thumb()
    f.save_final_thumb()
    while t.le.undobufferentries():
        f.save_undo()
        t.le.undo()
        print('Value of iterable: ' + str(t.iterable))
        print('Value of Undobufferentries:  ' + str(t.le.undobufferentries()))
        Tm.end_time()
        f.current_path()
        print('The current folder is:  ' + str(f.folder_name))
        f.try_video()
        f.sync_av()
#         f.move_all()
        time.sleep(3)
    Tm.end_time()
    # s.end_screen()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin








#novo_13
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def hued_polygram():  # Uses 2 pens with offset t.phi angle
#     time.sleep(3)
    Tm.set_time()
#     print('Starting hued_polygram() python code by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/hued_polygram_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting hued_polygram() python code by Leon Hatton on  ' + str(Tm.my_time))
    print('Located @ line 966 - 1026, 13th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range(len(a.i_angle)):
            t.my_venv()
            t.my_angle =  a.i_angle[a.i]
            au.pick_track()
            my_str = ' A Hued Polygram Mandala featuring    '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key + au.my_track
            t.my_str = my_str
            f.folder_name =  t.my_str
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str +';  ' 'music by Winston Rhodes & others\'s')
#             s.splash_screen()
            # s.watermark()
            turtle.bgcolor(10,100,10)
            print(str('The featured angle is     ') + str(t.my_angle) + 'with Winston Rhodes & others\'s   ' + au.my_track)
            for t.iterable in range(length):
                h.pick_indigo()
                t.li.left(-t.my_angle)
                t.li.forward(t.iterable * t.pi)
                h.pick_light()
                t.le.right(t.my_angle)
                t.le.forward(t.iterable / t.pi)
                h.pick_gold()
                t.la.forward(t.iterable)
                h.pick_dot()
                t.ld.dot(t.iterable /36 * t.phi)
                t.la.circle(t.iterable / 9, t.my_angle, 10)
                t.le.pensize(t.iterable / 66)
                t.li.pensize(t.iterable / 66)
                t.la.pensize(t.iterable / 66)
                f.save_thumb()
            f.save_final_thumb()
            turtle.setup(5,5)
            f.set_vid_env()
            f.sync_av()
#             f.move_all()
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
            f.folder_name = 'Pretty Polygonial Mandala' +'_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            au.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = ' A Pretty Polygram Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key  + au.my_track
            t.my_str = my_str
            turtle.title(t.my_str +';''   music by Winston Rhodes\'s and others   ')
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
#             f.move_all()
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
    print('Located @ line 1101 - 1186, 15th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Awesome Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        Tm.start_time()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            au.pick_track()
            my_str = 'An Awesome Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key  + au.my_track
            t.my_str = my_str
            f.folder_name =  t.my_str
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_title()  #turtle.title(t.my_str +'  with Winston Rhodes\'s   ' + au.my_track)
#             s.splash_screen()
            # s.watermark()
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
            h.pick_gold()
            t.la.left(t.my_angle/2)
            t.lm.left(t.my_angle/2)
            for t.iterable in range(450):  # 450 is default, use any number
                h.pick_gold()
                if t.iterable <= 255:
                    turtle.bgcolor(X, Y - t.iterable, Z - t.iterable)
                else:
                    turtle.bgcolor(X, 0, 0)
                t.la.pensize(t.iterable/120)
                t.la.left(t.my_angle)
                t.la.forward(t.iterable / t.phi)
                t.lm.pensize(t.iterable / 120)
                t.lm.rt(t.my_angle)
                if t.iterable <= 252:
                    t.lm.pencolor(L, M - t.iterable, M - t.iterable)
                else:
                    h.pick_magenta()  # t.me.pencolor(L, 0, t.iterable %250)
                t.lm.circle(t.iterable / t.phi, - t.my_angle, 6)
                f.save_thumb()
            print('The Value of color B is    ' + str(B))
            print('The Value of color L is    ' + str(L))
            f.save_final_thumb()
            turtle.setup(5,5)
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            #  #
            t.my_venv()
        Tm.end_time()
    # s.end_screen()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin




#novo_16
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_awesome_mandala():  # Based on Awesome Manadala
#     time.sleep(3)
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
    t.my_title = str('Featuring Pretty Awesome Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        with Timer("Elapsed time to run this code: {} minutes"):
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'pretty_awesome_mandala' + '_'  + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            au.pick_track()
            print(au.my_track)
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Pretty Awesome Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'  + t.my_key + au.my_track
            t.my_str = my_str
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
            f.move_all()
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
    t.my_title = str('Featuring Stupendous Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        print('===============================================================================')
        t.my_venv()
        Tm.start_time()
        with Timer("Elapsed time to run this code: {} minutes"):
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Stupendous_Mandala' + '_' + t.my_key + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            au.pick_track()
            my_str = 'A Stupendous Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles  -  ' + au.my_track
            os.chdir(f.loc_thumb + f.folder_name + '/')
            t.my_str = my_str
            my_title()
#             s.splash_screen()
            # s.watermark()
            turtle.bgcolor(0,0,0)
            print('The soundtrack being used for this show is: ' + str(au.my_track) + '   from the album \'Jubilee\'')
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
                    t.le.pencolor(B, R - t.iterable, G - t.iterable)
                else:
                    turtle.bgcolor(0, 0, 10)
                    t.me.pencolor(255,255,255)
                    t.me.pensize(4)
#                     t.me.pencolor(L, t.iterable - 75, t.iterable - 112)
                    t.le.pencolor(t.iterable - 75, t.iterable - 112, B)
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
            f.move_all()
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
    t.my_title = str('This Show Features Multi-Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_angle =  a.i_angle[a.i]
        f.folder_name = 'Multi-Hued Polygram' + '_' + str(t.my_angle) + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        au.pick_track()
        os.chdir(f.loc_thumb + f.folder_name + '/')
        my_str = 'A Multi-Hued Polygram Mandala featuring '+ str(round(t.my_angle)) + '  Degrees' + ' - v.' + t.my_key + au.my_track
        t.my_str = my_str
        my_title()
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
        f.move_all()
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
    f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Brave Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_angle =  a.i_angle[a.i]
        au.pick_track()
        my_str = 'A Brave Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
        t.my_str = my_str
        f.folder_name = 'Brave Mandala' + '_' + str(t.my_angle) + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        os.chdir(f.loc_thumb + f.folder_name + '/')
        my_title()
#             s.splash_screen()
        # s.watermark()
        turtle.bgcolor(0,0,0)
        print(str('The featured angle is     ') + str(t.my_angle))
        R = random.randrange(150, 250, 10)
        print('The value of color R :   ' + str(R))
        G = 0
        B = 255
        L = random.randrange(100, 200, 1)
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
            t.le.forward(t.iterable/2)
            t.le.left(t.my_angle)
            t.le.pencolor(R, G + t.iterable, B - t.iterable)
            t.me.pensize(1)
            t.me.pencolor(R, Y - t.iterable, L)
            t.me.circle(t.iterable / t.phi, t.my_angle)
            t.le.rt(t.my_angle)
            t.le.pencolor(L, M - t.iterable, N - t.iterable)
            t.le.circle(t.iterable * 1.26, - t.my_angle)
            f.save_thumb()   #Screenshot as a png set set up mp4
#                 f.save_undo() # Second screenshot as a png to set up reverse mp4
        f.save_final_thumb() #Saves completed image as a jpeg and a png
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        f.move_all()
        reset_all()
        t.my_venv()

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
    au.pick_track() # Uncomment to select random audio clip
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Color-Shifting Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'A Color-Shifting Mandala' + '_' + str(t.my_angle) + t.my_key
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            au.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Color Shifting Mandala featuring '+ str(round(t.my_angle)) + '  Degrees' + ' - v.' + t.my_key + au.my_track
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen() # Comment out for video with full audio as needed
            # s.watermark()
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
            f.move_all()
            reset_all()
            #  #
            t.my_venv()
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
    t.my_title = str('This Show Features Gold-Red Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            au.pick_track()
            my_str = 'A Gold-Red Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
            t.my_str = my_str
            f.folder_name = t.my_str
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
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
            time.sleep(3)
            f.save_final_thumb()
            turtle.setup(5,5)
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            #  #
            t.my_venv()
    # s.end_screen()
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin





#novo_22
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def Hued_freedom_star():
    time.sleep(3)
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
    t.my_title = str('This Show Features Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Hued Freedom Star' + '_' + str(t.my_angle) + t.my_key 
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            au.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Hued Freedom Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
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
            time.sleep(3)
            f.save_final_thumb()
            turtle.setup(5,5)
            f.set_vid_env()
            f.sync_av()
#             f.move_all()
            reset_all()
            #  #
            t.my_venv()
    t.reset_all()
    # s.end_screen()
    Tm.end_time()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin



#novo_23
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def blue_orange_mandala_144():
    time.sleep(3)
    Tm.set_time()
#     print('Starting blue_orange_mandala by Leon Hatton on  ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/blue_orange_mandala_144_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting blue_orange_mandala by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 1720 - 1784, 23rd module of 36')
#     f.code_backup()
    t.my_venv()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        t.my_angle =  420  #144 is the default
        f.folder_name = 'Blue-Orange-144 Mandala' + '_' + str(t.my_angle) + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        au.pick_track()
        os.chdir(f.loc_thumb + f.folder_name + '/')
        my_str = 'A Blue-Orange Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key  + au.my_track
        t.my_str = my_str
        turtle.title(t.my_str)
#         s.splash_screen()
        # s.watermark()
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
            t.le.forward(t.iterable  + 1.618)
            f.save_thumb()
            for g in range(12):
                R = 0 + t.iterable % 150
                Y = 100
                B = 255 - t.iterable % 150
                t.le.left(t.my_angle)
                t.le.color(R, Y, B)
                t.le.pensize(2)
                t.le.forward(500)
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
#         f.move_all()
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
    time.sleep(3)
    Tm.set_time()
#     print('Starting ribbons_mandala() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/ribbons_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting ribbons_mandala() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 1788 - 1861, 24th module of 36')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Ribbon-like Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
#     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            au.pick_track()
            my_str = 'A Ribbons Mandala featuring   '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
            t.my_str = my_str
            f.folder_name = 'Ribbons Mandala _' + str(t.my_angle) + t.my_key
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
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
                for g in range(10):
                    R = 101 + t.iterable %133
                    Y = 101 - t.iterable %100
                    B = 25 - t.iterable %20
                    t.le.left(t.my_angle)
                    t.le.color(R, Y, B)
                    t.le.pensize(2)
                    t.le.circle(81, t.my_angle, 9)
            f.save_thumb()
            reset_all()
            Tm.end_time()
            f.set_vid_env()
            f.sync_av()
#             f.move_all()
            reset_all()
            #  #
            t.my_venv()
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
    print('Located @ line 1829 -1897, 25th module of 36')
#     f.code_backup()
    t.my_venv()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        t.my_angle =  840 #205 is default
        f.folder_name = 'A Circular Mandala' + '_' + str(t.my_angle) + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        au.pick_track()
        os.chdir(f.loc_thumb + f.folder_name + '/')
        my_str = 'A Circular Mandala featuring '+ str(t.my_angle) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
        t.my_str = my_str
        turtle.title(t.my_str)
#         s.splash_screen()
        # s.watermark()
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
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
#         f.move_all()
        reset_all()
        t.my_venv()
    t.reset_all()
#     s.end_screen()
    Tm.end_time()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin




#novo_26
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def occillating_polygon(): # Needs work
    time.sleep(6)
#
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/occillating_polygon_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the occillating polygon() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1939 - 2019, 26th module of 36')
    Tm.start_time()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring Growing and Shrinking Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Occillating Polygon-auto' + '_' + str(t.my_angle) + t.my_key
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            au.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Growing and Shrinking Polygram featuring '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
            turtle.bgcolor(0,0,0)
            print(str('The featured angle is     ') + str(t.my_angle))
            turtle.title(t.my_str)
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
            #
        f.set_vid_env()
        f.sync_av()
        f.move_all()
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
    print('Located @ line 2023 - 2112, 27th module of 36')
    print('Ran on:  ' + str(Tm.my_time))
    Tm.start_time()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring Arc Star Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
#     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Arc-Star' + '_' + str(t.my_angle) + t.my_key
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            au.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'An Arc Star featuring    '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
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
#             f.move_all()
            reset_all()
            #  #
            t.my_venv()
        Tm.end_time()
#     s.end_screen()
    Tm.end_time()
    t.reset_all()
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin


#novo_28
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def home_star():
#     time.sleep(6)
    Tm.set_time()
#     print('Starting home_star() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/home_star_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting home_star() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2118- 2198, 28th module of 36')
    Tm.start_time()
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring Home Star Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
#     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        au.pick_track()
        t.my_angle =  a.i_angle[a.i]
        f.folder_name = 'Home-Star' +'_' + str(t.my_angle) + t.my_key + au.my_track
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        os.chdir(f.loc_thumb + f.folder_name + '/')
        my_str = 'A Home Star featuring    '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
        t.my_str = my_str
        turtle.title(t.my_str)
#             s.splash_screen()
        # s.watermark()
        turtle.bgcolor(25,50,0)
        print(str('The featured angle is     ') + str(t.my_angle))
        t.iterable = 0
        t.le.pensize(1)
        t.iterable = 0
        t.le.pensize(3)
#             t.le.right(t.my_angle * 2 )
        while t.iterable <= 359: #359 is default
            R = 150
            G = 230
            B = 255
            t.le.color(t.iterable % 75, G - t.iterable %75, B - t.iterable %150 )
            t.le.left(t.my_angle)
            t.le.penup()
            t.le.fd(t.iterable / t.phi )
            t.le.pendown()
            t.le.pensize(6)
            t.le.fd(t.iterable / t.phi)
            t.le.rt(t.my_angle)
            R =  0
            G =  0
            B=  90
            t.le.color( R + t.iterable %133 , G + t.iterable % 62, B + t.iterable % 100 )
            t.le.penup()
            t.le.fd(25)
            t.le.pensize(3)
            t.le.circle(12, t.my_angle, 10)
            t.le.pendown()
            t.le.backward(t.iterable + t.phi)
            t.le.pensize(t.iterable / 72)
            t.le.penup()
            t.le.setposition(0, 0)
            t.le.pendown()
            t.le.circle(t.iterable, t.my_angle, 5)
            t.iterable += 1
            f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
#             f.move_all()
        reset_all()
        #  #
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
    print('Located @ line 2262- 2320, 29th module of 36')
    Tm.start_time()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring Simple Star Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
#     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Simple Star' + '_' + str(t.my_angle) + t.my_key
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            au.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Simple Star featuring    '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            # s.watermark()
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
#             f.move_all()
            reset_all()
            #  #
            t.my_venv()
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
#     time.sleep(3)
#     print('Starting double_take() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/double_take_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting double_take() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2236 - 2295, 30th module of 36')
    Tm.start_time()
#     f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring Double-Penned Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
#     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle = a.i_angle[a.i]
            turtle.bgcolor(0, 50, 50)
            f.folder_name = 'Double-Penned Mandala_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            au.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Double-Penned Mandala featuring    '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
            t.my_str = my_str
            turtle.title(my_str)
#             s.splash_screen()
            # s.watermark()
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
#             f.move_all()
            reset_all()
            #  #
            t.my_venv()
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
    time.sleep(3)
    print('Starting cloverleaf() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/cloverleaf' + str(t.file_key) + '_log.txt', 'w')
#     print('Starting cloverleaf() by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2247 - 2304, 31st module of 36')
    Tm.start_time()
    f.code_backup()
    # Select which set of angles to run
    a.i_angle =a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring Cloverleaf Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
#     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        Tm.start_time()
        t.my_angle = a.i_angle[a.i]
        turtle.bgcolor(0, 50, 50)
        f.folder_name = 'CloverLeaf Mandala' + '_' + str(t.my_angle) + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        au.pick_track()
        os.chdir(f.loc_thumb + f.folder_name + '/')
        my_str = 'A Cloverleaf Mandala featuring    '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
        t.my_str = my_str
        turtle.title(my_str)
        # s.watermark()
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
        f.move_all()
        reset_all()
        #  #
        t.my_venv()
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
#     time.sleep(3)
#     print('Starting glorious_mandala by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/glorious_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Starting glorious_mandala by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2363- 2444, 32nd module of 36.')
#     f.code_backup()
    t.my_venv()
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        print('===============================================================================')
        t.my_venv()
        Tm.start_time()
        with Timer("Elapsed time to run this code: {} minutes"):
            t.my_angle =  a.i_angle[a.i]
            au.pick_track()
            t.my_str = 'A Glorious Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
            f.folder_name = str('Glorious_Mandala'+ '_' + str(t.my_angle)) + t.my_key
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            print(t.my_title)
            os.chdir(f.loc_thumb + f.folder_name + '/')
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
#             f.move_all()
            reset_all()
            #  #
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
def independent_mandala():
    Tm.set_time()
#     print('Starting independent_mandala() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/independent_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Starting Independent_Mandala Python module by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2519- 2594, 33rd module of 36.')
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
        with Timer("Elapsed time to run this code: {} seconds"):
            t.my_angle =  a.i_angle[a.i]
            au. pick_track()
            f.folder_name = 'independent_mandala' + '_' + str(t.my_angle) + t.my_key + au.my_track
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            t.my_str = 'An Independent Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles   ' + 'with   ' + au.my_track
            turtle.title(t.my_str)
            os.chdir(f.loc_thumb + f.folder_name + '/')
#             s.splash_screen()  # Commented out to facilitate accurate a/v processing of the .png images
            # s.watermark() # Commented out to facilitate accurate a/v processing of the .png images
            turtle.bgcolor(10,0,10)
            print('The soundtrack being used for this show is: ' + str(au.my_track))
            print('The featured angle is     ' + str(t.my_angle))
            global rand_num
            rand_num = random.randint(175, 255)
            print(('The value of rand_num is   ')  + str(rand_num))
            print('..........................................................................................................................................................................................')
            while t.iterable <= 255:
                R =  0
                G =  220
                B =  255
                t.le.color( R + t.iterable, G - t.iterable % 160, B - t.iterable)
                t.le.forward(t.iterable)
                t.le.left(t.my_angle)
                t.le.pensize(t.iterable / 56)
                t.le.color(t.iterable, rand_num, 255 - t.iterable)
                t.le.right(t.my_angle)
                t.le.circle(t.iterable + t.phi, t.my_angle, 6)

                t.ce.color( B - t.iterable, R + t.iterable, G - t.iterable % 150 )
                t.ce.forward(t.iterable * t.phi)
                t.ce.right(t.my_angle)
                t.ce.forward(t.iterable + t.phi)
                t.ce.pensize(t.iterable / 24)
                t.ce.color(255 - t.iterable, t.iterable, random.randint(50, 150))
                t.iterable += 1
                f.save_thumb()
        f.save_final_thumb()
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        f.move_all()
        reset_all()
        #  #
        t.my_venv()
    Tm.end_time()
#     s.end_screen() # Commented out to facilitate accurate a/v processing of the .png images
    t.reset_all()
    #  #  f.pause_option()
#     sys.stdout.close()
#     sys.stdout=stdoutOrig


#novo_34
def wall_show():
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    Tm.set_time()
    Tm.start_time()
#     print('Starting independent_mandala() by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/independent_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('Starting Wall Shows by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2591- 2659, 34th module of 36.')
#     f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using list comprehension
    t.my_title = str('Featuring wall shows with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
     # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        print('======================================================================')
        t.my_venv()
        Tm.start_time()
        au.pick_track()
        t.my_angle =  a.i_angle[a.i]
        f.folder_name = 'a wall show' + '_' + str(t.my_angle) + t.my_key + au.my_track
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        t.my_str = 'A Wall Show featuring '+ str(round(t.my_angle)) + '  Degree Angles   ' + '  with   '+ au.my_track
        os.chdir(f.loc_thumb + f.folder_name + '/')
        my_title()
    #             s.splash_screen()
        # s.watermark()
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
            f.save_thumb()
            turtle.bgcolor(30, 256 - t.iterable, 60)
        f.save_final_thumb()
        time.sleep(6)
        turtle.setup(5,5)
        f.set_vid_env()
        f.sync_av()
        f.move_all()
        reset_all()
        t.my_venv()
    Tm.end_time()
    t.reset_all()
    #  #  f.pause_option()
    


#novo_35
#Code for Black Seed of Life
def black_seed():
    Tm.set_time()
#     time.sleep(3)
#     print('Starting black seed mandala by Leon Hatton on   ' + str(Tm.my_time))
#     stdoutOrigin=sys.stdout
#     sys.stdout = open('/media/elemen/Container/Logs/glorious_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Starting black_seed_mandala by Leon Hatton on   ' + str(Tm.my_time))
    print('Located @ line 2679- 2768, 34th module of 36.')
#     f.code_backup()
    t.my_venv()
    turtle.title('Black Seed of Life')
    t.le.speed(30)
    t.le.pensize(36)

    t.ce.speed(30)
    t.ce.pensize(54)
    t.ce.pencolor(255,255,255)

    length = 234
    my_image = 'TBD'
    t.my_angle = 60 # 60 is default
    my_base = int(3600/ t.my_angle) # for loop integrity of the number of loops of the ce pen
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring Black Seed Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    # s.title_screen()
    for a.i  in range( len(a.i_angle)):
        print('===============================================================================')
        t.my_venv()
        Tm.start_time()
        t.my_angle =  a.i_angle[a.i]
        f.folder_name = 'Black Seed_Mandala'+ '_' + str(t.my_angle) + t.my_key
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        au.pick_track()
        my_str = 'A Black Seed Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles' + ' - v.' + t.my_key + au.my_track
        os.chdir(f.loc_thumb + f.folder_name + '/')
        t.my_str = my_str
        my_title()
#             s.splash_screen()
        # s.watermark()
        turtle.bgcolor(0,0,0)
        print('The soundtrack being used for this show is: ' + str(au.my_track))  #+ '   from the album \'Jubilee\'')
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
                f.move_all()
                reset_all()
            #  #
                t.my_venv()
        Tm.end_time()
    #     s.end_screen()
    Tm.end_time()
    t.reset_all()
    #  #  f.pause_option()
    #     sys.stdout.close()
    #     sys.stdout=stdoutOrig



#nomega
print('********************************************************************************************')
""" List of modules. To run, uncomment the row. A word of caution: Computer memory and speed take a hit with the 250+ looping, image creation,
 and video creation associated with each image file. No load testing has been made at this time. Also, because of the looping screenshots a dedicated,
 always on monitor is needed. The screenshot code will capture anything that is on the monitor screen while it is Starting. Power-saving and screensaver
 apps should be disabled while this code is running.
'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
"""
#  This first group of modules specifies a single angle; has no looping lists of angles
# basic_yin_yang()  # ( novo_1)  Located @ line 71 - 111, 1st module of 36. An animated rendition of the yin-yang grat.phic. My original; currently
                    # the most popular one on YouTube. Added the working do_video on 1/14/2022 which converts the png files/
                    #to gif, mp4, and avi files. Successfully automated video (.avi) creation 1/20/2022.

# blue_orange_mandala_144() novo_2 # 23 of 36; Located at rows 1510 - 1568. Added 12/7/2021 (Edited from Mandala_160_09292020)\
                            # Processed to mp4 12/7/2021
            # growing_yin_yang() #novo_3 12 of 36, Published to YouTube 11/11/2021, Need to work on further as of 4/3/2022


# circular_mandala_205()  # novo_4 25 of 36; Added 12/9/2021 (Edited from Mandala_160_09292020) Processed to mp4 12/9/2021
# '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# This group of modules specifies a list of angles to loop
#
# colorful_mandala() #novo_5 Row 101 - 151, #2 of 36 Updated to automate video creation 
# jagged_multigram() # novo_6 #Row 150, 3 of 36, Published to YouTube on 11/2/2021 Updated to automate video creation
# hued_polygonial() # novo_7 Rows 293 - 361,   4th module of 36. Features Blue and Red Hues. Modified 12/17/2021 Updated to automate video creation
          # On 4/28/2022, assigned an 'Offset Angle' to second turtle pen as the current angle times t.phi, looks good as a balance.
          # Base angle + it's t.phi offset. Nice.
# #'**********************************************************************************************************************'
# Fantastic_Mandala() # novo_8  Row 328 - 384, 5 of 36 # Works well. Updated to automate video creation Implemented 't.phi Offset' Angle on 4/28/2022.
# # #'**********************************************************************************************************************'
# dark_mandala() #novo_9 Row 352, 6 of 36, Revised 4/30/2022
# iridescent_polygram()  # novo_10 Row 516 - 577, 7 of 36 Modified 1/2/2022 Updated to automate video creation
# bold_mandala()  # novo_11 Row 578 - 643, 8 of 36, Updated to automate video creation  Implemented 't.phi Offset' Angle on 4/28/2022.
# hued_gradiant()  #novo_12 Row 647 - 733, 9 of 36
# animated_abstraction()  #  novo_10 10 of 36, Thumbs created 11/21/2021
# gradiant_mandala() #  novo_14 Row  785 - 852, 11 of 36. Last run date: 2/1/2022
# hued_polygram()  # novo_15  Row 799, number 13 of 36, created 11/14/2021; added print to file 3/1/2022
#               pretty_polygonial()   # novo_16   Row 856, 14 of 36, modified 11/19/2021  nEEDS WORK!

# awesome_mandala()  #  novo_17 15 of 36, Located at lines 1042 - 1118. Processed to mp4 and published to YouTube on 11/21/2021.\
#                                 # modified 11/20/2021, This is exceptional.
# #                                 # I might expand on it with other modules and angles. added print to file 3/1/2022\
#                                   # Altered code to randomnize gold color using h.pick_gold().
# 
# glorious_mandala() # novo_18 Created 4/6/2022, based on stupendous mandala. Located @ line 2337- 2419, 32nd module of 36.
# pretty_awesome_mandala() # novo_19 Row 997 - 1054, Number 16 of 36. Derived from awesome_mandala.\
#                             # Processed 90 degrees to MP4 on 12/15/2021
# #'**********************************************************************************************************************'
# stupendous_mandala() # novo_20 Row 1034 - 1101, number 17 of 36. Derived from pretty_awesome_mandala. Created 1/8/2022. added print to file 3/1/2022
#                         #Features a more prominent center than it's parent.  Works well.
# #'**********************************************************************************************************************'
# brave_mandala() #novo_21 Row 1116, Derived from awesome_mandala; 18 of 36
# color_shifting_mandala() # novo_22 Rows 1274 - 1327, 19 of 36 work on
# multi_hued_polygram() # novo_23 Row  1125 - 1180, 20 of 36
# gold_red_mandala()  # novo_25 Rows 1303 - 1353; 21 of 36 Added 12/3/2021; processed to mp4 12/16/2021(added 3 degrees)
# Hued_freedom_star() # novo_26 Row 1358 - 1428, 22 of 36; Added 12/4/2021
# # #
                  # occillating_polygon() # novo_27 NEED WORK ON THE UNDO FUNCTION Located @ line 1891 - 1968, 26th module of 36; Added 12/28/2021  Is first attempt to use undo function as way to create occillation
# arc_star() #novo_28 27 of 36; Located at lines 1586 - 1654. Added 01/06/2022. Derived from a Thought Matrix arc-star wriiten by me in 2020.\
#                        # Employs first use of automated creation of angle lists using numpy arange.
#
# home_star() #novo_28 28 of 36; Located at lines 1663 - 1730.  Added 01/06/2022. Derived from a Thought Matrix arc-star scripted by me in 2020.\
#                        # Employs first use of automated creation of angle lists using numpy arange. Called home_star because the turtle\
#                        # pen is picked up and dropped down at the center of the screen(0,0).
# ribbons_mandala()  #novo_30  24 of 36; Located at rows 1572 - 1635. Added 12/8/2021 (Edited from Mandala_160_09292020);\
#                         #converted to mult-angles on 1/20/2022
# use_abs() # novo_31 29 of 36; Located at line 1890. Uses the abs() function to draw the sides and points such that\
#                         #it continues until the point of origin is reached.
# double_take() # novo_32 30 of 36; Located at line 1843 - 1881. Facilitates the creation of a hexagram by using 2 pens drawn\
#                     # with same angles in opposite directions. Using specific angle array named a.i.angle_double.
cloverleaf() # novo_31 31 of 36, Located at line  2247 - 2304. Created 3/6/2022.
wall_show() # novo_32 of 36. Located at 2592 - 2659. Working on a suitable product to frame and display on a wall. Began development August 2022.
independent_mandala() # novo_33  Located @2492 - 2577. Developed June 2022, Added 6/28/2022. 33rd module of 36. Makes beautiful diagrams.
# black_seed()   # novo_36 Needs more work
f.code_backup()
# f.copy_videos() # Currently required to duplicate videos to Linux /home/elemen/Videos/Full_Vids from /media/elemen/Garage/Videos/Full_Vids.
turtle.exitonclick()  # Waits for mouse click to end the program;  Default is to leave uncommented.
