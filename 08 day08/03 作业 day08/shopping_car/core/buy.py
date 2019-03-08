#!/usr/bin/env python3
# author:Alnk(李成果)
import os
from shopping_car.core import login
from shopping_car.conf.settings import goods_info_dict, user_info_path
from shopping_car.core.settlement import Settlement


class Buy(login.Login, Settlement):  # 购物类

    def buy(self):  # 购物
        if login.login_flag:
            # 获取用户信息
            user_info_path_file = os.path.join(user_info_path, '%s.json' % login.user_name)
            user_info_dict = self.read_info(user_info_path_file)
            shopping_cat = user_info_dict['shopping_car']  # 用户购物车存储字典
            while 1:
                for key in goods_info_dict:  # 循环商品字典
                    print('\t', key, goods_info_dict[key]['name'], goods_info_dict[key]['price'])
                action = input("\n请输入你想购买的商品序号>>>")
                if action.lower() == "n":
                    # 调用结算接口支付
                    ret = self.settlemnt()
                    if ret == True:
                        print('\n支付完成了大兄弟!\n')
                        print('退出程序')
                        quit()
                elif action.lower() == 'q':
                    quit()
                elif goods_info_dict.get(action):  # 判断action的合法性
                    # 商品有没有已经添加过
                    if shopping_cat.get(goods_info_dict.get(action)['name']):
                        # 已经添加的商品直接数量+1
                        shopping_cat[goods_info_dict.get(action)['name']]['number'] += 1
                    else:
                        # 新的商品
                        shopping_cat[goods_info_dict.get(action)['name']] = {"number": 1, "price": goods_info_dict.get(action)['price'] }
                    print(user_info_dict)
                    self.write_info(user_info_dict, user_info_path_file)  # 写入文件
                else:
                    print("输入有误，请重新输入哦\n")
        else:
            print('先登录')
