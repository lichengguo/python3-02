#!/usr/bin/env python3
#author:Alnk(李成果)
import json
import hashlib

def md5_pwd(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode())
    return md5.hexdigest()

def create(name ,pwd):
    with open('user_info.json', 'r') as f:
        user_info = json.load(f)

    pwd_md5 = md5_pwd('%s' % pwd)
    user_info[name] = pwd_md5

    with open('user_info.json', 'w') as f:
        json.dump(user_info,f)


# if __name__ == '__main__':
    # create('tom', '789')

# alnk|123
# alex|456
# tom|789
dic = {"alnk": {'pwd':"202cb962ac59075b964b07152d234b70", 'quota':83886080}, # 单位字节 10M
       "alex": {'pwd':"250cf8b51c773f3f8dc8b4be867a9a02", 'quota':83886080},
       "tom": {'pwd':"68053af2923e00204c3ca7c6a3150cf7", 'quota':83886080},
       }

with open('user_info.json', 'w') as f:
    json.dump(dic, f)