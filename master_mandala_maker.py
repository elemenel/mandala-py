# A master_mandala_maker! Dependent on my_angles.py, Timer.py, my_splash_screen.py, my_hues.py, File_Scripts.py, and My_template.py
           # by LeonRHatton using Thonny IDE

import turtle
import time
import random
import My_template as t
import my_angles as a
import my_hues as h
import my_splash_screen as s
from PIL import Image #module for converting python output to image
import numpy as np
import cv2
import pyautogui
from datetime import datetime
from Timer import Timer 
import Timer as Tm
import FileScripts as f
import os
import sys
import audio_clips as au
import gc

t.my_venv()   #Initializes mandala drawing environments 

Tm.time_functions()   #Initializes time functions

def reset_all():   #Utility to clear screen and reset to sequence next screen drawing
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
    

turtle.bgcolor(0, 0, 10)

#Defines pens and pencolors
h.pick_red() #Pen lu
h.pick_indigo() #Pen li
h.pick_gold() #Pen la
h.pick_green() #Pen lg
h.pick_dark() #Pen ld
h.pick_blue() #Pen lb
h.pick_random() #Pen lr
h.pick_magenta() #Pen lm
h.pick_light() # Pen le

length = 252  #Default is 252; any lower number for testing


#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def basic_yin_yang():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/basic_yin_yang_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the yin_yang() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 58 - 97, 1st module of 30')
    t.my_venv()
    t.my_str = str('A Yin-Yang Expression')
    Tm.start_time()
    t.my_title = str('This show features the basic yin-yang, animated.')
    my_angle = 180
    turtle.title(t.my_str)
#     s.splash_screen()
    f.code_backup()
    f.folder_name = 'basic_yin_yang'
    f.make_png_folder()
    f.pick_track()
    os.chdir(f.loc_thumb + f.folder_name + '/')
    time.sleep(3)
    turtle.bgcolor('grey') # Has to be a neutral shade like grey to contrast the black and white theme.
    for t.iterable in range(300):  #360 is default. Use lower number for testing. The higher the number, the longer the show.
        t.le.pensize(30)
        s.watermark()
        t.le.color('indigo') # 0,0,0 is default (Black)
        t.le.left(-my_angle + t.phi)
        t.le.circle(250)
        t.le.color('aqua') # 255,255,255 is default (White)
        t.le.left(-my_angle)
        t.le.circle(250)
        f.save_thumb()
    f.save_final_thumb()
    time.sleep(5)
    f.set_vid_env()
    f.pick_track()
    f.sync_av()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

   
    
   
  

#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def colorful_mandala():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/colorful_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the colorful_mandala() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 95 - 147,  2nd module of 30')
    t.my_venv()
    f.code_backup()
    f.pick_track()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Colorful Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    s.title_screen() 
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            my_angle = a.i_angle[a.i]
            f.folder_name = 'colorful_mandala' + '_' + str(my_angle)
            f.make_png_folder()
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            t.my_venv()
            t.my_str = str('A  Colorful  Mandala  featuring   ' + str( my_angle) + '  ' + '    Degree Angles')
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            print('The angle for this mandala is    ' + str(my_angle) + '    degrees.')
            t.iterable = 0
            t.le.pensize(1)
            turtle.bgcolor(10,0,20)
            t.la.right(my_angle/2)
            t.le.left(my_angle/2)
            while t.iterable <= 359:  #400 is default. Use lower number for testing.
                X =  random.randint(100,250)
                Y =  random.randint(180,255)
                Z =  random.randint(30,255)
                h.pick_gold()
                turtle.bgcolor(t.iterable %81, t.iterable % 100, 0)
                t.la.forward(t.iterable * 1.25)
                t.la.right(my_angle)
                t.la.forward(t.iterable * 1.25)
                t.le.color( X , Y , Z - t.iterable %27)
                t.le.left(my_angle)
                t. le.circle(t.iterable / 2.5, my_angle )
                t.le.pensize(t.iterable / 72)
                t.la.pensize(t.iterable / 72)
                f.save_thumb()
                t.iterable += 1
            a.i += 1
            turtle.bgcolor(25,25,35)
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
        s.end_screen()
        reset_all()
        Tm.end_time()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

       




#**************************************************************************************************************        
  # Published to YouTube on 11/2/2021     
 #This script features three pens: le, me, and lb. They follow separate yet coordinated routes to compose the mandala.
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def jagged_multigram():
    print(str('********************************************************************************************************************'))
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/jagged_multigram_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the jagged_multigram() code')
    print('from the master_mandala_maker Python 3 module created and maintained by LR Hatton')
    print('Located @ line 153 - 235,   3rd module of 30')
    f.code_backup()
    t.my_venv() #Calls the template module
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Jagged Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    s.title_screen() 
    with Timer("Elapsed time to run this code: {} minutes"): #Starts timer
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            my_angle = a.i_angle[a.i]
            t.my_venv()
            f.folder_name = 'jagged_multigram' + '_' + str(my_angle)
            f.make_png_folder()
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_hue = random.randint(5, 100)
            my_hue_a = random.randint(100, 200)
            turtle.bgcolor(0, 0, 0)
            t.le.speed(0)
            t.me.speed(0)
            t.lb.speed(0)
            t.iterable = 0000
            t.my_str = str('A Jagged Mandala  featuring   ' + str(my_angle) + '  ' + '    Degree Angles')
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            print('The angle for this mandala is    ' + str(my_angle) + '    degrees.')
            print('The value of my_hue is' + '   ' + str(my_hue))
            print('The value of my_hue_a is' + '   ' + str(my_hue_a))
            t.iterable = 1
            turtle.bgcolor(0, 0, 0)
            t.le.left(my_angle/2)
            t.lb.left(my_angle/2)
            t.me.left(my_angle/2)
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
                t.le.left(my_angle)
                t.me.left(my_angle)
                t.lb.left(- my_angle)
                t.le.forward( t.iterable * 1.5 )
                t.me.forward( t.iterable  * t.phi )
                t.lb.forward( t.iterable  * 2)
                t.le.left(my_angle)
                t.me.left( - my_angle)
                t.lb.left( my_angle)
                t.me.forward(t.iterable  / 4)
                t.le.forward(t.iterable  / 3)
                t.lb.forward(t.iterable  / 5)
                t.le.circle(t.iterable / 63,  my_angle, 5)
                t.me.circle(t.iterable / 72,  my_angle)
                t.lb.circle(t.iterable / 54, my_angle)
                t.me.pensize(t.iterable  / 50 %25)
                t.le.pensize(t.iterable  / 50 %33)
                t.lb.pensize(t.iterable  / 50 %14)
                turtle.bgcolor(0, 0, t.iterable %252)
                f.save_thumb()
                t.iterable += 1
            turtle.bgcolor(5,9,5)
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
        Tm.end_time()
    reset_all()   
    s.end_screen()    
    Tm.end_time()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

 
 
 
 
 
