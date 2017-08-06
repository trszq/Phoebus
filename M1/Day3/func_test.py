# Author: Zhang Qing

def test(*args):
    print(args)

def test2(**kwargs):
    print(kwargs)

test(1,2,3,4)
test(*(1,2,3,4))
test2(name='zq',age=11,gender='m')
test2(**{'name':'zq','age':11,'gender':'m'})

