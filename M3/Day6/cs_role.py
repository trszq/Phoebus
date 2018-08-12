# Author: Zhang Qing

class Role(object):
	nationality = "JP"   #公有属性
	def __init__(self,name,role,weapon,life_value=100,money=15000):
		self.name=name    #成员属性
		self.role=role
		self.weapon=weapon
		self.life_value=life_value
		self.money=money
		self.__heart="Normal" #私有属性
	def tell(self):
		print("------info:%s-------"%self.name)
		for k,v in self.__dict__.items():
			print(k,v)
		print("------end-------")
	# def __del__(self):
	# 	print('del...running..')

r1 = Role('zq','police','M4')
r2 = Role('Jim', 'terrorist', 'AK')
print(r1.__dict__)

r1.tell()
r2.tell()
# import time
#
# time.sleep(5)