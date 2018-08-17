#!_*_coding:utf-8_*_
# Author: Zhang Qing

import os
import sys
import re
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(BASE_DIR)
from core import auth
from core import logger
from core import transaction
from core import accounts
from conf import settings

# access_logger = logger.logger('access')
transaction_logger = logger.logger('transaction')

def account_info(acc_data):
    print(acc_data)

def repay(acc_data):
    flag = True
    while flag:
        repay_amount = input("\033[33;1mInput repay amount(Press b to cancel):\033[0m").strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_acc_data = transaction.make_transaction(transaction_logger,acc_data,'repay',repay_amount)
            if new_acc_data:
                flag = False
        elif repay_amount == 'b':
            return
        else:
            input('\033[33;1mInvalid repay amount!\033[0m')
    balance_info='''-------Current Balance Info--------
    Balance: %s
    Credit: %s
    '''%(new_acc_data['balance'],new_acc_data['credit'])
    print(balance_info)

def withdraw(acc_data):
    flag = True
    while flag:
        wd_amount = input("\033[33;1mInput withdraw amount(Press b to cancel):\033[0m").strip()
        if len(wd_amount) > 0 and wd_amount.isdigit():
            new_acc_data = transaction.make_transaction(transaction_logger,acc_data,'withdraw',wd_amount)
            if new_acc_data:
                flag = False
        elif wd_amount == 'b':
            return
        else:
            input('\033[33;1mInvalid withdraw amount!\033[0m')
    balance_info='''-------Current Balance Info--------
    Balance: %s
    Credit: %s
    '''%(new_acc_data['balance'],new_acc_data['credit'])
    print(balance_info)

def transfer(acc_data):
    flag = True
    while flag:
        tran_id = input('\033[33;1mInput the account to transfer:\033[0m').strip()
        tran_acc_data = accounts.load_account(tran_id)
        if not tran_acc_data:
            return
        tran_amount = input("\033[33;1mInput transfer amount(Press b to cancel):\033[0m").strip()
        if len(tran_amount) > 0 and tran_amount.isdigit():
            new_acc_data = transaction.make_transaction(transaction_logger, acc_data, 'transfer', tran_amount)
            if new_acc_data:
                transaction.make_transaction(transaction_logger, tran_acc_data, 'transfer_in', tran_amount)
                flag = False
        elif tran_amount == 'b':
            return
        else:
            input('\033[33;1mInvalid transfer amount!\033[0m')
    balance_info = '''-------Current Balance Info--------
    Balance: %s
    Credit: %s
    ''' % (new_acc_data['balance'], new_acc_data['credit'])
    print(balance_info)


def pay_check(acc_data):
    log_file = "%s/logs/%s" % (settings.BASE_DIR, settings.LOG_TYPES['consumption'])
    with open(log_file,'r') as log_f:
        for log in log_f.readlines():
            log_match=re.match(".*account:%s.*"%acc_data['id'],log)
            if log_match:
                print(log_match.group())

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
            input('Press any key to continue...')
        else:
            input('Please choose the correct option')