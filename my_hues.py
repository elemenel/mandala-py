"""my_hues.py contains color manipulation scripts  that are utilized by master_mandala_maker.py
by Leon Hatton
"""
import My_template as t
import random
import turtle

turtle.colormode(255)
"""************************************************************************************************************************************"""

# Color Hue Mixer


# random yellow hues
def pick_yellow():  # Pen t.ly
    r = random.randrange(220, 255, 1)
    g = random.randrange(225, 255, 1)
    b = random.randrange(0, 10, 1)
    I = r
    J = g
    K = b
    t.ly.pencolor(I, J, K)
    return t.ly


#     print('The pick yellow pen is t.ly')


# random orange hues
def pick_orange():  # Pen t.lq
    r = random.randrange(242, 255, 1)
    g = random.randrange(136, 158, 1)
    b = random.randrange(37, 47, 1)
    Q = r
    L = g
    N = b
    t.lq.pencolor(Q, L, N)
    return t.lq


#     print('The pick orange pen is t.lq')


# random red hues
def pick_red():  # Pen t.lu
    r = random.randrange(150, 255, 1)
    g = random.randrange(0, 80, 1)
    b = random.randrange(25, 50, 1)
    R = r
    G = g
    B = b
    t.lu.pencolor(R, G, B)
    return t.lu


#     print('The pick_red pen is t.lu')


# random blue hues
def pick_blue():  # Pen t.lb
    r = random.randrange(9, 54, 1)
    g = random.randrange(6, 72, 1)
    b = random.randrange(253, 255, 1)
    L = r
    M = g
    N = b
    t.lb.pencolor(L, M, N)
    return t.lb


#     print('The pick_blue pen is t.lb')


# random green hues
def pick_green():  # Pen t.lg
    r = random.randrange(0, 50, 1)
    g = random.randrange(185, 255, 1)
    b = random.randrange(10, 20, 1)
    O = r
    P = g
    Q = b
    t.lg.pencolor(O, P, Q)
    return t.lg


#     print('The pick_green pen is t.lg')


# random indigo hues
def pick_indigo():  # pen t.li
    r = random.randrange(25, 75, 1)
    g = random.randrange(0, 5, 1)
    b = random.randrange(75, 150, 1)
    S = r
    T = g
    U = b
    t.li.pencolor(S, T, U)
    return t.li


#     print('The pick_indigo pen is t.li')


# random magenta hues
def pick_magenta():  # Pen t.me
    r = random.randrange(125, 175, 1)
    g = random.randrange(0, 5, 1)
    b = random.randrange(75, 150, 1)
    I = r
    J = g
    K = b
    t.me.pencolor(I, J, K)
    return t.me


#     print('The pick_magenta pen is t.me')


# random gold hues
def pick_gold():  # Pen t.go
    r = random.randrange(225, 254, 1)
    g = random.randrange(175, 220, 1)
    b = random.randrange(10, 50, 1)
    V = r
    W = g
    X = b
    t.go.pencolor(V, W, X)
    return t.go


#     print('The pick_gold pen is t.go')


# random dark hues
def pick_dark():  # pen t.lz
    r = random.randrange(0, 100, 1)
    g = random.randrange(0, 25, 1)
    b = random.randrange(0, 50, 1)
    X = r
    Y = g
    Z = b
    t.lz.pencolor(X, Y, Z)
    return t.lz


#     print('The pick_dark pen is t.lz')


# random light hues
def pick_light():  # Pen t.el
    r = random.randrange(190, 215, 1)
    g = random.randrange(191, 254, 1)
    b = random.randrange(200, 253, 1)
    Q = r
    M = g
    U = b
    t.el.pencolor(Q, M, U)
    return t.el


#     print('The pick_light pen is t.le')


# random hues
def pick_random():  # Pen t.ce
    r = random.randrange(50, 255, 1)
    g = random.randrange(50, 255, 1)
    b = random.randrange(50, 255, 1)
    D = r
    E = g
    F = b
    t.ce.pencolor(D, E, F)
    return t.ce


#     print('The pick_random pen is t.ce')


