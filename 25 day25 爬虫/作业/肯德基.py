# -*- encoding: utf-8 -*-

# 需求：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据

import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'  # 指定URL

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

city_lis = list()

for i in range(1, 9):
    params = {
        'cname': '',
        'pid': '',
        'keyword': '杭州',
        'pageIndex': i,
        'pageSize': '10',
    }
    res = requests.post(url=url, data=params, headers=headers)  # 请求数据
    for dic in res.json()['Table1']:  # 处理数据
        city_lis.append(dic)

print(city_lis)

# for dic in city_lis:
#     print(dic['rownum'], dic['storeName'], dic['addressDetail'], dic['pro'], dic['provinceName'], dic['cityName'])
