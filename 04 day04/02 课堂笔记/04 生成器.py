# def book():
#     for i in range(1,501):
#         print("python全战 编号%s" % (i))
#
# def book1():
#     for i in range(1,501):
#         yield "python全战 编号%s" % (i)
#
# # book()
# g = book1()
#
# for i in range(50):
#     print(next(g))
#
# i = 0
# l1 = []
# while i < 101:
#     l1.append(i)
#     i += 2
# print(l1)

# 列表推导式
print(['python%s期' % i for i in range(1,21)])
print( [ i**2 for i in range(1,8) ] )