#!/usr/bin/env python3
#author:Alnk(李成果)
'''
while：无限循环
    while 条件:
        循环体

    如何结束循环？
        1，条件不成立。
        2， break。
        3， 系统命令：quit() exit() --不建议使用
'''

# while 循环
'''
while True:
    print('光年之外')
    print('千里之外')
    print('美人鱼')
    print('沙漠骆驼')

flag = True
while flag:
    print('光年之外')
    print('千里之外')
    print('美人鱼')
    print('沙漠骆驼')
    flag = False

flag = True
while flag:
    print('光年之外')
    print('千里之外')
    print('美人鱼')
    flag = False
    print('沙漠骆驼')


count = 1
flag = True
while flag:
    print(count)
    count = count + 1
    if count == 101:
	    flag = False

count = 1
while count < 101:
    print(count)
    count = count + 1
'''

# break continue
# break: 遇到break直接结束循环。
'''
while True:
    print(111)
    print(222)
    break
    print(333)
print(555)
'''