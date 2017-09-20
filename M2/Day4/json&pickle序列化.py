# Author: Zhang Qing
import json

user = {'name':'zq','age':'22','gender':'male'}
users_js = json.dumps(user)


f_user = open("users.txt","w")
f_user.write(users_js)
f_user.write(users_js)
f_user.close()
