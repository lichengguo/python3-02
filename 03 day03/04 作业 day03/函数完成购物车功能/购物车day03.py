#!/usr/bin/env python3
#author:Alnk(李成果)
'''
作业题目：用函数完成登录注册以及购物车的功能
作业需求:
    1，启动程序，用户可选择四个选项：登录，注册，购物，退出。
    2，用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中。
    3，用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序。
    4，用户登录成功之后才能选择购物功能进行购物，购物功能（就是将购物车封装到购物的函数中）。
    5，退出则是退出整个程序。
'''
import os

# 设定一个默认没有登录的标志位
login_flag = False

def register():
    """
    注册
    :return:None
    """
    while 1:
        username = input('\n请输入你想注册的账户名称>>>:').strip()
        userpwd = input('请输入你想设置的登录密码>>>:').strip()
        if os.path.exists("user_info/%s" % (username)):
            print("该用户名已经被注册,请重新输入\n")
            continue
        with open("user_info/%s" % (username), encoding='utf-8', mode='w') as f:
            f.write("%s|%s|0" % (username,userpwd) )
            f.flush()
            print('账号注册成功！\n')
            return

def login():
    """
    登录
    :return:None
    """
    # 密码可输错次数
    count = 3
    while 1:
        username = input("\n请输入登录账号(返回B/b)>>>:").strip()
        if username.strip().lower() == 'b':
            print('\n')
            break
        userpwd = input("请输入登录密码>>>:").strip()
        # 用户是否存在
        if os.path.exists('user_info/%s' % (username) ):
            # 获取用户登录密码和密码输错次数
            with open('user_info/%s' % (username), encoding='utf-8', mode='r') as f1:
                user_l1 = f1.readline().strip().split('|')
                pwd = str(user_l1[1])
                count_pwd = int(user_l1[2])
                # 账号是否冻结
                if count_pwd == count:
                    print("账号 [%s] 已经被冻结,请联系管理员解除冻结或使用其他账号登陆\n" % (username))
                    continue
                # 密码是否正确
                if userpwd == pwd:
                    print('登录成功！\n')
                    # 重置密码输错次数
                    count_pwd = 0
                    user_l1[2] = count_pwd
                    with open('user_info/%s' % (username), encoding='utf-8', mode='w') as f2:
                        f2.write("%s|%s|%s" % (user_l1[0], user_l1[1], user_l1[2]))
                        f2.flush()
                    # 登录成功，修改默认的标志位
                    global login_flag
                    login_flag = True
                    return
                else:
                    # 登录失败，密码输错次数 +1
                    count_pwd += 1
                    user_l1[2] = count_pwd
                    with open('user_info/%s' % (username), encoding='utf-8', mode='w') as f3:
                        f3.write("%s|%s|%s" % (user_l1[0] ,user_l1[1], user_l1[2]) )
                        f3.flush
                    # 密码连续输错3次，直接退出程序
                    if count_pwd == count:
                        exit('[%s] 账号密码连续输错3次，程序退出！' % (username))
                    print('密码错误。\n')
                    continue
        else:
            print('用户不存在！')

def recharge():
    """
    充值
    :return:True，用户余额
    """
    while 1:
        user_balance = input("请先给账号充值(返回B/b):")
        if user_balance.lower() == "b":
            print('')
            return False
        elif user_balance.isdigit():
            user_balance = int(user_balance)
            print("账号充值成功！余额为[%s]元\n" % (user_balance))
            return True,user_balance
        else:
            print("输入有误，请重新输入。")

