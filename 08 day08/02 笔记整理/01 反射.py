#!/usr/bin/env python3
# author:Alnk(李成果)
# hasattr getattr setattr delattr

class Animal(object):
    gender = 'male'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        print('foo...')

# hasattr:判断一个对象中有没有某种方法或属性
# alex = Animal('alex', 34)
# ret = hasattr(alex, 'name')  # 判断alex这个对象是否有name这个属性或者方法，等价与 alex.name。如果有返回True，否则False
# print(ret)
# ret2 = hasattr(alex, 'gender')
# print(ret2)
# ret3 = hasattr(alex, 'run')
# print(ret3)


# getattr:获取对象中的某种属性或方法
# alex = Animal('alex', 34)
# ret = getattr(alex, 'name')  # 如果name存在并且为属性，则返回属性对应的值，等价于alex.name
# print(ret)
# ret2 = getattr(alex, 'foo')  # 如果foo存在并且为方法，则返回内存地址，等价与alex.foo
# print(ret2)
# ret2()  # alex.foo()
# ret3 = getattr(alex, 'run', None)  # 如果run不存在则返回None，不设置None的话，直接报错
# print(ret3)
# ret4 = getattr(alex, 'run')  # 如果run不存在则返回None，不设置None的话，直接报错
# AttributeError: 'Animal' object has no attribute 'run'

# hasattr 和 getattr 组合使用（常用的）
# alex = Animal('alex', 34)
# if hasattr(alex, 'name'):
#     # ret = getattr(alex,'name')
#     # print(ret)
#     ret = getattr(alex, 'foo')
#     ret()
# else:
#     print('没有该方法或者属性')


# setattr:增加一个属性或者方法
# 增加一个属性
# alex = Animal('alex', 34)
# setattr(alex, 'job', 'IT')  # 在alex的实例对象空间新增加一个属性
# print(alex.__dict__)  # {'name': 'alex', 'age': 34, 'job': 'IT'}
# print(getattr(alex,'job'))
# print(alex.job)
# 修改一个属性
# print(alex.age)
# setattr(alex, 'age', 1000)
# print(alex.age)
# # 增加一个方法
# def bar():
#     print('bar...')
# setattr(alex,'bar',bar)
# alex.bar()


# delattr：删除一个属性
# alex = Animal('alex', 34)
# print(alex.__dict__)  # {'name': 'alex', 'age': 34}
# delattr(alex, 'age')
# print(alex.__dict__)  # {'name': 'alex'}
# print(alex.age)  # AttributeError: 'Animal' object has no attribute 'age'


# 反射的应用
# 动态的，用户选择。
# 基于字典的映射分发方式
# def check():
#     print('check...')
# def pay():
#     print('pay...')
# def withdraw():
#     print('withdraw...')
# data={
#     "check":check,
#     "pay": pay,
#     "withdraw": withdraw,
# }
# while 1:
#     action = input('>>>')
#     data[action]()

# 基于反射的分发
class Atm(object):

    option_lis = [('check','检查'),
                  ('pay','支付'),
                  ('withdraw','提现'),
                  ('login_out','退出'),
                  ]

    def view(self):
        while 1:
            for k,i in enumerate(self.option_lis,1):
                print(k,i[1])
            action = int(input('请输入编号>>'))
            if 0 < (action - 1) < len(self.option_lis):
                if hasattr(self,self.option_lis[action - 1][0]):
                    getattr(self,self.option_lis[action - 1][0])()
                else:
                    print('xxx')
            else:
                print('编号有误')

    # def run(self):
    #     while 1:
    #         action = input('>>>')
    #         if hasattr(self, action):
    #             getattr(self, action)()
    #         else:
    #             print('没有该方法')

    def check(self):
        print('check...')
    def pay(slef):
        print('pay...')
    def withdraw(self):
        print('withdraw...')
    def login_out(self):
        exit()

a = Atm()
a.view()
