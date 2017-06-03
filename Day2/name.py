# Author: Zhang Qing

names = ["zhangsan","lisi","wangwu","zhaoliu"]
names.append("David")  #插入到最后
names.insert(1,"Bob")
#names.remove("wangwu")
#print(names[2])
names2 = [1,2,3,4]
#print(names.index("lisi"))
#print(names[-1])
#print(names[-3:])

names.extend(names2)
print(names,names2)

#print(names[0:-1:2])