#实参角度
    #位置参数
# def Tantan(sex,age):
#     print('筛选性别%s,年龄%s左右' % (sex,age))
#     print('搜索')
#     print('左滑一下')
#     print('右滑一下')
#     print('打招呼')
# Tantan('girl',28)

    #关键字参数
# def Tantan(sex,age):
#     print('筛选性别%s,年龄%s左右' % (sex,age))
#     print('搜索')
#     print('左滑一下')
#     print('右滑一下')
#     print('打招呼')
# Tantan(age=28,sex='girl')

    #混合参数
# def Tantan(sex,age,area):
#     print('筛选性别%s,%s附近,年龄%s左右' % (sex,area,age))
#     print('搜索')
#     print('左滑一下')
#     print('右滑一下')
#     print('打招呼')
# Tantan('girl',28,area='宝安')

#形参角度
    #位置参数
# def Tantan(sex,age):
#     print('筛选性别%s,年龄%s左右' % (sex,age))
#     print('搜索')
#     print('左滑一下')
#     print('右滑一下')
#     print('打招呼')
# Tantan('girl',28)

    #默认参数
# def Tantan(area,age,sex='girl'):
#     print('筛选性别%s,%s附近,年龄%s左右' % (sex,area,age))
#     print('搜索')
#     print('左滑一下')
#     print('右滑一下')
#     print('打招呼')
# Tantan('宝安',28,)

#万能参数
# def Tantan(*args,**kwargs):
#     print('筛选性别%s,%s附近' % (args))
#     print(kwargs)
#     print('搜索')
#     print('左滑一下')
#     print('右滑一下')
#     print('打招呼')
# Tantan('女','南山',body='身材好',hobby='笑')

#形参角度的顺序
#位置参数 ，*args ，默认参数 , **kwargs
# def Tantan(a,b,*args,sex='女',**kwargs):
#     print(a,b,args,sex,kwargs)
# Tantan(1,2,4,5,6,name='alnk')

#练习
def Tantan(*args,**kwargs):
    print(args)
    print(kwargs)
l1 = (1,2,3,)
l2 = [1,2,3,4]
dic1 = {'name':'alex'}
dic2 = {'age':45}
Tantan(*l1,*l2,**dic2,**dic1)