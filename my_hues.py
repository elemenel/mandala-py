# my_hues.py contains color manipulation scripts associated with master_mandala_maker.py
                 # by LeonRHatton

import My_template as t
import random

#random red hues
def pick_red():
    r = random.randint(190, 255)
    g = random.randint(0, 25)
    b = random.randint(50, 85)
    R = r
    G = g
    B = b
    t.lu.pencolor(R, G, B)


#random blue hues
def pick_blue():
    r = random.randint(50, 75)
    g = random.randint(50, 85)
    b = random.randint(235, 255)
    L = r
    M = g
    N = b
    t.lb.pencolor(L, M, N)



#random green hues
def pick_green():
    r = random.randint(0, 30)
    g = random.randint(215, 255)
    b = random.randint(0, 20)
    O = r
    P = g
    Q = b
    t.lg.pencolor(O, P, Q)



#random indigo hues
def pick_indigo():
    r = random.randint(25, 75)
    g = random.randint(0, 5)
    b = random.randint(75, 150)
    S = r
    T = g
    U = b
    t.li.pencolor(S, T, U)

#random magenta hues
def pick_magenta():
    r = random.randint(125, 175)
    g = random.randint(0, 5)
    b = random.randint(75, 150)
    I = r
    J = g
    K = b
    t.me.pencolor(I, J, K)

#random gold hues
def pick_gold():
    r = random.randint(225, 255)
    g = random.randint(175, 220)
    b = random.randint(10, 50)
    V = r
    W = g
    X = b
    t.la.pencolor(V, W, X)



#random dark hues
def pick_dark():
    r = random.randint(0, 100)
    g = random.randint(0, 25)
    b = random.randint(0, 50)
    X = r
    Y = g
    Z = b
    t.lz.pencolor(X, Y, Z)



#random light hues
def pick_light():
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    A = r
    B = g
    C = b
    t.le.pencolor(A, B, C)


#random hues
def pick_random():
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    D = r
    E = g
    F = b
    t.me.pencolor(D, E, F)

def pick_random_a():
    r = random.randint(200, 225)
    g = random.randint(200, 225)
    b = random.randint(200, 225)
    D = r
    E = g
    F = b
    t.lr.pencolor(D, E, F)
    
    
    
def pick_dot():
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    X = r
    Y = g
    Z = b
    t.ld.pencolor(X, Y, Z)    