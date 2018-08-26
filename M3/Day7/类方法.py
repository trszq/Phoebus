# Author: Zhang Qing

class Dog(object):
    name = "huazai"
    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating" %self.name)


d = Dog("ChenRonghua")
d.eat()