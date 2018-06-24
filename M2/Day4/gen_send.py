# Author: Zhang Qing

def fun():
    r = 'a'
    while True:
        n = (yield r)
        print("n=",n)
        # if not n:
        #     return
        print('fun test %s...' % n)
        r = '200 OK'

c = fun()
print("next=",c.__next__())
print("send=",c.send('first'))
print("next=",c.__next__())