#*****************************************************************************************************************************        
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++    
def hued_polygonial():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/hued_polygonial_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the hued_polygonial() from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 260 - 323,   4th module of 30')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('Featuring Blue and Red Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    s.title_screen()
    print(t.my_title)
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            t.my_venv()
            t.my_angle = a.i_angle[a.i]
            f.folder_name = 'Blue and Red Hued Mandala' + '_' + str(t.my_angle)
            f.make_png_folder()
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            t.my_str = ' A Mandala with Blues and Reds featuring ' + str(round(t.my_angle)) + '  Degree Angles'
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            h.pick_gold()
            h.pick_blue()
            t.la.rt(t.my_angle / 2)
            t.lb.rt(t.my_angle / 2)
            t.iterable = 0
            t.lb.speed(0)
            t.la.speed(0)
            turtle.bgcolor(a.i + 25 % 100, a.i + 20 %110, a.i + 50 % 250)
            while t.iterable <= 255:    #255 is default. Use lower number for testing.
                t.lb.pensize(t.iterable / 81)
                t.la.pensize(t.iterable / 63)
                R = 255
                G = random.randrange(0, 81, 7)       
                B = 0
                V = 0
                W = random.randrange(0, 81, 7)
                X =  255
                t.lb.color( R - t.iterable,  G,  B + t.iterable )
                t.la.color(V + t.iterable, W, X - t.iterable)
                t.lb.left(t.my_angle)
                t.lb.fd(t.iterable + t.phi)
                t.la.left(t.my_angle)
                t.la.circle(t.iterable * t.phi, t.my_angle, 9)
                turtle.bgcolor(255 - t.iterable, 155 - t.iterable %100, 50)
                f.save_thumb()
                t.iterable += 1
            print(t.my_str)
            time.sleep(3)
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
    Tm.end_time()
    s.end_screen()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

    
  
  
  
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++  
def Fantastic_Mandala():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/Fantastic_Mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the Fantastic_Mandala() from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 316 - 370,   5th module of 30')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = 'This Show Features Mixed Hued Mandalas with   ' + str(str_angles) + ' ' + 'angles'
    print(t.my_title)
    s.title_screen()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            t.my_venv()
            my_angle = a.i_angle[a.i]
            t.my_str = 'A Mandala with Mixed Hues featuring ' + str(round(my_angle)) + '  Degree Angles'
            f.folder_name = 'Mixed-Hued Mandala_'+ str(my_angle)
            f.make_png_folder()
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            h.pick_light()
            h.pick_gold()
            h.pick_indigo()
            t.la.rt(my_angle / 2)
            t.li.rt(my_angle / 2)
            t.iterable = 0
            t.li.speed(0)
            t.la.speed(0)
            turtle.bgcolor(10, 0, 10)
            while t.iterable <= 225:    #255 is default. Use lower number for testing. 300 for audio clip add.
                t.la.pensize(t.iterable / 46) #la is the gold hue
                t.li.pensize(t.iterable / 27)  #li is the purple hue
                t.le.pensize(t.iterable / 33)
                h.pick_light()
                h.pick_gold()
                h.pick_indigo()
                t.la.right(my_angle)
                t.la.fd(t.iterable * t.phi)
                t.le.fd(t.iterable)
                t.le.circle(t.iterable, my_angle) # le is a random light hue.
                t.li.circle(t.iterable, -my_angle)
                f.save_thumb()
                t.iterable += 1
            print(t.my_str)
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
    Tm.end_time()
    s.end_screen()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

      



