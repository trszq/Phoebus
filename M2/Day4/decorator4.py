# Author: Zhang Qing

import time

def timmer(func):
    def deco():
        start_time=time.time()
        func()
        stop_time=time.time()
        print('The func run time is %s' %(stop_time-start_time))
    return deco

@timmer   #test1=timer(test1)
def test1():
    time.sleep(3)
    print('in the test1')

test1()
