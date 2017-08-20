# Author: Zhang Qing
import time
user,passwd = 'zq','abcd'
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            print("wrapper func agrs:",*args,**kwargs)
            username = input("Username:").strip()  #strip()去除空格
            password = input("Password:").strip()
            if user == username and passwd == password:
                print("\033[32;1mUser has passed authentication\033[0m")
                res = func(*args,**kwargs)
                print("--after authentication")
                return res
            else:
                exit("\033[31;1mInvalid username or password\033[0m")
        return wrapper
    return outer_wrapper

def index():
    print("welcome to index page")

@auth(auth_type="local")
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")

index()
print(home())
bbs()