#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def square_spiral(): #Needs work
    print('This is the square_spiral() from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 380 - 429,   6th module of 30')
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Blue and Red Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    s.title_screen()
    print(t.my_title)
    f.code_backup()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            t.my_venv()
            t.my_angle = a.i_angle[a.i]
            my_str = ' A Dark Mandala with Mixed Greens and Reds featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            f.folder_name = 'square_spiral-auto' + '_' + str(t.my_angle)
            f.make_png_folder()
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(25, 25,100) 
            for t.iterable in range(length):
                h.pick_red()
                h.pick_dark()
                h.pick_green()
                h.t.ld.pensize(t.iterable / 72)
                h.t.ld.forward(t.iterable * t.phi )
                h.t.ld.left(t.my_angle)
                h.t.lu.pensize(t.iterable / 54)
                h.t.lu.forward(t.iterable)
                h.t.lu.left(t.my_angle)
                h.t.lg.pensize(t.iterable / 27)
                h.t.lg.circle(t.iterable, t.my_angle, 9)
                h.t.lg.left(t.my_angle)
                f.save_thumb()
            print(my_str)
            turtle.bgcolor(2,9,3)
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
        Tm.end_time()
        s.end_screen()
        reset_all()
        sys.stdout.close()
        sys.stdout=stdoutOrigin
        gc.collect()

             
       
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def iridescent_polygram():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/iridescent_polygram_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the iridescent_polygram() from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 429 - 481,   7th module of 30')
    f.code_backup()
    t.my_venv() #Favorite angles: 144/5P, 210/12P, 834/TightSpiral,2394/20P,1350/Square
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Iridescent Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    s.title_screen()
    print(t.my_title)
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range(len(a.i_angle)):
            t.my_venv()
            my_angle = a.i_angle[a.i]
            my_str = ' An Iridescent Mandala featuring '+ str(round(my_angle)) + '  Degree Angles'
            t.my_str = my_str
            f.folder_name = t.my_str
            f.make_png_folder()
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(0, 0, 100)
            t.le.left(my_angle / 2)
            t.me.left(my_angle / 2)
            for t.iterable in range (300):  #255 is default. Use lower number for testing.
                t.le.pensize(t.iterable / 36)
                t.me.pensize(t.iterable / 45)
                t.le.right(my_angle)
                t.me.left(my_angle)
                t.me.pencolor(t.my_hue, t.min_hue + t.iterable %216,  t.max_hue - t.iterable %216)
                t.le.pencolor(t.min_hue + t.iterable %126, t.max_hue - t.iterable %126, t.my_hue)
                t.le.circle( t.iterable, -my_angle)
                t.me.circle(t.iterable * t.phi, my_angle)
                t.le.pencolor(255,255,t.my_hue)
                t.me.pencolor(255,t.my_hue, 255)
                t.le.dot(t.iterable / t.phi / 18)
                t.me.dot(t.iterable / t.phi / 9)
                f.save_thumb()
            time.sleep(3)    
            print(my_str)
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv() 
        Tm.end_time()
        s.end_screen()
        reset_all()
        sys.stdout.close()
        sys.stdout=stdoutOrigin
        gc.collect()

        
        
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def bold_mandala():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/bpld_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the bold_mandala() from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 476 - 525, 8th module of 30')
    t.my_venv()
    f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Blue and Gold Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    s.title_screen()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            Tm.start_time()
            my_angle = a.i_angle[a.i]
            my_str = ' A Blue and Gold Mandala featuring '+ str(round(my_angle)) + '  Degree Angles'
            t.my_str = my_str
            f.folder_name = t.my_str
            f.make_png_folder()
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(0,0,0)
            t.la.speed(0)
            t.lb.speed(0)
            for t.iterable in range (300):  #255 is default. Use lower number for testing. 300 for audio.
                h.pick_gold()
                h.pick_blue()
                t.la.left(my_angle)
                t.lb.right(my_angle)
                t.la.circle(t.iterable * 2, my_angle, 6)
                t.lb.circle(t.iterable * t.phi, -my_angle, 6)
                t.lb.forward(t.iterable / t.phi)
                t.la.pensize(t.iterable / 30)
                t.lb.pensize(t.iterable /50)
                f.save_thumb()
            print(t.my_str)
            time.sleep(6)
            turtle.bgcolor(2,9,3)
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

  
        

 
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++ 
def hued_gradiant():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/hued_gradiant_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the  hued_gramagon() from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 529 - 609, 9th module of 30')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Gradiant Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    s.title_screen()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            t.my_venv()
            Tm.start_time()
            t.my_angle = a.i_angle[a.i]
            my_str = ' A Random Gradiant Hued Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            f.folder_name = t.my_str
            f.make_png_folder()
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(0,0,0)
            t.le.pensize(1)
            t.me.pencolor(200, 99, 102)
            while t.iterable <= 300:
                R =  t.my_hue
                G =  0
                B =  255
                L = 255
                M = t.my_hue
                N = 0
                t.le.pencolor( R , G + t.iterable %226, B - t.iterable %226 )
                t.me.pencolor(L, M, N)
                t.me.pencolor(L - t.iterable % 206, M, N + t.iterable %246)
                t.le.forward( t.iterable)
                t.me.forward( t.iterable)
                t.le.left(t.my_angle)
                t.me.left(t.my_angle)
                t.me.forward(t.iterable /4)
                t.le.forward(t.iterable /5 )
#                 t.le.forward(45)
#                 t.me.forward(27)
                t.le.left(t.my_angle)
                t.me.left(t.my_angle)
                t.le.forward(t.iterable / 54)
                t.me.forward(t.iterable / 81)
                t.le.pencolor(255,255,t.my_hue)
                t.me.pencolor(t.my_hue,255,t.my_hue)
                t.le.dot(9)
                t.me.dot(9)
                t.le.right(t.my_angle)
                t.me.right(t.my_angle)
                t.le.forward(t.iterable / t.phi)
                t.me.forward(t.iterable / t.phi)
                t.le.pencolor(t.my_hue,255,255)
                t.me.pencolor(25,t.my_hue,25)
                t.le.dot(9)
                t.me.dot(9)
                t.me.pensize(t.iterable / 72)
                t.le.pensize(t.iterable /72)
                t.iterable += 1
                f.save_thumb()
            turtle.bgcolor(2,9,3)
            time.sleep(3)
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
        s.end_screen()    
        reset_all()
        Tm.end_time()
    s.end_screen()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

  
     
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++        
def animated_abstraction():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/animated _abstraction_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the  animated_abstraction() from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 640 - 710,   10th module of 30')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Animated Abtract Mandalas with   ' + str(str_angles) + '  ' + 'angles')
    print(t.my_title)
    s.title_screen()    
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        for a.i  in range( len(a.i_angle)):
            t.my_angle = a.i_angle[a.i]
            my_str = ' An Animated Abstraction Mandala-auto featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            f.folder_name = t.my_str
            f.make_png_folder()
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
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
            time.sleep(3)    
            f.save_thumb()
            print(my_str)
            turtle.bgcolor(255,255,255)
            reset_all()
            t.my_venv()
        time.sleep(3)    
        f.save_final_thumb()
        f.set_vid_env()
        f.sync_av()
        f.move_all()
        reset_all()
        t.my_venv()
    Tm.end_time()
    s.end_screen()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

   


