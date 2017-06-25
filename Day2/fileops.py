# Author: Zhang Qing

import pickle
import json
'''
goods = [["iphone","7000"],["keyboard","600"],["TV","10000"],["book","80"]]


#goods_js=json.dumps(goods)
fgoods=open("goodslist.txt",'w')
tmp=[]
for goods_row in goods:
    tmp.append(goods_row[0]+","+goods_row[1]+"\n")
fgoods.writelines(tmp)
fgoods.close()

fgoods2=open("goodslist.txt",'r')

goods2=[]
for good_item in fgoods2.readlines():
    good_item=good_item.replace("\n","").split(",")
    goods2.append(good_item)
print(goods2[0][0])
fgoods2.close()
'''


user_info = {
    'Tom': [123,1400,[["iphone",7000],["keyboard",600],["book",80]]],
    'Mary': ['abc',10000,[["iphone",7000],["TV",10000],["book",80]]]
}

js_user_info = json.dumps(user_info)  #此时js_user_info为string数据类型而不是dict，dict是无法直接写入文件的

#print(user_info)
#print(js_user_info)

f1=open('dict.json','w')
f1.write(js_user_info)
f1.close()

f2=open('dict.json','r')
info_user = json.loads(f2.read())
# info_user = f2.read()
f2.close()

print(info_user.get("Toam"))
print(info_user["Tom"])

