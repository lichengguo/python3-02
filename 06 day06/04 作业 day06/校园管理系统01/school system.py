#!/usr/bin/env python3
# author:Alnk(李成果)

import os
import sys
import json


class Basic:
    '''基础类'''

    def read(self, file,):   # 读取所有课程或所有学生
        kecheng_lis = []
        if os.path.isfile('db_info/%s' % file):
            with open('db_info/%s' % file, encoding='utf-8', mode='r') as f:
                for i in f:
                    kecheng_lis.append(i.strip('\n'))
                return kecheng_lis
        else:
            return []

    def write(self, name, file):  # 创建课程列表或者学生列表
        with open('db_info/%s' % file, encoding='utf-8', mode='a+') as f:
            f.write('%s\n' % name)
            return True

    def write_dic(self,stu_name, stu_dict):  # 把学生详细信息字典写入到文件
        with open('db_info/%s' % stu_name, encoding='utf-8', mode='w') as f:
            json.dump(stu_dict,f)

    def read_dic(self, stu_name):  # 读取学生详细信息
        if  os.path.isfile('db_info/%s' % stu_name):
            with open('db_info/%s' % stu_name, encoding='utf-8', mode='r') as f:
                stu_dic = json.load(f)
            return stu_dic
        else:
            return False

    def see_all_kecheng(self):  # 查看所有课程
        kecheng_lis = self.read('kecheng_list')
        print('\n所有课程:%s' % kecheng_lis)

    def login_out(self):  # 退出
        sys.exit('退出!')


class Student(Basic):
    '''学生类'''

    def xuanke(self):  # 选择课程
        kecheng_list = self.read('kecheng_list')  # 课程列表
        print('\n课程列表:%s' % kecheng_list)
        hava_select = self.read_dic(user_name)['course']  # 已选课程
        print('\n已选课程:%s' % hava_select)
        for i in hava_select:  # 不可重复添加相同的课程
            if i in kecheng_list:
                kecheng_list.remove(i)
        print('\n可选课程:%s' % kecheng_list)
        if len(kecheng_list) == 0:
            print('\n所有课程都已经添加过了哦，暂时没有课程啦!')
            return
        choice = input('\n请输入你想选择的课程>>>:').strip()
        if choice in kecheng_list:  # 选课
            stu_dic = self.read_dic(user_name)
            stu_dic['course'].append(choice)
            self.write_dic(user_name, stu_dic)
            print('\n[%s]课程选择成功!' % choice)
        elif choice in hava_select:  # 已经选取的课程
            print('\n[%s]课程已经添加过了，不可重复添加' % choice)
        else:
            print('\n[%s]该课程不存在!' % choice)

    def see_all_xuanke(self):  # 查看所选课程
        stu_dic = self.read_dic(user_name)
        print('\n[%s]所选的课程有:%s' % (user_name, stu_dic['course']))


class Admin(Basic):
    '''管理类'''

    def create_kecheng(self):  # 创建课程
        kecheng = input('\n请输入你要创建的课程>>>:')
        all_kecheng_lis = self.read('kecheng_list')
        if kecheng in all_kecheng_lis:  # 不可重复创建课程
            print('\n课程[%s]已经创建过了，不可重复创建哟' % kecheng)
        else:
            self.write(kecheng,'kecheng_list')
            print('\n[%s]课程创建成功!' % kecheng)

    def create_stu(self): # 创建学生
        stu_name = input('\n学生账号>>>:')
        stu_pwd = input('密码>>>:')
        all_stu_dic = self.read('student_list')
        if stu_name in all_stu_dic:
            print('\n学生账号[%s]已经被注册了!' % stu_name)
        else:
            stu_dict = {'name':stu_name, 'passwd':stu_pwd, 'role':'1', 'course':[],}
            self.write_dic(stu_name, stu_dict)  # 学生个人信息写入单独文件
            self.write(stu_name, 'student_list')  # 统计所有学生姓名
            print('\n学生账号[%s]创建成功\n' % stu_name)

    def see_all_stu(self):  # 查看所有学生
        all_stu_dic = self.read('student_list')
        print('\n所有学生:%s' % all_stu_dic)

    def see_stu_xuanke(self):  # 查看所有学生选课情况
        student_lis = self.read('student_list')
        if student_lis:
            for stu_name in student_lis:
                stu_dic = self.read_dic(stu_name)
                print('\n学生[%s]的选课情况: %s' % (stu_name,stu_dic['course']))
        else:
            print('\n还没有学生哟!')


class View:
    '''视图类'''

    def student_user(self): # 学生视图
        msg = '''------- 欢迎来到学生界面 -------
        1、查看所有课程
        2、选择课程
        3、查看所选课程
        4、退出程序      
        '''
        dic = {
            '1':Student().see_all_kecheng,
            '2':Student().xuanke,
            '3':Student().see_all_xuanke,
            '4':Student().login_out,
        }
        while 1:
            print('\n%s' % msg)
            choice = input('请输入编号>>:')
            if dic.get(choice):
                dic[choice]()
            else:
                print('请输入正确的编号\n')

    def admin_user(self):  # 管理员视图
        msg = '''------- 欢迎来到管理员界面 -------
        1、创建课程
        2、创建学生账号
        3、查看所有课程
        4、查看所有学生
        5、查看所有学生的选课情况
        6、退出程序
        '''
        dic = {
            '1':Admin().create_kecheng,
            '2':Admin().create_stu,
            '3':Admin().see_all_kecheng,
            '4':Admin().see_all_stu,
            '5':Admin().see_stu_xuanke,
            '6':Admin().login_out,
        }
        while 1:
            print('\n%s' % msg)
            choice = input('请输入编号>>:')
            if dic.get(choice):
                dic[choice]()
            else:
                print('请输入正确的编号\n')


class Login(View, Basic):
    '''登录类'''

    def __init__(self, user_name, user_pwd):
        self.name = user_name
        self.passwd = user_pwd

    def login(self):
        user_dict = self.read_dic(self.name)  # 获取以账号名返回的字典
        if user_dict:
            if user_dict['passwd'] == self.passwd:  # 判断密码
                if user_dict['role'] == '0':  # 管理员角色
                    self.admin_user()  # 调用视图
                elif user_dict['role'] == '1':  # 学生角色
                    self.student_user()
            else:
                print('账号或密码有误啊!\n')
        else:
            print('账号或密码有误!\n')


if __name__ == '__main__':
    user_name = input('请输入登录账号>>>:')
    user_pwd = input('请输入密码>>>:')
    l = Login(user_name, user_pwd)
    l.login()
