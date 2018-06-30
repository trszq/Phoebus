# Author: Zhang Qing

import os
import re

NAME=0
AGE=1
PHONE=2
DEPT=3
ENROLL_DATE=4
ATTR=["NAME","AGE","PHONE","DEPT","ENROLL_DATE"]
SYMBOLS=["=",">","<",">=","<=","!=","<>","like"]

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

def _query(que):
    IDS=[]
    symbol=que[1].lower()
    if symbol not in SYMBOLS:
        print("\033[5;31mInvalid comparison symbol!\033[0m")
        return IDS
    if que[0].upper() not in ATTR:
        print("Could not find the attribute",que[0].upper())
        return IDS
    else:
        _attr=eval(que[0].upper())
        for id in staff_info:
            if symbol == '=' and staff_info[id][_attr] == " ".join(que[2:]).strip("\"\'"):
                IDS.append(id)
            elif symbol == '>' and int(staff_info[id][_attr]) > int(" ".join(que[2:]).strip("\"\'")):
                IDS.append(id)
            elif symbol == '<' and int(staff_info[id][_attr]) <= int(" ".join(que[2:]).strip("\"\'")):
                IDS.append(id)
            elif symbol == '>=' and int(staff_info[id][_attr]) >= int(" ".join(que[2:]).strip("\"\'")):
                IDS.append(id)
            elif symbol == '<=' and int(staff_info[id][_attr]) <= int(" ".join(que[2:]).strip("\"\'")):
                IDS.append(id)
            elif (symbol == '<>' or symbol == '!=') and staff_info[id][_attr] != " ".join(que[2:]).strip("\"\'"):
                IDS.append(id)
            elif symbol == 'like' and " ".join(que[2:]).strip("\"\'") in staff_info[id][_attr]:
                IDS.append(id)
            # elif eval(staff_info[id][_attr]+symbol+" ".join(que[2:]).strip("\"\'")):
            #     IDS.append(id)
        return IDS

def _select(_request): #string
    global staff_info
    request=_request.split()
    opt_req = " ".join(_request.lower().split())
    if not re.match("select .* from staff_table where .*", opt_req):
        input("\033[5;31mInvalid Syntax of select!!\033[0m\n(Press any key to continue...)")
        return
    if request[1] == '*':
        attrs=ATTR
    else:
        attrs=request[1].upper().split(",")
    for attr in attrs:
        if attr not in ATTR:
            print("Could not find the attribute", attr)
            input("(Press any key to continue...)")
            return
    id_to_sel = _query(request[5:])
    for id in id_to_sel:
        print(",".join(list(map(lambda x:staff_info[id][eval(x)],attrs))))
    print("Found",len(id_to_sel),"record(s)")
    input("(Press any key to continue...)")




def _update(_request): # string
    global staff_info
    request = _request.split()
    _attr = eval(request[3].upper())
    value=request[5].strip("\"\'")

    if " ".join(request[:3]).lower() != "update staff_table set" or \
    request[4] != '=' or request[6].lower() != "where":
        input("\033[5;31mInvalid Syntax of update!!\033[0m\n(Press any key to continue...)")
        return
    if request[3].upper() not in ATTR:
        print("Could not find the attribute",request[3].upper())
        input("(Press any key to continue...)")
        return
    if _attr == PHONE and not chk_phone_num(value):
        input("There is a duplicate phone number.\n(Press any key to continue...)")
        return
    id_to_upt = _query(request[7:])
    for id in id_to_upt:
        staff_info[id][_attr]=value
    print("Affected",len(id_to_upt),"record(s)")
    input("(Press any key to continue...)")


def _insert(request): # string
    global staff_info
    global MAX_ID
    _cmd_=re.split('[()]',request)
    if " ".join(_cmd_[0].lower().split()) != "insert into staff_table values":
        input("\033[5;31mInvalid Syntax of insert!!\033[0m\n(Press any key to continue...)")
    else:
        values=_cmd_[1].split(",")
        values=list(map(lambda x:x.strip("\"\'"),values))
        if chk_phone_num(values[PHONE]):
            MAX_ID+=1
            staff_info[str(MAX_ID)]=values
            input("Staff information is recorded.\n(Press any key to continue...)")
        else:
            input("There is a duplicate phone number.\n(Press any key to continue...)")


def _delete(request):  # list
    global staff_info
    if " ".join(request[:4]).lower() != "delete from staff_table where":
        input("\033[5;31mInvalid Syntax of delete!!\033[0m\n(Press any key to continue...)")
        return
    id_to_del = _query(request[4:])
    for id in id_to_del:
        staff_to_del=staff_info[id][NAME]
        del staff_info[id]
        print(staff_to_del, "is deleted.")
    print("Affected",len(id_to_del),"record(s)")
    input("(Press any key to continue...)")


while True:
    os.system('cls')
    print('''
    Usage:
    1. To query staff information: 
    select name,age from staff_table where age > 22
    select * from staff_table where dept = "IT"
	select * from staff_table where enroll_date like "2013"
	2. To add staff information:
	INSERT INTO staff_table VALUES (Alex Li,22,13651054608,IT,2013-04-01)
	3. To update staff information:
	UPDATE staff_table SET dept = "Market" where dept = "IT"
	4. To delete staff information:
	DELETE FROM staff_table WHERE NAME = 'Alex Li'
	or just enter staff id
	5. Enter 'q' or 'exit' to quit
    ''')
    _cmd=input("Please input your request:")
    if _cmd == 'q' or _cmd == 'exit':
        break
    elif _cmd == '':
        continue
    elif _cmd.isdigit():
        if _cmd in staff_info:
            confirm=input("Are you sure to delete staff "+staff_info[_cmd][NAME]+"?(Y/N)")
            if confirm.upper() == "Y":
                del staff_info[_cmd]
        else:
            input("Staff id "+_cmd+" is not found")
        continue
    cmd=_cmd.split()
    if cmd[0].upper() not in ["SELECT","UPDATE","INSERT","DELETE"]:
        input("\033[5;31mPlease choose the correct mothods: SELECT,UPDATE,INSERT,DELETE\033[0m\n(Press any key to continue...)")
    elif cmd[0].upper()=="SELECT":
        _select(_cmd)
    elif cmd[0].upper()=="UPDATE":
        _update(_cmd)
    elif cmd[0].upper()=="INSERT":
        _insert(_cmd)
    elif cmd[0].upper()=="DELETE":
        _delete(cmd)


with open("staff_info.txt","w") as fw_info:
    for line in staff_info:
        new_line=line+","+",".join(staff_info[line])+"\n"
        fw_info.write(new_line)

