#!/usr/bin/env python3
#author:Alnk(李成果)
import random
# 和随机相关的内容 random模块

# # 随机小数
# print(random.random())  #(0,1)
# print(random.uniform(1,2))  #(n,m)

# 随机整数
# print(random.randint(1,2))  # [1,2] 包含了2
# print(random.randrange(1,2))    # [1,2) 不包含2
# print(random.randrange(1,5,2))  # 不长为2

# 随机从一个列表中取一个值
# ret = random.choice([1, 2, 3, ('k', 'v'), {'name':'alex'}])
# print(ret)

# 随机从一个列表中取2个值
# ret2 = random.sample([1, 2, 3, ('k', 'v'), {'name':'alex'}], 2)
# print(ret2)

# 打乱顺序  洗牌
# l1 = [1, 2, 3, 4, 5]
# random.shuffle(l1)
# print(l1)

# 验证码例子
# def my_code(n=6, flag=True):
#     code = ''
#     for i in range(n):
#         num = random.randint(0, 9)
#         # 注意这里的小技巧
#         if flag:
#             alp = chr(random.randint(65, 90))
#             num = random.choice([num, alp])
#         code += str(num)
#     return code
#
# ret = my_code()
# print(ret)


# 红包例子
# 思路：
# 1.需要确定红包个数，红包总金额
# 2.最低金额为0.01元
# 3.每抽中一次，需要用红包当前总金额减去抽中的金额，然后在继续在该区间内随机抽取
# 4.最小金鹅为
# def hb(num, money):
#     # 定义空列表用来存储抽奖金额
#     lst = []
#     # 金额乘以100，便于计算，后续加入到列表在除以100
#     money = money * 100
#     # 判断传递参数的合法性
#     if type(num) is int and num >=1 and (type(money) is int or type(money) is float):
#         # for循环应该比num少一次,例如2个红包个数，for循环1次就可以
#         for i in range(num-1):
#             # 保证不出现抽中0元的现象
#             p = random.randint(1, money-1*(num-1))
#             lst.append(p/100)
#             # 需要减去已经抽取的红包金额
#             money = money - p
#             # 这里的意思是没抽一次，没抽过的人减少1
#             num -= 1
#         else:
#             # 循环结束了，把剩余的红包总金额放入到一个红包内
#             lst.append(money/100)
#         return lst
#     else:
#         print('参数有误!')
#
# ret = hb(1,1.1)
# print(ret)
