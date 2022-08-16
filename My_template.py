"""  My_template.py contains file manipulation scripts associated with master_mandala_maker.py.
 This custom module is needed to run master_mandala_maker. It sets up the environment that each of the
  30 or so mandala makers (modular scripts) depend upon to run all functions to successful completions.
 by LeonRHatton using Thonny IDE.
"""

global folder_name
folder_name = 'novonno_mandala'
import time
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
    turtle.setup(1910, 1070)  # This is the default screen size. Choose any size.
    turtle.title('The Novonno Healing Mandalas by LeonRHatton') # Placeholder. Is unique to each mandala maker
    turtle.shape('blank')
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
    
    global rand_pick, rand_num
    rand_num = random.randint(1,50)
    rand_pick = random.randint(51,120)
    
    global pi
    pi = 4 * math.atan(1)
    
    global phi
    phi = ( 1 + math.sqrt(5) ) / 2
    
    global my_pen # An instance of turtle. Used exclusivley to write on the images.
    my_pen = turtle.Turtle()
    my_pen.speed(0)
    my_pen.shape('blank')
    my_pen.pensize(1)
    
    global le # An instance of turtle.
    le = turtle.Turtle()
    le.speed(0)
    le.shape('blank')
    le.pensize(1)
    
    global ce # An instance of turtle.
    ce = turtle.Turtle()
    ce.speed(0)
    ce.shape('blank')
    ce.pensize(1)
    
    global lr # An instance of turtle.
    lr = turtle.Turtle()
    lr.speed(0)
    lr.shape('blank')
    lr.pensize(1)
    
    global li  # An instance of turtle.
    li = turtle.Turtle()
    li.speed(0)
    li.shape('blank')
    li.pensize(1)
    
    global lu # An instance of turtle.
    lu = turtle.Turtle()
    lu.speed(0)
    lu.shape('blank')
    lu.pensize(1)
    
    global ld  # An instance of turtle.
    ld = turtle.Turtle()
    ld.speed(0)
    ld.shape('blank')
    ld.pensize(1)
    
    global la # An instance of turtle.
    la = turtle.Turtle()
    la.speed(0)
    la.shape('blank')
    la.pensize(1)
    
    global lg # An instance of turtle.
    lg = turtle.Turtle()
    lg.speed(0)
    lg.shape('blank')
    lg.pensize(1)
    
    global lb # An instance of turtle.
    lb = turtle.Turtle()
    lb.speed(0)
    lb.shape('blank')
    lb.pensize(1)
    
    global lc  # An instance of turtle.
    lc = turtle.Turtle()
    lc.speed(0)
    lc.shape('blank')
    lc.pensize(1)
    
    global lm # An instance of turtle.
    lm = turtle.Turtle()
    lm.speed(0)
    lm.shape('blank')
    lm.pensize(1)
    
    global ll # An instance of turtle.
    ll = turtle.Turtle()
    ll.speed(0)
    ll.shape('blank')
    ll.pensize(1)
    
    global me # An instance of turtle.
    me = turtle.Turtle()
    me.speed(0)
    me.shape('blank')
    me.pensize(1)
    
    global lz # An instance of turtle.
    lz = turtle.Turtle()
    lz.speed(0)
    lz.shape('blank')
    lz.pensize(1)
    
    global iterable # Universal counter used as iterator.
    iterable = 0
    
    global file_key, my_key # Used to set a random number to avoid making duplicate file names.
    file_key = random.randrange(100,1000,1)
    my_key = ' -r.' + str(file_key)
    
        
    
    
    gc.enable()   
    
    
      
    #Utility to clear screen and reset to sequence next screen drawing
def reset_all():
    import time
    turtle.reset()
    my_pen.reset()
    le.reset()
    me.reset()
    lb.reset()
    la.reset()
    lg.reset()
    ld.reset()
    lr.reset()
    lc.reset()
    ll.reset()
    lu.reset()
    lm.reset()
    lu.reset()
    li.reset()
    time.sleep(9)
    
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
    
    
    
    
