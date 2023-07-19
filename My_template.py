"""  My_template.py contains file manipulation scripts associated with master_mandala_maker.py.
 This custom module is needed to run master_mandala_maker. It sets up the environment that each of the
  40+ mandala makers (modular scripts) depend upon to run all functions to successful completions.
 by LeonRHatton using Thonny 4.0.1 IDE.
"""
import time
import turtle # The main turtle module is used in this module.
import time
import datetime as datetime
import random
import sys
import PIL 
import Timer as Tm
import math
import gc


turtle.colormode(255)

global my_filename
my_filename = str('The Novonno File') # Placeholder. Final filename is determined at runtime.

global folder_name
folder_name = 'novonno_files'

global count
count = 0

global file_key, my_key # Used to set a random number to avoid making duplicate file names.

file_key = random.randrange(100,90000,1)
my_key = '-r.' + str(file_key)

global my_project
my_project = str('The Novanno Healing Mandalas Project') # Placeholder. Final project name is determined at runtime.

global my_title
my_title = ()

global my_logfile
my_logfile = '/home/champ/Modules/Mandala Maker/Logs/my_filename.log'

global my_angle
my_angle = ()

global v_pen
v_pen = turtle.Turtle()
v_pen.shape('blank')
v_pen.speed(0)


global v_pen_a
v_pen_a = turtle.Turtle()
v_pen_a.shape('blank')
v_pen_a.speed(0)
 

def my_venv():
    Tm.set_time()
    turtle.setup(1950, 1070)  # This is the default screen size. Choose any size.
    turtle.title('The Novonno Healing Mandalas by LeonRHatton') # Placeholder. Is unique to each mandala maker
    turtle.shape('blank')
    turtle.mode('standard') #standard
    turtle.colormode(255)
    turtle.pensize(2)
    R = 255
    G = 255
    B = 255
    turtle.bgcolor(R,G,B)
   
   
    global rand_pick, rand_num
    rand_num = random.randint(1,50)
    rand_pick = random.randint(51,120)

    global pi
    pi = 4 * math.atan(1)

    global phi
    phi = ( 1 + math.sqrt(5) ) / 2
    
    # Create Turtle instances        
    global my_pen # 1. An instance of turtle. Used exclusivley to write on the Turtle canvas.
    my_pen = turtle.Turtle()
    my_pen.speed(0)
    my_pen.shape('blank')
    my_pen.pensize(1)
    

    global ce # 3. An instance of turtle. Used by my_hues module as 'pick_random' pen.
    ce = turtle.Turtle()
    ce.speed(0)
    ce.shape('blank')
    ce.pensize(1)
       
    global el # 2. An instance of turtle. Used by my_hues module as ' pick_light' pen.
    el = turtle.Turtle()
    el.speed(0)
    el.shape('blank')
    el.pensize(1)
    
    global go # 8. An instance of turtle. Used by my_hues module as 'pick_gold' pen.
    go = turtle.Turtle()
    go.speed(0)
    go.shape('blank')
    go.pensize(1)
    
    global lc  # 11. An instance of turtle.
    lc = turtle.Turtle()
    lc.speed(0)
    lc.shape('blank')
    lc.pensize(1)
       
    global lb # 10. An instance of turtle. Used by my_hues module as 'pick_blue' pen.
    lb = turtle.Turtle()
    lb.speed(0)
    lb.shape('blank')
    lb.pensize(1)
    
    global ld  # 7. An instance of turtle. Used by my_hues module as 'pick_dot' pen.
    ld = turtle.Turtle()
    ld.speed(0)
    ld.shape('blank')
    ld.pensize(1)
    
    global lg # 9. An instance of turtle. Used by my_hues module as 'pick_green' pen.
    lg = turtle.Turtle()
    lg.speed(0)
    lg.shape('blank')
    lg.pensize(1)
    
    global li  # 5. An instance of turtle. Used by my_hues module as 'pick_indigo' pen.
    li = turtle.Turtle()
    li.speed(0)
    li.shape('blank')
    li.pensize(1)
    
    global ll # 13. An instance of turtle.
    ll = turtle.Turtle()
    ll.speed(0)
    ll.shape('blank')
    ll.pensize(1)
    
    global lm # 12. An instance of turtle.
    lm = turtle.Turtle()
    lm.speed(0)
    lm.shape('blank')
    lm.pensize(1)
        
    global lq # 17. An instance of turtle. Used by my_hues module as 'pick_orange' pen
    lq = turtle.Turtle()
    lq.speed(0)
    lq.shape('blank')
    lq.pensize(1)
    
    global lr # 4. An instance of turtle. Used by my_hues module as ' pick_random_a' pen
    lr = turtle.Turtle()
    lr.speed(0)
    lr.shape('blank')
    lr.pensize(1)
    
    global lu # 6. An instance of turtle. Used by my_hues module as 'pick_red' pen.
    lu = turtle.Turtle()
    lu.speed(0)
    lu.shape('blank')
    lu.pensize(1)
    
    global ly # 16. An instance of turtle. Used by my_hues module as 'pick_yellow' pen.
    ly = turtle.Turtle()
    ly.speed(0)
    ly.shape('blank')
    ly.pensize(1)

    global lz # 15. An instance of turtle. Used by my_hues module as 'pick_dark' pen.
    lz = turtle.Turtle()
    lz.speed(0)
    lz.shape('blank')
    lz.pensize(1)
    
    global me # 14. An instance of turtle. Used by my_hues module as 'pick_magenta' pen.
    me = turtle.Turtle()
    me.speed(0)
    me.shape('blank')
    me.pensize(1)



    # Universal counter used as iterator.
    global iterable, iterable_time
    def get_iterable():
        current_date = datetime.datetime.now()
        dtime = int(current_date.strftime("%Y%m%d%H%M%S"))
        iterable = str(dtime)
        return iterable
    # get_iterable()
      
    #Garbage collector  
    gc.enable()     
    
    
      

