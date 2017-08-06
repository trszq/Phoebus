# Author: Zhang Qing
#import getpass

_username='zq'
_password='123'

username = input("username:")
#password = getpass.getpass("password:")
password=input("password:")

if _username == username and _password == password:
    print("welcome {name}".format(name=username))
else:
    print("Invalid username or password!")
