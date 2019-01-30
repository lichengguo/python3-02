#!/usr/bin/env python3
#author:Alnk(李成果)
'''
作业需求:
实现加减乘除及括号优先级解析
用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式
注意：不能调用eval等类似功能偷懒实现
'''
import re
from decimal import Decimal
from decimal import getcontext

# 设置小数点精度
# getcontext().prec = 10

def calc(s):

    s = s1.replace(' ', '')

    while re.search('\([\d\+\-\*\/]+\)', s):
        res = re.search('\([\d\+\-\*\/]+\)', s).group()

        # 乘除
        while re.search('\d+(\.\d+)?[\*\/]{1}\d+(\.\d+)?', res):
            res = re.search('\d+(\.\d+)?[\*\/]{1}\d+(\.\d+)?', s).group()

            if re.search('[\*\/]', res).group() == '*':
                res_ = res.split('*')
                print('*res_', res_)
                jieguo = Decimal(res_[0]) * Decimal(res_[1])
            else:
                res_ = res.split('/')
                print('/res_', res_)
                jieguo = Decimal(res_[0]) / Decimal(res_[1])

            s = s.replace(res, str(jieguo))


            # 加减
            s = s.replace(' ', '')

            while re.search('\d+(\.\d+)?[\+\-]{1}\d+(\.\d+)?', s):
                res = re.search('\d+(\.\d+)?[\+\-]{1}\d+(\.\d+)?', s).group()
                print('res', res)
                if re.search('[\+\-]', res).group() == '+':
                    res_ = res.split('+')
                    print('+res_', res_)
                    jieguo = Decimal(res_[0]) + Decimal(res_[1])
                else:
                    res_ = res.split('-')
                    print('-res_', res_)
                    jieguo = Decimal(res_[0]) - Decimal(res_[1])

                s = s.replace(res, str(jieguo))



        s = s.replace(res, end_res)


if __name__ == '__main__':

    s1 = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    calc(s1)
    # s2 = '9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14'
    # chchu(s2)
    # print(eval(s2))