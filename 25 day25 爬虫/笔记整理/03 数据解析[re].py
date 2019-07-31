# -*- encoding: utf-8 -*-
"""
@File    : 03 数据解析[re].py
@Time    : 2019/7/31 14:36
@Author  : Alnk
@Email   : 1029612787@qq.com
@Software: PyCharm
"""

"""
如何实现聚焦爬虫(数据解析)
    聚焦爬虫的编码流程
        1. 指定url
        2. 基于requests模块发起请求
        3. 获取响应对象中的数据
        4. 数据解析
        5. 进行持久化存储

如何实现数据解析
    三种数据解析方式
        正则表达式
        bs4
        xpath
"""

"""
# 如何爬取一张图片
import requests

# 1 指定URL
url = "https://pic.qiushibaike.com/system/pictures/12206/122065848/medium/57J15TGANJTJBS2J.jpg"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

# 2 基于requests模块发起请求
res = requests.get(url=url, headers=headers)

# 3 获取响应数据
page_content = res.content

# 4 持久化存储
with open('./qiutu.jpg', mode='wb') as f:
    f.write(page_content)
"""


"""
# 使用urllib模块下载图片
from urllib import request
url = "https://pic.qiushibaike.com/system/pictures/12207/122074760/medium/KLJKLR9S5KL0F3QA.jpg"
request.urlretrieve(url=url, filename='kobe.jpg')
"""

'''
# 正则表达式
import re
page_html = """
<a>111222</a>
<div class="thumb">
    <a href="/article/122065919" target="_blank">
        <img src="//pic.qiushibaike.com/system/pictures/12206/122065919/medium/RX08K1QIBROHKKK1.jpg" alt="今天送趟孩子">
    </a>
</div>
<div>4455</div>
"""

ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
print(re.findall(ex, page_html, re.S))
'''


"""
# 需求：爬取糗事百科指定页面的糗图，并将其保存到指定文件夹中
import os
import re
import requests
from urllib import request

url = "https://www.qiushibaike.com/pic/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
}

# 获取糗事百科糗图版块的页面全部数据
res = requests.get(url=url, headers=headers).text

# 通过正则匹配解析图片URL
ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
img_list = re.findall(ex, res, re.S)  # list数据类型
# print(img_list)

# 在本地创建存储图片的文件夹
if not os.path.exists('./qiutu'):
    os.mkdir('./qiutu')

# 向每张图片发送请求，获取每张图片
for i in img_list:
    img_url = 'https:' + i
    name = i.split('/')[-1]
    img_path = 'qiutu/' + name

    # 使用urllib发送请求获取并存储图片
    request.urlretrieve(url=img_url, filename=img_path)
"""
