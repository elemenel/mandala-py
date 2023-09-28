""" Timer.py contains timer function and display scripts
associated with MasterMandalaMaker.py
by Leon Hatton
"""
import time
import datetime
from timeit import default_timer as timer

import My_logger as Lg
import logging
my_filename = '/home/sels/Modules/Mandala Maker/Logs/my_filename.log'

# logger= logging.getLogger() #t.my_project)
# fileHandler = logging.FileHandler(my_filename)
# fileHandler.setLevel(logging.INFO)
# logger.addHandler(fileHandler)
# 
# logger = logging.getLogger()  #t.my_project)
# consoleHandler = logging.StreamHandler()
# consoleHandler.setLevel(logging.INFO)
# logger.addHandler(consoleHandler)
# Lg.logger.info('Child Logger in Timer.py is functioning')


class Timer():
    def __init__(self, message):
        self.message = message
    def __enter__(self):
        self.start = time.time()
        return None # could return anything, to be used like this: with Timer('Message) as value:
    def __exit__(self, type, value, traceback):
        elapsed_time = ( time.time( ) - self.start * 60) # / 60  # can changed to show seconds(60) or milliseconds(1000)
        print(self.message.format(elapsed_time))
        
        
#Set up Time and Date Functions
def set_time():
    global date_time
    global my_date
    global my_time
    global project_time
    global now
    global iterable_time
    global end_time
    global end
    date_time = datetime.datetime.now()
    my_date = date_time.strftime('%x')
    now = datetime.datetime.now()
    my_time = now.strftime('%D;%H:%M:%S')
    project_time = now.strftime('%y%j%M%S')  #Small y = , small j =  , cap M = minutes, cap S = seconds
    iterable_time =  str(datetime.datetime.now().strftime('%m%d%Y%H%M%S%f')) #now.strftime(('%m%d%H%M%S'))
    end = now.strftime(('%D; %H%S'))
    return my_time, project_time, my_date, date_time  #, iterable_time
    
#Set Up Start and End Times
def start_time():
    global started
    start = datetime.datetime.now()
    started = start.strftime('%D; %H:%M:%S')
#     print ('Start:      ' + started)
    return started
     
    
def end_time():
    global ended
    end = datetime.datetime.now()
    ended = end.strftime('%D; %H:%M:%S')
#     print('End:  ' + ended)
    return ended


        
def time_functions():
    set_time()
    start_time()
    end_time()

time_functions()

Lg.logger.info(f'Run Start: {my_date}')
Lg.logger.info:(f'master_mandala_maker_production start time: {project_time}')

