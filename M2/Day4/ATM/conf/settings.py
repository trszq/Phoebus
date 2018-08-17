# Author: Zhang Qing

import os
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DATABASE = {
#     'engine': 'file_storage',
#     'name':'accounts',
#     'path': "%s/db" % BASE_DIR
# }

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
    'management': 'management.log',
    'consumption': 'consumption.log'
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'transfer_in':{'action':'plus', 'interest':0},
    'consume':{'action':'minus', 'interest':0},
}