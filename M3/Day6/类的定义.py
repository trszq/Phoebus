# Author: Zhang Qing

class Dog(object):
    def __init__(self,name):  #构造函数，构造方法==初始化方法
        self.NAME = name

    def sayhi(self): # 类的方法
        print("Hello, Dog's name is", self.NAME)

d1 = Dog("Tom")  # 相当于Dog(d,"Tom")，实例化后产生的对象叫实例
d2 = Dog("Mary")

d1.sayhi()
d2.sayhi()