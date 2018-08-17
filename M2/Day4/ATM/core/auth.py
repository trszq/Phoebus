#!_*_coding:utf-8_*_

import os
import json
import time
from conf import settings
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from core import logger

access_logger = logger.logger('access')

def auth(func):
    def wrapper(*args,**kwargs):
        count = 0
        while count < 3:
            account = input("\033[32;1maccount:\033[0m").strip()
            password = input("\033[32;1mpassword:\033[0m").strip()
            account_file = '%s/db/accounts/%s.json'%(settings.BASE_DIR,account)
            if os.path.isfile(account_file):
                with open(account_file, 'r') as f:
                    acc_data = json.load(f)
                    if acc_data['password'] == password:
                        exp_time = time.mktime(time.strptime(acc_data['expire_date'], "%Y-%m-%d"))
                        if time.time() >= exp_time:  # 验证账户是否过期
                            print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
                        elif acc_data['status'] > 0: # 验证账户是否冻结
                            print("\033[31;1mAccount [%s] is frozen.\033[0m" % account)
                        else:
                            access_logger.info("[%s] login successfully"%acc_data['id'])
                            print("Welcome,%s"%acc_data['id'])
                            res = func(acc_data,*args,**kwargs)
                            return res
                    else:
                        print("\033[31;1mPassword is incorrect!\033[0m")
            else:
                print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)
            count += 1
        else:
            access_logger.error("Too many login attempts")
            exit()
    return wrapper


