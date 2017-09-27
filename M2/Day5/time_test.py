# Author: Zhang Qing

import time

x=time.localtime(123412444)
print(x)
print(x.tm_year)

print(time.strftime("%Y-%m:%d %H:%M:%S",x))

print(time.strptime("1973-11:29 17:14:04","%Y-%m:%d %H:%M:%S"))

print(time.mktime(x))

print(time.asctime(x))
print(time.ctime(123412444))