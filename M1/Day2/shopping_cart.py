# Author: Zhang Qing

import os

cart = []
goods = [["iphone",7000],["keyboard",600],["TV",10000],["book",80]]


while 1:
    os.system('cls')
    print("Welcome to ZQ's shopping mall!")
    _money = input("Please charge your account:")
    if not _money.isdigit():
        input("Please enter a appropriate number.")
    elif int(_money) > 0:
        money = int(_money)
        break
    else:
        input("Please enter an appropriate number.")


#money.isdigit()
#下标方法：
#法一
#goods.index(_good_info)
#法二
#for index,item in enumerate(goods)
#    print(index,item)
#判断列表长度：len(goods)

while 1:
    os.system('cls')
    n = 1
    for _good_info in goods:
        print(n,_good_info[0],_good_info[1])
        n+=1
    print("0 quit")
    _id = input("Please choose the goods id(choose 0 to quit):")
    if not _id.isdigit():
        input("Please enter an appropriate number.")
        continue
    else:
        id = int(_id)
    if id > 0 and id < n:
        if money >= goods[id - 1][1]:
            cart.append(goods[id-1])
            money -= goods[id - 1][1]
            print(goods[id-1][0],"has been added into your shopping cart.Your balance is:",money)
            input("")
        else:
            print("You have not enough balance.")
            break
    elif id == 0:
        break
    else:
        input("Please enter an appropriate number.")

i=1
print("Here is your shopping list:")
for list in cart:
   print(i,list)
   i+=1
input("Thank you for your coming!")
