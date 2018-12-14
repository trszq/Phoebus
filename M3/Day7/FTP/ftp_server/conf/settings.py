#_*_coding:utf-8_*_
#__author__: Zhang Qing
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOME_BASE = "%s/home" % BASE_DIR
LOG_DIR =  "%s/log" % BASE_DIR
LOG_LEVEL = "DEBUG"

ACCOUNT_FILE = "%s/conf/accounts.cfg" % BASE_DIR

HOST = "0.0.0.0"
PORT = 9999