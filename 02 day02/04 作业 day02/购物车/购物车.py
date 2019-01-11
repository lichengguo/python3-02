#!/usr/bin/env python3
#author:Alnk(李成果)
"""
作业需求:
1. 用户先给自己的账户充钱：比如先充3000元
2. 页面显示 序号 + 商品名称 + 商品价格，如：
    1 电脑 1999
    2 鼠标 10
    …
    n 购物车结算
3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品
4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入
5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，
    若充值的钱数充足，则可以直接购买
6. 用户输入Q或者q退出程序
7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少
"""

#商品列表
goods_dic = {
    "1":{"name":"电脑","price":1999,},
    "2":{"name":"鼠标","price":10,},
    "3":{"name":"键盘","price":60,},
    "4":{"name":"手机","price":4000,},
    "5":{"name":"ipad","price":2999,},
    "n":{"name":"购物车结算","price":'',},
}

#用户购物车
user_shopping_cart = {}

#标志位
flag = True

#充值
while flag:
    print('------------ 您好，欢迎来到老男孩购物商城 ----------------')
    user_balance = input("请先给账号充值(退出Q/q):")
    if user_balance.lower() == "q":
        print("退出，欢迎下次光临！")
        flag = False
    elif user_balance.isdigit():
        user_balance = int(user_balance)
        print("账号充值成功！余额为[%s]元\n" % (user_balance))
        break
    else:
        print("输入有误，请重新输入。")

#主程序
while flag:
    print("下列是您可以选购的商品(退出Q/q):")
    for key in goods_dic:
        print('\t',key,goods_dic[key]['name'],goods_dic[key]['price'])

    user_choice = input("请输入你想购买的商品序号:")
    if user_choice.lower() == "q":
        print("退出购物商城")
        flag = False

    #结算
    elif user_choice == "n":
        while flag:
            #显示购车里的商品
            print("\n您的购车里商品如下:")
            for k in user_shopping_cart:
                print("\t商品[%s] 数量[%s] 价格[%s]" % (k, user_shopping_cart[k]['number'] ,user_shopping_cart[k]['price']) )

            # 购物车所有商品总价
            shopp_cart_total = 0

            print("\n正在结算，请稍候...")
            #计算商品总价格
            for k in user_shopping_cart:
                shopp_cart_total = shopp_cart_total + user_shopping_cart[k]['number'] * user_shopping_cart[k]['price']

            #判断余额是否能够支付
            if user_balance >= shopp_cart_total:
                print("您本次总共需要支付[%s]元，余额为[%s]元" % (shopp_cart_total,user_balance))
                print("\n您本次购买的商品详单如下：")
                for k in user_shopping_cart:
                    print('\t商品[%s] 数量[%s] 价格[%s]' % (k, user_shopping_cart[k]['number'], user_shopping_cart[k]['price']) )
                print("\n本次总共消费[%s]元，账户余额为[%s]元" % (shopp_cart_total,user_balance-shopp_cart_total) )
                print("\n购买成功!")
                flag = False
            else:
                print("本次总共需要支付[%s]元 你的余额为[%s]元" % (shopp_cart_total,user_balance))
                print("余额不足，请先删除购物车里的一些商品再去结算哟\n")

                while flag:
                    print("\n购物车的商品列表如下:")
                    for k in user_shopping_cart:
                        print('\t商品[%s] 数量[%s] 价格[%s]' % (k,user_shopping_cart[k]['number'],user_shopping_cart[k]['price']) )

                    user_choice2 = input("请输入你想删除的商品名称:")
                    if user_shopping_cart.get(user_choice2):
                        if user_shopping_cart[user_choice2]['number'] == 1:
                            del user_shopping_cart[user_choice2]
                            print('商品[%s]已从购物车删除' % (user_choice2))
                        elif user_shopping_cart[user_choice2]['number'] > 1:
                            user_shopping_cart[user_choice2]['number'] -= 1
                            print("商品[%s]数量减少1件" % (user_choice2))
                        break
                    else:
                        print("\n输入的商品名称有误，请重新输入")

    #添加商品到用户购物车
    elif goods_dic.get(user_choice):
        if user_shopping_cart.get(goods_dic[user_choice]['name']):
            user_shopping_cart[goods_dic[user_choice]['name']]['number'] += 1
        else:
            user_shopping_cart[goods_dic[user_choice]['name']] = {"number":1,"price":goods_dic[user_choice]['price']}
        print("\n商品[%s] 价格[%s] " % (goods_dic[user_choice]['name'], goods_dic[user_choice]['price']) )
        print('添加到购物车成功！\n')

    else:
        print("输入有误，请重新输入哦\n")