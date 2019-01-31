#!/usr/bin/env python3
#author:Alnk(李成果)
'''
作业需求:
实现加减乘除及拓号优先级解析
用户输入
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式
注意：不能调用eval等类似功能偷懒实现
'''


import re


def calc(s):
    '''计算加减乘除'''
    # 去掉空格
    s = s.replace(' ', '')
    # 替换运算符号
    s = s.replace('--', '+').replace('++', '+').replace('-+', '-').replace('+-', '-')

    # 计算乘除
    while re.search('[.\d]+[*/]+[-+]?[.\d]+', s):
        # 匹配第一个乘除公式
        res = re.search('[.\d]+[*/]+[-+]?[.\d]+', s).group()
        # 判断乘除
        if res.count('*'):
            res_list = res.split('*')
            ret = float(res_list[0]) * float(res_list[1])
        else:
            res_list = res.split('/')
            ret = float(res_list[0]) / float(res_list[1])
        # 把结果替换回原来的公式中，并且替换运算符
        s = s.replace(res, str(ret)).replace('--', '+').replace('++', '+').replace('-+', '-').replace('+-', '-')

    # 计算加减
    # 找到所有的 正数或者负数，生成一个列表
    s_list =  re.findall('[-]?[.\d]+', s)
    sum = 0
    # 循环列表，都做加法（减法可以看作加一个负数）
    for i in s_list:
        sum += float(i)
    return sum


def strip_kuohao(s):
    # 去掉空格
    s = s.replace(' ', '')
    # 替换运算符号
    s = s.replace('--', '+').replace('++', '+').replace('-+', '-').replace('+-', '-')
    # 匹配最里层的括号
    while re.search('\([^\(\)]+\)', s):
        # 替换运算符号
        s = s.replace('--', '+').replace('++', '+').replace('-+', '-').replace('+-', '-')
        # 获取匹配到的最里层的括号公式
        kuohao_res = re.search('\([^\(\)]+\)', s).group()
        # 去掉括号，传入calc函数进行加减乘除运算
        kuohao_res_strip = kuohao_res.strip('(,)')
        ret = calc(kuohao_res_strip)
        # 结果替换到原来的公式中
        s = s.replace(kuohao_res, str(ret))
    else:
        # 最后没有括号的公式还要进行一次加减乘除运算，算出最后的结果
        ret = calc(s)
        s = s.replace(s, str(ret))
    return  s


s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
ret = strip_kuohao(s)
print(ret)
print(eval(s))