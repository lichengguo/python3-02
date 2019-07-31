# -*- encoding: utf-8 -*-
"""
@File    : 05 数据解析[xpath].py
@Time    : 2019/7/31 16:25
@Author  : Alnk
@Email   : 1029612787@qq.com
@Software: PyCharm
"""

"""
xpath解析
    - 通用性比较强
    - 环境的安装: pip install lxml
    - 解析原理:
        - 1. 实例化一个etree对象，且将解析的页面源码加载到该对象中
        - 2. 使用该对象中的xpath方法结合着xpath表达式进行标签定位和数据解析提取
    - etree对象的实例化:
        - 本地加载: 
            tree = etree.parse("filePath")
        - 网络加载: 
            tree = etree.HTML(page_text)

常用的xpath表达式: 基于标签的层级实现定位,返回的永远是一个列表
    - /: 从标签开始实现层级定位
    - //: 从任意位置实现标签的定位
    - 属性定位: tag[@attrName="attrValue"]
    - 索引定位: //div[@class="tang"]/ul/li[5] 注意索引值是从1开始
    - 取文本:
        - 取直系文本内容: /text()
        - 取所有文本内容: //text()
    - 取属性: /@attrName
"""

"""
# from lxml import etree
# tree = etree.parse('./test_page.html')  # 实例化对象
# print(tree.xpath('//div[@class="tang"]'))  # 查找div属性为tang的标签，返回一个列表
# print(tree.xpath('//div'))  # 查找素有的div标签

# print(tree.xpath('//div[@class="tang"]/ul/li[3]'))  # 查找div的class属性为tang的标签下的ul标签下的第三个li标签
# print(tree.xpath("//div[@class='song']/p[4]/text()"))  # 查找class属性为song的div标签下的第四个p标签的文本内容
# print(tree.xpath("//div[@class='song']/p[4]/text()")[0])  # 查找class属性为song的div标签下的第四个p标签的文本内容

# text_list = tree.xpath('//div[@class="song"]//text()')
# print(text_list)
# text_str = ''.join(text_list)
# print(text_str.strip())

# print(tree.xpath("//div[@class='tang']/ul/li[1]/a/@href"))  # 获取a标签href属性值
# print(tree.xpath("//div[@class='tang']/ul/li[1]/a/text()"))  # 获取a标签直系文本值

# print(tree.xpath("//div[@class='song']/img/@src"))
"""


"""
案例：爬取58二手房的房源信息

"""


"""
需求: 爬取当前页面全部的城市名称https://www.aqistudy.cn/historydata/

import requests
from lxml import etree

# 1 指定URL
url = 'https://www.aqistudy.cn/historydata/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

# 2 发送请求，获取收据
page_text = requests.get(url=url, headers=headers).text

# 3 实例化一个etree对象，解析数据
tree = etree.HTML(page_text)
all_city_names = tree.xpath('//div[@class="bottom"]/ul/li/a/text() | //div[@class="bottom"]/ul/div[2]/li/a/text()')
# 最重要的一个知识点，就是管道符|, 它表示或的意思，只要满足其中一个条件就可以匹配到

# 4 打印数据
print(len(all_city_names), all_city_names)
"""



"""
需求：处理中文乱码

import requests
from lxml import etree

url = "http://pic.netbian.com/4kqiche/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

response = requests.get(url=url, headers=headers)
# 手动设置响应数据的编码格式
# response.encoding = "utf-8"

page_text = response.text

tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul/li')

for li in li_list:
    img_src = "http://pic.netbian.com" + li.xpath("./a/img/@src")[0]  # ./ 表示当前标签 ./表示的就是li标签
    img_name = li.xpath('./a/b/text()')[0]
    img_name = img_name.encode("iso-8859-1").decode("gbk")

    print(img_src, img_name)
"""
