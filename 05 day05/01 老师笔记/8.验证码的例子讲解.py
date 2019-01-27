# -*- coding: utf-8 -*-
# @Time    : 2019/1/27 14:59
# @Author  : xxx
# @Email   : xxx@admin.com
# @File    : 8.验证码的例子讲解.py
# @Software: PyCharm

# 带数字的
import random
# def get_code(n = 6):
#     code = ''
#     for i in range(n):
#         num = random.randint(0,9)
#         code += str(num)
#     return code
#
# print(get_code(4))
# print(get_code(6))
# print(get_code())

# 随即拼凑 数字 或者 字母
# 生成随机的数字 和 字母
# chr()
# 0,1,2,3,4,5,6,7,8,9,10:a,11:b...
# 97 - 122  a-z
# 65 - 91   A-Z
import random
def get_code(n = 6,alpha = True):
    code = ''
    for i in range(n):
        selected = random.randint(0, 9)
        if alpha:
            alpha_upper = random.randint(65,91)
            selected = random.choice([selected,chr(alpha_upper)])
        code += str(selected)
    return code

print(get_code(alpha=False))