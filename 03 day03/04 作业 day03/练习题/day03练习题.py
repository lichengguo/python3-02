#!/usr/bin/env python3
#author:Alnk(李成果)
'''
# 1、 文件a1.txt内容
# 序号 部门 人数 平均年龄 备注
# 1 python 30 26 单身狗
# 2 Linux 26 30 没对象
# 3 运营部 20 24 女生多
# 通过代码，将其构建成这种数据类型：
# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},......]

l1 = []
with open('a1.txt',encoding='utf-8',mode='r') as f:
    k1,k2,k3,k4,k5 = f.readline().strip('').split()
    for line in f:
        dic = {}
        v1,v2,v3,v4,v5 = line.strip('').split()
        dic[k1] = v1
        dic[k2] = v2
        dic[k3] = v3
        dic[k4] = v4
        dic[k5] = v5
        l1.append(dic)
print(l1)
'''


'''
# 2、 传入函数的字符串中,统计[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。

def my_count(str1):
    """
    统计数字，字母，空格，其他的字符个数
    :param str1: 字符串
    :return: 数字，字母，空格，其他 
    """
    count_num = 0
    count_letter = 0
    count_space = 0
    count_other = 0
    for i in str1:
        if i.isdigit():
            count_num += 1
        elif i.isalpha():
            count_letter += 1
        elif i == ' ':
            count_space += 1
        else:
            count_other += 1
    return '数字[%s] 字母[%s] 空格[%s] 其他[%s]' % (count_num,count_letter,count_space,count_other)
print(my_count('1 b # 3s'))
'''


'''
# 3、 写函数，接收两个数字参数，返回比较大的那个数字

def my_compare(*args):
    """
    比较两个数大小
    :param args:传入2个数字
    :return: 大的数字
    """
    return args[0] if args[0] > args [1] else args[1]
print(my_compare(3,62))
'''


'''
# 4、 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}   PS:字典中的value只能是字符串或列表

def func(**kwargs):
    """
    检查字典值的长度，大于2，保留前两个长度的内容
    :param kwargs: 字典
    :return: 新列表
    """
    for k,v in kwargs.items():
        kwargs[k] = v[:2] if len(v) > 2 else v
    return kwargs
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
ret = func(**dic)
print(ret)
'''


'''
# 5、 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一
# 个字典，此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为
# {0:11,1:22,2:33}

def fun(lis):
    """
    接受列表数据类型，返回字典
    :param args: 列表
    :return: 字典
    """
    if type(lis) is list:
        dic = {}
        for k in range(len(lis)):
            dic[k] = lis[k]
        return dic
    else:
        return '参数必须为列表'

l1 = [11,22,33,]
print(fun(l1))
'''


'''
# 6、 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这
# 四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中

def func(name,sex,age,edu):
    """
    接收四个参数，将接收的内容追加到student_msg文件中
    :param name: 姓名
    :param sex: 性别
    :param age: 年龄
    :param edu: 学历
    :return:
    """
    with open('student_msg',encoding='utf-8',mode='a+') as f:
        f.write('%s %s %s %s \n' % (name,sex,age,edu) )
        f.flush()
name = input('name>>>:')
sex = input('sex>>>:')
age = input('age>>>:')
edu = input('edu>>>:')
func(name,sex,age,edu)
'''


'''
# 7、 对第6题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入
# 女。

def func(name,age,edu,sex='男'):
    """
    接收四个参数，将接收的内容追加到student_msg文件中
    :param name: 姓名
    :param sex: 性别
    :param age: 年龄
    :param edu: 学历
    :return:
    """
    with open('student_msg',encoding='utf-8',mode='a+') as f:
        f.write('%s %s %s %s \n' % (name,sex,age,edu) )
        f.flush()

while 1:
    name = input('name(Q/q exit)>>>:')
    if name.strip().lower() == 'q':
        break
    sex = input('sex>>>:')
    age = input('age>>>:')
    edu = input('edu>>>:')

    if sex.strip() == '男':
        func(name,age,edu)
    else:
        func(name,age,edu,sex)
'''


