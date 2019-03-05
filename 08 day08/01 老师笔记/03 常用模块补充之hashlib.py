


import hashlib
################################### 简单使用
# md5=hashlib.md5()
# md5.update(b"12345678")
# print(md5.hexdigest())
# print(len(md5.hexdigest()))
################################### 迭代使用
sha256=hashlib.sha256()
# md5.update(b"helloyuan")
# print(md5.hexdigest()) # d843cc930aa76f7799bba1780f578439
sha256.update(b"hello")
sha256.update(b"yuan")
print(sha256.hexdigest()) # d843cc930aa76f7799bba1780f578439

##################################### 加盐操作

sha256=hashlib.sha256("salt".encode("utf8"))

sha256.update(b"hello")
sha256.update(b"yuan")
print(sha256.hexdigest()) # 32969d77ae4b0c01c24873abb7f073d69453ddadbf6e31b11564a4490a9ccac8

