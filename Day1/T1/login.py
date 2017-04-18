# Author: Zhang Qing
import os



f1=open('users.txt')
f2=open('passwd.txt')
username=[]
password=[]
for linea in f1.readlines():
    username.append(linea.replace("\n",""))

for lineb in f2.readlines():
    password.append(lineb.replace("\n",""))

i=len(username)
count=[0]*i
f1.close()
f2.close()

#print(username)
#print(password)
#print(count)

while 1:
    os.system('cls')
    print("Welcome to python's world! Please login.")
    _username = input("username:")
    _password = input("password:")
    j = 0
    while j < i:
        if _username == username[j] and _password == password[j]:
            if count[j] >= 3:
                input("Your account is locked!Please try other accounts.")
                break
            else:
                print("Welcome {name}".format(name=_username))
                exit()
        if _username == username[j] and _password != password[j]:
            count[j] = count[j]+1
        j=j+1
    else:
        input("Invalid username or password!Please try other accounts.")



