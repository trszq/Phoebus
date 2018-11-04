#!_*_coding:utf-8_*_
# Author: Zhang Qing

from src.models import Admin

def initialize():
    try:
        user=input("请输入初始化管理员账户：")
        pwd=input("请输入初始化管理员密码：")
        obj=Admin(user,pwd)
        obj.save()
        return True
    except Exception as e:
        print(e)

def main():
    menu='''
        1. 初始化管理员账户
    '''
    choice_dict={
        '1':initialize
    }
    while True:
        print(menu)
        choice=input("请输入选项：")
        if choice not in choice_dict:
            print("请输入正确的选项")
            continue
        else:
            ret=choice_dict[choice]()
            if ret:
                print("初始化成功！")
                return
            else:
                print("发生异常，请重新操作")