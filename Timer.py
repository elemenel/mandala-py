#  Timer.py conntains timer function and display scripts associated with MasterMandalaMaker.py

import time
import datetime
from timeit import default_timer as timer
import My_logger as l
import logging
import My_template as t


logger = logging.getLogger(t.my_project)

logger.info('Child Logger in Timer.py is working')
# start = timer()
# 
# logger.info(23*2.3)
# 
# end = timer()
# logger.info(end - start)

class Timer():
    def __init__(self, message):
        self.message = message
    def __enter__(self):
        self.start = time.time()
        return None # could return anything, to be used like this: with Timer('Message) as value:
    def __exit__(self, type, value, traceback):
        elapsed_time = ( time.time( ) - self.start * 60) # / 60  # can changed to show seconds or milliseconds(1000)
        logger.info(self.message.format(elapsed_time))
        
        
#Set up Time and Date Functions
def set_time():
    global date_time
    global my_date
    global my_time
    global project_time
    global now
    date_time = datetime.datetime.now()
    my_date = date_time.strftime('%x')
    now = datetime.datetime.now()
    my_time = now.strftime('%D;%H:%M')
    project_time = now.strftime('%y%j%M%S')
    return my_time, project_time, my_date, date_time
    
#Set Up Start and End Times
def start_time():
    now = datetime.datetime.now()
    started = now.strftime('%D; %H:%M:%S')
    logger.info ('Start:      ' + started)
    return started
     
    
def end_time():
    now = datetime.datetime.now()
    ended = now.strftime('%D; %H:%M:%S')
    logger.info ('End:      ' + ended)
    return ended
        
#     global elapsed_time  # Need to work on
# set_time()

# duration = lambda end_time, start_time: str(end_time() - str(start_time()))
# logger.info(duration)

# def sleeper(): #Work on this to automate pauses between mandala module execution
#     fn_01 = turtle.exitonclick()
#     fn_02 = continue
#     fn_03 =  time.sleep(10)
   
    # keyboard input to quit or continue

        
def time_functions():
    set_time()
    start_time()
    end_time()
# 
time_functions()
# logger.info('date_time:  ' + str(date_time))
# logger.info('my_date:  ' + str(my_date))
# logger.info('my_time  :' + str(my_time))
# logger.info('now  :'+  str(now))
logger.info('project_time:  ' + str(project_time))
     