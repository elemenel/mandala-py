#  My_template.py conntains file manipulation scripts associated with master_mandala_maker.py.
# This custom module is needed to run master_mandala_maker. It sets up the environment that each of the
#  30 or so mandala makers (modular scripts) depends upon to run it's functions to successful completions.
# by LeonRHatton using Thonny IDE.

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
    
    
    turtle.setup(1920, 1050)  # This is the default screen size. Choose any size.
    turtle.title('A Healing Mandala by LeonRHatton') # Placeholder. Is unique to each mandala maker
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
    my_title = str('A Healing Mandala featuring multiple angles') # Placeholder. Is unique to each mandala maker
    
    global my_str
    my_str = str('A Healing Mandala') # Placeholder. Is unique to each mandala maker
    
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
    
    global iterable # Universal counter used as iterator.
    iterable = 0
    
    global file_key # Used to set a random number to avoid making dupilcate file names.
    file_key = random.randrange(1,999,1)
    
        
    global lc  # An instance of turtle.
    lc = turtle.Turtle()
    lc.speed(0)
    lc.shape('blank')
    lc.pensize(1)
    
    global my_hue
    my_hue = random.randint(100, 255)
    
    global min_hue
    min_hue = 0
    
    global max_hue
    max_hue = 255
    
    
    
    #Utility to clear screen and reset to sequence next screen drawing
def reset_all():
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
    
    
    
    
