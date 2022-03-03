#my_angles.py contains file manipulation scripts associated with master_mandala_maker.py
             # by LeonRHatton

import turtle
import My_template as t
import random
import numpy as np
#import FileScripts as f

global r_angle
r_angle = random.randrange(72, 1500, 9)

turtle.setup(10,10)

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
                    
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::                    
# Automated Angle Generator using numpy.arange module; produces a list of angles based on custom algorithms.
angle_min = 110
angle_max = 1300
key = 100

i_angle_auto = [i for i in np.arange(int(angle_min),int(angle_max),key) \
                if i % float(180) != 0]  + [211.7647] + [211.5385] # Can append any angle(s) to list.  
print(i_angle_auto)
print('The number of auto list elements is: ' + str(len(i_angle_auto)))
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# # https://howchoo.com/python/generate-a-list-of-primes-numbers-in-python
# # Non-prime numbers formula using list comprehension
# noprimes = set(j for i in range(2, 8) for j in range(i*2, 10000, i))
# #Prime numbers formula
# i_angle_primes = [x for x in range(1100, 1300) if x not in noprimes]
# print(i_angle_primes)
# print('The number of primes list elements is: ' + str(len(i_angle_primes)))




#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




# global my_angle
# my_angle = turtle.numinput('Angle', 'Enter Angle Number:', float(r_angle))

# this_angle = turtle.numinput('Enter Angle Number', 'Angle #', 396) # or any specific angle

i_angle_cus = [576,585, 565.7143, 520, 540, 1211, 1350] #angles are changeable Ran on 1/29/2022

# i_angle = [150,561,1286,120,576,270,252,2394,1211,470] #angles are changeable

# x = turtle.numinput('Enter Angle Number', 'Angle Number', 432)
# i_angle = [x-3.5, x-2.5, x-1.5,x-.5, x, x+1, x+2, x+2.5]

i_angle_double = [90, 120, 144, 205.7142857, 150, 135]

i_angle_6 = [60,120,240,300,420,480,540,600,780,840,900,960,1020,1140] # 6 points or sides

i_angle_5 = [72,144,216,288,432,504,576,648,792,864,936,1008,1152,1224,1296,1368] # 5 points or sides

i_angle_7 = [51.42857,102.857,154.29,205.7143,257.143,308.571,\
           411.4286,462.86,514.2857,565.7143,617.1429,\
           668.5714,771.4286,822.8571,874.2857,925.7143,977.1429] #7 points or sides

i_angle_9 = [40, 80, 120, 160, 200, 240, 280, 320, 400, 440, 480, 520, 560, 600, 640, 680, 760] # 9 points or sides

i_angle_17 = [105.882, 127.059,148.2353, 169.4118, 190.59, 211.7647,\
           232.9412, 254.1176, 275.2941, 296.4706,317.6417, 338.8253, 381.1765, 402.3529] # 17 points or sides

i_angle_13 = [110.7692,138.462, 166.154, 193.8462, 221.5385, 249.23,\
           276.9231, 304.6154, 332.3077, 387.6923, 415.3846,\
           443.0769, 470.7692, 498.4615, 526.1538]   # 13 points or sides

i_angle_12 = [30, 60,90,120,150,210,240,270,300,330,390,420,450,480,510,540,570]
i_angle_s = [120,480, 90, 144, 576, 240, 154.29, 140, 2394,\
             1211, 138, 471, 498, 510, 405, 105.882, 320, 170.53]
i_angle_m = [1368,1140,977.1429,855,760,684,621.8182,570,526.1538,488.5714,456,427.5,402.3529,380]

i_angle_basic = [585, 1170, 1755] # Mainly for testing

i_angle_o = [141, 91.5, 227, 1211] # odd angles

freedom_angle = [360/1.75]

# length = len(i_angle)

i_angle_f = [144, 210, 834, 2394, 1350, 1211, 771.3, 1140, 526.1538 ]  #Favorite angles: 144/5P, 210/12P, 834/TightSpiral,2394/20P,1350/Square

i_angle_d_9 = [ 108, 117, 126, 135, 144, 153, 162, 171, 180, 207, 216, 225, 234, 243, 252, 261,\
              270, 306, 315, 324, 333, 342, 351, 405, 414, 423, 432, 441, 450, 504, 513,\
              522, 531, 540, 603, 612, 621, 630, 702, 711, 720, 801, 810, 900 ]  # The sum of digits is 9

i_angle_d_10 = [109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 208,\
               217, 226, 235, 244, 253, 262, 271, 280, 307, 316,\
               325, 334, 343, 352, 361, 370, 406, 415, 424,\
               433, 442, 451, 460, 505, 514, 523, 532, 541, 550,\
               604, 613, 622, 631, 640, 703, 712, 721, 730, 802, 811, 820, 901, 910] # The sum of digits is 10

i_angle_d_5 = [104, 113, 122, 131, 140, 203, 212, 221, 230, 302, 311, 320, 401, 410, 500]


i_angle_d_7  = [411.36, 462.78000000000003, 514.2, 565.62, 617.04, 668.4599999999999,\
                719.88, 771.3, 822.72, 874.14, 925.56, 976.98, 1028.4,\
                1131.24, 1182.66, 1234.0800000000002, 1285.5, 1336.92,51.42, 102.84, 154.26, 205.68, 257.1, 308.52000000000004 ]


fib_angles = [144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393]

i_angle_single = [126, 135, 144, 150] # Run on a single angle, or as many as you wish

i_angle_awesome = [792,765, 977, 315, 432, 947, 1140, 1065, 990, 690, 257.143]

i_angle_iridescent = [257, 315, 270, 432, 612, 225, 972, 912, 257.143]


''' From Geeks for Geeks
# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
  
# Using for loop
for i in list:
    print(i)
    
# getting length of list
length = len(list)
  
# Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
    print(list[i])    

# Iterating using while loop
#i = 0
while i < length:
    print(list[i])
    i += 1
    
 
# Using list comprehension
[print(i) for i in list]

'''
# print(list(i_angle))


