#!_*_coding:utf-8_*_
# Author: Zhang Qing
from src.models import Admin
from src.models import School
from src.models import Teacher
from src.models import Student
from src.models import Course
from src.models import Classes
from src.models import Course_to_teacher

def create_school():
    try:
        name=input("请输入学校名称：").strip()
        addr=input("请输入学校地址：").strip()
        school_list=[(obj.name,obj.addr) for obj in School.get_all_obj_list()]
        if (name,addr) in school_list:
            raise Exception('\033[31;1m[%s] [%s]校区 已经存在,不可重复创建\033[0m' %(name,addr))
        obj = School(name, addr)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m[%s] [%s]校区 创建成功\033[0m' % (obj.name, obj.addr)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_school():
    for obj in School.get_all_obj_list():
        print('\033[32;1m学校[%s] 地址[%s] 创建日期[%s]\033[0m'%(obj.name,obj.addr,obj.create_time))

def create_teacher():
    try:
        username=input("请输入教师登录账户：")
        teacher_list = [obj.username for obj in Teacher.get_all_obj_list()]
        if username in teacher_list:
            raise Exception('\033[31;1m教师登录账户[%s] 已经存在,不可重复创建\033[0m' %username)
        password=input("请输入教师登录密码：")
        name=input("请输入教师姓名：").strip()
        level=input("请输入教师级别：").strip()

        school_list=School.get_all_obj_list()
        for k,obj in enumerate(school_list):
            print(k, obj, obj.addr)
        sid = int(input('请选择学校: '))
        school_obj = school_list[sid]

        obj=Teacher(username,password,name,level,school_obj.nid)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m教师 %s [%s]创建成功\033[0m' % (obj.name, obj.username)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}

def show_teacher():
    for obj in Teacher.get_all_obj_list():
        print('\033[32;1m教师姓名[%s] 级别[%s] 学校[%s] [%s]校区 创建日期[%s]\033[0m'
              %(obj.name,obj.level,obj.school_nid.get_obj_by_uuid().name,obj.school_nid.get_obj_by_uuid().addr,obj.create_time))

def create_student():
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
    except Exception as e:
        status=False
        error=str(e)
        data=''
    return {'status':status,'error':error,'data':data}

def show_student():
    for obj in Student.get_all_obj_list():
        print('\033[32;1m学生姓名[%s] 年龄[%s] 手机[%s] 学校[%s] 班级[%s] 任课老师[%s] 创建日期[%s]\033[0m'
              % (obj.name,obj.age,obj.mobile,obj.school_nid.get_obj_by_uuid(),obj.classes_nid.get_obj_by_uuid(),
                obj.classes_nid.get_obj_by_uuid().course_to_teacher_list.teacher_nid.get_obj_by_uuid(),obj.create_time))

def create_course():
    try:
        print('创建课程'.center(60,'='))
        school_list=School.get_all_obj_list()
        for k,obj in enumerate(school_list):
            print(k,obj,obj.addr)
        sid=int(input('请选择学校: '))
        school_obj=school_list[sid]

        name=input('请输入课程名: ').strip()
        course_name_list=[(obj.name,obj.school_nid.uuid) for obj in Course.get_all_obj_list()]
        if (name,school_obj.nid.uuid) in course_name_list:
            raise Exception('\033[31;1m课程[%s] ([%s] [%s]校区) 已经存在,不可重复创建\033[0m' %(name,school_obj.name,school_obj.addr))

        price=input('请输入课程价格: ').strip()
        period=input('请输入课程周期: ').strip()
        obj=Course(name,price,period,school_obj.nid)
        obj.save()
        status=True
        error=''
        data='\033[33;1m课程[%s] 价格[%s] 周期[%s]创建成功\033[0m' %(obj.name,obj.price,obj.period)
    except Exception as e:
        status=False
        error=str(e)
        data=''
    return {'status':status,'error':error,'data':data}


def show_course():
    for obj in Course.get_all_obj_list():
        print('\033[33;1m[%s] [%s]校区 [%s]课程 价格[%s] 周期[%s]\033[0m'
              %(obj.school_nid.get_obj_by_uuid().name,obj.school_nid.get_obj_by_uuid().addr,
                obj.name,obj.price,obj.period))

def create_classes():
    try:
        print('创建班级'.center(60,'='))
        name=input('请输入班级名称: ').strip()

        school_list=School.get_all_obj_list()
        for k,obj in enumerate(school_list):
            print(k,obj,obj.addr)
        sid=int(input('请选择学校: '))
        school_obj=school_list[sid]

        class_name_list=[(obj.name,obj.school_nid.uuid) for obj in Classes.get_all_obj_list()]
        if (name,school_obj.nid.uuid) in class_name_list:
            raise Exception('\033[31;1m班级[%s] (校区[%s])已经存在,不可重复创建\033[0m' %(name,school_obj))

        course_to_teacher_all_list=Course_to_teacher.get_all_obj_list()
        course_to_teacher_selection=[]
        k=0
        for obj in course_to_teacher_all_list:
            if obj.school_nid.uuid == school_obj.nid.uuid:
                print(k,obj.teacher_nid.get_obj_by_uuid(),obj.course_nid.get_obj_by_uuid(),'[%s] [%s]校区'
                        %(obj.school_nid.get_obj_by_uuid().name,obj.school_nid.get_obj_by_uuid().addr))
                course_to_teacher_selection.append(obj)
                k+=1
        if k == 0:
            raise Exception('\033[31;1m该学校尚未有适合的课程开设\033[0m')
        else:
            ctid=int(input("请选择教师和课程："))
        course_to_teacher_list=course_to_teacher_selection[ctid]

        obj=Classes(name,school_obj.nid,course_to_teacher_list)
        obj.save()
        status=True
        error=''
        data='\033[33;1m班级[%s] 校区[%s] 任课老师[%s] 课程[%s]创建成功\033[0m' \
             %(obj.name,obj.school_nid.get_obj_by_uuid(),obj.course_to_teacher_list.teacher_nid.get_obj_by_uuid(),
               obj.course_to_teacher_list.course_nid.get_obj_by_uuid())
    except Exception as e:
        status=False
        error=str(e)
        data=''
    return {'status':status,'error':error,'data':data}

def show_classes():
    for obj in Classes.get_all_obj_list():
        print('\033[33;1m班级[%s] 校区[%s] 任课老师[%s] 课程[%s]\033[0m'
              % (obj.name,obj.school_nid.get_obj_by_uuid(),obj.course_to_teacher_list.teacher_nid.get_obj_by_uuid(),obj.course_to_teacher_list.course_nid.get_obj_by_uuid()))

def create_course_to_teacher():
    try:
        print('关联教师与课程'.center(60,'='))

        course_list=Course.get_all_obj_list()
        for k,obj in enumerate(course_list):
            print(k,'课程[%s] ([%s] [%s]校区)'%(obj.name,obj.school_nid.get_obj_by_uuid().name,obj.school_nid.get_obj_by_uuid().addr))
        cid=int(input("请选择课程："))
        course_obj=course_list[cid]

        teacher_list=Teacher.get_all_obj_list()
        teacher_list_selection=[]
        k=0
        for obj in teacher_list:
            if obj.school_nid.uuid == course_obj.school_nid.uuid:
                print(k,obj.name,'[%s] [%s]校区'%(obj.school_nid.get_obj_by_uuid().name,obj.school_nid.get_obj_by_uuid().addr))
                teacher_list_selection.append(obj)
                k+=1
        if k == 0:
            raise Exception('\033[31;1m该学校还未有合适的教师\033[0m')
        else:
            tid=int(input("请选择教师："))
        teacher_obj=teacher_list_selection[tid]

        course_to_teacher_list = [(obj.course_nid.uuid,obj.teacher_nid.uuid) for obj in Course_to_teacher.get_all_obj_list()]
        if (course_obj.nid.uuid,teacher_obj.nid.uuid) in course_to_teacher_list:
            raise Exception('\033[31;1m教师[%s] 已与课程[%s]([%s] [%s]校区)关联,不可重复创建\033[0m'
                            %(teacher_obj.name,course_obj.name,course_obj.school_nid.get_obj_by_uuid().name,course_obj.school_nid.get_obj_by_uuid().addr))
        obj=Course_to_teacher(course_obj.nid,teacher_obj.nid)
        obj.save()
        status=True
        error=''
        data='\033[33;1m教师[%s] 与课程[%s]([%s] [%s]校区)关联 创建成功\033[0m' \
             % (teacher_obj.name, course_obj.name, course_obj.school_nid.get_obj_by_uuid().name,
                course_obj.school_nid.get_obj_by_uuid().addr)

    except Exception as e:
        status=False
        error=str(e)
        data=''
    return {'status':status,'error':error,'data':data}



def show_menu():
    menu='''
        0.查看本菜单
        1.创建学校
        2.查看学校
        3.创建教师
        4.查看教师
        5.创建学生
        6.查看学生
        7.创建课程
        8.查看课程
        9.创建班级
        10.查看班级
        11.关联教师与课程
        12.退出
    '''
    print(menu)

def main():
    choice_dict={
        '0':show_menu,
        '1':create_school,
        '2':show_school,
        '3':create_teacher,
        '4':show_teacher,
        '5':create_student,
        '6':show_student,
        '7':create_course,
        '8':show_course,
        '9':create_classes,
        '10':show_classes,
        '11':create_course_to_teacher,
        '12':exit
    }
    show_menu()
    while True:
        choice=input(">>: ").strip()
        if choice not in choice_dict:
            print("请输入正确选项")
            continue
        elif choice == '12':
            break
        ret=choice_dict[choice]()    # 执行动作
        if ret:
            if ret['status']:
                print(ret['data'])
            else:
                print(ret['error'])

def login():
    ret=Admin.login()
    if ret:
        if ret['status']:
            print(ret['data'])
            main()
        else:
            print(ret['error'])

if __name__ == '__main__':
    main()



