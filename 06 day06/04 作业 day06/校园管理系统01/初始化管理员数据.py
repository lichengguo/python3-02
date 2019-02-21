#!/usr/bin/env python3
#author:Alnk(李成果)
import json

def write():
    admin_dict = {
        'username':'admin',
        'passwd':'123',
        'role':'0',  # 0：管理员用户   1：学生用户
    }

    with open('db_info/admin', encoding='utf-8', mode='w') as f:
        json.dump(admin_dict,f)

if __name__ == '__main__':
    write()

stu_dict = {
    'alnk':{'passwod'},
    'tom':{},

}