#_*_coding:utf-8_*_

import os
import pickle
import time
from conf import settings
from src import identifier

class BaseModel:
    def save(self):
        file_path = os.path.join(self.db_path,self.nid)
        pickle.dump(self,open(file_path,'wb'))

    @classmethod
    def get_all_obj_list(cls):
        ret=[]
        for file_name in os.listdir(cls.db_path):
            file_path=os.path.join(cls.db_path,file_name)
            ret.append(pickle.load(open(file_path,'rb')))
        return ret

class Admin(BaseModel):
    db_path = settings.ADMIN_DB_DIR
    def __init__(self,username,password):
        self.nid=identifier.Nid(self.db_path)
        self.username=username
        self.password=password
        self.create_time = time.strftime('%Y-%m-%d')

    @staticmethod
    def login():
        try:
            name=input("用户名：").strip()
            passwd=input("密码：").strip()
            for obj in Admin.get_all_obj_list():
                if obj.username == name and obj.password == passwd:
                    status=True
                    error=''
                    data='\033[45;1m登录成功\033[0m'
                    break
            else:
                raise Exception ('\033[43;1m用户名或密码错误\033[0m')
        except Exception as e:
            status=false
            error=str(e)
            data=''
        return {'status':status,'error':error,'data':data}


class School(BaseModel):
    pass

class Teacher(BaseModel):
    pass

class Student(BaseModel):
    pass

class Course(BaseModel):
    pass

class Classes(BaseModel):
    pass

class Course_to_teacher(BaseModel):
    pass

class Score:
    pass