#my_angles.py contains file manipulation scripts associated with master_mandala_maker.py
             # by LeonRHatton

import turtle
import random
import numpy as np
import math

global r_angle
r_angle = random.randrange(72, 1500, 9)

turtle.setup(10,10)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::                    
# Automated Angle Generator using numpy.arange module; produces a list of angles based on custom algorithms.
angle_min =   1350 #random.randrange(150, 750, 72)102.85714
angle_max =  2000 #random.randrange(500, 1500, 50)4500
key = 144  #102.85714
#Using List comprehension with numpy to create list of angles dynamically, and it offers good variation in angles and element count(from 4 to 10).
i_angle_auto = [i for i in np.arange(float(angle_min), float(angle_max), key) if i % float(180) != 0]# and if i % float(360) != 0]#+ [random.randrange(2160, 4280, 288)]
#                # + [random.randrange(144, 432, 56)] + [random.randrange(135, 270, 10)] \
#                 #+ [random.randrange(150, 500, 75)]  # Can append any angle(s) to list.  Can also run sequenced angles

# i_angle_auto =[120, 90, 72, 60, 144, 154.28571, 771.42855, 1008, 240, 135, 150, 405]

valuesRounded = [round(number) for number in i_angle_auto]
if 360 in i_angle_auto:
    i_angle_auto.remove(360)
else:
    pass
print('...................................................................................................')
print('The Automated Set of Angles to be Drawn Are:')
print(valuesRounded)
print('....................................................................................................')
print('The number of Automated Angle Generator elements is: ' + str(len(valuesRounded)))
      
  
# valuesRoundUp = [math.ceil(number) for number in i_angle_auto]
# valuesRoundDown = [math.floor(number) for number in i_angle_auto]

# print(valuesRoundUp)
# print(valuesRoundDown)


# Python3 code to demonstrate
# Sum of number digits in List
# using sum() + list comprehension
x = list(map(lambda ele: sum(int(sub) for sub in str(ele)), valuesRounded))
# print(x)
print('...................................................................................................')      
print('Sum of digits in the elements of the list are:   ' )
# print(list(map(lambda ele: sum(int(sub) for sub in str(ele)), valuesRounded)))
print(list(map(lambda ele: sum(int(sub) for sub in str(ele)), x)))    
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
# # print('These are prime numbers from ' + str(start_prime) + '  to ' + str(end_prime) +':' + str(i_angle_primes))
# print('The number of primes list elements is: ' + str(len(i_angle_primes)))




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
# i_angle_5 = [72,144,216,288,432,504,576,648,792,864,936,1008,1152,1224,1296,1368] # 5 points or sides
# 
# i_angle_7 = [51.42857,102.857,154.29,205.7143,257.143,308.571,\
#            411.4286,462.86,514.2857,565.7143,617.1429,\
#            668.5714,771.4286,822.8571,874.2857,925.7143,977.1429] #7 points or sides
# 
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
# 
# i_angle_basic = [585, 1170, 1755] # Mainly for testing
# 
# i_angle_o = [141, 91.5, 227, 1211] # odd angles
# 
# freedom_angle = [360/1.75]
# 
# # length = len(i_angle)
# 
# i_angle_f = [120, 90, 135, 150, 144, 210, 834,910, 410, 2394, 1350, 1211, 771.3, 1140, 526.1538 ]  #Favorite angles: 144/5P, 210/12P, 834/TightSpiral,2394/20P,1350/Square
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
# i_angle_d_7  = [411.36, 462.78000000000003, 514.2, 565.62, 617.04, 668.4599999999999,\
#                 719.88, 771.3, 822.72, 874.14, 925.56, 976.98, 1028.4,\
#                 1131.24, 1182.66, 1234.0800000000002, 1285.5, 1336.92,51.42, 102.84, 154.26, 205.68, 257.1, 308.52000000000004 ]
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
#     print(i)
#     
# # getting length of list
# length = len(list)
#   
# # Iterating the index
# # same as 'for i in range(len(list))'
# for i in range(length):
#     print(list[i])    
# 
# # Iterating using while loop
# #i = 0
# while i < length:
#     print(list[i])
#     i += 1
    
 
# Using list comprehension
# [print(i) for i in list]


# print(list(i_angle))
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
# print('For   ' + str(num_a) + ',   ' +  'the sum of digits is ' + str(x))
# print('For   ' + str(num_b) + ',   ' +  'the sum of digits is ' + str(y))
# print('For   ' + str(num_c) + ',   ' +  'the sum of digits is ' + str(z))
#==================================================================================
# Find sum of odd digits in a number, and can be used to find even, too by tweaking code in set [2468]
# num = "123"
# odds = re.findall(r'[13579]', num)
# sum = sum(int(odd) for odd in odds)
# print("the sum is: " + str(sum))


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
#     print(a*i +b)
