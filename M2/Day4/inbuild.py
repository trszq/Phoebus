# Author: Zhang Qing

#print(any([0,1,0]))
#print(all([0,1,4]))
#print(bool(0))

#res = filter(lambda n:n>5,range(10))
#res = map(lambda n:n*2,range(10))
#res = [ lambda i:i*2 for i in range(10) ]
#import functools

#res = functools.reduce( lambda x,y:x*y,range(1,10))

# def test():
#     local_var = 111
#     print(locals())
#     print(globals())
#
# test()
# print(globals())
#
# a = [1,1,2,3,2,3,6,89]
#
# print(a[-1])

a = {1:123,3:2,-4:10,99:-8,6:22}

print(a)
print(sorted(a))
print(sorted(a.items()))
print(sorted(a.items(),key=lambda x:x[1]))
print(a.items())