def jiesuan(user_shopping_cart,user_balance):
    """
    结算功能
    :param user_shopping_cart: 用户选购商品的临时字典
    :param user_balance: 用户充值的余额
    :return:None
    """
    while 1:
        # 显示购物车里的商品
        print("\n您的购车里商品如下:")
        for k in user_shopping_cart:
            print("\t商品[%s] 数量[%s] 价格[%s]" % (k, user_shopping_cart[k]['number'], user_shopping_cart[k]['price']))
        # 购物车所有商品总价
        shopp_cart_total = 0
        print("\n\n正在结算，请稍候...")
        # 计算商品总价格
        for k in user_shopping_cart:
            shopp_cart_total = shopp_cart_total + user_shopping_cart[k]['number'] * user_shopping_cart[k]['price']
        # 余额是否能够支付
        if user_balance >= shopp_cart_total:
            print("您本次总共需要支付[%s]元，余额为[%s]元" % (shopp_cart_total, user_balance))
            print("\n您本次购买的商品详单如下：")
            for k in user_shopping_cart:
                print('\t商品[%s] 数量[%s] 价格[%s]'%(k,user_shopping_cart[k]['number'],user_shopping_cart[k]['price']))
            print("\n本次总共消费[%s]元，账户余额为[%s]元" % (shopp_cart_total, user_balance - shopp_cart_total))
            print("\n购买成功!\n")
            return
        else:
            print("本次总共需要支付[%s]元 你的余额为[%s]元" % (shopp_cart_total, user_balance))
            print("余额不足，请先删除购物车里的一些商品再去结算哟\n")
            while 1:
                print("\n购物车的商品列表如下:")
                for k in user_shopping_cart:
                    print('\t商品[%s] 数量[%s] 价格[%s]' % (k, user_shopping_cart[k]['number'], user_shopping_cart[k]['price']))
                user_choice2 = input("请输入你想删除的商品名称:")
                # 从购物车删除商品
                if user_shopping_cart.get(user_choice2):
                    # 商品数量为1，直接删除。否则减少商品的数量1
                    if user_shopping_cart[user_choice2]['number'] == 1:
                        del user_shopping_cart[user_choice2]
                        print('商品[%s]已从购物车删除' % (user_choice2))
                    elif user_shopping_cart[user_choice2]['number'] > 1:
                        user_shopping_cart[user_choice2]['number'] -= 1
                        print("商品[%s]数量减少1件" % (user_choice2))
                    break
                else:
                    print("\n输入的商品名称有误，请重新输入")

def buy():
    """
    购物
    :return:None
    """
    # 默认标志为是否被修改，即是否已经登录
    if login_flag:
        print('\n')
        # 获取充值函数返回值，为一个元组(True,user_balance)
        ret = recharge()
        if ret[0]:
            # 用户余额
            user_balance = ret[1]
            # 用户选购商品临时购物车
            user_shopping_cart = {}
            # 商品列表
            goods_dic = {
                "1": {"name": "电脑", "price": 1999, },
                "2": {"name": "鼠标", "price": 10, },
                "3": {"name": "键盘", "price": 60, },
                "4": {"name": "手机", "price": 4000, },
                "5": {"name": "ipad", "price": 2999, },
                "n": {"name": "购物车结算", "price": '', },
            }
            while 1:
                print("下列是您可以选购的商品(退出Q/q):")
                for key in goods_dic:
                    print('\t', key, goods_dic[key]['name'], goods_dic[key]['price'])
                user_choice = input("请输入你想购买的商品序号:")
                if user_choice.lower() == "q":
                    print("退出购物商城")
                    break
                # 结算
                elif user_choice == "n":
                    jiesuan(user_shopping_cart,user_balance)
                    break
                # 添加商品到用户购物车
                elif goods_dic.get(user_choice):
                    # 判断购物车是否已经有该商品，如果有直接数量加1，没有则创建一个新的键值对
                    if user_shopping_cart.get(goods_dic[user_choice]['name']):
                        user_shopping_cart[goods_dic[user_choice]['name']]['number'] += 1
                    else:
                        user_shopping_cart[goods_dic[user_choice]['name']] = {"number": 1,"price": goods_dic[user_choice]['price']}
                    print("\n商品[%s] 价格[%s] " % (goods_dic[user_choice]['name'], goods_dic[user_choice]['price']))
                    print('添加到购物车成功！\n')
                else:
                    print("输入有误，请重新输入哦\n")
    else:
        print('请先登录哦\n')

def sign_out():
    """
    退出程序
    :return:None
    """
    exit('退出程序！')

def display():
    """
    程序入口，显示
    :return:None
    """
    msg = """---- 欢迎来到老男孩购物商城 ----
        1 注册
        2 登录
        3 购物
        4 退出
    """
    dic = {
        '1': register,
        '2': login,
        '3': buy,
        '4': sign_out,
    }
    while 1:
        print(msg)
        keys = input('请输入你要选择的操作序号>>>:')
        if keys in dic:
            dic[keys]()
        else:
            print('输入有误，请输入序号哟')
            continue

if __name__ == '__main__':
    display()