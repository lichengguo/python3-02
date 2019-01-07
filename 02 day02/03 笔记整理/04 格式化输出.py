#!/usr/bin/env python3
#author:Alnk(李成果)
"""
# % 格式化输出
name = input('姓名')
age = input('年龄')
sex = input('性别')
hobby = input('爱好')
job = input('工作')

msg = '''------------ info of %s -----------
Name  : %s
Age   : %s
job   : %s
Hobbie: %s
------------- end -----------------''' % (name,name,age,job,hobby)
print(msg)

#格式化输出
#补充：注意其中的一个坑
# 当用格式化输出的时候，里面有百分号，表示百分之几，需要两个百分号转义
msg1 = '我叫%s ,今年%s岁，学习进度3%%' % ('alnk',18)
print(msg1)
"""

"""
format 格式化输出
"""
# # 第一种
# msg = '我叫{} 今年{} 性别{}'.format('太白', '18', '男')
# print(msg)

# 第二种
# msg = '我叫{0} 今年{1} 性别{2}，我依然叫{0}'.format('太白', '18', '男')
# print(msg)

# # 第三种
# msg = '我叫{name} 今年{age} 性别{sex}'.format(name='太白', sex='男',age='18',)
# print(msg)
