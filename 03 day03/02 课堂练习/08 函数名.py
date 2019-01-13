#1,
def fun():
    pass




#2,函数名当作变量进行赋值运算
# def func():
#     print(666)
# f = func
# f()


#3，函数名可以当作容器数据的元素
# def func1():
#     print(777)
# def func2():
#     print(888)
# def func3():
#     print(999)
# l1 = [func1,func2,func3]
# for i in l1:
#     i()


#4，函数名可以作为函数的参数
# def fun1():
#     print(111)
# def fun2(x):
#     x()
#     print(222)
# fun2(fun1)


#5，函数名可以作为函数的返回值
# def fun1():
#     print(111)
# def fun2(x):
#     print(222)
#     return fun1
# ret = fun2(fun1)
# ret()