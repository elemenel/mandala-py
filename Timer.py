""" Timer.py contains timer function and display scripts
associated with MasterMandalaMaker.py
Copyright (C) 2017 - 2024 by Leon R.Hatton
"""
import time
import sys
import datetime
from timeit import default_timer as timer
import My_logger as Lg
import logging

if sys.platform.startswith('linux'):
    my_path = '/home/sels/Modules/'
else:
    my_path = 'D:/'
    
    
my_filename = f'{my_path}Mandala Maker/Logs/my_filename.log'

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
        self.start = timer()
        return None # could return anything, to be used like this: with Timer('Message) as value:
    def __exit__(self, type, value, traceback):
        elapsed_time = ( timer( ) - self.start * 60) # / 60  # can changed to show seconds(60) or milliseconds(1000)
        print(self.message.format(elapsed_time))
        
        
#Set up Time and Date Functions
def set_time():
    global date_time, my_date, my_time, project_time, now, iterable_time, end_time, start_time, end, this_time, start, this_start, this_end
    my_date = datetime.datetime.now().strftime('%x')
    now = datetime.datetime.now()
    my_time = now.strftime('%D; %I:%M:%S %p')
    project_time = now.strftime('%y%j%M%S')  #Small y = , small j =  , cap M = minutes, cap S = seconds
    iterable_time =  str(datetime.datetime.now().strftime('%d%m%y%H%M%S%f')) #now.strftime(('%m%d%H%M%S'))
    this_start = time.time()
    this_end = time.time()
    start = now.strftime(('%D;%H:%S%p'))
    end = now.strftime(('%D;%H:%S'))
    this_time = now.strftime('%I:%M:%S')
       
    return my_time, project_time, my_date, now
set_time()
 
#Set Up Start and End Times
# set_time()
# start_time = now
# timer_start_time = timer()
# set_time()
# Lg.logger.info('Holding  for 2 seconds:')
# time.sleep(2)
# set_time()
# end_time =now
# execution_time  = (end_time - start_time) 
# elapsed_time = (this_end - this_start)
# timer_end_time = timer()
# timer_elapsed_time = timer_end_time - timer_start_time
# print(f'The timer() time is {timer()}')
# print(f'timer_elapsed_time is {timer_elapsed_time:.2f} seconds')
# print(f'timer_elapsed_time is {timer_elapsed_time/60:.2f} minutes')
# print(f'timer_elapsed_time is {timer_elapsed_time/3600:.2f} hours')


# set_time()
# print(f'this_start time is {this_start}')
# print(f'start_time is {start_time}')
# print(f'this_time is {this_time}')
# print(f'my_date is {my_date}')
# print(f'now is {now}')
# print(f'my_time is {my_time}')
# print(f'project_time is {project_time}')
# print(f'iterable_time is {iterable_time}')
# print(f'end is {end}')
# print(f'start is {start}')
# print(f'end_time is {end_time}')
# print(f'execution_time is {execution_time} seconds')
# print(f'Elapsed time: {elapsed_time // 3600}h, {elapsed_time %3600 //60}m, {elapsed_time %60}s')
# print(f'this_end_time is {this_end}')
# print(f'timer elapsed_time: {timer_elapsed_time/3600:.6f} hours')
# print(f'timer elapsed_time: {timer_elapsed_time/60:.2f} minutes')
# print(f'timer elapsed_time: {timer_elapsed_time:.2f} seconds')
# Lg.logger.info(f'Run Start: {my_date}')
# Lg.logger.info:(f'master_mandala_maker_production start time: {project_time}')


# Start time
# start_time = datetime.datetime.now()
# my_start_time = timer()

# Your code here...
# Lg.logger.info(f'Holding for 3 seconds:')
# time.sleep(3)

# End time
# end_time = datetime.datetime.now()
# my_end_time = timer()

# Calculate elapsed time
# elapsed_time = end_time - start_time
# my_elapsed_time = my_end_time - my_start_time

# # Format the output
# hours, remainder = divmod(my_elapsed_time.seconds, 3600)
# minutes, seconds = divmod(remainder, 60)
# milliseconds = my_elapsed_time.microseconds // 1000
# formatted_time = "{:02}:{:02}:{:02}.{:02}".format(hours, minutes, seconds, milliseconds)
# 
# print("Elapsed time: ", formatted_time)
# Lg.logger.info(f"Elapsed time: {formatted_time} hours")
# print(f'{my_elapsed_time/3600:.6f} hours:  {my_end_time} - {my_start_time}')
# print(f'{my_elapsed_time/60:.3f} minutes:  {my_end_time} - {my_start_time}')
# print(f'{my_elapsed_time:.2f} seconds:  {my_end_time} - {my_start_time}')

# start_time = time.time()
# # your script
# elapsed_time = time.time() - start_time
# time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
