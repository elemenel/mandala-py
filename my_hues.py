'''my_hues.py contains color manipulation scripts associated with master_mandala_maker.py
                  by LeonRHatton
'''
import My_template as t
import random
import turtle
turtle.colormode(255)
'''************************************************************************************************************************************'''



#  Gradually change screen background hues between  two hues


'''************************************************************************************************************************************'''
def bg_fade_dark_to_yellow():
    if t.bg_count <= 765:
         turtle.bgcolor(fade_count_3 ,fade_count_3, 0) # Counter t.iterable starts at zero; background starts black, fades to yellow
    else:
        turtle.bgcolor(255, 255, 0) # Stops at Yellow Hue # Counter t.iterable starts at zero; background starts black, fades to yellow

def bg_fade_yellow_to_dark():
    if t.bg_count <= 765:
        turtle.bgcolor(255 - fade_count_3, 255 - fade_count_3, 10) # Counter t.iterable starts at zero; background starts yellow, fades to black
    else:
        turtle.bgcolor(0, 0, 10) # Stops at black hue @ 765
        
'''************************************************************************************************************************************'''


def bg_fade_dark_to_skyblue():
    global R, G, B, Z
    R =  0
    G = int(t.bg_count_2)
    B = int(t.bg_count_3)
    
    if t.bg_count <= 255:
        turtle.bgcolor(R, G, B) 
    else:
       turtle.bgcolor(0, 255, 255) # Stops at sky blue hue
       

def bg_fade_skyblue_to_dark():
    if t.bg_count <= 765:
         turtle.bgcolor(0, 255 - fade_count_3, 255 - fade_count_3) # Counter t.iterable starts at zero; background starts sky blue, fades to black
    else:
        turtle.bgcolor(0, 0, 0) # Stops at black hue
     
'''************************************************************************************************************************************'''

def bg_fade_dark_to_green():
    if t.bg_count <= 765:
        turtle.bgcolor(0,fade_count_3, 0) # Counter t.iterable starts at zero; background starts black, fades to green
    else:        
        turtle.bgcolor(0, 255, 0) # Stops at green hue
         

def bg_fade_green_to_dark():
    if t.bg_count <= 765:
        turtle.bgcolor(0, 255 - fade_count_3, 0) # Counter t.iterable starts at zero; background starts green, fades to black
    else:        
        turtle.bgcolor(0, 0, 0) # Stops at black hue
       
'''************************************************************************************************************************************'''

def bg_fade_dark_to_gold():
    if t.bg_count <= 765:
        turtle.bgcolor(fade_count_3, fade_count_2 % 510, 10) # Counter t.iterable starts at zero; background starts black, fades to gold
    else:
        turtle.bgcolor(255, 153, 10) # Stops at gold hue
 
# 1/16/2023:  Created, tested and deployed to Stupendous Mandala, inside master_mandala_maker.py.
def bg_fade_gold_to_dark(): # Background starts gold, fades to black
    global R, G, B, Z
    #Variable declarations for RGB Gold hue;  This extends the RGB count by a multiple of 3, so instead of 255, it is now incrementing up to 765 with no errors.
    R = 255 - int(t.bg_count)  # This RGB sequence creates a gold hue
    G = 153 - int(t.bg_count_2)
    B = 10 - int(t.bg_count_3)
    Z = 0
    turtle.bgcolor(R, G, B)
    # Iterations from gold hue to black
def iterate_gold_to_dark(): # Iteration count is 765 ( 255 multiplied by 3); 
    t.bg_count = t.iterable / 3 # Takes variable in R (255)
    t.bg_count_2 = t.bg_count * .6 # Takes variable G (153); Calcualeted 153/255 = .6
    t.bg_count_3 = t.bg_count * .0392156 # Takes variable B (10); Calulated 10/255 = .0328156
    if t.bg_count <= 255:
        turtle.bgcolor(R, G, B) 
    else:
        turtle.bgcolor(Z, Z, Z)  # Stops at black hue, RGB all reach 0 value at final iteration 
       
