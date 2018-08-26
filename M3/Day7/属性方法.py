# Author: Zhang Qing

class Dog(object):

    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print("%s is eating" %self.name)
    @eat.setter
    def Eat(self,food):
        print("Set to food:",food)

d = Dog("ChenRonghua")
d.eat