# -*- encoding: utf-8 -*-

"""
# 需求：爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据http://125.35.6.84:81/xk/

# 分析:
#     1. 首页企业名称列表的数据是通过ajax动态请求获取到的
#     2. 我们获取到的首页企业名称列表的数据里面有一条ID数据很重要,需要通过这个ID来获取详情页的URL
#     3. 企业详情页的数据也是通过ajax请求动态获取到的
#     4. 获取企业详情页的数据发送的请求携带的参数就有这个ID值,通过这个请求才能获取到企业详情页的数据
"""

import requests
url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}
company_id = list()  # 用来保存公司的ID
for i in range(1, 3):  # 先爬取2页数据,页数太多会报错
    params = {
        'on': 'true',
        'page': i,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': '',
    }
    res = requests.post(url=url, data=params, headers=headers)  # 请求数据
    for dic in res.json()['list']:  # 获取每个公司的ID，添加到列表
        company_id.append(dic['ID'])
# print(company_id)

detail_url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById"
detail_lis = list()  # 用来存放公司详情页信息的列表
for id_ in company_id:
    detail_params = {
        'id': id_
    }
    detail_res = requests.post(url=detail_url, data=detail_params, headers=headers).json()
    detail_lis.append(detail_res)

print(len(detail_lis), detail_lis)
