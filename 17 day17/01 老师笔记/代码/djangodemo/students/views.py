from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
	return HttpResponse("<h1>hello django</h1>")


def list(reuqest):
	print("列表页1视图")
	return HttpResponse("<a href='%s'>首页</a>列表页2" % reverse("home:index") )

def list2(reuqest,mobile):
	print("列表页2视图")
	return HttpResponse("手机号：%s<br> <img src='/static/avatars/3.jpg'>列表页" % mobile)

def list3(request,cat,pn):
	return HttpResponse("cat=%s pn=%s" % (cat,pn) )

def list4(request,num, city):
	return HttpResponse("num=%s<br>city=%s" % (num,city))

def detail(request):
	"""获取查询字符串
	:param request 客户端请求对象，里面包含了所有提交过来的请求信息
	"""
	# 获取客户端请求行中的查询字符串

	print( request.GET )
	# 打印效果：
	# 返回的结果是一个对象，我们可以看做是一个类字典对象
	# <QueryDict: {'name': ['ziaoming']}>

	# [少用]获取查询字符串中的指定名称的参数值[一个值]
	# print( request.GET["name"] )
	# [常用]获取查询字符串中的指定名称的参数值[一个值]
	print( request.GET.get("name","佚名") )
	# getlist 获取查询字符串中的指定名称的参数值[多个值]
	print(request.GET.get("del") )     # 2 只会获取最后一个值
	print(request.GET.getlist("del") ) # ['1', '2']

	return HttpResponse("detail")

def detail2(request):
	"""
	获取请求内容
	:param request:
	:return:
	"""
	# 获取请求内容
	print( request.POST )
	# 打印效果：
	# reuqest.POST 返回结果和request.GET一致,，也是QueryDict对象
	# <QueryDict: {'username': ['小会']}>
	print( request.POST["username"] )
	print( request.POST.get("username","默认值") )
	print( request.POST.getlist("like") ) # ['游泳', '电脑']

	# 获取上传文件信息
	print( request._files )

	return HttpResponse("获取请求内容")

def detail3(request):
	"""获取请求内容[其他格式内容]"""
	# 其他格式数据: json/xml
	print(request.body)
	# request.body接受到数据，是bytes类型的数据
	# b'{\n\t"username": "xiaoming",\n\t"age":32,\n\t"achievement": 13.5,\n\t"son":{\n\t\t"username":"xiaoxiaoming",\n\t\t"age":12\n\t},\n\t"love":["\xe6\xb8\xb8\xe6\x88\x8f","\xe6\xb8\xb8\xe6\xb3\xb3"]\n}'
	# 我们需要手动对请求体中的数据进行识别转换
	data_str = request.body.decode()
	print(data_str)
	print(type(data_str)) # <class 'str'>
	import json
	data_dict = json.loads(data_str)
	print(data_dict)
	print(type(data_dict)) # <class 'dict'>
	return HttpResponse("获取请求内容")


def detail4(request):
	"""获取请求头
	:param request
	"""
	# http的请求头
	print( request.META.get("REQUEST_METHOD") ) # http请求方法
	# 自定义请求头[postman的请求头不支持中文]
	# 请求头名称必须大写,前面拼接 "HTTP_"
	print( request.META.get("HTTP_COMPANY") )
	# 客户端信息,服务器信息,服务器系统信息[环境变量],python解析器相关信息
	# """
	# {
	# 	 'OS': 'Windows_NT',
	# 	 'SERVER_PORT': '8000',
	# 	 'REMOTE_HOST': '',
	# 	 'SCRIPT_NAME': '',
	# 	 'REQUEST_METHOD': 'GET',
	# 	 'PATH_INFO': '/home/detail4/',
	# 	 'QUERY_STRING': '',
	# 	 'REMOTE_ADDR': '127.0.0.1',
	# 	 'CONTENT_TYPE': 'text/plain',
	# 	 'HTTP_USER_AGENT': 'PostmanRuntime/7.13.0',
	# 	 'HTTP_HOST': '127.0.0.1:8000',
	# """
	return HttpResponse("获取请求头信息")

def detail5(request):
	"""request对象的其他属性"""
	# print( request.method ) # 获取http请求方法, 等同于 request.META.get("REQUEST_METHOD")
	# print( request.FILES )  # 获取上传文件      等同于 request._files
	print( request.user )   # 获取已经登录的用户信息[模型对象]
	print( request.user.last_login )   # 获取登录用户的信息[如果没有登录,则报错]
	# 没有登录的用户访问,request.user = AnonymousUser

	return HttpResponse("request对象的其他属性")


def res1(request):
	"""响应html文档内容"""
	# 响应html
	# return HttpResponse(content="<h1>响应内容</h1>",content_type="text/plain; charset=utf-8")

	# 响应json
	data_dict = {
		"name":"xiaohong",
		"age":15
	}

	# import json
	# data_json = json.dumps(data_dict)
	# print(data_json)
	# return HttpResponse(content=data_json,content_type="application/json")

	# 响应xml数据
	data_xml = """<xml version="1.0" encoding="utf-8"><name>小红</name><age>15</age></xml>"""
	return HttpResponse(content=data_xml,content_type="text/xml")

# shortcuts 简写函数库
from django.shortcuts import redirect
def res2(request):
	"""页面重定向响应"""
	# return redirect("http://www.baidu.com")

	# redirect 其实本质上就是 HttpResponse的简写操作,以下是还原代码:
	response = HttpResponse(status=302)
	response["Location"] = "http://www.baidu.com"
	return response