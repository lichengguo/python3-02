#!/usr/bin/env python3
#author:Alnk(李成果)
"""
作业需求:
1)，启动程序，首页面应该显示成如下格式：
    欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序
2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功
3)，用户选择登录，用户名密码从register文件中读取验证，三次机会， 没成功则结束整个程序运行，成功之后，可以选择访问3~6项，
    访问页面之前， 必须要在log文件中打印日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
    访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
"""
import datetime

# 标志位
flag = False

def read_register(*args,mode='r'):
    """
    写入、获取账号密码信息
    :param args: 注册时，接收用户名和密码
    :param mode: 默认r 模式读取，a 模式写入注册
    :return: r 模式返回用户信息字典 a模式返回True
    """
    if mode == 'r':
        user_dic = {}
        with open('register', encoding='utf-8', mode='r') as f:
            for line in f:
                l1 = line.strip().split('|')
                user_dic[l1[0]] = l1[1]
        return user_dic

    elif mode == 'a':
        if args:
            # 声明为全局变量，以便其他函数也可以调用 user_name 这个变量
            global user_name
            user_name = args[0]
            user_pwd = args[1]

            # 判断用户是否已经注册过
            user_dic = read_register(mode='r')
            if not user_dic.get(user_name):
                with open('register', encoding='utf-8', mode='a') as f:
                    f.write('%s|%s\n' % (user_name,user_pwd) )
                    f.flush()
                return True
            else:
                print('[%s] 用户已经被注册了哦!\n' % user_name )
        else:
            print('请输入用户名和密码哦!\n')

    else:
        return '参数有误!\n'


def login():
    """登录"""
    # 读取帐号密码信息
    user_dic = read_register(mode='r')

    count = 0
    while count < 3:
        global user_name
        user_name = input('请输入账号>>>:')
        user_pwd = input('请输入密码>>>:')

        # 判断账号密码是否正确
        if user_dic.get(user_name) and user_dic[user_name] == user_pwd:
            print('恭喜,登录成功!\n')
            global flag
            flag = True
            break
        else:
            print('账号或者密码错误!\n')
            count += 1

        if count == 3:
            exit('密码错误次数过多，程序结束运行!')


def auth(func):
    """装饰器，认证"""
    def inner(*args,**kwargs):
        while 1:
            if flag:
                res = func(*args,**kwargs)
                return res
            else:
                login()
    return inner


def register(): # 要判断该用户是否已经注册
    """注册"""
    global user_name
    user_name = input('请输入你要注册的账号>>>:')
    user_pwd = input('请输入你要注册的密码>>>:')

    # 调用函数注册，获取返回值
    ret = read_register(user_name, user_pwd, mode='a')

    if ret:
        global flag
        flag = True
        print('[%s] 用户注册成功!\n' % user_name )
    else:
        print('注册失败!\n')


def write_log(user_name, func_name):
    """日志记录"""
    # 获取当前时间
    time = datetime.datetime.now()
    year = time.year
    month = time.month
    day = time.day
    # 记录日志
    with open('log', encoding='utf-8', mode='a') as f:
        f.write("用户:[%s] 在 %s 年 %s 月 %s 日，执行了 [%s] 函数\n" % (user_name, year, month, day, func_name) )
        f.flush()


@auth   #article = auth(article)
def article():
    """文章页面"""
    print('欢迎 [%s] 用户访问文章页面\n' % user_name )
    func_name = 'article'
    write_log(user_name,func_name)


@auth
def diary():
    """日记页面"""
    print('欢迎 [%s] 用户访问日记页面\n' % user_name )
    func_name = 'diary'
    write_log(user_name,func_name)


@auth
def comment():
    """评论页面"""
    print('欢迎 [%s] 用户访问评论页面\n' % user_name )
    func_name = 'comment'
    write_log(user_name,func_name)


@auth
def colle():
    """收藏页面"""
    print('欢迎 [%s] 用户访问收藏页面\n' % user_name )
    func_name = 'colle'
    write_log(user_name,func_name)


def log_out():
    """注销"""
    global flag
    flag = False
    print('[%s] 账号注销成功!\n' % user_name )


def sign_out():
    """退出"""
    exit('退出程序!')


def view():
    """显示"""
    msg = '''------ 欢迎来到博客园首页 ------
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序
    '''
    dic = {
        '1':login,
        '2':register,
        '3':article,
        '4':diary,
        '5':comment,
        '6':colle,
        '7':log_out,
        '8':sign_out,
    }
    while 1:
        print(msg)
        choice = input('请输入编号>>>:')
        if dic.get(choice):
            dic[choice]()
        else:
            print('请输入正确的标号哟\n')


if __name__ == '__main__':
    view()