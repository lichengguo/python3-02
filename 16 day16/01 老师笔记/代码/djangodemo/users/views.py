from django.shortcuts import render

# Create your views here.
# def login(request):
# 	pass
#
# def information(request):
# 	pass
#
# def register(request):
# 	pass
#
# def password(request):
# 	pass

"""
# django的类视图一共提供了多个以http请求方法命名的类方法给我们使用。
# 当客户端使用不同的http请求方法访问当前视图类，django会根据请求方法访问到当前类视图中的同名对象方法中。
# http常用请求方法
# GET 客户端向服务端请求读取数据
# POST 客户端向服务器请求创建数据
# PUT  客户端向服务器请求修改数据[全部]
# PATCH  客户端向服务器请求修改数据[修改部分数据]
# DELETE 客户端向服务器请求删除数据
"""
from django.views import View
from django.http.response import HttpResponse
class UserView(View):

	def post(self,request):
		print( request.method.lower() )
		print("客户端进行post请求")
		return HttpResponse("post")

	def get(self,request):
		print("客户端进行get请求")
		return HttpResponse("get")

	def put(self,request):
		print("客户端进行put请求")
		return HttpResponse("put")

	def delete(self,request):
		print("客户端进行delete请求")
		return HttpResponse("delete")


def my_decorator(func):
	def wrapper(request, *args, **kwargs):
		print('自定义装饰器被调用了')
		print('请求路径%s' % request.path)
		return func(request, *args, **kwargs)
	return wrapper

@my_decorator
def decoratordemo(request):
	return HttpResponse("函数视图")

"""不能直接在类视图的方法中直接使用装饰器,会出现参数位置的错误,会多传递一个self当前对象给装饰器,从而导致错误"""
# class UAPI(View):
# 	@my_decorator
# 	def get(self,request):
# 		return HttpResponse("类视图使用装饰器")


class UAPI2(View):
	def get(self,request):
		return HttpResponse("类视图使用装饰器")

"""要装饰类方法,可以使用django.utils.decorators.method_decorator装饰器来装饰"""
from django.utils.decorators import method_decorator
# class UAPI3(View):
# 	@method_decorator(my_decorator)
# 	def get(self,request):
# 		return HttpResponse("类视图get方法使用装饰器")
#
# 	@method_decorator(my_decorator)
# 	def post(self,request):
# 		return HttpResponse("类视图post方法使用装饰器")

# 在开发中，一般不建议在类中的方法上面添加装饰器，而是建议写在类的前面
# @method_decorator(my_decorator,name="get")
# @method_decorator(my_decorator,name="post")
# class UAPI3(View):
# 	def get(self,request):
# 		return HttpResponse("类视图get方法使用装饰器")
#
# 	def post(self,request):
# 		return HttpResponse("类视图post方法使用装饰器")


"""如果同一个类中所有方法公用一个装饰器，把装饰器添加到dispatch中，因为类视图中任意一个方法都会执行到as_view,as_view里面必然调用了当前对象的dispatch"""
@method_decorator(my_decorator,name="dispatch")
class UAPI3(View):
	def get(self,request):
		return HttpResponse("类视图get方法使用装饰器")

	def post(self,request):
		return HttpResponse("类视图post方法使用装饰器")


"""在多个类视图中如果要公用代码，可以使用多继承[Mixin扩展类]"""
@method_decorator(my_decorator,name='dispatch')
class BaseView(View):
	pass

class UAPI4(BaseView):
	def get(self,request):
		return HttpResponse("类视图4get方法使用装饰器")

	def post(self,request):
		return HttpResponse("类视图4post方法使用装饰器")


class MyDecoratorMixin(object):
	@classmethod
	def as_view(cls, *args, **kwargs):
		print( super() ) # View
		view = super().as_view(*args, **kwargs)
		# 进行装饰
		view = my_decorator(view)
		return view

class DemoView(MyDecoratorMixin, View):
	def get(self, request):
		print('get方法')
		return HttpResponse('getok')

	def post(self, request):
		print('post方法')
		return HttpResponse('postok')