#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def gradiant_mandala():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/gradiant_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the gradiant_mandala() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 686 - 736, 11th module of 30')
    f.code_backup()
    f.pick_track()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Gradiant Star Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            my_str = ' A Gradiant Star Mandala featuring     '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            f.folder_name = t.my_str
            f.make_png_folder()
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(10,0,15)
            t.le.pensize(1)
            t.me.pencolor(200, 99, 102)
            t.le.left(t.my_angle / 2)
            t.me.rt(t.my_angle / 2)
            for t.iterable in range(300):  #250 is default. Use lower number for testing, 300 for audio add.
                t.le.pensize(t.iterable/63)
                t.le.right(t.my_angle)
                R = 0
                G = 255
                B = 255
                t.le.color(R + t.iterable %150, G - t.iterable %150, B - t.iterable %150)
                t.le.forward(t.iterable  * t.pi )
                t.me.left(t.my_angle)
                t.me.circle(t.iterable / t.phi, t.my_angle, 12)
                t.me.pencolor(200, 99 + t.iterable %75, 102)
                t.me.pensize(t.iterable / 54)
                if t.iterable <= 255:
                    turtle.bgcolor(t.iterable, 0, t.iterable)
                else:
                    turtle.bgcolor(t.iterable - 200, 0, t.iterable - 200)
                f.save_thumb()
            turtle.bgcolor(2,9,3)
            t.my_pen.color( 10, 15, 50)
            Tm.end_time()
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            reset_all()
            t.my_venv()
            f.move_all()
        reset_all()
        t.my_venv()
        Tm.end_time()        
    s.end_screen()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

   
 
 
 
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def growing_yin_yang(): #Published to YouTube 11/11/2021
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/growing_yin_yang_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the growing yin_yang() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 772 - 808, 12th module of 30')
    f.code_backup()
    f.folder_name = 'Growing Yin-Yang'
    f.make_png_folder()
    f.pick_track()
    os.chdir(f.loc_thumb + f.folder_name + '/')
    t.my_venv()
    Tm.start_time()
    t.my_title = 'This show features the growing yin-yang, animated.'
    t.my_angle = 180
    t.my_str = 'A Growing Yin-Yang Expression'
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
        f.move_all()
        time.sleep(3)
    Tm.end_time()
    s.end_screen()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

    






#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def hued_polygram():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/hued_polygram_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the hued_polygram() code')
    print('from the master_mandala_maker Python module created and maintained by LeonRHatton')
    print('Located @ line 839 - 898, 13th module of 30')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration
    t.my_title = str('This Show Features Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range(len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            my_str = ' A Hued Polygram Mandala featuring    '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            f.folder_name = t.my_str
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str +'  with Winston Rhodes\'s   ' + f.my_track)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(10,100,10)
            print(str('The featured angle is     ') + str(t.my_angle) + 'with Winston Rhodes\'s   ' + f.my_track)
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
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_polygonial():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/pretty_polygonial_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the pretty_polygonial() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 880 - 938, 14th module of 30')
    f.code_backup()
    f.pick_track()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('This Show Features Pretty Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Pretty Polygonial Mandala' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = ' A Pretty Polygram Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            turtle.title(t.my_str +'  with Winston Rhodes\'s   ' + f.my_track)
#             s.splash_screen()
            s.watermark()
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
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
        s.end_screen()
        Tm.end_time()
        reset_all()
        sys.stdout.close()
        sys.stdout=stdoutOrigin
        gc.collect()

        


#**************************************************************************************************************        
  # First Published to YouTube on 11/21/2021
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++  
def awesome_mandala():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/awesome_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the awesome_mandala() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 964 - 1043, 15th module of 30')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('This Show Features Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        Tm.start_time()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            my_str = 'An Awesome Polygram Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            f.folder_name = 'Awesome Mandala' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track() 
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str +'  with Winston Rhodes\'s   ' + f.my_track)
#             s.splash_screen() 
            s.watermark() 
            turtle.bgcolor(0,0,0)
            print(str('The featured angle is     ') + str(t.my_angle))
            R = 0
            G = 0
            B = random.randrange(10, 100, 6)
            L = random.randrange(100, 255, 9)
            M = 255
            N = 110
            X = 10
            Y = 255
            Z = 255
            turtle.bgcolor(10, 255, 255)
            t.le.left(t.my_angle/2)
            t.me.left(t.my_angle/2)
            for t.iterable in range(450): # 255 is default, use lower number for testing
                if t.iterable <= 255:
                    turtle.bgcolor(X, Y - t.iterable, Z - t.iterable)
                else:
                    turtle.bgcolor(X, 0, 0)
                t.le.pensize(t.iterable/120)
                t.le.left(t.my_angle)
                if t.iterable <= 252:
                    t.le.pencolor('goldenrod')
                else:
                    t.le.pencolor('goldenrod')
#                 t.le.setpos(0,0)
                
                t.le.forward(t.iterable / t.phi)
                t.me.pensize(t.iterable / 120)
                t.me.rt(t.my_angle)
                if t.iterable <= 252:
                    t.me.pencolor(L, M - t.iterable, M - t.iterable)
                else:
                    t.me.pencolor(L, 0, t.iterable %250)
                t.me.circle(t.iterable / t.phi, - t.my_angle, 6)
               
                f.save_thumb()
            print('The Value of color B is    ' + str(B))
            print('The Value of color L is    ' + str(L))
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all() 
            reset_all()
            t.my_venv()
        Tm.end_time()     
    s.end_screen() 
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()




