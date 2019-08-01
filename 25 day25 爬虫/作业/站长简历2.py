# -*- encoding: utf-8 -*-
"""
@File    : 05 数据解析[xpath].py
@Time    : 2019/7/31 16:25
@Author  : Alnk
@Email   : 1029612787@qq.com
@Software: PyCharm
"""
import os
import requests
from lxml import etree
from urllib import request
"""
尽量多获取数据，所以无法连接的报错直接忽略了
"""

# 创建简历文件夹，用于存放简历图片
if not os.path.exists('./resume2'):
    os.mkdir('./resume2')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

# 存储首页数据列表
page_text_list = list()
for i in range(1, 20):
    try:
        # 指定首页URL
        if i == 1:
            url = "http://sc.chinaz.com/jianli/free.html"
        else:
            url = "http://sc.chinaz.com/jianli/free_%s.html" % i
        print('=====', url)
        # 发送首页请求
        response = requests.get(url=url, headers=headers, timeout=15)
        # 获取首页数据
        response.encoding = "utf-8"
        page_text = response.text
        page_text_list.append(page_text)
    except Exception as e:
        print('e1', e)
        continue

# 循环page_text_list列表中每个首页的数据
for page_text in page_text_list:
    try:
        # 实例化etree对象
        tree = etree.HTML(page_text)
        # 解析首页数据，获取首页div标签
        resume_div_lis = tree.xpath("//div[@class='box col3 ws_block']")
        # 详情页链接列表
        detail_lis = list()
        # 把每个详情页的链接添加的列表
        for div in resume_div_lis:
            resume_lis_img_url = div.xpath("./a/@href")[0]  # 详情页下载链接
            detail_lis.append(resume_lis_img_url)
        print('detail_lis', detail_lis)

        # 访问每个详情页
        for detail_url in detail_lis:
            detail_response = requests.get(url=detail_url, headers=headers, timeout=15)  # 向每个详情页的url发送请求
            detail_response.encoding = "utf-8"
            detail_page_text = detail_response.text  # 获取数据
            detail_tree = etree.HTML(detail_page_text)  # 实例化一个对象
            detail_img_url = detail_tree.xpath("//div[@class='show_warp jl_warp clearfix']/span/img/@src")[0]  # 解析详情页数据
            resume_lis_img_name = detail_tree.xpath("//div[@class='ppt_tit clearfix']/h1/text()")[0]  # 获取名词

            # 使用urllib发送请求获取并存储图片
            filename = './resume2/' + resume_lis_img_name + '.jpg'
            request.urlretrieve(url=detail_img_url, filename=filename)
    except Exception as e:
        print('e2', e)
        continue