'''************************************************************************************************************************************'''
'''************************************************************************************************************************************'''
#Work on 
# def cycle_skyblue_to_dark():
#     new_count = t.iterable - t.bg_count
#     if t.iterable in range(0, 255):
#          turtle.bgcolor(0, 255 - t.bg_count, 255 - t.bg_count) # Counter t.iterable starts at zero; background starts sky blue, fades to black
#     elif t.iterable in range(201,400):
#          turtle.bgcolor(0, 0,  t.bg_count % 255) # Counter t.iterable starts at zero; background starts black, fades to sky blue
#     else:
#          turtle.bgcolor(0, 0, 0) # Counter t.iterable starts at zero and stays at dark setting   
    
# def bg_fade_dark_to_green_to_dark():
#     if t.bg_count <=765:
#         turtle.bgcolor(0, 255 - fade_count_3, 0) # Counter t.iterable starts at zero; background starts black, fades to green
#         
#         turtle.bgcolor(0, t.bg_count, 0) # Stops at green hue
#     else:
#        


#Color Hue Mixer

#random red hues
def pick_red(): #Pen t.lu
    r = random.randint(190, 255)
    g = random.randint(0, 25)
    b = random.randint(50, 85)
    R = r
    G = g
    B = b
    t.lu.pencolor(R, G, B)
    return t.lu
#     print('The pick_red pen is t.lu')


#random blue hues
def pick_blue():  # Pen t.lb
    r = random.randint(50, 75)
    g = random.randint(50, 85)
    b = random.randint(235, 255)
    L = r
    M = g
    N = b
    t.lb.pencolor(L, M, N)
    return t.lb
#     print('The pick_blue pen is t.lb')



#random green hues
def pick_green(): # Pen t.lg
    r = random.randint(0, 30)
    g = random.randint(215, 255)
    b = random.randint(0, 20)
    O = r
    P = g
    Q = b
    t.lg.pencolor(O, P, Q)
    return t.lg
#     print('The pick_green pen is t.lg')



#random indigo hues
def pick_indigo(): # pen t.li
    r = random.randint(25, 75)
    g = random.randint(0, 5)
    b = random.randint(75, 150)
    S = r
    T = g
    U = b
    t.li.pencolor(S, T, U)
    return t.li
#     print('The pick_indigo pen is t.li')

#random magenta hues
def pick_magenta(): # Pen t.me
    r = random.randint(125, 175)
    g = random.randint(0, 5)
    b = random.randint(75, 150)
    I = r
    J = g
    K = b
    t.me.pencolor(I, J, K)
    return t.me
#     print('The pick_magenta pen is t.me')

#random gold hues
def pick_gold(): # Pen t.la
    r = random.randrange(225, 254,1)
    g = random.randrange(175, 220,1)
    b = random.randrange(10, 50,1)
    V = r
    W = g
    X = b
    t.la.pencolor(V, W, X)
    return t.la
#     print('The pick_gold pen is t.la')

#random dark hues
def pick_dark(): # pen t.lz
    r = random.randint(0, 100)
    g = random.randint(0, 25)
    b = random.randint(0, 50)
    X = r
    Y = g
    Z = b
    t.lz.pencolor(X, Y, Z)
    return t.lz
#     print('The pick_dark pen is t.lz')



#random light hues
def pick_light(): # Pen t.le
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    A = r
    B = g
    C = b
    t.le.pencolor(A, B, C)
    return t.le
#     print('The pick_light pen is t.le')


#random hues
def pick_random(): #Pen t.ce
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    D = r
    E = g
    F = b
    t.ce.pencolor(D, E, F)
    return t.ce
#     print('The pick_random pen is t.ce')

def pick_random_a(): # Pen t.lr
    r = random.randint(200, 225)
    g = random.randint(200, 225)
    b = random.randint(200, 225)
    D = r
    E = g
    F = b
    t.lr.pencolor(D, E, F)
    return t.lr
#     print('The pick_random_a pen is t.lr')
    
    
    
def pick_dot(): # Pen t.ld
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    X = r
    Y = g
    Z = b
    t.ld.shape('dot')
    t.ld.pencolor(X, Y, Z)
    return t.ld
#     print('The pick_dot pen is t.ld')
    
hue_dict = {'pick_dot': 't.ld', 'pick_random_a': 't.lr', 'pick_random': 't.ce', 'pick_light': 't.le', 'pick_dark': 't.lz', 'pick_gold': 't.la', 'pick_magenta': 't.me', 'pick_indigo': 't.li', 'pick_green': 't.lg', 'pick_blue': 't.lb', 'pick_red': 't.lu'}
# print( str(hue_dict))