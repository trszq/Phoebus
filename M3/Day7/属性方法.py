# Author: Zhang Qing

class Dog(object):
    '''To describe the species dog'''
    def __init__(self, name):
        self.name = name
        self.__food = None

    # @property
    # def eat(self):
    #     print("%s is eating" %(self.name,self.__food)

    # @eat.setter
    # def eat(self,food):
    #     print("Set to food:",food)
    #     self.__food = food

    # @eat.deleter
    # def eat(self):
    #     del self.__food
    #     print("food deleted")


d = Dog("ChenRonghua")
# d.eat
# d.eat = "shit"
# d.eat
print(Dog.__doc__)