# 不是闭包
# def func(setp):
#     num = 1
#     num += setp
#     print(num)
#
# for i in range(5):
#     func(2)


# 闭包
# def func(step):
#     num = 1
#     def inner():
#         nonlocal num
#         num += step
#         print(num)
#     return inner
#
# f = func(2)
# for i in range(5):
#     f()



