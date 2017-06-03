# Author: Zhang Qing

import os

cart = []
goods = [["iphone",7000],["keyboard",600],["TV",10000],["book",80]]


while 1:
    os.system('cls')
    print("Welcome to ZQ's shopping mall!")
    money = int(input("Please charge your account:"))
    if money > 0:
        break
    else:
        input("Invalid input!")


while 1:
    os.system('cls')
    n = 1
    for _good_info in goods:
        print(n,_good_info[0],_good_info[1])
        n+=1
    print("0 quit")
    id = int(input("Please choose the goods id(choose 0 to quit):"))
    if id > 0 and id < n:
        if money >= goods[id - 1][1]:
            cart.append(goods[id-1])
            money -= goods[id - 1][1]
            print(goods[id-1][0],"has been added into your shopping cart.")
            input("")
        else:
            print("You have not enough balance.")
            break
    elif id == 0:
        break
    else:
        input("Invalid input!")

i=1
print("Here is your shopping list:")
for list in cart:
   print(i,list)
input("Thank you for your patronage!")
