#!_*_coding:utf-8_*_
# Author: Zhang Qing

import os
import sys
import time
from datetime import datetime, timedelta
#上级目录路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加进环境变量
sys.path.append(BASE_DIR)
print(BASE_DIR)

from core import accounts
from core import logger

management_logger = logger.logger('management')

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
        expire_date=datetime.now()+timedelta(days=1825)
        acc_data['expire_date'] = expire_date.strftime("%Y-%m-%d")
        acc_data['enroll_date'] = time.strftime("%Y-%m-%d",time.localtime())
        acc_data['balance'] = int(credit)
        acc_data['credit'] = int(credit)
        accounts.dump_account(acc_data)
        management_logger.info('Account [%s] is created successfully.'%acc_data['id'])
        flag = False

def mod_passwd(id):
    acc_data=accounts.load_account(id)
    password=input('Please input the new password:')
    if len(password) == 0:
        print('Password cannot be empty.')
    else:
        acc_data['password'] = password
        accounts.dump_account(acc_data)
        management_logger.info('Account [%s] password is changed successfully'%acc_data['id'])

def mod_pay_day(id):
    acc_data = accounts.load_account(id)
    pay_day = input('Please input the new pay day:')
    if pay_day.isdigit():
        if int(pay_day) > 0 and int(pay_day) < 31:
            acc_data['pay_day']=pay_day
            accounts.dump_account(acc_data)
            management_logger.info('Account [%s] pay day is changed successfully' % acc_data['id'])
        else:
            print('It must be a day number(1-30)')
    else:
        print('Invalid day number')

def mod_credit(id):
    acc_data = accounts.load_account(id)
    credit = input('Please input the new credit:')
    if credit.isdigit():
        acc_data['credit']=credit
        accounts.dump_account(acc_data)
        management_logger.info('Account [%s] credit is changed successfully' % acc_data['id'])
    else:
        print("Invalid credit number.")

def modify_account(acc_data):
    modify_menu='''
    1. 密码
    2. 每月还款日期
    3. 额度
    b. 退出
    '''
    mod_menu_dict={
        '1': mod_passwd,
        '2': mod_pay_day,
        '3': mod_credit
    }
    account_id = input("Account id:")
    print(modify_menu)
    opt = input(">>:").strip()
    if opt == 'b':
        return
    elif opt in mod_menu_dict:
        mod_menu_dict[opt](account_id)
    else:
        print('Please choose the correct option')


def account_info(acc_data):
    account_id=input("Account id:")
    print(accounts.load_account(account_id))

def logout(acc_data):
    exit()

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