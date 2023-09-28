"""my_angles.py contains functions, generators, and formatters needed to output
a chosen set of angles to master_mandala_maker.py
by Leon Hatton
"""
import turtle
import random
import numpy as np
import math
import sys
import os
import platform
import time
global r_angle
import Timer as Tm
import sys
import My_logger as Lg
import My_template as t



global i_angle_auto
i_angle_auto = [ ]

# if sys.platform.startswith('linux'):
#     my_path = '/media/elemen/'
#     my_log_path = '/home/elemen/Git/Logs'
# else:
#     my_path = 'M:'
#     my_log_path = 'B:/Logs'

Tm.time_functions()

turtle.setup(10,10)

# r_angle = random.randrange(72, 1500, 9)

# filter_360 = [i for i in np.arange(float(357.01), float(363.99), .01) if i % float(180) != 0]
# Lg.logger.info(str(filter_360))
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# past auto angles: # 72,1500, 72 on 1/8/2022. Produces 5 points or sides.
                    # 257.142857, 1500, 51.42857 on 1/8/2022. Produces 7 points or sides.
                    # 150, 1500, 60 on 1/9/2022. Produces assortment of 12, 4 points or sides.
                    # 63, 2000, 63 on 1/9/2022. Produces designs having angles whose digits sum to 9. Like it.
                    # 54, 2000, 54 on 1/10/2022. Also has digits summing up to 9.
                    # 73, 1000, 73 on 1/11/2022. Arbitrary. Mostly 11 sides or points. Nice ones.
                    # 68, 1500, 68.
                    # 44, 1500, 44 on 1/12/2022.
                    # 216, 400, 144 on 1/12/2022. For testing
                    # 88,1000, 104 on 1/17/2022. Successfully automated video creation using Python code!
                    # 150, 1000, 75 on 1/18/2022. Makes 11.
                    # 135, 1200, 75 on 1/18/2022. Makes 14.
                    # 144, 500, 60 on1/19/2022. Makes 6.
                    # 257.142857, 2000, 257.142857 on 1/19/2022. Seven points or sides. Makes 7.
                    # 145, 1300, 71. On 1/19/2022. Makes 17. Ran on Fantastic, Awesome, and stupendous.
                    # 144, 1300, 52. On 1/20/2022. Makes 22. Ran on Ribbons on 1/20/2022.
                    # 144, 1300, 82  On 1/20/2022. Makes 15. Ran on Fantastic and stupendous.
                    # 144, 300, 60 on 1/21/2022. Makes 3. Ran on stupendous.
                    # 144, 3000, 600 on 1/21/2022. Makes 5. Ran on stupendous and jagged.
                    # 144, 3000, 540 on 1/21/2022. Makes 6. Ran on hued polygonial.
                    # 441, 3000, 441 on 1/21/2022. Makes 6. Ran on bold mandala.
                    # 60, 500, 15 on 1/22/2022. Makes 12. Ran on colorful, bold mandala, hued polygonial, stupendous, jagged, and Fantastic.
                    # 75, 500, 45 on 1/23/2022. Makes 10.  Ran on colorful, bold mandala, hued polygonial, stupendous, jagged, and Fantastic.
                    # 81, 720, 36. on 1/23/2022. Makes 18. Ran it on the bunch.
                    # 60, 1300, 60. oN 1/26/2022. makes 18, ran it on Multi-Hued.
                    # 60, 1300, 61. on 1/27/2022, makes 21. Ran it on Mult-Hued and stupendous.
                    # 60,2000, 180. On 1/27/2022. makes 11. On stupendous, pretty, double and bold.
                    # 585, 8000, 585 on 1/28/2022. Makes 10. on Hued Freedom, home_star.
                    # 432, 1000, 60. Makes 10. On 11., 1/30/2022
                    # 90, 1500, 75. Makes 17. Ran on 1/30/2022 on 12.
                    #90, 400, 45. Appended 257.142857. Ran on 1/31/2022, on all except spiral.
                    # 135, 500, 90. Appended 257.142857(7 points), 144(5 points, 1211(11 points)  Makes 8 total. on 2/1/2022.
                    # 120, 500, 72. Makes 6. Appends added totals 9. Ran on the 4 hued's. 2/1/2022.
                    #240, 700, 72. makes 10. Ran on just about all. 2/2/2022
                    #1425, 3350, 135. Makes 15. Ran on stupendous on 2/9/2022. Perfected randomnizing the audio selections.
                    # 126, 2000, 126. Makes 14. Ran on awesome, multi-hued, colorful, iridescent, home-star, pretty, hued poly, hued gradiant.
                    # 90, 2000, 150. Makes 11. Ran on home_star and color_shifting. added more music and created new file dedicated to audio.
                    # 51.42, 1800, 205.71428. Makes 9. # Ran on multiple modules; make spectacular 7-pointed polygrams and/or 7-sided polygons
                    # 1439.984, 3600, 51.428.  Seven points themes. Some are beauties, some are too close to 180 and 360 multiples. Added 510, 135. Makes 46. Ran on Glorious Mandala, on 4/6/2022
                    # 60, 501, 10 Ran on 4/7/2022
                    # 420, 421, 1.  4/8/2022. Ran on all available modules(25). 420 is the least common multiple of 2, 3, 4, 5, 7. \
                                                        #  Ran to compare the variations against a single number.
                    # 840, 7600, 420. Ran on all available. Wanted to see how the 420 modes develop.
                    #225.5, 2000, 676.5 Ran on Reversing Simple Mandala, on 07/20/2023; uploaded to YouTube.
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::                    
# Solfeggio Angles
solfeggio_3 = [174, 417, 741] #Digits sum to 3
solfeggio_6 = [285, 528, 852] # Digits sum to 6
solfeggio_9 = [396, 639, 963] # Digits sum to 9

