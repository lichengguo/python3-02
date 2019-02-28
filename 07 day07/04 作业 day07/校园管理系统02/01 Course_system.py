#!/usr/bin/env python3
# author:Alnk(李成果)
import sys
import os
import json


class Base:  # 基础类

    def __read_dic__(self, filename):  # 读取json格式的文件
        with open(filename, encoding='utf', mode='r') as f:
            info_dic = json.load(f)
            return info_dic

    def __wirte_dic__(self, filename, info_dic):  # 写入json类型文件
        with open(filename, encoding='utf', mode='w') as f:
            json.dump(info_dic, f)
        return True

    def __read_file__(self, filename):  # 读取普通文件
        file_list = []
        with open(filename, encoding='utf', mode='r') as f:
            for line in f:
                file_list.append(line.strip())
        return file_list

    def __write_file__(self, filename, info):  # 写入普通文件
        with open(filename, encoding='utf', mode='a') as f:
            f.write('%s\n' % info)
        return True


class Parent(Base):  # 父类
    def show_courses(self):  # 查看所有课程
        courses_list = self.__read_file__('course_list')
        print('\n所有课程:%s' % courses_list)
        return courses_list

    def exit(self):  # 退出
        exit()


class Student(Parent):  # 学生类
    option_lis = [('show_courses', '查看所有课程'),
                  ('select_course', '选择课程'),
                  ('check_selected_course', '查看已选课程'),
                  ('exit', '退出'),
                  ]

    def __init__(self, name):
        self.name = name

    def select_course(self):  # 选择课程
        course_list = self.show_courses()  # 查看所有课程
        select_course = input('输入课程名称>>')
        if select_course in course_list:
            stu_dic = self.__read_dic__(self.name)  # 读取学生个人详细信息
            stu_dic["select_course"].append(select_course)
            self.__wirte_dic__(self.name, stu_dic)  # 写入学生个人信息
        else:
            print('课程不存在')

    def check_selected_course(self):  # 查看已选课程
        stu_dic = self.__read_dic__(self.name)  # 读取学生个人信息
        print('已选课程：', stu_dic["select_course"])


