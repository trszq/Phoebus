# Author: Zhang Qing

#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield 1 #返回给c.send(i)的值总是为1，baozi的值是i而不是1，注意yield返回值与表达式值的区别

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(5):
        time.sleep(1)
        print("做了2个包子!")
        print("c_send=",c.send(i))
        print("c2_send=",c2.send(i))

producer("alex")

#通过生成器实现协程并行运算