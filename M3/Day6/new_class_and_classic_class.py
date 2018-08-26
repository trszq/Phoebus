# Author: Zhang Qing

class A:
	def __init__(self):
		self.n='A'

class B(A):
	def __init__(self):
		self.n='B'

class C(A):
	def __init__(self):
		self.n='C'

class D(B,C):
	def __init__(self):
		self.n='D'

d=D()
print(d.n)
