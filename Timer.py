#  Timer.py conntains timer function and display scripts associated with MasterMandalaMaker.py

import time
import datetime
from timeit import default_timer as timer

# start = timer()
# 
# print(23*2.3)
# 
# end = timer()
# print(end - start)

class Timer():
    def __init__(self, message):
        self.message = message
    def __enter__(self):
        self.start = time.time()
        return None # could return anything, to be used like this: with Timer('Message) as value:
    def __exit__(self, type, value, traceback):
        elapsed_time = ( time.time( ) - self.start * 60) # / 60  # can changed to show seconds or milliseconds(1000)
        print(self.message.format(elapsed_time))
        
        
#Set up Time and Date Functions
def set_time():
    global date_time
    global my_date
    global my_time
    date_time = datetime.datetime.now()
    my_date = date_time.strftime('%x')
    now = datetime.datetime.now()
    my_time = now.strftime('%D; %H:%M:%S')
    
    #Set Up Start and End Times
    global start_time
    def start_time():
        now = datetime.datetime.now()
        start_time = now.strftime('%D; %H:%M:%S')
        print ('Start:      ' + str(start_time))
        return start_time
  
       
        
        
    global end_time    
    def end_time():
        finis_time = time.localtime()
        end_time = time.strftime('%D; %H:%M:%S',finis_time)
        print ('End:      ' + str(end_time))
        return end_time
        
#     global elapsed_time  # Need to work on
# set_time()
# start_time()
# time.sleep(12)
# end_time()
# duration = lambda end_time, start_time: str(end_time() - str(start_time()))
# print(duration)

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

# print(str(start_time))
# print(str(end_time))
     