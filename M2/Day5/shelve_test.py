# Author: Zhang Qing

import shelve
import datetime

d = shelve.open('shelve_test')
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))

# info = {'age':22, "job":'it'}
# name = ["alex", "rain", "bob"]
# d["name"]=name
# d["info"]=info
# d["date"]=datetime.datetime.now()
d.close()