# i_angle_auto = [528, 432, 174, 417, 741, 285, 852, 396, 639, 963]
#Earth Frequencies
#136.10 and up: angle_min = 136.1
# angle_max = 9000
#key = 136.10

def select_angle():
    # Create an input box
    my_angle = turtle.numinput("Enter Angle:  " )

   # Wait 4 seconds for keypress
    time.sleep(4)

      # If no response, select default
    if my_angle == null:
        my_angle = random.randint(150,135,432,1350,1211)
        return my_angle    
    Lg.logger.info('The selected angle is:  ' + str(my_angle))

 


# Automated Angle Generator using numpy.arange module; produces a list of angles based on custom algorithms.
# 
def pick_angles():
    global i_angle_auto, i_angle_float
    angle_min = float(135)
    angle_max = float(angle_min *5)
    key = float(angle_min  / 2)   #Dividing angle_min by 2 and using that as a key results in a harmonic angle family; also multiply by 3 or 5 
    
#     angle_min_a = float(80)
#     float(angle_min_a * 12)
#     key = float(angle_min_a) #Dividing angle_min by 2 and using that as a key results in a harmonic angle family; also multiply by 3 or 5 
    
#     angle_min_b = float(72)
#     float(angle_min_b * 12)
#     key = float(angle_min_b) #Dividing angle_min by 2 and using that as a key results in a harmonic angle family; also multiply by 3 or 5 
     
    i_angle_float = [angle for angle in np.arange(float(angle_min), float(angle_max), int(key)) if angle  %(180) != 0] #+ \
#                     [angle for angle in np.arange(float(angle_min), float(angle_max), float(key)) if angle  %(181) != 0] + \
#                     [angle for angle in np.arange(float(angle_min), float(angle_max), float(key)) if angle  %(182) != 0] +\
#                     [angle for angle in np.arange(float(angle_min), float(angle_max), float(key)) if angle  %(183) != 0] + \
#                     [angle for angle in np.arange(float(angle_min), float(angle_max), float(key)) if angle  %(179) != 0] +\
#                     [angle for angle in np.arange(float(angle_min), float(angle_max), float(key)) if angle  %(178) != 0] + \
#                     [angle for angle in np.arange(float(angle_min), float(angle_max), float(key)) if angle  %(177) != 0]
    
    
    i_angle_auto = [angle for angle in np.arange(math.trunc(float(angle_min)), math.trunc(float(angle_max)), math.trunc(float(key))) if angle %(180) != 0] #+ [3024] + [3888] +[4752]+ [7344] +[8208]
#                    #[i for i in np.arange(float(angle_min_b), float(angle_max_b), key_b) if i % float(180) != 0]  #+ [ 221.5385]
    return i_angle_auto , i_angle_float     
