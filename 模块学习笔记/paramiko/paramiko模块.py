#!/usr/bin/env python3
# author:Alnk
"""
paramiko模块提供了基于ssh连接，进行远程登录服务器执行命令和上传下载文件的功能。
这是一个第三方的软件包，使用之前需要安装:
pip3 install paramiko
"""

"""
# 一.基于用户名和密码的sshclient方式登录
import paramiko
# 1 创建sshclient对象
ssh = paramiko.SSHClient()
# 2 允许连接不在know_hosts文件中的主机，此方法必须放在connect方法的前面
# 否则可能报错：paramiko.ssh_exception.SSHException: Server '192.168.43.140' not found in known_hosts
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 3 调用connect方法连接服务器
ssh.connect(hostname='192.168.166.132', port=22, username='root', password='redhat')
# 4 执行命令，输出结果在stdout中，如果是错误则放在stderr中
stdin, stdout, stderr = ssh.exec_command("top")
# 5 read方法读取输出结果
result = stdout.read()
# 6 判断如果正常输出结果长度等于0，那么则是错误输出
if len(result) == 0:
    print(stderr.read().decode())
else:
    print(result.decode())
# 7 关闭连接
ssh.close()
"""

"""
# 封装ssh类
import paramiko
import configparser
class ParamikoClient:
    def __init__(self, ini_file):
        self.config = configparser.ConfigParser()  # 实例化配置文件类
        self.config.read(ini_file, encoding='utf-8')  # 读取配置文件
        self.host = self.config.get('ssh', 'host')  # 地址
        self.port = self.config.get('ssh', 'port')  # 端口
        self.user = self.config.get('ssh', 'user')  # 账号
        self.pwd = self.config.get('ssh', 'pwd')  # 密码
        self.timeout = self.config.get('ssh', 'timeout')  # 超时时间
        self.client = paramiko.SSHClient()  # 创建sshclient对象
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname=self.host,
            port=self.port,
            username=self.user,
            password=self.pwd,
            timeout=float(self.timeout),
        )

    def run_ssh(self, cmd_command):
        # 执行命令，输出结果在stdout中，如果是错误则放在stderr中
        stdin, stdout, stderr = self.client.exec_command(cmd_command)
        result = stdout.read()
        if len(result) == 0:
            print(stderr.read().decode())
        else:
            print(result.decode())

    def close(self):
        self.client.close()


cmd = ParamikoClient('conf.ini')
cmd.run_ssh('df -Th')
cmd.close()
"""

"""
# 二 通过transport方式登录
import paramiko
# 1.实例化一个transport对象
transport = paramiko.Transport(('192.168.166.132', 22))
# 2.建立连接
transport.connect(username='root', password='redhat')
# 3.建立ssh对象
ssh = paramiko.SSHClient()
# 4.绑定transport到ssh对象
ssh._transport = transport
# 5.执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 6.打印输出
print(stdout.read().decode())
# 7.关闭连接
transport.close()
"""

"""
# 三 sftp文件传输
# 基于SSHClient是传统的连接服务器、执行命令、关闭的一个操作，有时候需要登录上服务器执行多个操作，比如执行命令、上传/下载文件，
# 上面方法则无法实现，可以通过如下方式来操作
import paramiko
# 实例化transport对象，并建立连接
transport = paramiko.Transport(('192.168.166.132', 22))
transport.connect(username='root', password='redhat')
# 实例化sftp对象，指定连接对象
sftp = paramiko.SFTPClient.from_transport(transport)
# 上传文件
sftp.put(localpath='config.ini', remotepath='/tmp/config.ini')
# 下载文件
# sftp.get(remotepath='/tmp/config.ini', localpath='conf2.ini')
# 关闭连接
transport.close()
"""

"""
# 四 传输目录
"""
import os
import paramiko


# os.walk()方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
def sftp_put_dir(local_dir, remote_dir):
    t = paramiko.Transport(('192.168.166.132', 22))
    t.connect(username='root', password='redhat')
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.chdir(remote_dir)
    dangqiandir = ''
    for root, dirs, files in os.walk(local_dir):

        for file in files:
            try:
                if root.split('\\')[-1] not in dangqiandir:
                    dangqiandir = '%s/%s' % (dangqiandir, root.split('\\')[-1])
                    try:
                        print('try:', '%s%s' % (remote_dir, dangqiandir))
                        sftp.chdir('%s%s' % (remote_dir, dangqiandir))
                        print(sftp.listdir())
                        sftp.put(os.path.join(root, file), file)
                    except:
                        print(root.split('\\')[-1])
                        sftp.mkdir(root.split('\\')[-1])
                        sftp.chdir('%s%s' % (remote_dir, dangqiandir))
                        print('%s%s' % (remote_dir, dangqiandir))
                        sftp.put(os.path.join(root, file), file)
                else:
                    sftp.chdir('%s%s' % (remote_dir, dangqiandir))
                    sftp.put(os.path.join(root, file), file)
            except Exception as e:
                print(e)


# print(os.walk(r"E:\test1"))
# sftp_put_dir(r"E:\test1", '/tmp/')  # bug 有目录没上传
for j in os.walk(r"E:\test1"):
    print(j)
"""
打印结果：
('E:\\test1', ['d1', 'd2'], ['f1.txt', 'f2.txt'])
('E:\\test1\\d1', ['dd1'], ['ff1.txt'])
('E:\\test1\\d1\\dd1', ['cc'], ['fff1.txt'])
('E:\\test1\\d1\\dd1\\cc', [], ['cc.txt'])
('E:\\test1\\d2', [], [])
"""
