# f = open('d:\练习.txt',encoding='utf-8',mode='r')
# content = f.read()
# print(content)

#1.1 read
# f = open('d:\练习.txt',encoding='utf-8',mode='r')
# content = f.read()
# print(content)

#1.2 readline()
# f = open('d:\练习.txt',encoding='utf-8',mode='r')
# content = f.readline()
# print(content)

#1.3 readlines()
# f = open('d:\练习.txt',encoding='utf-8',mode='r')
# content = f.readlines()
# print(content)

#for 最好的读取文件的方法
f = open('d:\练习.txt',encoding='utf-8',mode='r')
for line in f:
    print(line.strip())