pick_angles()
'''Use this pick_angles to specify the angles manually'. Comment the section out if the automated pick_angles script is prefferred'''
# def pick_angles():
#      global i_angle_auto
#      i_angle_auto = [144, 288, 412, 864, 1008, 1152, 1296]
# pick_angles()


# i_angle_auto =[120, 90, 72, 60, 51.42857142857143, 45, 40, 36, 32.72727272727273, 30, 27.692307692307693,\
#                25.714285714285715, 24, 22.5, 21.176470588235293, 20, 18.94736842105263, 18, 17.142857142857142,\
#                16.3636363636363631, 15.652173913043478, 15 ]
# Set up do develop a catalog which would include a sample. Decided to try angle 135 first, for 8 points mostly.
# i_angle_auto = [7350,7140]  #, 315, 280, 252, 229.090909, 210, 193.846154, 168, 157.5, 148.235294]
# i_angle_auto = [640, 800, 1280, 1600, 1760]
 
#----------------------------------------------------------------------------------------------------------------------------------
# Run sequences of angles using List Compehension
# start_seq = 361
# stop_seq = 1212
# i_angle_seq = [ n  for  n in range(start_seq, stop_seq)]

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# i_angle_cus = [288, 324, 396, 432, 468, 504, 576, 612, 648, 2430, 368, 215, 225] #angles are changeable Ran on 05/2/2022



# # https://howchoo.com/python/generate-a-list-of-primes-numbers-in-python
# # Non-prime numbers formula using list comprehension
# noprimes = set(j for i in range(2, 8) for j in range(i*2, 10000, i))
# # #Prime numbers formula
# start_prime = 371
# end_prime = 470
# i_angle_primes = [x for x in range(start_prime, end_prime) if x not in noprimes]
# # Lg.logger.info('These are prime numbers from ' + str(start_prime) + '  to ' + str(end_prime) +':' + str(i_angle_primes))
# Lg.logger.info('The number of primes list elements is: ' + str(len(i_angle_primes)))




#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




# global my_angle
# my_angle = turtle.numinput('Angle', 'Enter Angle Number:', float(r_angle))

# this_angle = turtle.numinput('Enter Angle Number', 'Angle #', 396) # or any specific angle

# x = turtle.numinput('Enter Angle Number', 'Angle Number', 432)
# i_angle = [x-3.5, x-2.5, x-1.5,x-.5, x, x+1, x+2, x+2.5]

# i_angle_double = [90, 120, 144, 205.7142857, 150, 135]
# 
# i_angle_6 = [60,120,240,300,420,480,540,600,780,840,900,960,1020,1140] # 6 points or sides
# 
# i_angle_5 = [i for i in np.arange(float(72), float(1000), 72) if i % float(180) != 0] # 5 points or sides
# # # 
# i_angle_7 = [i for i in np.arange(float(51.42857), float(900), 51.42857) if i % float(180) != 0] #7 points or sides
# 
# for lambda x: for i for i in range(float(356.01, 363.99, .01)):
#     i_angle_5.remove(x)

# for x in range(i_angle_7.count(float(360))):
#     i_angle_7.remove((float(360)))


# i_angle_9 = [40, 80, 120, 160, 200, 240, 280, 320, 400, 440, 480, 520, 560, 600, 640, 680, 760] # 9 points or sides
# 
# i_angle_17 = [105.882, 127.059,148.2353, 169.4118, 190.59, 211.7647,\
#            232.9412, 254.1176, 275.2941, 296.4706,317.6417, 338.8253, 381.1765, 402.3529] # 17 points or sides
# 
# i_angle_13 = [110.7692,138.462, 166.154, 193.8462, 221.5385, 249.23,\
#            276.9231, 304.6154, 332.3077, 387.6923, 415.3846,\
#            443.0769, 470.7692, 498.4615, 526.1538]   # 13 points or sides
# 
# i_angle_12 = [30, 60,90,120,150,210,240,270,300,330,390,420,450,480,510,540,570]
# i_angle_s = [120,480, 90, 144, 576, 240, 154.29, 140, 2394,\
#              1211, 138, 471, 498, 510, 405, 105.882, 320, 170.53]
# i_angle_m = [1368,1140,977.1429,855,760,684,621.8182,570,526.1538,488.5714,456,427.5,402.3529,380]
# i_angle_auto = i_angle_mix = [138.462,148.2353,792,520,532, 154.29, 120, 90, 150, 257.143, 135,  1211 ]

