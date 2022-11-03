# my_hues.py contains color manipulation scripts associated with master_mandala_maker.py
                 # by LeonRHatton

import My_template as t
import random
import turtle
turtle.colormode(255)


#random red hues
def pick_red():
    r = random.randint(190, 255)
    g = random.randint(0, 25)
    b = random.randint(50, 85)
    R = r
    G = g
    B = b
    t.lu.pencolor(R, G, B)
#     print('The pick_red pen is t.lu')


#random blue hues
def pick_blue():
    r = random.randint(50, 75)
    g = random.randint(50, 85)
    b = random.randint(235, 255)
    L = r
    M = g
    N = b
    t.lb.pencolor(L, M, N)
#     print('The pick_blue pen is t.lb')



#random green hues
def pick_green():
    r = random.randint(0, 30)
    g = random.randint(215, 255)
    b = random.randint(0, 20)
    O = r
    P = g
    Q = b
    t.lg.pencolor(O, P, Q)
#     print('The pick_green pen is t.lg')



#random indigo hues
def pick_indigo():
    r = random.randint(25, 75)
    g = random.randint(0, 5)
    b = random.randint(75, 150)
    S = r
    T = g
    U = b
    t.li.pencolor(S, T, U)
#     print('The pick_indigo pen is t.li')

#random magenta hues
def pick_magenta():
    r = random.randint(125, 175)
    g = random.randint(0, 5)
    b = random.randint(75, 150)
    I = r
    J = g
    K = b
    t.me.pencolor(I, J, K)
#     print('The pick_magenta pen is t.me')

#random gold hues
def pick_gold():
    r = random.randrange(225, 254,1)
    g = random.randrange(175, 220,1)
    b = random.randrange(10, 50,1)
    V = r
    W = g
    X = b
    return(t.la.pencolor(V, W, X))
#     )
#     print('The pick_gold pen is t.la')

#random dark hues
def pick_dark():
    r = random.randint(0, 100)
    g = random.randint(0, 25)
    b = random.randint(0, 50)
    X = r
    Y = g
    Z = b
    t.lz.pencolor(X, Y, Z)
#     print('The pick_dark pen is t.lz')



#random light hues
def pick_light():
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    A = r
    B = g
    C = b
    t.le.pencolor(A, B, C)
#     print('The pick_light pen is t.le')


#random hues
def pick_random():
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    D = r
    E = g
    F = b
    t.me.pencolor(D, E, F)
#     print('The pick_random pen is t.me')

def pick_random_a():
    r = random.randint(200, 225)
    g = random.randint(200, 225)
    b = random.randint(200, 225)
    D = r
    E = g
    F = b
    t.lr.pencolor(D, E, F)
#     print('The pick_random_a pen is t.lr')
    
    
    
def pick_dot():
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    X = r
    Y = g
    Z = b
    t.ld.pencolor(X, Y, Z)
#     print('The pick_dot pen is t.ld')
    
dict = {'pick_dot': 't.ld', 'pick_random_a': 't.lr', 'pick_random': 't.me', 'pick_light': 't.le', 'pick_dark': 't.lz', 'pick_gold': 't.la', 'pick_magenta': 't.me', 'pick_indigo': 't.li', 'pick_green': 't.lg', 'pick_blue': 't.lb', 'pick_red': 't.lu'}
# print ("dict ['pick_gold'] :   ", dict ['pick_gold']  )
