#!_*_coding:utf-8_*_
# Author: Zhang Qing

import os
import sys
#上级目录路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加进环境变量
sys.path.append(BASE_DIR)
print(BASE_DIR)
#导入模块
from core import main

if __name__ == '__main__':
    main.run()
