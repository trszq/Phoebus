# Author: Zhang Qing

list_1 = [1,1,33,2,22,22,4,9,8]
list_1 = set(list_1)
print(list_1,type(list_1))

list_2 = set([1,4,123,5,0])

print(list_1,list_2)

print(list_1.intersection(list_2))

print(list_1.union(list_2))

print(list_1.difference(list_2))
print(list_2.difference(list_1))

list_3 = set([1,4,9])

print(list_3.issubset(list_1))
print(list_1.issuperset(list_3))

print(list_1.symmetric_difference(list_2))

print(list_1 & list_2)
print(list_1 | list_2)
print(list_1 - list_2)
print(list_1 ^ list_2)


print(1 in list_1)