def pick_random_a():  # Pen t.lr
    r = random.randrange(180, 225, 1)
    g = random.randrange(180, 225, 1)
    b = random.randrange(200, 225, 1)
    D = r
    E = g
    F = b
    t.lr.pencolor(D, E, F)
    return t.lr


#     print('The pick_random_a pen is t.lr')


# def pick_dot(): # Pen t.ld
#     r = random.randrange(200, 255,1)
#     g = random.randrange(200, 255,1)
#     b = random.randrange(200, 255,1)
#     X = r
#     Y = g
#     Z = b
#     t.ld.shape('circle')
#     t.ld.pencolor(X, Y, Z)
#     return t.ld
# #     print('The pick_dot pen is t.ld')

# global my_pen_a
# my_pen_a = t.v_pen
# global my_pen_b
# my_pen_b = t.v_pen_a


def pick_all_pens():
    t.my_venv()
    pick_red()
    pick_blue()
    pick_magenta()
    pick_gold()
    pick_green()
    pick_indigo()
    pick_random()
    pick_random_a()
    pick_dark()
    pick_light()
    pick_yellow()
    pick_orange()


def pick_two_pens():
    pick_all_pens()
    global my_pen_a
    global my_pen_b
    global my_a_pens
    global my_b_pens
    my_a_pens = [t.lb, t.li, t.la, t.le, t.lu, t.lr]
    my_b_pens = [t.lg, t.me, t.ld, t.ce, t.ly, t.lb, t.li, t.go, t.le, t.lu, t.lr]
    my_pen_a = random.choice(my_a_pens)
    my_pen_b = random.choice(my_b_pens)
    print(str(my_pen_a))
    print(str(my_pen_b))
    return my_pen_a
    return my_pen_b


# pick_two_pens()


def modulo_hues():
    R = 160
    G = 0
    B = 255
    if R <= 100:
        t.la.color(0, t.count % 140, B - t.count % 199)
        t.li.color(0, t.count % 199, B - t.count % 199)
    else:
        t.la.color(R - t.count % 160, t.count % 199, B - t.count % 199)
        t.li.color(R + t.count % 80, t.count % 199, B - t.count % 250)


#  Gradually change screen background hues between  two hues

#
# '''************************************************************************************************************************************'''
# def bg_fade_dark_to_yellow():
#     global R, G, B, Z
#     #Variable declarations for RGB Gold hue;  This extends the RGB count by a multiple of 3, so instead of 255, it is now incrementing up to 765 with no errors.
#     R = 0 - int(t.bg_count)  # This RGB sequence creates a gold hue
#     G = 0 - int(t.bg_count_2)
#     B = 0 - int(t.bg_count_3)
#     Z = 0
#     turtle.bgcolor(R, G, B)
#     # Iterations from gold hue to black
# def iterate_dark_to_yellow():
#     # Iteration count is 765 ( 255 multiplied by 3);
#     t.bg_count = t.iterable / 3 # Takes variable in R (255)
#     t.bg_count_2 = t.bg_count # Takes variable G (153); Calculated 153/255 = .6
#     t.bg_count_3 = Z # Takes variable B (10); Calculated 10/255 = .0328156
#     if t.bg_count <= 255:
#         turtle.bgcolor(R, G, B)
#     else:
#         turtle.bgcolor(255, 255, Z)  # Stops at black hue, RGB all reach 0 value at final iteration
#
#
#
#
# def bg_fade_yellow_to_dark():
#     global R, G, B, Z
#     #Variable declarations for RGB Gold hue;  This extends the RGB count by a multiple of 3, so instead of 255, it is now incrementing up to 765 with no errors.
#     R = 255 - int(t.bg_count)  # This RGB sequence creates a gold hue
#     G = 255 - int(t.bg_count_2)
#     B = 10 - int(t.bg_count_3)
#     Z = 0
#     turtle.bgcolor(R, G, B)
#     # Iterations from gold hue to black
# def iterate_yellow_to_dark(): # Iteration count is 765 ( 255 multiplied by 3);
#     t.bg_count = R - t.iterable / 3 # Takes variable in R (255)
#     t.bg_count_2 = t.bg_count # Takes variable G (153); Calculated 153/255 = .6
#     t.bg_count_3 = 0 # Takes variable B (10); Calculated 10/255 = .0328156
#     if t.bg_count <= 255:
#         turtle.bgcolor(R, G, B)
#     else:
#         turtle.bgcolor(Z, Z, Z)  # Stops at black hue, RGB all reach 0 value at final iteration
#
"""************************************************************************************************************************************"""


