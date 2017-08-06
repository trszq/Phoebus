# Author: Zhang Qing

import os
import json

#goods = [["iphone",7000],["keyboard",600],["TV",10000],["book",80]]

fgoods = open("goodslist.txt",'r')

goods = []

for good_item in fgoods.readlines():
    good_item = good_item.replace("\n","").split(",")
    goods.append(good_item)

fgoods.close()

cart = []

f_user = open("users.txt","r")
_users = f_user.read()
f_user.close()

if _users:
    users = json.loads(_users)
else:
    users = {}

user = input("Welcome to ZQ's shopping mall! Please login:")
# user does not exist
if user not in users:
    users[user] = {}
    record = []
    users[user]["record"] = []
    _password=input("Your account has not been created. Please enter your password:")
    users[user]["password"] = _password
    while True:
        os.system('cls')
        _money = input("Please charge your account:")
        if not _money.isdigit():
            input("\033[5;31mPlease enter an appropriate number.\033[0m")
        elif int(_money) > 0:
            money = int(_money)
            break
        else:
            input("\033[5;31mPlease enter an appropriate number.\033[0m")
# user exists
else:
    password = users[user]["password"]
    money = int(users[user]["money"])
    record = users[user]["record"]
    i = 0
    while True:
        os.system('cls')
        _password = input("Please enter your password:")
        if password == _password:
            break
        elif i >= 3:
            input("Tried too many times!")
            exit(1)
        else:
            input("Password is not matched.")
            i += 1

while True:
    os.system('cls')
    n = 1
    for _good_info in goods:
        print(n,_good_info[0],_good_info[1])
        n += 1
    print("0  quit")
    print("p  show your previous shopping record.")
    print("c  show your shopping cart.")
    print("m  show your balance.")
    _id = input("Please choose the goods id:")
    if _id == 'p':
        input(record)     # query the previous shopping record
        continue
    elif _id == 'c':
        input(cart)     # query the previous shopping record
        continue
    elif _id == 'm':
        print("\033[1;32m",money,"\033[0m")     # query the previous shopping record
        input("")
        continue
    elif not _id.isdigit():
        input("\033[5;31mPlease enter an appropriate number.\033[0m")
        continue
    else:
        id = int(_id)
# shopping
    if id > 0 and id < n:
        if money >= int(goods[id - 1][1]):
            cart.append(goods[id-1])
            money -= int(goods[id - 1][1])
            print(goods[id-1][0],"has been added into your shopping cart.Your balance is:","\033[1;32m",money,"\033[0m")
            input("")
        else:
            print("You have not enough balance.")
            break
    elif id == 0:
        break
    else:
        input("\033[5;31mPlease enter an appropriate number.\033[0m")
# checking out
i = 1
print("Here is your shopping list:")
for list in cart:
   print(i,list)
   i += 1
print("Your balance is:","\033[1;32m",money,"\033[0m")
input("Thank you for your coming!")
# record data
users[user]["money"] = money
users[user]["record"].extend(cart)

users_js = json.dumps(users)

f_user = open("users.txt","w")
f_user.write(users_js)
f_user.close()