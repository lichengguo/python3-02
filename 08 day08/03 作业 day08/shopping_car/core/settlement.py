#!/usr/bin/env python3
# author:Alnk(李成果)
import os
import time
from shopping_car.conf.settings import user_info_path
from shopping_car.core import login
from shopping_car.core.basic import Basic
from atm.core import payment


class Settlement(Basic):  # 结算类

    def settlemnt(self):
        user_info_path_file = os.path.join(user_info_path, '%s.json' % login.user_name)
        user_info_dict = self.read_info(user_info_path_file)
        shopping_car = user_info_dict['shopping_car']  # 用户购物车存储字典

        while 1:
            total_money = 0
            for k in shopping_car:
                money = shopping_car[k]['price'] * shopping_car[k]['number']
                total_money += money  # 需要支付的总额
            print('\n需要支付金额[%s]\n' % total_money)

            if total_money == 0:
                print('没有商品不需要支付哦，先去选购商品吧\n\n')
                break

            # 调用atm接口进行支付
            p = payment.PayMent()
            ret = p.payment(total_money)
            if ret == 2:
                print('支付成功，开始清理购物车')
                time.sleep(3)
                del shopping_car
                user_info_dict['shopping_car'] = {}  # 清理购物车
                print('aaaaaaa', user_info_dict)
                self.write_info(user_info_dict, user_info_path_file)  # 写入文件
                print('购物车已经清空\n')
                return True
            elif ret == 0:
                print('银行卡号或者密码输错了\n')
                return
            elif ret == 1:
                print('余额不足!\n')
                print('请删除一些商品然后支付\n')
                while 1:
                    for k in shopping_car:
                        print(k,shopping_car[k]['price'],shopping_car[k]['number'])
                    action = input('\n请输入商品名称>>>')
                    if shopping_car.get(action):
                        # 商品数量为1,直接删除，否则减少商品的数量
                        if shopping_car[action]['number'] == 1:
                            del shopping_car[action]
                        elif shopping_car[action]['number'] > 1:
                            shopping_car[action]['number'] -= 1
                        break