# def bg_fade_dark_to_skyblue():
#     global R, G, B, Z
#     R =  0
#     G = int(t.bg_count_2)
#     B = int(t.bg_count_3)
#
#     if t.bg_count <= 255:
#         turtle.bgcolor(R, G, B)
#     else:
#        turtle.bgcolor(0, 255, 255) # Stops at sky blue hue
#
#
# def bg_fade_skyblue_to_dark():
#     if t.bg_count <= 765:
#          turtle.bgcolor(0, 255 - t.bg_count, 255 - t.bg_count) # Counter t.iterable starts at zero; background starts sky blue, fades to black
#     else:
#         turtle.bgcolor(0, 0, 0) # Stops at black hue
#
# '''************************************************************************************************************************************'''
#
# def bg_fade_dark_to_green():
#     if t.bg_count <= 765:
#         turtle.bgcolor(0,t.bg_count, 0) # Counter t.iterable starts at zero; background starts black, fades to green
#     else:
#         turtle.bgcolor(0, 255, 0) # Stops at green hue
#
#
# def bg_fade_green_to_dark():
#     if t.bg_count <= 765:
#         turtle.bgcolor(0, 255 - t.bg_count, 0) # Counter t.iterable starts at zero; background starts green, fades to black
#     else:
#         turtle.bgcolor(0, 0, 0) # Stops at black hue
#
# '''************************************************************************************************************************************'''
#
# def bg_fade_dark_to_gold():
#     if t.bg_count <= 765:
#         turtle.bgcolor(t.bg_count, t.bg_count % 510, 10) # Counter t.iterable starts at zero; background starts black, fades to gold
#     else:
#         turtle.bgcolor(255, 153, 10) # Stops at gold hue
#
# # # 1/16/2023:  Created, tested and deployed to Stupendous Mandala, inside master_mandala_maker.py.
# def bg_fade_gold_to_dark(): # Background starts gold, fades to black
#     global R, G, B, Z
#     #Variable declarations for RGB Gold hue;  This extends the RGB count by a multiple of 3, so instead of 255, it is now incrementing up to 765 with no errors.
#     R = 255 - int(t.bg_count)  # This RGB sequence creates a gold hue
#     G = 153 - int(t.bg_count_2)
#     B = 10 - int(t.bg_count_3)
#     Z = 0
#     turtle.bgcolor(R, G, B)
#     # Iterations from gold hue to black
# def iterate_gold_to_dark(): # Iteration count is 765 ( 255 multiplied by 3);
#     t.bg_count = t.iterable / 3 # Takes variable in R (255)
#     t.bg_count_2 = t.bg_count * .6 # Takes variable G (153); Calcualeted 153/255 = .6
#     t.bg_count_3 = t.bg_count * .0392156 # Takes variable B (10); Calulated 10/255 = .0328156
#     if t.bg_count <= 255:
#         turtle.bgcolor(R, G, B)
#     else:
#         turtle.bgcolor(Z, Z, Z)  # Stops at black hue, RGB all reach 0 value at final iteration
#
"""************************************************************************************************************************************"""
"""************************************************************************************************************************************"""
# Work on
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
#         turtle.bgcolor(0, 255 - t.bg_count, 0) # Counter t.iterable starts at zero; background starts black, fades to green
#
#         turtle.bgcolor(0, t.bg_count, 0) # Stops at green hue
#     else:
#


hue_dict = {
    "pick_dot": "t.ld",
    "pick_random_a": "t.lr",
    "pick_random": "t.ce",
    "pick_light": "t.le",
    "pick_dark": "t.lz",
    "pick_gold": "t.la",
    "pick_magenta": "t.me",
    "pick_indigo": "t.li",
    "pick_green": "t.lg",
    "pick_blue": "t.lb",
    "pick_red": "t.lu",
}
# print( str(hue_dict))
