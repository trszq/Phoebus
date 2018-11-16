#_*_coding:utf-8_*_

import os
import pickle
import time
from conf import settings
from src import identifier

class BaseModel:
    def save(self):
        file_path = os.path.join(self.db_path,str(self.nid))
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
                    data='\033[32;1m登录成功\033[0m'
                    break
            else:
                raise Exception ('\033[43;1m用户名或密码错误\033[0m')
        except Exception as e:
            status=False
            error=str(e)
            data=''
        return {'status':status,'error':error,'data':data}


class School(BaseModel):
    db_path = settings.SCHOOL_DB_DIR
    def __init__(self,name,addr):
        self.nid=identifier.Nid(self.db_path)
        self.name=name
        self.addr=addr
        self.create_time = time.strftime('%Y-%m-%d %X')
        self.__income = 0

    def __str__(self):
        return self.name

class Teacher(BaseModel):
    db_path = settings.TEACHER_DB_DIR
    def __init__(self,username,password,name,level,school_nid):
        self.nid=identifier.Nid(self.db_path)
        self.username=username
        self.password=password
        self.name=name
        self.level=level
        self.school_nid=school_nid
        self.__account=0
        self.create_time=time.strftime('%Y-%m-%d %X')

    def __str__(self):
        return self.name

    @staticmethod
    def login():
        try:
            name=input("用户名：").strip()
            passwd=input("密码：").strip()
            for obj in Teacher.get_all_obj_list():
                if obj.username == name and obj.password == passwd:
                    status=True
                    error=''
                    data='\033[32;1m登录成功\033[0m'
                    teacher_obj = obj
                    break
            else:
                raise Exception ('\033[33;1m用户名或密码错误\033[0m')
        except Exception as e:
            status=False
            error=str(e)
            data=''
            teacher_obj=None
        return {'status':status,'error':error,'data':data,'teacher':teacher_obj}

class Student(BaseModel):
    db_path = settings.STUDENT_DB_DIR
    def __init__(self,username,password,name,age,mobile,school_nid,classes_nid):
        self.nid=identifier.Nid(self.db_path)
        self.username=username
        self.password=password
        self.name=name
        self.age=age
        self.mobile=mobile
        self.school_nid=school_nid
        self.classes_nid=classes_nid
        self.score=Score(self.nid)
        self.create_time = time.strftime('%Y-%m-%d %X')

    def __str__(self):
        return self.name

    @staticmethod
    def login():
        try:
            name=input("用户名：").strip()
            passwd=input("密码：").strip()
            for obj in Student.get_all_obj_list():
                if obj.username == name and obj.password == passwd:
                    status=True
                    error=''
                    data='\033[32;1m登录成功\033[0m'
                    break
            else:
                raise Exception ('\033[33;1m用户名或密码错误\033[0m')
        except Exception as e:
            status=False
            error=str(e)
            data=''
        return {'status':status,'error':error,'data':data}


class Course(BaseModel):
    db_path=settings.COURSE_DB_DIR
    def __init__(self,name,price,period,school_nid):
        self.nid=identifier.Nid(self.db_path)
        self.name=name
        self.price=price
        self.period=period
        self.school_nid=school_nid
        self.create_time = time.strftime('%Y-%m-%d %X')

    def __str__(self):
        return self.name

class Classes(BaseModel):
    db_path=settings.CLASSES_DB_DIR
    def __init__(self,name,school_nid,course_to_teacher_list):
        self.nid=identifier.Nid(self.db_path)
        self.name=name
        self.school_nid=school_nid
        self.course_to_teacher_list=course_to_teacher_list
        self.create_time = time.strftime('%Y-%m-%d %X')

    def __str__(self):
        return self.name

class Course_to_teacher(BaseModel):
    db_path=settings.COURSE_TO_TEACHER_DB_DIR
    def __init__(self,course_nid,teacher_nid):
        self.nid=identifier.Nid(self.db_path)
        self.course_nid=course_nid
        self.teacher_nid=teacher_nid
        self.school_nid=self.teacher_nid.get_obj_by_uuid().school_nid
        self.create_time = time.strftime('%Y-%m-%d %X')

    def get_course_to_teacher_list(self):
        ret=self.get_all_obj_list()
        if ret:
            return [ret.course_nid.get_obj_by_uuid(),ret.teacher_nid.get_obj_by_uuid()]
        return [None,None]

class Score:
    def __init__(self,nid):
        self.nid=nid
        self.score_dict={}

    def set(self,course_to_teacher_nid,number):
        self.score_dict[course_to_teacher_nid]=number

    def get(self,course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid)