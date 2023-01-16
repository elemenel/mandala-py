"""  My_template.py contains file manipulation scripts associated with master_mandala_maker.py.
 This custom module is needed to run master_mandala_maker. It sets up the environment that each of the
  40+ mandala makers (modular scripts) depend upon to run all functions to successful completions.
 by LeonRHatton using Thonny IDE.
"""
import time
# from functools import lru_cache



global file_name
file_name = 'novonno_file'

global folder_name
folder_name = 'novanno_files'

global count
count = 0

global bg_count, bg_count_2,bg_count_3
bg_count = 0
bg_count_2 = 0
bg_count_3 = 0

global file_key, my_key # Used to set a random number to avoid making duplicate file names.
import random
file_key = random.randrange(100,10000,1)
my_key = ' -r.' + str(file_key)

global my_project
my_project = 'Master Mandala Maker'



def my_venv():
    import turtle # The main turtle module is used in this module.
    import time
    import datetime as datetime
    import random
    import sys
    from PIL import Image
    import Timer as Tm
    import my_angles as a
    import math
    import gc
    
    
    Tm.set_time()
    
    global turtle
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
    
    global my_angle
    my_angle = 120
    
    global my_title
    my_title = str('The Novonno Healing Mandalas featuring multiple angles') # Placeholder. Is unique to each mandala maker
    
    global my_str
    my_str = str('The Novonno Healing Mandalas') # Placeholder. Is unique to each mandala maker
    
    global my_project
    my_project = 'a mandala'
    
    global rand_pick, rand_num
    rand_num = random.randint(1,50)
    rand_pick = random.randint(51,120)
    
    global pi
    pi = 4 * math.atan(1)
    
    global phi
    phi = ( 1 + math.sqrt(5) ) / 2
    
    global my_pen # 1. An instance of turtle. Used exclusivley to write on the Turtle canvas.
    my_pen = turtle.Turtle()
    my_pen.speed(0)
    my_pen.shape('blank')
    my_pen.pensize(1)
    
    global le # 2. An instance of turtle. Used by my_hues module as ' pick_light' pen.
    le = turtle.Turtle()
    le.speed(0)
    le.shape('blank')
    le.pensize(1)
    
    global ce # 3. An instance of turtle. Used by my_hues module as 'pick_random' pen.
    ce = turtle.Turtle()
    ce.speed(0)
    ce.shape('blank')
    ce.pensize(1)
    
    global lr # 4. An instance of turtle. Used by my_hues module as ' pick_random_a' pen
    lr = turtle.Turtle()
    lr.speed(0)
    lr.shape('blank')
    lr.pensize(1)
    
    global li  # 5. An instance of turtle. Used by my_hues module as 'pick_indigo' pen.
    li = turtle.Turtle()
    li.speed(0)
    li.shape('blank')
    li.pensize(1)
    
    global lu # 6. An instance of turtle. Used by my_hues module as 'pick_red' pen.
    lu = turtle.Turtle()
    lu.speed(0)
    lu.shape('blank')
    lu.pensize(1)
    
    global ld  # 7. An instance of turtle. Used by my_hues module as 'pick_dot' pen.
    ld = turtle.Turtle()
    ld.speed(0)
    ld.shape('blank')
    ld.pensize(1)
    
    global la # 8. An instance of turtle. Used by my_hues module as 'pick_gold' pen.
    la = turtle.Turtle()
    la.speed(0)
    la.shape('blank')
    la.pensize(1)
    
    global lg # 9. An instance of turtle. Used by my_hues module as 'pick_green' pen.
    lg = turtle.Turtle()
    lg.speed(0)
    lg.shape('blank')
    lg.pensize(1)
    
    global lb # 10. An instance of turtle. Used by my_hues module as 'pick_blue' pen.
    lb = turtle.Turtle()
    lb.speed(0)
    lb.shape('blank')
    lb.pensize(1)
    
    global lc  # 11. An instance of turtle.
    lc = turtle.Turtle()
    lc.speed(0)
    lc.shape('blank')
    lc.pensize(1)
    
    global lm # 12. An instance of turtle.
    lm = turtle.Turtle()
    lm.speed(0)
    lm.shape('blank')
    lm.pensize(1)
    
    global ll # 13. An instance of turtle.
    ll = turtle.Turtle()
    ll.speed(0)
    ll.shape('blank')
    ll.pensize(1)
    
    global me # 14. An instance of turtle. Used by my_hues module as 'pick_magenta' pen.
    me = turtle.Turtle()
    me.speed(0)
    me.shape('blank')
    me.pensize(1)
    
    global lz # 15. An instance of turtle. Used by my_hues module as 'pick_dark' pen.
    lz = turtle.Turtle()
    lz.speed(0)
    lz.shape('blank')
    lz.pensize(1)
    
    
   # Universal counter used as iterator.
    global iterable 
    iterable = 0
      
    #Garbage collector  
    gc.enable()   
    
    
      