# i_angle_auto = i_angle_7 + i_angle_5

# i_angle_basic = [585, 1170, 1755] # Mainly for testing
# 
 
# freedom_angle = [360/1.75]
# 
# # length = len(i_angle)
# 
#i_angle_auto = i_angle_f = [60, 75, 90, 105, 120, 135, 144, 150, 165, 11219, 1211, 205.1428, 432, 1350, 7050, 7048, 7046] # 2394, 834, 432, 210,1350, 1028.5714, 420, 240, 576] #1065, #Favorite angles: 144/5P, 210/12P, 834/TightSpiral,2394/20P,1350/Square
# 
# i_angle_d_9 = [ 108, 117, 126, 135, 144, 153, 162, 171, 180, 207, 216, 225, 234, 243, 252, 261,\
#               270, 306, 315, 324, 333, 342, 351, 405, 414, 423, 432, 441, 450, 504, 513,\
#               522, 531, 540, 603, 612, 621, 630, 702, 711, 720, 801, 810, 900 ]  # The sum of digits is 9
# 
# i_angle_d_10 = [109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 208,\
#                217, 226, 235, 244, 253, 262, 271, 280, 307, 316,\
#                325, 334, 343, 352, 361, 370, 406, 415, 424,\
#                433, 442, 451, 460, 505, 514, 523, 532, 541, 550,\
#                604, 613, 622, 631, 640, 703, 712, 721, 730, 802, 811, 820, 901, 910] # The sum of digits is 10
# 
# i_angle_d_5 = [104, 113, 122, 131, 140, 203, 212, 221, 230, 302, 311, 320, 401, 410, 500]
# 
# 
# i_angle_auto = i_angle_d_7  = [411.36] #, 462.78000000000003, 514.2, 565.62, 617.04, 668.4599999999999,\
                #719.88, 771.3, 822.72, 874.14, 925.56, 976.98, 1028.4,\
                #1131.24, 1182.66, 1234.0800000000002, 1285.5, 1336.92,51.42, 102.84, 154.26, 205.68, 257.1, 308.52000000000004 ]
# 
# 
# fib_angles = [144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393]
# 
# i_angle_single = [90] # Run on a single angle, or as many as you wish
# 
# i_angle_awesome = [792,765, 977, 315, 432, 947, 1140, 1065, 990, 690, 257.143]
# 
# i_angle_iridescent = [257, 315, 270, 432, 612, 225, 972, 912, 257.143]


# ''' From Geeks for Geeks
# # Python3 code to iterate over a list
# list = [1, 3, 5, 7, 9]
#   
# # Using for loop
# for i in list:
#     Lg.logger.info(i)
#     
# # getting length of list
# length = len(list)
#   
# # Iterating the index
# # same as 'for i in range(len(list))'
# for i in range(length):
#     Lg.logger.info(list[i])    
# 
# # Iterating using while loop
# #i = 0
# while i < length:
#     Lg.logger.info(list[i])
#     i += 1
    
 
# Using list comprehension
# [Lg.logger.info(i) for i in list]


# Lg.logger.info(list(i_angle))
#================================================================================
# function to analyze numerical sequences such as 120 = 1+2+0 = 3
# Using List comphension

# num_a = 2680
# num_b = 1211
# num_c = 1354
# x = sum([int(a) for a in str(num_a)])
# y = sum([int(a) for a in str(num_b)])
# z = sum([int(a) for a in str(num_c)])
# 
# Lg.logger.info('For   ' + str(num_a) + ',   ' +  'the sum of digits is ' + str(x))
# Lg.logger.info('For   ' + str(num_b) + ',   ' +  'the sum of digits is ' + str(y))
# Lg.logger.info('For   ' + str(num_c) + ',   ' +  'the sum of digits is ' + str(z))
#==================================================================================
# Find sum of odd digits in a number, and can be used to find even, too by tweaking code in set [2468]
# num = "123"
# odds = re.findall(r'[13579]', num)
# sum = sum(int(odd) for odd in odds)
# Lg.logger.info("the sum is: " + str(sum))


# Function to analyze numerical squences from auto angle list output
# def find_sums():
#     pass
#  
# find_sums()   

