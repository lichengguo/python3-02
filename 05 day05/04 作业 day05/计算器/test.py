#!/usr/bin/env python3
#author:Alnk(李成果)
import re
from decimal import Decimal

def jiajian(s):
    # 去空格
    s = s.replace(' ', '')
    # 匹配第一个加或者减的公式
    while re.search('\d+(\.\d+)?[\+\-]{1}\d+(\.\d+)?', s):
        # 获取第一个加减公式
        res = re.search('\d+(\.\d+)?[\+\-]{1}\d+(\.\d+)?', s).group()
        # 判断是加法运算还是减法运算
        if re.search('[\+\-]', res).group() == '+':
            res_ = res.split('+')
            jieguo = Decimal(res_[0]) + Decimal(res_[1])
        else:
            res_ = res.split('-')
            jieguo = Decimal(res_[0]) - Decimal(res_[1])
        # 把计算出来的结果替换到之前的公式继续循环
        s = s.replace(res, str(jieguo))
    return s


def chenchu(s):
    # 去空格
    s = s.replace(' ', '')
    # 匹配第一个乘或者除的公式
    while re.search('\d+(\.\d+)?[\*\/]{1}\d+(\.\d+)?', s):
        # 获取第一个乘除公式
        res = re.search('\d+(\.\d+)?[\*\/]{1}\d+(\.\d+)?', s).group()
        # 判断是乘法运算还是除法运算
        if re.search('[\*\/]', res).group() == '*':
            res_ = res.split('*')
            jieguo = Decimal(res_[0]) * Decimal(res_[1])
        else:
            res_ = res.split('/')
            jieguo = Decimal(res_[0]) / Decimal(res_[1])
        # 把计算出来的结果替换到之前的公式继续循环
        s = s.replace(res, str(jieguo))
    else:
        ret = jiajian(s)
    return ret


def calc(s):
    # 去空格
    s = s.replace(' ', '')
    # 匹配最里层的括号
    while re.search('\([^\(\)]+\)', s):
        # 获取最里层的括号
        res = re.search('\([\d\+\-\*\/]+\)', s).group()
        s = s.replace(res, '999.999')
        print(s)

s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
calc(s)





# s = '3 * 2 / 3 * 9 * 7 /6+6-1+9.0'
# ret = chenchu(s)
# print(ret)
# print(eval(s))



# s = '19.333 + 2 -3 + 4.123456 - 5'
# ret = jiajian(s)
# print(ret)
# print(eval(s))