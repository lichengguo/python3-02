"""
requests模块的意义:
    发送请求获取响应数据

requests模块的作用:
    模拟浏览器发送请求

requests模块的安装:
    pip3 install requests

requests模块的编码流程
    指定URL
    发送请求
    获取响应数据
    持久化存储

反爬机制: UA检测(User-Agent)
反反爬策略: UA伪装
"""


"""
# 需求: 爬取搜狗首页的页面数据
import requests

# 1.指定URL
url = "https://www.sogou.com/"

# 2.发送请求
response = requests.get(url=url)
print(response, type(response))

# 3.获取响应数据
page_text = response.text
# print(page_text, type(page_text))

# 4.持久化存储，存储到文件或者数据库
with open('sogou.html', encoding='utf-8', mode='w') as f:
    f.write(page_text)
"""


"""
需求：爬取搜狗指定词条搜索后的页面数据

import requests

search = input('输入需要搜索的关键词>>:')

# 1.指定URL
url = "https://www.sogou.com/web"
param = {
    "query": search,
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

# 2.发送请求
response = requests.get(url=url, params=param, headers=headers)
response.encoding = 'utf-8'  # 防止乱码

# 3.获取响应数据
page_txt = response.text
print(page_txt)

# 4.持久化存储
name = search + ".html"
with open(name, encoding='utf-8', mode='w') as f:
    f.write(page_txt)
# 总结:
# 1.在通过requests发送请求时,携带了参数
# 2.进行了UA伪装,破解服务器的UA检测反爬机制
"""


"""
需求：爬取 百度 指定词条搜索后的页面数据
import  requests

wd = input('>>>:')
# 1 指定url
url = "https://www.baidu.com/s"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}
param = {
    "wd": wd,
}
# 2 发送请求
response = requests.get(url=url, params=param, headers=headers)
print(response)
# response.encoding = 'utf-8'
# 3 获取响应数据
page_text = response.text
# print(page_text)
# 4 持久化存储
name = wd + '.html'
with open(name, encoding='utf-8', mode='w') as f:
    f.write(page_text)
"""


"""
# 需求：百度翻译

import requests

# 1 指定URL
wd = input('翻译>>>')
url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}
param = {
    "kw": wd
}

# 2 发送请求
response = requests.post(url=url, data=param, headers=headers)

# 3 获取数据
# page_txt = response.text
# # print(page_txt)
# import json
# page_dict = json.loads(page_txt)
# print(page_dict)
# 返回的数据是json格式
page_dict = response.json()
print(page_dict)

# 4 持久化存储

# 总结:
# 1.使用requests的POST请求方式发送请求,并携带参数
# 2.指定响应对象的编码方式
# 3.在响应对象的数据类型为JSON的前提下,可以使用response.json()方法直接获取json数据
"""


"""
# 需求：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据
# 分析: 此页面上的数据是通过ajax请求获取到的数据"""
import requests

url = "https://movie.douban.com/j/chart/top_list"
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "100",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}
obj_json = requests.get(url=url, params=params, headers=headers).json()
print(len(obj_json))
# print(len(obj_json), obj_json)  # 这里用jupyter运行没问题，直接用pycharm运行会报编码错误
# UnicodeEncodeError: 'gbk' codec can't encode character '\xf6' in position 8341: illegal multibyte sequence



"""
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
"""


"""
# 需求：爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据http://125.35.6.84:81/xk/

# 分析: 
#     1. 首页企业名称列表的数据是通过ajax动态请求获取到的
#     2. 我们获取到的首页企业名称列表的数据里面有一条ID数据很重要,需要通过这个ID来获取详情页的URL
#     3. 企业详情页的数据也是通过ajax请求动态获取到的
#     4. 获取企业详情页的数据发送的请求携带的参数就有这个ID值,通过这个请求才能获取到企业详情页的数据

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
print(len(detail_lis))
"""