#****************************************************************************************************************
# Algorithm to determine groups of like angles
# a = 1
# b = 2
# for i in range(10):
#     Lg.logger.info(a*i +b)
# i_angle_auto = i_angle_5


# def filter_360():
#     if filter_360 in i_angle_auto:
#         i_angle_auto.remove(filter_360)
#         
#     elif float(360) in valuesRounded:
#         i_angle_auto.remove( x for x ifloat(360,/))
#     else:
#         pass
# filter_360()

# i_angle_auto = [1296]
# # '___________________________________________________________________________________________________________________________________________'
integer_values = [int for int in i_angle_auto]
valuesRounded = [round(float) for float in i_angle_auto]
float_values = [float for float in i_angle_float]                      
Lg.logger.info('*******************************************************************************************************')
Lg.logger.info(f'Running Scripts from Master MandalaMaker @ {Tm.my_time}')
Lg.logger.info('...................................................................................................')
Lg.logger.info(f'The Automated Set of Angles to be Drawn as integers are: {integer_values} ')
Lg.logger.info(f'The Automated Set of Angles to be Drawn as float numbers are: {float_values} ')
Lg.logger.info(f'The Automated Set of Angles to be Drawn  rounded are: {valuesRounded}')
Lg.logger.info('....................................................................................................')
Lg.logger.info('The number of Automated Angle Generator elements for rounded elements is:' + str(len(valuesRounded)))
Lg.logger.info('The number of Automated Angle Generator elements for float values is:' + str(len(float_values)))            
# '___________________________________________________________________________________________________________________________________________________'
# # # # Python3 code to demonstrate
# # # # Sum of number digits in List
# # # # using sum() + list comprehension
# # x = list(map(lambda ele: sum(int(sub) for sub in str(ele)), valuesRounded))
# # Lg.logger.info(x)
# Lg.logger.info('...................................................................................................')      
# Lg.logger.info('Sum of digits in the elements of the list are:   ' )
# Lg.logger.info(list(map(lambda ele: sum(int(sub)for sub in str(ele)), float_values)))
# # Lg.logger.info(list(map(lambda ele: sum(int(sub) for sub in str(ele)), x)))
# Lg.logger.info('*******************************************************************************************************')
Lg.logger.info('Logger Source: my_angles.py')
Lg.logger.info('*******************************************************************************************************')
# # Lg.logger.info('Stopping shell output to file...')
# # sys.stdout.close()
# # sys.stdout = stdoutOrigin
# # Lg.logger.info('Shell output default restored')

# #Output to shell
# Lg.logger.info('Running Scripts from Master MandalaMaker @' +str(Tm.my_time) + '')
# Lg.logger.info('...................................................................................................')
# Lg.logger.info('The Automated Set of Angles to be Drawn Are:')
# Lg.logger.info(valuesRounded)
# Lg.logger.info('....................................................................................................')
# Lg.logger.info('The number of Automated Angle Generator elements is: ' + str(len(valuesRounded)))

# Python3 code to demonstrate
# Sum of number digits in List
# using sum() + list comprehension
# '_________________________________________________________________________________________________________________'
# x = list(map(lambda ele: sum(int(sub) for sub in str(ele)), valuesRounded))
# # Lg.logger.info(x)
# # Lg.logger.info('...................................................................................................')      
# Lg.logger.info('Sum of digits in the elements of the list are:   ' )
# # Lg.logger.info(list(map(lambda ele: sum(int(sub) for sub in str(ele)), valuesRounded)))
# Lg.logger.info(list(map(lambda ele: sum(int(sub) for sub in str(ele)), x)))

def report_angle_status():
    Lg.logger.info('The current list of angles  being processed is:')
    Lg.logger.info(valuesRounded)
    Lg.logger.info('Current angle selection is ' +  str(t.my_angle))
# report_angle_status()

# time.sleep(6)




#****************************************************************************************************************
def log_factorial():
    my_title = '/Factorial_output.txt'
#     stdoutOrigin=sys.stdout
#     sys.stdout = open(my_path + my_title + '_log.txt', 'w')
    count = 1
    x = 360
    while count <= 361:
        Lg.logger.info('Factorial '+ str(count) + ':    ' + str(x / count))
        count += 1
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin
    
#  log_factorial()    
