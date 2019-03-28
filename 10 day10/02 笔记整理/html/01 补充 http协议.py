#!/usr/bin/env python3
#author:Alnk(李成果)
'''
GET\POST请求方式差异：
    1、传送方式：get通过地址栏传输，post通过报文传输
    2、传送长度：get参数有长度限制（受限于url长度），而post无限制
    3、GET和POST还有一个重大区别，
        简单的说：
            GET产生一个TCP数据包；POST产生两个TCP数据包
        长的说：
            对于GET方式的请求，浏览器会把http header和data一并发送出去，服务器响应200（返回数据）；
            对于POST，浏览器先发送header，服务器响应100 continue，浏览器再发送data，服务器响应200 ok（返回数据）
    4、建议：
        1、get方式的安全性较Post方式要差些，包含机密信息的话，建议用Post数据提交方式；
        2、在做数据查询时，建议用Get方式；而在做数据添加、修改或删除时，建议用Post方式；

URL格式：
    协议 /  域名  /  路径  /  参数
    https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=alex

补充http协议：
                            请求协议
    浏览器 -----------------------------------------------> 服务器
           <-----------------------------------------------
                            响应协议

    https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=alex
    http之请求协议格式：
        第一种 GET方式
            GET   /s?a=1&b=2  HTTP/1.1          # 请求首行 （/s 是路径,问号以后的是参数数据）
            看 01 请求头.png                    # 请求头
            空行                                # 空行
            None                                # 请求体 （get请求没有请求体）

        第二种 POST方式
            POST   /s  HTTP/1.1        # 请求首行 （/s 是路径）
            看 01 请求头.png           # 请求头
            空行                       # 空行
            a=1&b=2                    # 请求体


    http之响应协议格式：
        HTTP/1.1 200 OK         # 响应首行
        看 01 响应头.png        # 响应头
        html页面字符串          # 响应体
'''


'''
GET请求示例 
# 请求首行
GET / HTTP/1.1

# 请求头
Host: 127.0.0.1:8899
Connection: keep-alive
Cache-Control: max-age=0
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6776.400 QQBrowser/10.3.2577.400
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9

# 空行
\r\n  

# 请求体（无请求体）
'''


'''
POST请求示例

# 请求首行
POST / HTTP/1.1

# 请求头
Host: 127.0.0.1:8899
Connection: keep-alive
Content-Length: 17
Cache-Control: max-age=0
Origin: http://localhost:63342
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://localhost:63342/python3_14/10%20day10/02%20%E7%AC%94%E8%AE%B0%E6%95%B4%E7%90%86/11%20form%E6%A0%87%E7%AD%BE%E4%B8%8Eweb%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%BA%A4%E4%BA%92.html?_ijt=tg0k7v9jag2hm67q5ss7lan9ap
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8

# 空行
\r\n

# 请求体
user=alnk&pwd=123
'''