#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def pretty_awesome_mandala():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/pretty_awesome_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the pretty_awesome_mandala() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1014 - 1072, 16th module of 30')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('Featuring Pretty Awesome Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'pretty_awesome_mandala' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track() 
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Pretty Awesome Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(0,0,0)
            print(str('The featured angle is     ') + str(t.my_angle))
            R = 255
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
            for t.iterable in range(length): # 255 is default, use lower number for testing
                if t.iterable <= 255:
                    turtle.bgcolor(X- t.iterable, Y - t.iterable, Z)
                else:
                    turtle.bgcolor(0, 0, 10)
                t.le.pensize(t.iterable/27)
                t.le.left(t.my_angle)
                t.le.pencolor(R - t.iterable, G - t.iterable, B)
                t.le.forward(t.iterable / 2)
                t.me.pensize(3)
                t.me.rt(t.my_angle)
                t.me.pencolor(L, M + t.iterable, N + t.iterable)
                t.me.circle(t.iterable, - t.my_angle)
                f.save_thumb()
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

        



#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def stupendous_mandala():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/stupendous_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('This is the stupendous_mandala() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1121- 1201, 17th module of 30.')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('Featuring Stupendous Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        print('===============================================================================')
        t.my_venv()
        Tm.start_time()
        with Timer("Elapsed time to run this code: {} minutes"):
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Stupendous_Mandala' + '_' + str(t.my_angle) 
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()   
            my_str = 'A Stupendous Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            os.chdir(f.loc_thumb + f.folder_name + '/')
            t.my_str = my_str
            turtle.title(t.my_str +'  with Winston Rhodes\'s   ' + f.my_track)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(0,0,0)
            print('The soundtrack being used for this show is: ' + str(f.my_track) + '   from the album \'Jubilee\'')
            print('The featured angle is     ' + str(t.my_angle))
            R = 255
            G = 255
            B = random.randrange(150, 255, 1)
            print('The value of hue /B/ is   ' + str(B))
            L = random.randrange(10, 150, 1)
            print('The value of hue /L/ is   ' + str(L))
            M = 0
            N = 0
            X = 255
            Y = 255
            Z = 10
            turtle.bgcolor(10, 255, 255)
#             t.le.left(t.my_angle /2)
#             t.me.rt(t.my_angle /2)
            for t.iterable in range(359): # 255 is default, use lower number for testing; 300 for audio sync.
                if t.iterable <= 255:
                    turtle.bgcolor(X- t.iterable, Y - t.iterable, Z)
                    t.me.pencolor(L, M + t.iterable, N + t.iterable)
                    t.le.pencolor(R - t.iterable, G - t.iterable, B)
                else:
                    turtle.bgcolor(0, 0, 10)
                    t.me.pencolor(L, t.iterable - 112, t.iterable - 112)
                    t.le.pencolor(t.iterable - 112, t.iterable - 112, B)
#                 t.le.left(t.my_angle)
                t.me.circle(t.iterable + t.phi, - t.my_angle, 9)
                t.le.pensize(t.iterable /54)
                t.le.left(t.my_angle)
                t.le.forward(t.iterable)
                t.me.pensize(t.iterable / 54)
                t.me.rt(t.my_angle)
                t.me.forward(t.iterable / t.phi)
                f.save_thumb()
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
        Tm.end_time()    
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
          


#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def multi_hued_polygram():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/multi_hued_polygram_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the multi_hued_polygram() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1193- 1250, 18th module of 30')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('This Show Features Multi-Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Multi-Hued Polygram' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Multi-Hued Polygram Mandala featuring '+ str(round(t.my_angle)) + '  Degrees'
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark() # Be sure to customize to correctly id the music track
            t.iterable = 0
            t.le.right(t.my_angle /2)
        while t.iterable <= 536: #360 is default, use lower number for testing
            R =  0
            G =  230
            B =  200
            L =  0
            M =  0
            N =  36
            t.le.pensize(t.iterable /179)
            t.le.color( R + t.iterable %239, G - t.iterable %179, B - t.iterable %179)
            t.le.backward(t.iterable + t.phi)