'''
# 8、 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作

import os
def modify_file(file_name,old_modify,new_modify):
    """
    文本修改
    :param file_name: 文件
    :param old_modify: 被修改的内容
    :param new_modify: 修改的内容
    :return: True
    """
    if os.path.exists(file_name):
        with open(file_name,encoding='utf-8',mode='r') as f1, open(file_name+'.bak',encoding='utf-8',mode='w') as f2:
            for old_line in f1:
                new_line = old_line.replace(old_modify,new_modify)
                f2.write(new_line)
                f2.flush()
        os.remove(file_name)
        os.rename(file_name+'.bak',file_name)
        return  True
    else:
        return '文件不存在'

file_name = input("请输入文件名称:")
old_modify = input("请输入需要修改的内容：")
new_modify = input("请输入修改后的内容：")
ret = modify_file(file_name,old_modify,new_modify)
print(ret)
'''


'''
# 9、 读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a=10
# b=20
# def test5(a,b):  #a=20 b=10
#     a=3
#     b=5
#     print(a,b)      #a=3 b=5
# c = test5(b,a) #a=3 b=5 因为在函数内部打印的，先从局部变量开始找
# print(c)  #none 函数没有return，所以没有返回值C=None。
'''


'''
# 10、 写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次
# 添加到函数的动态参数args里面
# 例如 传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)

def func(*args):
    """
    :param args:
    :return:
    """
    print(args)

l1 = [1,2,3,]
t1 = (22,33)
func(*l1,*t1)
'''


'''
# 11、 写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面
# 例如 传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}

def fun(**kwargs):
    """
    :param kwargs:
    :return:
    """
    print(kwargs)
dic1 = {'name':'alex'}
dic2 = {'age':1000}
fun(**dic1,**dic2)
'''


'''
# 12、 下面代码成立么?如果不成立为什么报错?怎么解决?
# 题目一：
# a = 2
# def wrapper():
#     print(a)
# wrapper()
# 
# 题目二：
# a = 2
# def wrapper():
#     a += 1
#     print(a)
# wrapper()
#     
# 题目三：
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     inner()
# wrapper()
#     
# 题目四：
# def wrapper():
#     a = 1
#     def inner():
#         a += 1
#         print(a)
#     inner()
# wrapper()

# 题目一   可以执行

# 题目二修改为如下
# a = 2
# def wrapper():
#     global a
#     a += 1
#     print(a)
# wrapper()

# 题目三 可以执行

# 题目四修改为如下
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a
#         a += 1
#         print(a)
#     inner()
# wrapper()
'''


'''
13、 写函数,接收两个数字参数,将较小的数字返回

def min_(a,b):return a if a < b else b
print(min_(13,2))
'''


'''
# 14、 写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回
# 例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’

def fun(item):
    """
    :param item:
    :return:
    """
    s = ''
    for i in item:
        s = s + '%s_' % (i)
    s = s.rstrip('_')
    return s
l1 = [1,'老男孩','武sir']
ret = fun(l1)
print(ret)
'''


'''
# 15、 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如：如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)

def min_max(*args):
    dic = {'max':max(args),'min':min(args)}
    return dic
ret = min_max(2,5,7,8,4)
print(ret)
'''


'''
# 16、 写函数，传入一个参数n，返回n的阶乘
# 例如:cal(7) 计算7*6*5*4*3*2*1

def fun(n):
    s = 1
    for i in range(1,n+1):
        s = s * i
    print(s)
fun(7)
print(7*6*5*4*3*2*1)
'''


'''
17、 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]

def poker():
    poker_list = []
    l1 = ['红心','草花','黑桃','方片']
    l2 = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    for i in l1:
        for k in l2:
            poker_list.append((i,k))
    return poker_list
print(poker())
'''


'''
18、 有如下函数:
def wrapper():
    def inner():
        print(666)
wrapper()
你可以任意添加代码,用两种或以上的方法,执行inner函数

#方法1
# def wrapper():
#     def inner():
#         print(666)
#     inner()
#
# wrapper()

#方法2
# def wrapper():
#     def inner():
#         print(666)
#     return inner
# 
# ret = wrapper()
# ret()
'''