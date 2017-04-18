# Author: Zhang Qing
import os

f=open('menu.txt')
menu=f.read()
f.close()

f=open('menu1.txt')
menu1=f.read()
f.close()

f=open('menu2.txt')
menu2=f.read()
f.close()

f=open('menu_a.txt')
menu_a=f.read()
f.close()

f=open('menu_b.txt')
menu_b=f.read()
f.close()

f=open('menu_c.txt')
menu_c=f.read()
f.close()

f=open('menu_d.txt')
menu_d=f.read()
f.close()

while 1:
    os.system('cls')
    num1 = input(menu)
    if num1 == "0":
        break
    elif num1 == "1":
        os.system('cls')
        num2=input(menu1)
        if num2 == "0":
            break
        elif num2 == "1":
            os.system('cls')
            num3=input(menu_a)
            if num3 == "0":
                break
            else:
                continue
        elif num2 == "2":
            os.system('cls')
            num3=input(menu_b)
            if num3 == "0":
                break
            else:
                continue
        elif num2 == "3":
            continue
        else:
            input("Invalid input!Please select again.Press any key to continue:")
    elif num1 == "2":
        os.system('cls')
        num2=input(menu2)
        if num2 == "0":
            break
        elif num2 == "1":
            os.system('cls')
            num3=input(menu_c)
            if num3 == "0":
                break
            else:
                continue
        elif num2 == "2":
            os.system('cls')
            num3=input(menu_d)
            if num3 == "0":
                break
            else:
                continue
        elif num2 == "3":
            continue
        else:
            input("Invalid input!Please select again.Press any key to continue:")
    else:
        input("Invalid input!Please select again.Press any key to continue:")


