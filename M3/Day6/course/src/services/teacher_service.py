#!_*_coding:utf-8_*_
# Author: Zhang Qing

from src.models import Teacher
from src.models import Classes
from src.models import Student

#查看班级信息
def class_info(teacher_obj):
    try:
        class_list=Classes.get_all_obj_list()
        k=0
        for obj in class_list:
            if obj.course_to_teacher_list.teacher_nid.uuid == teacher_obj.nid.uuid:
                print('\033[33;1m班级[%s] 学校[%s] [%s]校区 课程[%s]\033[0m'
                      %(obj.name,obj.school_nid.get_obj_by_uuid().name,obj.school_nid.get_obj_by_uuid().addr,obj.course_to_teacher_list.course_nid.get_obj_by_uuid().name))
                k+=1
        status=True
        error=''
        data='\033[33;1m共有%s个班级\033[0m'%(str(k))
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

#查看学生信息
def student_info(teacher_obj):
    try:
        student_list=Student.get_all_obj_list()
        k=0
        for obj in student_list:
            if obj.classes_nid.get_obj_by_uuid().course_to_teacher_list.teacher_nid.uuid == teacher_obj.nid.uuid:
                print('\033[33;1m班级[%s] 学校[%s] [%s]校区 课程[%s]\033[0m'
                      %(obj.name,obj.school_nid.get_obj_by_uuid().name,obj.school_nid.get_obj_by_uuid().addr,obj.course_to_teacher_list.course_nid.get_obj_by_uuid().name))
                k+=1
        status=True
        error=''
        data='\033[33;1m共有%s个班级\033[0m'%(str(k))
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

#给学生打分
def set_student_score(teacher_obj):
    pass

def show_menu():
    menu='''
        0.查看本菜单
        1.查看班级信息
        2.查看学生信息
        3.学生成绩录入
        4.退出
    '''
    print(menu)

def main(teacher_obj):
    choice_dict = {
        '0': show_menu,
        '1': class_info,
        '2': student_info,
        '3': set_student_score,
        '4': exit
    }
    show_menu()
    while True:
        choice = input(">>: ").strip()
        if choice not in choice_dict:
            print("请输入正确选项")
            continue
        if choice == '4':
            exit()
        else:
            ret = choice_dict[choice](teacher_obj)  # 执行动作
            if ret:
                if ret['status']:
                    print(ret['data'])
                else:
                    print(ret['error'])


def login():
    ret = Teacher.login()
    if ret:
        if ret['status']:
            print(ret['data'])
            main(ret['teacher'])
        else:
            print(ret['error'])



