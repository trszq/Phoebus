# Author: Zhang Qing
names=['zhangsan','lisi']
data={}

try:
    names[3]
    data['name']

except (KeyError,IndexError) as e:
    print("There is no key:",e)
# except IndexError as e:
#     print(e)