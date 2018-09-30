# Author: Zhang Qing

class Dog(object):

    def __init__(self, name):
        self.name = name

    @staticmethod  # 把eat方法变为静态方法
    def eat(self):
        print("%s is eating" % self.name)


d = Dog("ChenRonghua")
d.eat(d)