#!_*_coding:utf-8_*_
# Author: Zhang Qing

# import os
# import sys
#上级目录路径
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加进环境变量
# sys.path.append(BASE_DIR)

from core import auth
from core import logger
from core import transaction

consumption_logger = logger.logger('consumption')
transaction_logger = logger.logger('transaction')

@auth.auth
def consume_api(acc_data,amount,goods):
    new_acc_data = transaction.make_transaction(transaction_logger, acc_data, 'consume', amount)
    if new_acc_data:
        consumption_logger.info('account:%s   goods:%s   payed:%s'%(new_acc_data['id'],goods,amount))
        return True
    else:
        print('Payment is failed.')
        return False
