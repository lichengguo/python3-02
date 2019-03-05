#!/usr/bin/env python3
# author:Alnk(李成果)

# 把任意长度的字节，通过算法，转化为固定长度的字符串

import hashlib

# md5
# 简单使用
# md5 = hashlib.md5()
# md5.update(b"yuan")
# print(md5.hexdigest())  # 46cc45a727bec7de97f9e738ad428153
# print(len(md5.hexdigest()))

# 迭代使用（对于大文件用这种方法）（*********）
# 对于校验上传下载大文件的一致性，用迭代的方法校验，节省内存
# md5 = hashlib.md5()
# # md5.update(b"helloword")  # 59284aa85709ddaf3bd246030060f6a2
# md5.update(b"hello")
# md5.update(b"word")
# print(md5.hexdigest())  # 59284aa85709ddaf3bd246030060f6a2


# sha256
# sha256 = hashlib.sha256()
# sha256.update(b"helloword")  # 0b322d15ea034793a8646baa1744ffacbdf7f959b66c68970f032c4ac8b9c8cb
# # sha256.update(b"hello")
# # sha256.update(b"word")  # 0b322d15ea034793a8646baa1744ffacbdf7f959b66c68970f032c4ac8b9c8cb
# print(sha256.hexdigest())


# 加盐操作
# 当用户设置的密码过于简单的时候，我们可以加入自定义的字符串，提高md5后的复杂度，防止撞库
md5 = hashlib.md5(b'Alnk')  # 加盐
md5.update(b'helloword')
print(md5.hexdigest())  # 60c4984bf98f82954f4d87d589a8c206
