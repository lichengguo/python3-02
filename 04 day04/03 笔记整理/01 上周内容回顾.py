#!/usr/bin/env python3
#author:Alnk(李成果)
"""
深浅copy:
        浅copy：内存中创建一个新列表，但是列表里面的内容还是沿用之前的指向关系。
        深copy：内存中创建一个新的列表以及可变的数据类型，不可变的数据类型沿用之前的指向关系。

文件操作：
    path，encoding mode
    读 r rb r+ r+b
        r:
            read()
            read(n)
            readline()
            readlines()
            for 循环      --- 最好的方式

    写 w wb w+ w+b
        w:没有文件创建文件，有文件清空内容，在写入。

    追加：a a+.....
        a:没有文件创建文件，有文件在文件末尾追加内容。

    f = open(path,encoding='utf-8',mode='r')
    f.read()
    f.close()

    with open(path,encoding='utf-8',mode='r') as f1, open() ... as f2:
        f1.read()
        f2.write()

    tell()
    seek()
    truncate()  --截取原文件，必须可写的模式下
    readable()
    writable()
    f.flush()

    文件的改的操作：  -- 一定要会，重点
        5步

函数：
    1，一个函数封装一个功能。

    2，基本结构
    def func(参数):
        函数体

    执行：func()

    函数的返回值：
        return：
            1，结束函数。
            2，给函数的执行者func()返回值。
                return  None
                return  单个值
                return  多个值 1,2,[1,2,3]
                    func() ---> (1,2,[1,2,3])  --- 返回值是一个元组

    函数的参数：
        def func(参数):   --形参
            函数体
        func(参数)        --实参

        1，实参：
                a, 位置参数：从左至右一一对应。
                b, 关键字参数：name='alex' 一一对应。
                c, 混合参数。关键字参数一定要在位置参数后面。
        2，形参：
                a, 位置参数：从左至右一一对应。
                b, 默认参数。一定要放在位置参数后面。
                c, 万能参数。*args，**kwargs。
        形参角度参数顺序：
            位置参数，*args，默认参数，**kwargs

        def func(*args,**kwargs): 函数的定义：*代表聚合。
            print(args)
            print(kwargs)
        func(*[1,2,43],**{'name':'alex'}) # 函数的执行：*代表打散。

        名称空间：全局名称空间：变量与值得对应关系。
        局部名称空间：临时名称空间。
        内置名称空间：存放的是内置函数等。

        加载顺序：内置名称空间   全局名称空间  临时名称空间
        取值顺序：就近原则。

        globals() locals()

        函数的嵌套：
        pass

        函数名的应用：
            1，函数名是一个特殊的变量。
            2，函数名可以作为容器类数据类型的元素。
            3，函数名可以作为函数的参数。
            4，函数名可以作为函数的返回值。

        global nonlocal
"""

# 函数的嵌套
# def func():
#     print(123)
#
# def func1():
#     func()
#     print(222)
#
# def func2():
#     func1()
#     print(333)
#
# print(4)
# func2()
# print(5)
# # 4 123 222 333 5

# def wrapper():
#     print(1)
#     def inner():
#         print(2)
#     print(3)
#     inner()
#     print(4)
# print(5)
# wrapper()
# print(6)
# # 5 1 3 2 4 6