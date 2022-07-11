#  Timer.py conntains timer function and display scripts associated with MasterMandalaMaker.py

import time
import datetime

class Timer():
    def __init__(self, message):
        self.message = message
    def __enter__(self):
        self.start = time.time()
        return None # could return anything, to be used like this: with Timer('Message) as value:
    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start) / 60  # can changed to show seconds or milliseconds(1000)
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
        start_time = time.localtime()
        current_time = time.strftime('%D; %H:%M:%S',start_time)
        print ('Start:    ' + current_time)
        return start_time
        
        
    global end_time    
    def end_time():
        end_time = time.localtime()
        current_time = time.strftime('%D; %H:%M:%S',end_time)
        print ('End:    ' + current_time)

# def sleeper(): #Work on this to automat pauses between mandala module execution
#     fn_01 = turtle.exitonclick()
#     fn_02 = continue
#     fn_03 =  time.sleep(10)
   
    # keyboard input to quit or continue

        
def time_functions():
    set_time()
    start_time()
    end_time()
# 
# time_functions()

# print(start_time())
# print(end_time())
     