from .models import Student
class StudentView(View):
	def post1(self,request):
		"""数据库操作：添加数据"""
		# save添加数据
		student = Student(
			name="刘德华",
			age=17,
			sex=1,
			class_no=305,
			money=10000,
			born="1964-10-01",
			description="17岁那天不要脸~"
		)

		student.save()

		# 响应结果
		return HttpResponse("post")
	def post(self,request):
		"""数据库操作：使用模型管理器 objects 提供的 create 添加数据
		模型.objects.create(
			字段名=字段值,
			字段名=字段值,
			字段名=字段值,
		)

		# 返回值都是一个模型对象

		"""

		student = Student.objects.create(
			name='周星星',
			class_no='304',
			sex=1,
			age=18,
			money=100000,
			born='1978-01-03',
			description='少林功夫好~好耶~'
		)

		print(student)

		# 响应结果
		return HttpResponse("post")

	def get1(self,request):
		"""查询一条数据"""
		# 根据主键id获取数据
		# 模型.objects.get(字段名=值)
		student = Student.objects.get(id=102)
		# student = Student.objects.get(pk=102) # 主键未必是叫ID,但是pk变量一定是代表了主键
		print( student ) # 学生：周星星

		# 通过模型对象获取对应的字段值
		print( student.description )
		print( student.born )

		# 使用get获取一条数据时,如果找不到数据会报错 DoesNotExist !
		# 为了避免因为数据库查询错误导致程序中断或出现其他异常,我们需要使用容错异常处理语句
		try:
			student = Student.objects.get(id=200)
			print(student)
		except Student.DoesNotExist:
			print("查无此人!")

		return HttpResponse("获取一条数据")


	def get2(self,request):
		"""获取所有数据"""

		student_list = Student.objects.all()
		print(student_list) # 结果是一个对象,模型的查询结果集对象,这个QuertSet我们可以看做是一个类列表的对象

		# 可以通过循环把查询结果提取出来
		for student in student_list:
			print(student.name)

		# 还可以对于所有的数据进行统计
		count = Student.objects.count()
		print( count )

		return HttpResponse("获取所有数据")

	def get3(self,request):
		"""根据条件筛选,查询多条数据"""


		# 查询305班所有学生
		# 单个条件
		# student_list = Student.objects.filter(class_no__exact=305)
		student_list = Student.objects.filter(class_no=305)
		# print(student_list)

		# 根据2个条件查询多个数据[必须同时满足多个条件]
		student_list = Student.objects.filter(age=22,sex=1)
		# print(student_list)

		# 模糊查询
		# 查询姓王的所有同学
		student_list = Student.objects.filter(name__startswith="王")
		# print(student_list)

		# 查询所有名字中带"文"的学生
		student_list = Student.objects.filter(name__contains="文")
		# print(student_list)


		# 范围查询
		# 例如，查询出303,304,305的所有学生
		student_list = Student.objects.filter(class_no__in=[303,304,305])

		# 例如，查询303,304,305的所有男生
		student_list = Student.objects.filter(class_no__in=[303,304,305], sex=1)


		# 比较查询
		# 例如，年龄小于19岁的学生
		# age__lte=19 表示年龄小于或等于19岁
		# age__lt=19 表示年龄小于19岁
		# age__gt=19 表示年龄大于19岁
		# age__gte=19 表示年龄大于或等于19岁
		student_list = Student.objects.filter(age__lt=19)

		# 不等于
		# exclude 用法和filter一致，但是结果相反
		student_list = Student.objects.exclude( age=19 )

		# 查询1999年出生的学生
		student_list = Student.objects.filter( born__year="1999" )

		# 查询6月份生日的学生
		student_list = Student.objects.filter(born__month="6")

		# 查询1997年1月1日以后出生的学生
		from datetime import date
		student_list = Student.objects.filter(born__gt=date(1997,1,1))
		# print(student_list)


		# 针对多条件中的逻辑运算，要Q对象来完成
		# 多个条件并且    Q(字段__运算符=值) & Q(字段__运算符=值)
		# 多个条件或者    Q(字段__运算符=值) | Q(字段__运算符=值)
		# 单个条件取反    ~Q(字段__运算符=值)    不推荐使用，可以直接使用exclude来代替

		# 查询1997年 或者 1999年 出生
		from django.db.models import Q
		student_list = Student.objects.filter( Q(born__year=1997) | Q(born__year=1999) ) # 或者
		# print(student_list)

		# 复杂的Q查询
		# 查询1997年以后出生的女生 或者 1998年出生以后的男生
		student_list = Student.objects.filter( Q( born__gt=date(1997,1,1),sex=2 ) | Q(born__gt=date(1998,1,1),sex=1) )


		# F对象可以在查询数据值时，进行字段间的比较
		# ID比年龄小的学生
		from django.db.models import F
		student_list = Student.objects.filter( id__lt= F('age') )
		print(student_list)

		return HttpResponse("查询多条数据")


	def get4(self,request):
		"""使用聚合函数来对多条数据进行统计"""
		from django.db.models import Sum,Avg,Max,Min,Count
		# result = Student.objects.filter(sex=1).aggregate( Count('sex') )
		# print( result ) # {'sex__count': 59}
		result = Student.objects.filter(sex=1).count()
		# print(result) # 59

		# # 年龄最大的
		result = Student.objects.aggregate(Max('age'))
		print(result) # {'age__max': 23}

		# 出生最早的
		# result = Student.objects.aggregate(Min('born'))
		# {'born__min': datetime.date(1964, 10, 1)}

		return HttpResponse("聚合函数")


	def get5(self,request):
		"""排序"""
		# 降序   从大到小   -字段名
		# 升序   从小到大   字段名
		# 按年龄进行升序
		student_list = Student.objects.all().order_by("-age")
		print(student_list)

		return HttpResponse("排序")

	def put(self,request):
		"""更新数据"""

		# 使用save除了添加数据以外,也可以进行更新
		# 例如,修改id=102的学生的年龄为41岁
		# student = Student.objects.get(pk=102)
		# student.age = 41
		# student.sex = 1
		# student.class_no = 305
		# student.save()

		# 使用update进行更新数据[修改操作必须加上条件，否则默认修改全部数据]
		# 返回之就是被修改操作影响的数据表行数
		# result = Student.objects.filter(pk=102).update(age=18,sex=1,class_no=304)
		# print( result )

		return  HttpResponse("更新")

	def delete(self,request):
		"""删除数据"""
		# 删除一条数据
		try:
			student = Student.objects.get(id=102).delete()
		except Student.DoesNotExist:
			print("当前数据已经被删除！")

		# 删除多条数据
		result = Student.objects.filter(id__gt=100).delete()
		print(result) # 返回结果，(3, {'users.Student': 3})
		return HttpResponse("删除")


	def get6(self,request):
		"""关于save方法的使用"""
		"""
		面试题：save怎么识别是添加或者更新操作的
		# 依靠save方法中判断当前模型是否存在primary_key的主键值来识别。
		  if not field.primary_key and not hasattr(field, 'through'):
		"""
		# student = Student(
		# 	name='周小星',
		# 	class_no='304',
		# 	sex=1,
		# 	age=18,
		# 	money=100000,
		# 	born='1978-01-03',
		# 	description='少林功夫好~好耶~'
		# )
		#
		# student.save()

		student = Student.objects.get(pk=106)
		student.name='周大型'
		student.save()
		return HttpResponse(student)

	def get(self, request):
		"""数据集 QuerySet
		0. 支持切片
		1. 惰性执行，只有在输出结果的时候，ORM才会真正的操作数据库
		2. 缓存查询结果
		"""
		# student_list = Student.objects.filter(id=33)
		# input("准备：")
		# print( student_list )  # 此时才会到数据库中进行读取操作【第一次输出结果时，才是mysql的SQL语句执行的地方】

		# 支持切片
		# print( student_list[:10] ) # 获取前10条数据
		# 除了提供基本的列表操作功能，还支持数据的查询缓存

		# 缓存数据结果
		student_list = Student.objects.filter(id__lt=33)
		# 针对循环结构中的查询集，django会自动缓存

		for student in student_list:
			print(student.name)


		print('------')
		for student in student_list:
			print(student.name)

		return HttpResponse("ok")