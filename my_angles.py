"""my_angles.py contains functions, generators, and formatters needed to output
a chosen set of angles to master_mandala_maker.py
by Leon Hatton
"""

import random
import numpy as np
import math
import sys
import os
import platform
import time

import Timer as Tm
import My_logger as Lg

if sys.platform.startswith("linux"):
    my_path = "/home/sels/Modules/"
    my_log_path = "/home/sels/Modules/MandalaMaker/Logs"
else:
    my_path = "D:"
    my_log_path = "D:/Modules/MandalaMaker/Logs"


def get_my_multiples():
    global my_multiples, my_multiples_number, max_value, my_multiples_key
    my_multiples_number = 4628.571429
    my_multiples_key = my_multiples_number * 2
    max_value = my_multiples_number * 3
    my_multiples = [
        my_number
        for my_number in np.arange(
            int(my_multiples_number), my_multiples_key, max_value
        )
        if my_multiples_number % (180) != 0 
    ] + [400, 1000, 1600, 2200]
# get_my_multiples()


# Automated Angle Generator using numpy.arange module; produces a list of angles based on custom algorithms.
#
def pick_angles():
    global i_angle_auto, i_angle_float
    get_my_multiples()
    angle_min = float(my_multiples_number)  # 51.42857
    angle_max = max_value
    key = my_multiples_key  # Dividing angle_min by 2 and using that as a key results in a harmonic angle family; also multiply by 3 or 5

    i_angle_float = [
            angle  for angle in np.arange(float(angle_min), float(angle_max), float(key))
            if angle % (180) != 0
            ]   # +  [4000, 22000] 

    i_angle_auto = [
            angle
            for angle in np.arange(
                int(float(angle_min)), int(float(angle_max)), int(float(key))
                )
            if angle % (180) != 0
            ]
    return i_angle_auto, i_angle_float

pick_angles()

Lg.logger.info(
    "*******************************************************************************************************"
)
Lg.logger.info(f"Running Scripts from Master MandalaMaker, my_angles.py @ {Tm.my_date_time}")
Lg.logger.info(
    "..........................................................................................................................................."
)
Lg.logger.info(
    f"my_angles.py: The automated set of {len(i_angle_float)} angles to be drawn for the selected mandala is: {i_angle_float}"
)
