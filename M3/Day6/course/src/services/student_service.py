#!_*_coding:utf-8_*_
# Author: Zhang Qing
from src.models import Student
from src.models import School
from src.models import Classes

#注册学生信息，报名班级
def register():
    try:
        username=input("请输入学生登录账户：")
        student_list = [obj.username for obj in Student.get_all_obj_list()]
        if username in student_list:
            raise Exception('\033[31;1m学生登录账户[%s] 已经存在,不可重复创建\033[0m' %username)
        password=input("请输入学生登录密码：")
        name=input("请输入学生姓名：").strip()
        age=input("请输入学生年龄：").strip()
        mobile=input("请输入学生手机号码：").strip()

        school_list=School.get_all_obj_list()
        for k,obj in enumerate(school_list):
            print(k, obj, obj.addr)
        sid = int(input('请选择学校: '))
        school_obj = school_list[sid]

        class_list = Classes.get_all_obj_list()
        class_list_s = []
        k=0
        for obj in class_list:
            if obj.school_nid.uuid == school_obj.nid.uuid:
                print(k,obj)
                class_list_s.append(obj)
                k+=1
        if k==0:
            raise Exception('\033[31;1m该学校尚未有开课班级\033[0m')
        else:
            cid=int(input("请选择班级："))
        class_obj=class_list_s[cid]

        obj=Student(username,password,name,age,mobile,school_obj.nid,class_obj.nid)
        obj.save()
        status=True
        error=''
        data='\033[33;1m学生姓名[%s] 年龄[%s] 手机[%s] 学校[%s] 班级[%s]创建成功\033[0m' %(obj.name,obj.age,obj.mobile,school_obj,class_obj)
        student_obj=obj
    except Exception as e:
        status=False
        error=str(e)
        data=''
        student_obj=None
    return {'status':status,'error':error,'data':data,'student':student_obj}

#查看个人成绩
def score(student_obj):
    if student_obj.score:
        print('班级[%s] 课程[%s] 任课老师[%s] 分数[%s]'
              %(student_obj.classes_nid.get_obj_by_uuid(),student_obj.classes_nid.get_obj_by_uuid().course_to_teacher_list.course_nid.get_obj_by_uuid(),
                student_obj.classes_nid.get_obj_by_uuid().course_to_teacher_list.teacher_nid.get_obj_by_uuid(),student_obj.score))
    else:
        print('任课老师还未给你打分')

#交学费
def pay_tuition(student_obj):
    try:
        choice=input('是否要缴纳课程[%s]学费[%s]?(y/n)'
                     %(student_obj.classes_nid.get_obj_by_uuid().course_to_teacher_list.course_nid.get_obj_by_uuid(),
                       student_obj.classes_nid.get_obj_by_uuid().course_to_teacher_list.course_nid.get_obj_by_uuid().price)).strip()
        if choice == 'y':
            # student_obj.school_nid.get_obj_by_uuid().__income += int(student_obj.classes_nid.get_obj_by_uuid().course_to_teacher_list.course_nid.get_obj_by_uuid().price)
            # student_obj.school_nid.get_obj_by_uuid().save()
            print('缴纳学费...')
        else:
            raise Exception('未缴纳学费')
        status = True
        error = ''
        data = '\033[33;1m学费缴纳成功\033[0m'
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_menu(student_obj):
    menu='''
        0.查看本菜单
        1.查看分数
        2.缴费
        3.退出
    '''
    print(menu)

def main(student_obj):
    choice_dict = {
        '0': show_menu,
        '1': score,
        '2': pay_tuition,
        '3': exit
    }
    show_menu(student_obj)
    while True:
        choice = input(">>: ").strip()
        if choice not in choice_dict:
            print("请输入正确选项")
            continue
        if choice == '3':
            return
        else:
            ret = choice_dict[choice](student_obj)  # 执行动作
            if ret:
                if ret['status']:
                    print(ret['data'])
                else:
                    print(ret['error'])

def login():
    menu='''
        1.注册
        2.登录
        3.退出
    '''
    choice_dict = {
        '1': register,
        '2': Student.login,
        '3': exit
    }
    while True:
        print(menu)
        choice = input(">>: ").strip()
        if choice not in choice_dict:
            print("请输入正确选项")
        elif choice == '3':
            break
        else:
            ret = choice_dict[choice]()
            if ret:
                if ret['status']:
                    print(ret['data'])
                    main(ret['student'])
                else:
                    print(ret['error'])