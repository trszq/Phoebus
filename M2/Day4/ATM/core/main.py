# Author: Zhang Qing

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(BASE_DIR)
from core import auth
from core import logger

access_logger = logger.logger('access')
transaction_logger = logger.logger('transaction')

def account_info(acc_data):
    print(acc_data)

def repay(acc_data):
    print('repay')

def withdraw(acc_data):
    print('withdraw')

def transfer(acc_data):
    print('transfer')

def pay_check(acc_data):
    print('pay_check')

def logout(acc_data):
    exit()

@auth.auth
def run(acc_data):
    menu = '''
    ------- ZQ's Bank ---------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m
    '''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout
    }
    while True:
        os.system('cls')
        print(menu)
        user_opt=input(">>:").strip()
        if user_opt in menu_dic:
            menu_dic[user_opt](acc_data)
