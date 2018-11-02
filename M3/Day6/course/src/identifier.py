#_*_coding:utf-8_*_
#__author__: Zhang Qing

import os
import uuid
import pickle

def create_uuid():
    return str(uuid.uuid1())

class Nid:
    def __init__(self,db_path):
        # role_list=[
        #     'admin','school','teacher','course','course_to_teacher','classes','student'
        # ]
        # if role not in role_list:
        #     raise Exception('用户角色错误,选项: %s' % ','.join(role_list))
        # self.role=role
        self.uuid=create_uuid()
        self.db_path = db_path

    def __str__(self):
        return self.uuid

    def get_obj_by_uuid(self):
        for file_name in os.listdir(self.db_path):
            if file_name == self.uuid:
                file_path=os.path.join(self.db_path,file_name)
                return pickle.load(open(file_path,'rb'))

# class AdminNid(Nid):
#     def __init__(self,db_path):
#         super(AdminNid,self).__init__('admin',db_path)
#
#
# class SchoolNid(Nid):
#     def __init__(self,db_path):
#         super(SchoolNid,self).__init__('school',db_path)
#
#
# class TeacherNid(Nid):
#     def __init__(self,db_path):
#         super(TeacherNid,self).__init__('teacher',db_path)
#
# class StudentNid(Nid):
#     def __init__(self,db_path):
#         super(StudentNid,self).__init__('student',db_path)
#
# class CourseNid(Nid):
#     def __init__(self,db_path):
#         super(CourseNid,self).__init__('course',db_path)
#
# class ClassesNid(Nid):
#     def __init__(self,db_path):
#         super(ClassesNid,self).__init__('classes',db_path)
#
# class Course_to_teacherNid(Nid):
#     def __init__(self,db_path):
#         super(Course_to_teacherNid,self).__init__('course_to_teacher',db_path)