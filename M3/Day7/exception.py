dic = ["wupeiqi", 'alex']
try:
    dic[11]
except IndexError as e:
    print(e)


try:
    raise Exception('错误了。。。')
except Exception as e:
    print(e)

raise Exception('错误了。。。')