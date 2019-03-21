#!/usr/bin/env python3
# author:Alnk(李成果)
import subprocess  # 执行系统命令，获取返回结果

# 还有paramiko模块，基于SSH用于连接远程服务器并执行相关操作

res = subprocess.Popen("ipconfig",  # 命令
                       shell=True,
                       stdout=subprocess.PIPE,  # 标准输出
                       stderr=subprocess.PIPE,  # 标准错误
                       )

temp = res.stdout.read()  # 数据只能read一次
print(temp.decode('gbk'))
print('字符长度：', len(temp.decode('gbk')))
print('字节长度：', len(temp))

# 错误的命令返回
res2 = subprocess.Popen("cc",  # 命令
                        shell=True,
                        stdout=subprocess.PIPE,  # 标准输出
                        stderr=subprocess.PIPE,  # 标准错误
                        )

temp_err = res2.stderr.read()
print(temp_err.decode('gbk'))
