# -*- encoding: utf-8 -*-
"""
@File    : 04 数据解析[bs4].py
@Time    : 2019/7/31 15:40
@Author  : Alnk
@Email   : 1029612787@qq.com
@Software: PyCharm
"""

"""
bs4数据解析
    - 环境安装:
        pip install bs4
        pip install lxml # 它是一个解析器,如果使用bs4进行数据解析,需要依靠lxml
    - BeautifulSoup解析原理:
        - 实例化一个BeautifulSoup对象,并将需要解析的页面源码数据加载到对象中
        - 使用该对象的相关属性和方法进行数据解析或提取
    - 如何实例化一个BeautifulSoup对象
        - 本地加载: 
            soup = BeautifulSoup("./test_page.html", "lxml")
        - 网络加载: 
            soup = BeautifulSoup(page_text, "lxml")
    - BeautifulSoup对象相关的属性和方法
        - soup.tagName 获取页面源码中遇到的第一个标签
        - 取属性: 返回的永远是一个单数
            - soup.tagName.attrs 取得标签里面所有的属性
            - soup.tagName.attrs[属性名] 取标签的单个属性
            - soup.tagName[属性名] 取标签的单个属性
        - 取文本:
            - soup.string: 只可以获取直系标签中的文本内容
            - soup.text: 获取标签下的所有文本内容
            - soup.get_text(): 获取标签下的所有文本内容
        - find() 返回的永远是一个单数
            - find(tagName): 通过标签名进行数据解析
            - find(tagName, 标签属性): 通过标签属性进行标签定位
        - find_all() 返回的永远是一个列表
            - 找到所有符合要求的标签
        - select 选择器 返回的永远是一个列表
            - 标签选择器, 类选择器, ID选择器, 层级选择器
            - 层级选择器:
                - 单层级: soup.select(".tang > ul > li")
                - 多层级: soup.select(".tang li")
"""
'''
# from bs4 import BeautifulSoup

# 实例化一个BeautifulSoup对象,并将需要解析的页面源码数据加载到对象中
# fp = open('./test_page.html', mode='r', encoding='utf-8')  # 打开一个文件
# soup = BeautifulSoup(fp, "lxml")  # 实例化

# print(soup)  # 打印这个页面
# print(soup.head)  # 打印head标签所有内容
# print(soup.body)  # 打印body标签
# print(soup.div)  # 打印遇到的第一个div标签
# print(soup.a)  # 打印遇到的第一个a标签
# print(soup.a.attrs['title'])  # 打印a标签里面的title属性内容
# print(soup.a.attrs['href'])  # 打印a标签里面的href属性内容
# print(soup.a['title'])  # 打印a标签里面的title属性内容
# print(soup.p)  # 打印第一个P标签
# print(soup.p.string)  # 打印标签里的文本
# print(soup.p.text)  # 打印标签里的文本
# print(soup.p.get_text())  # 打印标签里的文本

# print(soup.find('a'))  # 找到第一个a标签
# print(soup.find('div', class_='tang'))  # 找到class='tang' 的div标签
# print(soup.find('div', class_='tang').string)  # 只可以获取直系标签中的文本内容 ,本次实验返回为None
# print(soup.find('div', class_='tang').text)  # 获取标签下的所有文本内容
# print(soup.find('div', class_='tang').get_text())  # 获取标签下的所有文本内容

# print(soup.find_all('div'))  # 找到所有的div标签，返回值是一个列表
# print(soup.find_all(['div', 'p']))  # 找到所有的 div 和 P 标签，返回值是一个列表
# print(soup.find_all('li', limit=2))  # 从上往下，找到2个li标签，返回一个列表

# print(soup.select('.song'))  # 找到属性有song的标签，返回值是一个列表
# print(soup.select(".tang > ul > li"))  # 找到tang属性下的ul下的li标签，返回的是由li标签组成的列表
# print(soup.select(".tang li"))  # 找到tang属性下的li标签，返回的是由li标签组成的列表
'''


'''
案例：
    爬取三国演义上面的文章内容
'''
import requests
from bs4 import BeautifulSoup

url = 'http://www.shicimingju.com/book/sanguoyanyi.html'  # 首页的URL

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

page_text = requests.get(url=url, headers=headers).text  # 获取首页所有的内容

soup = BeautifulSoup(page_text, 'lxml')  # 实例化
li_list = soup.select('.book-mulu li')  # 获取每一章节的li标签，返回一个列表

f = open('sanguo.txt', encoding='utf-8', mode='w')  # 打开一个文件句柄

for li in li_list:
    detail_url = "http://www.shicimingju.com" + li.a['href']  # 每张详细内容的url
    title = li.a.string  # 每个章节的标题

    # 向详情页的URL发送请求，获取详情页的文本数据
    detail_page_text = requests.get(url=detail_url, headers=headers).text  # 获取详情页所有的内容
    detail_soup = BeautifulSoup(detail_page_text, 'lxml')  # 这里在实例化一次，对详情页的数据进行过滤
    detail_text = detail_soup.find("div", class_="chapter_content").text

    f.write(title + detail_text + '\n')  # 写入到文件

f.close()
