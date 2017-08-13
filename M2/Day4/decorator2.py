# Author: Zhang Qing

def bar():
    print('in the bar')

def test1(func):
    print(func)
    func()

test1(bar)