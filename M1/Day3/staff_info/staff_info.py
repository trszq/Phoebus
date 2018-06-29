# Author: Zhang Qing

import os
import re

NAME=0
AGE=1
PHONE=2
DEPT=3
ENROLL_DATE=4

with open("staff_info.txt","r") as f_info:
    staff_info={}
    MAX_ID=0
    for info_item in f_info.readlines():
        info_item = info_item.strip().split(",")
        if int(info_item[0]) > MAX_ID:
            MAX_ID=int(info_item[0])
        staff_info[info_item[0]]=info_item[1:6]

def chk_phone_num(num):
    for id in staff_info:
        if staff_info[id][PHONE]==num:
            return False
    return True

def _select(request):
    input(request)

def _update(request):
    input(request)

def _insert(request):
    global staff_info
    global MAX_ID
    _cmd_=re.split('()',request)
    if _cmd_[0].lower()!="insert into staff_table values ":
        input("\033[5;31mSyntax of insert error!\033[0m\n(Press any key to continue...)")
    else:
        values=_cmd_[1].split(",")
        values=list(map(lambda x:x.strip("\""),values))
        if chk_phone_num(values[PHONE]):
            MAX_ID+=1
            staff_info[str(MAX_ID)]=values
        else:
            input("There is a duplicate phone number.")


def _delete(request):
    input(request)

while True:
    os.system('cls')
    print('''
    Usage:
    1. To query staff information: 
    select name,age from staff_table where age > 22
    select  * from staff_table where dept = "IT"
	select  * from staff_table where enroll_date like "2013"
	2. To add staff information:
	INSERT INTO staff_table VALUES (Alex Li,22,13651054608,IT,2013-04-01)
	3. To update staff information:
	UPDATE staff_table SET dept="Market" where dept = "IT"
	4. To delete staff information:
	DELETE FROM Person WHERE NAME = 'Wilson'
	or just enter staff id
	5. Enter 'q' or 'exit' to quit
    ''')
    _cmd=input("Please input your request:")
    if _cmd == 'q' or _cmd == 'exit':
        break
    elif _cmd.isdigit():
        if _cmd in staff_info:
            confirm=input("Are you sure to delete staff "+staff_info[_cmd][NAME]+"?(Y/N)")
            if confirm.upper() == "Y":
                del staff_info[_cmd]
        else:
            input("Staff id ",_cmd,"is not found")
        continue
    cmd=_cmd.split()
    if cmd[0].upper() not in ["SELECT","UPDATE","INSERT","DELETE"]:
        input("\033[5;31mPlease choose the correct mothods: SELECT,UPDATE,INSERT,DELETE\033[0m\n(Press any key to continue...)")
    elif cmd[0].upper()=="SELECT":
        _select(cmd)
    elif cmd[0].upper()=="UPDATE":
        _update(cmd)
    elif cmd[0].upper()=="INSERT":
        _insert(_cmd)
    elif cmd[0].upper()=="DELETE":
        _delete(cmd)



with open("staff_info.txt","w") as fw_info:
    for line in staff_info:
        new_line=line+","+",".join(staff_info[line])+"\n"
        fw_info.write(new_line)