#             t.le.circle(t.iterable * t.phi, -t.my_angle, 9)
            t.le.right(t.my_angle)
            
            t.le.backward(t.iterable + t.phi)
            if t.iterable <= 179:
                turtle.bgcolor(G - t.iterable, B - t.iterable, N)
            else:
                turtle.bgcolor(L, M, N)
            t.iterable += 1
            f.save_thumb()
        f.save_final_thumb()
        f.set_vid_env()
        f.sync_av()
        f.move_all()
        reset_all()
        t.my_venv()
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

    
    
    
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def awesome_mandala_b():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/awesome_mandala_b_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the awesome_mandala_b() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1166 - 1227, 19th module of 30')
    f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('This Show Features Random-Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Awesome Random-Hued Mandala' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'An Awesome Polygram Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(0,0,0)
            print(str('The featured angle is     ') + str(t.my_angle))
            R = random.randrange(100, 250, 25)
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
            for t.iterable in range(length): #255 is default, use lower number for testing
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
            time.sleep(3)    
            f.save_final_thumb() #Saves completed image as a jpeg and a png
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            t.my_venv()
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()




#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def color_shifting_mandala():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/color_shifting_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the color_shifting_mandala() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1317 - 1377, 20th module of 30')
    f.code_backup()
    f.pick_track() # Uncomment to select random audio clip
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('This Show Features Color-Shifting Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen() 
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'A Color-Shifting Mandala' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Color Shifting Mandala featuring '+ str(round(t.my_angle)) + '  Degrees'
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen() # Comment out for video with full audio as needed
            s.watermark() 
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
            f.set_vid_env()
            f.sync_av() 
            f.move_all() 
            reset_all()
            t.my_venv()
    f.save_final_thumb()     
    s.end_screen() 
    Tm.end_time() 
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

    
    
    
    
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++                
def gold_red_mandala():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/gold_red_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the gold_red_mandala() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1303 - 1353, 21st module of 30')
    f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('This Show Features Gold-Red Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            my_str = 'A Gold-Red Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            f.folder_name = t.my_str
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(0,0,0)
            print(str('The featured angle is     ') + str(t.my_angle))
            turtle.bgcolor("indigo")
            for t.iterable in range(359): #252 is default, use lower number for testing; 300 for audio clip add
                h.pick_gold()
                h.pick_red()
                h.pick_light()
                t.la.pensize(t.iterable / 27)
                t.la.circle(t.iterable, - t.my_angle)
                t.lu.pensize(t.iterable/18)
                t.lu.backward(t.iterable)
                t.lu.right(t.my_angle)
                t.le.dot(3)
                t.le.left(t.my_angle)
                t.le.forward(t.iterable/6)
                f.save_thumb()
            time.sleep(3)    
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

    
    

    
#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++                
def Hued_freedom_star():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/Hued_Freedom_star_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the Hued_freedom_star code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1358 - 1428, 22nd module of 30')
    f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('This Show Features Hued Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
#     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Hued Freedom Star' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Hued Freedom Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            print(str('The featured angle is     ') + str(t.my_angle))
            t.le.color(122,133,215)
            R = 0
            G = 50
            B = 255
            turtle.bgcolor(R, G, B)
#             t.le.penup()
#             t.le.setpos(-25,450)
#             t.le.pendown()

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
                t.le.forward(t.iterable + 63)
                white_dot()
                t.le.rt(t.my_angle)
                t.le.pencolor(123 + t.iterable %100 ,135,216 -t.iterable %200)
                t.le.forward(t.iterable)
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
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
        reset_all()        
    s.end_screen()
    Tm.end_time()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()




#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def blue_orange_mandala_144():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/blue_orange_mandala_144_' + str(t.file_key) + '_log.txt', 'w')
    print('This is theblue_orange_mandala_144 code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1510 - 1568, 23rd module of 30')
    f.code_backup()
    t.my_venv()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        t.my_angle =  144
        f.folder_name = 'Blue-Orange-144 Mandala' + '_' + str(t.my_angle)
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        f.pick_track()
        os.chdir(f.loc_thumb + f.folder_name + '/')
        my_str = 'A Blue-Orange Mandala featuring '+ str(round(t.my_angle)) + '  Degree Angles'
        t.my_str = my_str
        turtle.title(t.my_str)
#         s.splash_screen()
        s.watermark()
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
       
        for t.iterable in range(300): #251 is default, use lower number for testing
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
        f.set_vid_env()
        f.sync_av()
        f.move_all()
        reset_all()
        t.my_venv()
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()



#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def ribbons_mandala():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/ribbons_mandala_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the ribbons_mandala code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1571 - 1641, 24th module of 30')
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('This Show Features Ribbon-like Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            my_str = 'A Ribbons Mandala featuring   '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            f.folder_name = 'Ribbons Mandala _' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
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
            f.move_all()
            reset_all()
            t.my_venv()
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()




#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def circular_mandala_205():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/circular_mandala_205_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the circular_mandala 205 code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1597 - 1662, 25th module of 30')
    f.code_backup()
    t.my_venv()
    with Timer("Elapsed time to run this code: {} minutes"):
        Tm.start_time()
        t.my_angle =  205
        f.folder_name = 'A Circular Mandala' + '_' + str(t.my_angle)
        f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
        f.pick_track()
        os.chdir(f.loc_thumb + f.folder_name + '/')
        my_str = 'A Circular Mandala featuring '+ str(t.my_angle) + '  Degree Angles'
        t.my_str = my_str
        turtle.title(t.my_str)
#         s.splash_screen()
        s.watermark()
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
        t.le.setpos(0, -50)
        t.le.pendown()
        t.le.speed(0)
        t.le.shape("circle")
        t.le.shapesize(1)
        t.le.pensize(1)
        t.le.hideturtle()
        t.le.color(R, G, B)


        for t.iterable in range(300): #200 is default, use lower number for testing
            turtle.bgcolor(L, C, H + t.iterable %299)
            t.le.pensize(10)
            t.le.right(t.my_angle)
            t.le.color(L +t.iterable %80 , C + t.iterable %80, H)
            t.le.forward(t.iterable  + 1.618)
            f.save_thumb()
            for g in range(8):
                R = 101 + t.iterable %133
                Y = 101 - t.iterable %130
                B = 25 + t.iterable %100
                t.le.left(t.my_angle)
                t.le.color(R, G - t.iterable % 25, B)
                t.le.pensize(2)
                t.le.circle(70, t.my_angle, 11)
        f.save_final_thumb()
        f.set_vid_env()
        f.sync_av()
        f.move_all()
        reset_all()
        t.my_venv()
    reset_all()
    s.end_screen()
    Tm.end_time()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()




#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def occillating_polygon():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/occillating_polygon_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the occillating polygon() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1665 - 1727, 26th module of 30')
    Tm.start_time()
    f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('Featuring Growing and Shrinking Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Occillating Polygon-auto' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Growing and Shrinking Polygram featuring '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(0,0,0)
            print(str('The featured angle is     ') + str(t.my_angle))
            turtle.title(t.my_str)
            t.iterable = 0
            t.le.pensize(1)
            print('The Angle is   ' + str(t.my_angle))
            while t.iterable <= 149: # Default is 149; can use lower number for testing
                R = 100  #  random.randrange(100,255)
                G = 255  #  random.randrange(171, 255)
                B = 255
                t.le.color( R + t.iterable, G - t.iterable, B - t.iterable % 27)
#                 t.le.left(t.my_angle / 2)
#                 t.le.left(t.my_angle)
                t.le.forward( t.iterable * 5.5)
                t.le.left(t.my_angle)
                t.le.color(255, G , B - t.iterable)
                t.le.dot(t.iterable / 6)
                t.le.pensize(t.iterable / 15)
                t.iterable += 1
                f.save_thumb()
                            
            f.save_final_thumb() 
            # The Undo routine which animates the shrinking
#             for t.iterable in range(1200): # Default is 1200; can use lower number for testing
            while t.le.undobufferentries():
                f.save_undo()
                t.le.undo()
                print('Value of iterable: ' + str(t.iterable))
                print('Value of Undobufferentries:  ' + str(t.le.undobufferentries()))
                
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            Tm.end_time()
            reset_all()
            t.my_venv()
    
    reset_all()        
    s.end_screen()
    Tm.end_time()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()



#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def arc_star():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/arc_star_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the arc-star() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1734 - 1806, 27th module of 30')
    Tm.start_time()
    f.code_backup()
    f.pick_track()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('Featuring Arc Star Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Auto_Arc-Star' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'An Arc Star featuring    '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
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
                t.le.color( t.iterable %150, G - t.iterable %100, B - t.iterable %150 )
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
            f.set_vid_env()
            f.pick_track()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
        Tm.end_time()
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

    
    

#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
def home_star():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/home_star_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the home-star() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 11736- 1807, 28th module of 30')
    Tm.start_time()
    f.code_backup()
    t.my_venv()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('Featuring Home Star Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
#     s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Home-Star' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Home Star featuring    '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(25,50,0)
            print(str('The featured angle is     ') + str(t.my_angle))
            turtle.title(t.my_str)
            t.iterable = 0
            t.le.pensize(1)
            t.iterable = 0
            t.le.pensize(3)
#             t.le.right(t.my_angle * 2 )
            while t.iterable <= 359:
#                 turtle.bgcolor(25, 50, t.iterable % 150)
                R =  0
                G =  0
                B =  90
                t.le.color( R + t.iterable %133 , G + t.iterable % 62, B + t.iterable % 100 )
                t.le.left(t.my_angle)
                t.le.penup()
                t.le.fd(t.iterable / t.phi )
                t.le.pendown()
                t.le.pensize(6)
                t.le.fd(t.iterable / t.phi)
                t.le.rt(t.my_angle)
                R = 150
                G = 230
                B = 255
                t.le.color(t.iterable % 75, G - t.iterable %75, B - t.iterable %150 )
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
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
    Tm.end_time()        
    s.end_screen()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()




#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#Deals best with whole number angles
def use_abs():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/use_abs_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the use_abs() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1890 - 1937, 29th module of 30')
    Tm.start_time()
    f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('Featuring Simple Star Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            t.my_angle =  a.i_angle[a.i]
            f.folder_name = 'Simple Star' + '_' + str(t.my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Simple Star featuring    '+ str(round(t.my_angle)) + '  Degree Angles'
            t.my_str = my_str
            turtle.title(t.my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(0,0,0)
            print(str('The featured angle is     ') + str(t.my_angle))
            turtle.title(t.my_str)
            t.iterable = 0
            t.le.pensize(1)
            t.iterable = 0
            t.le.pensize(3)
            t.le.color('red', 'yellow')
            t.le.begin_fill()
            while True:
                t.le.left(t.my_angle)
                t.le.forward(250)
                f.save_thumb()
                if abs(t.le.pos()) < 1:
                    break
            t.le.end_fill()
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
        Tm.end_time()
    s.end_screen()
    Tm.end_time()
    reset_all()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()

   
    
    
    

#+++++++++++MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++
#TEMPLATE FOR CODE TO CREATE Six-Pointed Mandalas or doubles.
def double_take():
    stdoutOrigin=sys.stdout 
    sys.stdout = open('/media/elemen/Container/Logs/double_take_' + str(t.file_key) + '_log.txt', 'w')
    print('This is the double_take() code')
    print('from the master_mandala_maker Python module of LR Hatton')
    print('Located @ line 1841 - 1882, 30th module of 30')
    Tm.start_time()
    f.code_backup()
    # Select which set of angles to run
    a.i_angle = a.i_angle_auto # Select set of angles to use.
    str_angles = [str(round(i)) for i in (a.i_angle)] #Convert integers in angle list to string for use in title screen, using iteration                 
    t.my_title = str('Featuring Double-Penned Mandalas with   ' + str(str_angles) + '  ' + 'angles.')
    print(t.my_title)
    s.title_screen()
    for a.i  in range( len(a.i_angle)):
        t.my_venv()
        with Timer("Elapsed time to run this code: {} minutes"):
            Tm.start_time()
            my_angle = a.i_angle[a.i]
            turtle.bgcolor(0, 50, 50)
            f.folder_name = 'Double-Penned Mandala' + '_' + str(my_angle)
            f.make_png_folder() # Deletes old folder and contents and creates new folder wth folder name
            f.pick_track()
            os.chdir(f.loc_thumb + f.folder_name + '/')
            my_str = 'A Double-Penned Mandala featuring    '+ str(round(my_angle)) + '  Degree Angles'
            t.my_str = my_str
            turtle.title(my_str)
#             s.splash_screen()
            s.watermark()
            turtle.bgcolor(0,0,0)
            R = random.randrange(155,255, 5)
            G = 255
            B = 0
            print('The value of color R is    ' + str(R))
            for t.iterable in range(359):
                t.le.pensize(4)
                t.li.pensize(4)
                t.le.left(my_angle)
                t.le.color(R, G - t.iterable %255, B + t.iterable %255)
                t.le.forward(t.iterable * t.phi)
                t.li.color(R, G - t.iterable %250, B + t.iterable %250)
                t.li.right(my_angle)
                t.li.forward(t.iterable * t.phi)
                f.save_thumb()
            f.save_final_thumb()
            f.set_vid_env()
            f.sync_av()
            f.move_all()
            reset_all()
            t.my_venv()
        Tm.end_time()        
    s.end_screen()
    reset_all()
    Tm.end_time()
    sys.stdout.close()
    sys.stdout=stdoutOrigin
    gc.collect()


   


# List of modules. To run, uncomment the row. A word of caution: Computer memory and speed take a hit with the 250+ looping, image creation,\
# and video creation associated with each image file. No load testing has been made at this time. Also, because of the screenshots a dedicated \
# machine is needed. The screenshot code will capture anything that is on the monitor screen while it is running.
# '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
#  This first group of modules specifies a single angle; no looping lists of angles
# basic_yin_yang() # Located at rows 58 - 97.  # 1 of 30. An animated rendition of the yin-yang graphic. My original; currently
                    # the most popular one on YouTube. Added the working do_video on 1/14/2022 which converts the png files/
                    #to gif, mp4, and avi files. Successfully automated video (.avi) creation 1/20/2022.

# blue_orange_mandala_144() # 23 of 30; Located at rows 1510 - 1568. Added 12/7/2021 (Edited from Mandala_160_09292020)\
                            # Processed to mp4 12/7/2021
# growing_yin_yang() #12 of 30, Published to YouTube 11/11/2021, Need to work on
 

# circular_mandala_205()  # 25 of 30; Added 12/9/2021 (Edited from Mandala_160_09292020) Processed to mp4 12/9/2021
# '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# This group of modules specifies a list of angles to loop
# 
# colorful_mandala() # Row 101 - 151, #2 of 30 Updated to automate video creation
# jagged_multigram()  #Row 150, 3 of 30, Published to YouTube on 11/2/2021 Updated to automate video creation
hued_polygonial() # Row 260 - 323, 4 of 30. Features Blue and Red Hues. Modified 12/17/2021 Updated to automate video creation
#'**********************************************************************************************************************'
Fantastic_Mandala() # Row 328 - 384, 5 of 30 # Works well. Updated to automate video creation
#'**********************************************************************************************************************'
# square_spiral() # Row 352, 6 of 30, Work on some more
# iridescent_polygram()  # Row 441 - 468, 7 of 30 Modified 1/2/2022 Updated to automate video creation
bold_mandala()  # Row 476 - 525, 8 of 30 Updated to automate video creation
# hued_gradiant()  # Row 528, 9 of 30
# animated_abstraction()  # 10 of 30, Thumbs created 11/21/2021
# gradiant_mandala() # Row 686 - 736, 11 of 30. Last run date: 2/1/2022

# hued_polygram()  # Row 799, number 13 of 30, created 11/14/2021; added print to file 3/1/2022
# pretty_polygonial()  #Row 856, 14 of 30, modified 11/19/2021
# 
awesome_mandala()  # 15 of 30, Located at lines 911 - 971. Processed to mp4 and published to YouTube on 11/21/2021.\
#                                 # modified 11/20/2021, This is exceptional.
#                                 # I might expand on it with other modules and angles. added print to file 3/1/2022

pretty_awesome_mandala() # Row 997 - 1054, Number 16 of 30. Derived from awesome_mandala.\
#                             # Processed 90 degrees to MP4 on 12/15/2021
# #'**********************************************************************************************************************'
stupendous_mandala() # Row 1034 - 1101, number 17 of 30. Derived from pretty_awesome_mandala. Created 1/8/2022. added print to file 3/1/2022
#                         #Features a more prominent center than it's parent.  Works well.
# #'**********************************************************************************************************************'
# awesome_mandala_b() # Row 1116, Derived from awesome_mandala; 18 of 30
color_shifting_mandala() # Rows 1274 - 1327, 19 of 30
multi_hued_polygram() # Row  1125 - 1180, 20 of 30
gold_red_mandala()  # Rows 1303 - 1353; 21 of 30 Added 12/3/2021; processed to mp4 12/16/2021(added 3 degrees)
# Hued_freedom_star() # Row 1358 - 1428, 22 0f 28; Added 12/4/2021
# 
# occillating_polygon()  #26 of 30; Added 12/28/2021  Is first attempt to use undo function as way to create occillation
# arc_star() #27 of 30; Located at lines 1586 - 1654. Added 01/06/2022. Derived from a Thought Matrix arc-star wriiten by me in 2020.\
                       # Employs first use of automated creation of angle lists using numpy arange.
# 
# home_star() #28 of 30; Located at lines 1663 - 1730.  Added 01/06/2022. Derived from a Thought Matrix arc-star scripted by me in 2020.\
#                        # Employs first use of automated creation of angle lists using numpy arange. Called home_star because the turtle\
#                        # pen is picked up and dropped down at the center of the screen(0,0).
# ribbons_mandala()  # 24 of 30; Located at rows 1572 - 1635. Added 12/8/2021 (Edited from Mandala_160_09292020);\
                        #converted to mult-angles on 1/20/2022
# use_abs() # 29 of 30; Located at line 1890. Uses the abs() function to draw the sides and points such that\
                        #it continues until the point of origin is reached.
# double_take() # 30 of 30; Located at line 1843 - 1881. Facilitates the creation of a hexagram by using 2 pens drawn\
#                     # with same angles in opposite directions. Using specific angle array named a.i.angle_double.

turtle.exitonclick()  # Exits the final module and shuts down turtle. Default is to leave uncommented.


