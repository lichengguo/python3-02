#方法1 建议使用方法1
# import os
# with open('alex个人简历',encoding='utf-8',mode='r') as f1, \
#         open('alex个人简历.bak',encoding='utf-8',mode='w') as f2:
#     for old_line in f1:
#         new_line = old_line.replace('alex','SB')
#         f2.write(new_line)
# os.remove('alex个人简历')
# os.rename('alex个人简历.bak','alex个人简历')

#方法2
import os
with open('alex个人简历',encoding='utf-8',mode='r') as f1, \
        open('alex个人简历.bak',encoding='utf-8',mode='w') as f2:
    old_content = f1.read()
    new_content = old_content.replace('alex','sb')
    f2.write(new_content)
os.remove('alex个人简历')
os.rename('alex个人简历.bak','alex个人简历')