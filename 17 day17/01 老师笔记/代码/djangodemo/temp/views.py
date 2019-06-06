# shortcuts 这个文件里面，声明了一系列 固定代码的简写函数
from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader
# Create your views here.
def index(request):
	"""

	:param request:
	:return:
	"""
	"""
	render 三个参数:
	1. 必填, request
	2. 必填, 模板路径,
	3. 模板中如果要使用数据,最好通过这里传递过去
	"""
	# return render(request, "son/index.html",{"title":"网页的标题"})
	return render(request, "index.html",{"title":"网页的标题"})

	"""
	# render函数是以下三句代码的简写: 
	template = loader.get_template("index.html")   # Engine类  -> 引擎配置调用和引擎的查找
	content = template.render({"title":"网页的新标题"},request) # DjangoTemplate模板引擎 -> 实现了模板的渲染工作
	return HttpResponse(content)  # HttpResponse -> 把内容返回给客户端
 	"""

from django.views import View
class HomeView(View):
	def get1(self,request):
		"""加载模板"""
		return render(request, "son/index.html")

	def get2(self,request):
		"""输出视图中的数据内容"""
		return render(request, "index.html", {"title": "网页的标题"})

	def get3(self,request):
		"""输出所有的字典/列表和元组,都需要使用点语法"""
		# print( (1,2,3)[2] )
		return render(request,"index.html",{
			"title":"新的标题",
			"tuple1": ("张三","李四",3,4,5),
			"list1": ["苹果","葡萄",'aaa','bbbb'],
			"dict1": {"title":"python","price":88.5}
		})

	def get4(self,request):
		"""模板中不支持使用函数,也不支持编写表达式"""
		print(len(['1','2']))
		return render(request,"index.html",{"num":100})

	def get5(self,request):
		# for (key,value) in dict1.items():
		# 	print(item)
		return render(request,"index.html",{
			"tuple1": ("张三","李四",3,4,5),
			"list1": ["苹果","葡萄",'aaa','bbbb'],
			"dict1": {"title":"python","price":88.5}
		})

	def get6(self,request):
		"""循环输出字典"""
		return render(request,"index.html",{
			"dict1": {"title":"python","price":88.5}
		})

	def get7(self,request):
		"""了解循环内部的遍历对象 forloop"""
		return render(request,"index.html",{
			"book_list": [
				{"title": "python1", "price": 68.5},
				{"title": "django1", "price": 88.5},
				{"title": "django1", "price": 88.5},
				{"title": "django1", "price": 88.5},
				{"title": "django1", "price": 88.5},
			]
		})

	def get8(self,request):
		"""判断输出"""
		return render(request,"index.html",{"num":21})

	def get9(self,request):
		"""多条循环语句或者判断语句之前可以嵌套使用"""
		return render(request, "index.html", {
			"book_list": [
				{"title": "python1", "price": 68.5},
				{"title": "django1", "price": 88.5},
				{"title": "django1", "price": 88.5},
				{"title": "django1", "price": 88.5},
				{"title": "django1", "price": 88.5},
			]
		})

	def get10(self,request):
		"""多层循环嵌套"""
		return render(request, "index.html", {
			"people": [
				{"name":"张三","age":24,"lve":["吹牛","睡觉","吃饭","看漫画"]},
				{"name":"lisi ","age":24,"lve":["吹牛","睡觉","吃饭","看漫画"]},
				{"name":"wangwu","age":24,"lve":["吹牛","睡觉","吃饭","看漫画"]},
				{"name":"老六","age":24,"lve":["吹牛","睡觉","吃饭","看漫画"]},
				{"name":"xiaohei","age":24,"lve":["吹牛","睡觉","吃饭","看漫画"]},
			]
		})

	def get(self,request):
		"""过滤器"""
		from datetime import datetime
		return render(request,"index2.html",{
			"title": "我是中国人，welcome to oldboy!",
			"title2": "<h1>大标题</h1>",
			"title3": "<h1>大标题</h1>",
			# "title4": "title4",
			"pub_date": datetime.now()
		})

"""模板继承"""
# class IndexView(View):
# 	def get(self,request):
# 		"""首页"""
# 		return render(request,"index/index.html",{"title":"标题"})
#
# class ListView(View):
# 	def get(self,request):
# 		"""商品列表页"""
# 		return render(request,"index/list.html",{"title":"标题"})

class IndexView(View):
	def get(self,request):
		"""首页"""
		return render(request,"exten/index.html",{"title":"标题"})

class ListView(View):
	def get(self,request):
		"""商品列表页"""
		return render(request,"exten/list.html",{"title":"标题"})

"""表单系统的使用"""
# 使用系统完成一个登陆的功能
# 先显示登录表单,提供给用户填写
# 用户提交表单信息到视图中接受,视图中验证数据
from .forms import LoginForm
class UserView(View):
	def get(self,request):

		return render(request,"form.html",{
			"forms":LoginForm(),
		})

	def post(self,request):
		"""提交表单"""
		# 使用表单系统提供的验证流程
		form = LoginForm(request.POST)
		if form.is_valid(): # is_valid 验证函数,会提取表单中的限制选项进行进行验证
			print( form.cleaned_data )
			print( "到数据库中查询账号密码,进行数据对比" )
		else:
			print("验证失败!")

		return render(request,"form.html",{
			# 这里必须返回的是用户提交过的表单对象，这个表单对象里面才会有错误信息
			"forms":form,
		})

"""模型类表单"""
from .forms import UserForm
class User2View(View):
	def get(self,request):
		return render(request,"form.html",{
			"forms": UserForm(),
		})