class Manage(Parent):  # 管理员类
    option_lis = [('create_course', '创建课程'),
                  ('create_stu', '创建学生'),
                  ('show_courses', '查看所有课程'),
                  ('show_students', '查看所有学生'),
                  ('show_students_courses', '查看所有学生的选课情况'),
                  ('create_teacher', '创建讲师'),
                  ('create_class', '创建班级'),
                  ('appoint_tearcher_class', '为讲师指定班级'),
                  ('appoint_stu_class', '为学生指定班级'),
                  ('exit', '退出'),
                  ]

    def __init__(self, name):
        self.name = name

    def create_course(self):  # 创建课程
        course_name = input('课程名称>>>').strip()
        self.__write_file__('course_list', course_name)  # 写入课程文件
        print('\n%s课程创建成功\n' % course_name)

    def create_stu(self):  # 创建学生
        stu_name = input('学生账号>>>')
        stu_pwd = input('密码>>>')
        stu_info_dic = {'username': stu_name, 'passwd': stu_pwd, 'id': 'Student', 'select_course': [], 'class': []}
        self.__wirte_dic__(stu_name, stu_info_dic)  # 写入学生详细信息
        self.__write_file__('students_list', stu_name)  # 学生总列表
        print('\n学生%s创建成功\n' % stu_name)

    def show_students(self):  # 查看所有学生
        students_list = self.__read_file__('students_list')  # 读取学生总列表文件
        print('\n所有的学生:%s' % students_list)

    def show_students_courses(self):  # 查看所有学生的选课情况
        stu_lis = self.__read_file__('students_list')  # 读取学生总列表文件
        for i in stu_lis:
            stu_dic = self.__read_dic__(i)  # 学生个人详细信息
            print('%s 选课情况：%s' % (i, stu_dic['select_course']))

    def create_teacher(self):  # 创建讲师
        t_name = input('讲师账号>>>')
        t_pwd = input('密码>>>')
        t_dic = {"username": t_name, "passwd": t_pwd, "id": "Teacher", "class": []}
        self.__wirte_dic__(t_name, t_dic)  # 写入老师详细信息
        self.__write_file__('teacher_list', t_name)  # 写入老师总文件
        print('讲师 %s 创建成功' % t_name)

    def appoint_tearcher_class(self):  # 为讲师指定班级
        teacher_list = self.__read_file__('teacher_list')  # 读取老师总文件
        class_list = self.__read_file__('class_list')  # 读取班级总文件
        print('所有老师:%s' % teacher_list)
        t_name = input('讲师名称>>>').strip()
        print('所有班级:%s' % class_list)
        c_name = input('班级名称>>>').strip()
        if t_name in teacher_list and c_name in class_list:
            teacher_dic = self.__read_dic__(t_name)  # 读取老师个人信息
            teacher_dic['class'].append(c_name)
            self.__wirte_dic__(t_name, teacher_dic)  # 写入老师个人信息
            print('已为讲师 %s 指定班级 %s' % (t_name, c_name))
        else:
            print('讲师或班级不存在')

    def create_class(self):  # 创建班级
        class_name = input('创建班级名称:')
        self.__write_file__('class_list', class_name)  # 写入班级总文件
        print('%s 班级创建成功' % class_name)

    def appoint_stu_class(self):  # 为学生指定班级
        stu_list = self.__read_file__('students_list')  # 读取学生总列表文件
        class_list = self.__read_file__('class_list')  # 读取班级总文件
        print('所有学生:%s' % stu_list)
        stu_name = input('学生名称>>>')
        print('所有班级:%s' % class_list)
        class_name = input('班级名称>>>')
        if stu_name in stu_list and class_name in class_list:
            self.__write_file__(class_name, stu_name)  # 写入班级文件
            stu_dic = self.__read_dic__(stu_name)  # 读取学生信息
            stu_dic['class'].append(class_name)
            self.__wirte_dic__(stu_name, stu_dic)
            print('为学生 %s 指定班级 %s 成功' % (stu_name, class_name))
        else:
            print('班级或学生不存在')


class Teacher(Parent):  # 讲师类
    option_lis = [('show_courses', '查看所有课程'),
                  ('show_class', '查看所教班级'),
                  ('show_class_students', '查看班级中的学生'),
                  ('exit', '退出'),
                  ]

    def __init__(self, name):
        self.name = name

    def show_class(self):  # 查看所教班级
        tearcher_dic = self.__read_dic__(self.name)
        print('所教班级%s' % tearcher_dic['class'])

    def show_class_students(self):  # 查看班级中的学生
        tearcher_dic = self.__read_dic__(self.name)
        print('%s 班级中的学生:' % tearcher_dic['class'])
        for i in tearcher_dic['class']:
            stu_list = self.__read_file__(i)
            print(stu_list)


def login():  # 登录函数
    name = input('username>>>')
    pwd = input('password>>>')
    if os.path.isfile(name):
        with open(name, encoding='utf-8', mode='r') as f:
            user_dic = json.load(f)
        if user_dic['passwd'] == pwd:
            return {'result': True, 'name': name, 'id': user_dic['id']}
        else:
            return {'result': False, 'name': name, }
    else:
        return {'result': False, 'name': name, }


def main():
    ret = login()
    if ret['result']:
        print('登录成功')
        if hasattr(sys.modules[__name__], ret['id']):
            cls = getattr(sys.modules[__name__], ret['id'])  # 类
            obj = cls(ret['name'])  # 实例化
            while 1:
                print('\n')
                for k, i in enumerate(cls.option_lis, 1):
                    print(k, i[1])
                func_str = cls.option_lis[int(input('>>>:')) - 1][0]
                if hasattr(obj, func_str):
                    getattr(obj, func_str)()
    else:
        print('登录失败')


if __name__ == '__main__':
    main()