# l1 = ['wusir','ba', 'aa' ,'alex']
# print([ i.upper() for i in l1 if len(i) > 3])
#
# print([i**2 for i in range(31) if i % 2 == 0])

names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# new_list = []
#
# for i in names:
#     for j in i:
#         if j.count('e')  >= 2:
#             new_list.append(j)
# print(new_list)

print( [j for i in names for j in i if j.count('e') >= 2] )