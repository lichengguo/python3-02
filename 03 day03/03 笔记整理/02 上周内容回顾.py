#!/usr/bin/env python3
#author:Alnk(李成果)
"""
格式化输出：
    % s d i f r
    format
        '{}{}{}'.format('alex',46,'women')
        '{0}{1}{2}{0}{0}'.format('alex',46,'women')
        '{name}{age}{hobby}'.format(age=46,name='alex',hobby='women')

str:
    s1 = 'alex'
    print(s1[0])
    print(s1[:2])
    print(s1[::2])
    upper() lower()
    replace
    calptlize()
    strip()
    split() 分割，str----> list
    默认按照空格分割。指定分割符，指定分割次数。
    find index:通过元素查找索引值。
    join：将list ---> str 功能之一
     '|'.join(iterable)
     starstwith endswith
     isdigit()
     isalpha()
     isalnum()
    count()
    内置函数：len() 取总长度

list: 容器型数据类型，按照顺序存值。
    索引切片（步长）
    增： append() insert() extend()
    删:  pop()  remove() clear()
         del 索引切片（步长） del l1[1]
    改
        l1[0] = 'barry'
        l1[:3] = 'barry'
    查：
        索引切片（步长）
        for 循环
    其他操作方法：
        count index sort(reverse=True) 排序 reverse()
        len()
    range(10)
    range(1,12,2)
    for i in range(10,0,-1):
        print(i)
    l1 = [1,2,3,4,5]
    for i in range(len(l1)):
        print(i)

tuple (1,2,3,4,[22]) 只读列表

dict: key:value 大量关系型数据
    查询速度快，数据之间的关系性强。
    key: 不可变的数据类型。
    values: 任意数据类型 对象。

    增：dic['name'] = 'Alex' setdefault
    删：pop 按照key删除 del clear popitem(随机删除，但是3.6以后字典有序了)
    改：dic[key] = 'value' update
    查：
        dic['key'] 如果没有此key
        dic.get('key'，'设置返回值') 没有此键不报错,返回None,或者自己设定的值
        dic.keys() dic.values() dic.items()
        a,b = 1,2       分别赋值 a = 1  b = 2
        a,b = (2,3)     a = 2  b = 3
        for k,v in dic.items():
            pass

数据类型的补充：
    数据类型的转换
编码：
    str:python3x 编码是unicode
    str ---> bytes
    unicode ---> 非Unicode
    s1 = 'alex'
    b1 = s1.encode('utf-8') 编码
    b1.decode('utf-8') 解码

    b1 gbk----->  b2  utf-8
    b1.decode('gbk').encode('utf-8')
"""
