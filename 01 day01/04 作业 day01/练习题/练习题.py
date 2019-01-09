#!/usr/bin/env python3
#author:Alnk(李成果)
# 1、简述变量命名
"""
变量命名规则：
    1，变量名必须由 数字 字母 下划线 任意组合
    2，变量名不能是数字开头
    3，变量名不能是Python中的关键字
        ['and', 'as', 'assert', 'break', 'class', 'continue', 'def','del', 'elif', 'else', 'except', 'exec', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in', 'is','lambda', 'not', 'or', 'pass', 'print', 'raise','return',
        'try', 'while', 'with', 'yield']
    4，变量名不能使用中文
    5，变量名要具有可描述性
    6，变量名不能过长。
    7，变量名的推荐：
        下划线： age_of_oldboy = 47
"""


# 2、name = input(“>>>”) name变量是什么数据类型？
"""
name变量的数据类型是字符串
"""


# 3、if条件语句的基本结构？
"""
有5种基本结构，如下：

第一种：单独 if
if  条件:
    执行语句

第二种：if ... else
if  条件:
    执行语句
else:
    执行语句
    
第三种：if elif elif ...
if  条件:
    执行语句
elif 条件:
    执行语句
elif 条件:
    执行语句
elif 条件:
    执行语句
...

第四种：if elif elif ... else
if  条件:
    执行语句
elif 条件:
    执行语句
elif 条件:
    执行语句
...
else:
    执行语句
    
第五种：嵌套if
if 条件:
    if 条件:
        执行语句
    ...
...

"""


# 4、用print打印出下面内容：
# 文能提笔安天下,
# 武能上马定乾坤.
# 心存谋略何人胜,
# 古今英雄唯是君.
"""
msg = '''
文能提笔安天下,
武能上马定乾坤.
心存谋略何人胜,
古今英雄唯是君.
'''
print(msg)
"""


# 5、利用if语句写出猜大小的游戏
# 设定一个理想数字
# 比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；
# 如果比66小，则显示猜测的结果小了;
# 只有等于66，显示猜测结果正
"""
num = 66
flag = True
while flag:
    user_num = input("请输入数字（退出Q）：")
    if user_num.lower() == "q":
        break
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num > num:
            print("结果大了")
        elif user_num < num:
            print("结果小了")
        else:
            print("结果正确")
            flag = False
    else:
        print("您输入的不是数字哦")
"""


# 6、提示用户输入他的年龄, 程序进行判断
# 如果小于等于10, 提示小屁孩,
# 如果大于10, 小于等于20, 提示青春期叛逆的小屁孩.
# 如果大于20, 小于等于30. 提示开始定性, 开始混社会的小屁孩儿,
# 如果大于30, 小于等于40. 体制看老大不小了, 赶紧结婚小屁孩儿.
# 如果大于40, 小于等于50. 提示家里有个不听话的小屁孩儿.
# 如果大于50, 小于等于60. 提示自己马上变成不听 话的老屁孩儿.
# 如果大于60, 小于等于70. 提示活着还不错的老屁孩儿.
# 如果大于70, 小于等于90. 提示人生就快结束了的一个老屁孩儿.
# 如果大于90以上. 提示. 再见了这个世界.
"""
age = int(input("请输入你的年龄："))
if age > 90:
    print("再见了这个世界")
elif age > 70:
    print("人生就快结束了的一个老屁孩儿")
elif age > 60:
    print("活着还不错的老屁孩儿")
elif age > 50:
    print("自己马上变成不听话的老屁孩儿")
elif age > 40:
    print("家里有个不听话的小屁孩儿")
elif age > 30:
    print("看老大不小了, 赶紧结婚小屁孩儿")
elif age > 20:
    print("开始定性, 开始混社会的小屁孩儿")
elif age > 10:
    print("青春期叛逆的小屁孩")
elif 0 < age <= 10:
    print("小屁孩")
"""


# 7、单行注释以及多行注释？
#单行注释： #
#多行注释： """被注释内容"""  '''被注释内容'''


# 8、简述你所知道的Python3x和Python2x的区别？
"""
第一：源码
    python2x：源码冗余，源码重复，源码不规范。
    python3x：源码清晰优美简单。
第二：编码
    python2x：编码默认是ascii
    python3x: 编码是utf-8
第三：input函数
    python2x:raw_input() 相当于python3xinput。input() 只接受数字类型。
	python3x:input
"""


# 9、提示用户输入麻花藤. 判断用户输入的对不对. 如果对, 提示真聪明, 如果不对, 提示你 是傻逼么
"""
user_str = input("请输入麻花藤：")

if user_str.strip() == '麻花藤':
    print("真聪明")
else:
    print("你是傻逼么")
"""


# 10、使用while循环输入 1 2 3 4 5 6 8 9 10
"""
count = 0
while count < 10:
    count += 1
    if count == 7:
        continue
    print(count)
"""


# 11、求1-100的所有数的和
"""
sum = 0
count = 0
while count < 101:
    sum = sum + count
    count = count + 1
print(sum)
"""


# 12、输出 1-100 内的所有奇数
"""
count = 1
while count < 100:
    if count % 2 == 1:
        print(count)
    count = count + 1
"""

# 13、输出 1-100 内的所有偶数
"""
count = 1
flag = True
while flag:
    if count == 100:
        flag = False

    if count % 2 != 1:
        print(count)
    
    count = count + 1
"""


# 14、求1-2+3-4+5 ... 99的所有数的和
"""
odd_sum = 0     #奇数总和
even_sum = 0    #偶数总和
count = 1
flag = True

while flag:
    if count == 99:
        flag = False

    if count % 2 == 1:
        odd_sum = odd_sum + count
    else:
        even_sum = even_sum + count

    count = count + 1

sum = odd_sum - even_sum
print("和为:",sum)
"""