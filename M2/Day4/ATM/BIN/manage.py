#!_*_coding:utf-8_*_
# Author: Zhang Qing

import os
import sys
import time
#上级目录路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加进环境变量
sys.path.append(BASE_DIR)
print(BASE_DIR)

from core import accounts

acc_data_template = {
    "id": None,
    "password": None,
    "pay_day": None,
    "expire_date": None,
    "balance": None,
    "enroll_date": None,
    "status": 0,
    "credit": None
    }

def create_account(acc_data):
    flag = True
    while flag:
        id = input('Account_name:').strip()
        if len(id) == 0:
            print('Account name is empty.')
            continue
        password = input('Password:').strip()
        if len(password) == 0:
            print('Password cannot be empty.')
            continue
        pay_day = input('Pay day:').strip()
        if not pay_day.isdigit():
            print('Pay day is invalid.')
            continue
        credit = input('Credit:').strip()
        if not credit.isdigit():
            print('Credit is invalid.')
            continue
        acc_data['id'] = id
        acc_data['password'] = password
        acc_data['pay_day'] = int(pay_day)
        acc_data['expire_date'] = time.strftime("%Y-%m-%d",time.localtime())
        acc_data['enroll_date'] = time.strftime("%Y-%m-%d", time.localtime())
        acc_data['balance'] = int(credit)
        acc_data['credit'] = int(credit)
        accounts.dump_account(acc_data)
        print('Account [%s] is created successfully.'%acc_data['id'])
        flag = False

def modify_account(acc_data):
    pass

def account_info(acc_data):
    pass

def logout(acc_data):
    pass

def manage():
    menu='''------ZQ's Bank Management------
    \033[32;1m1.  添加账户
    2.  更改账户信息
    3.  查看账户信息
    4.  退出
    \033[0m
    '''
    menu_dic = {
        '1': create_account,
        '2': modify_account,
        '3': account_info,
        '4': logout,
    }
    while True:
        os.system('cls')
        print(menu)
        user_opt=input(">>:").strip()
        if user_opt in menu_dic:
            menu_dic[user_opt](acc_data_template)
            input('Press any key to continue...')
        else:
            input('Please choose the correct option')

if __name__ == '__main__':
    manage()