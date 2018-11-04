#_*_coding:utf-8_*_
#__author__: Zhang Qing
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from src.services import admin_service
from src.services import teacher_service
from src.services import student_service
from src.services import initialize_service

if __name__ == "__main__":
    msg = '''
    0:初始化
    1:管理员
    2:老师
    3:学生
    4:退出
    '''
    role_main={
        '0':initialize_service.main,
        # '1':admin_service.login,
        # '2':teacher_service.login,
        # '3':student_service.login,
    }
    # role_main={
    #     '0':'你要初始化？',
    #     '1':'你是管理员？',
    #     '2':'你是老师？',
    #     '3':'你是学生？',
    # }
    while True:
        print(msg)
        choice=input('>>: ').strip()
        if choice == '4':
            exit()
        elif choice not in role_main:
            input("请输入正确选项")
            continue
        role_main[choice]()

