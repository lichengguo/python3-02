from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
"""
django的请求和响应
"""
class DemoView(View):
	def get(self,request):
		print(request)
		"""打印效果:
		# from django.http.request import HttpRequest
		<WSGIRequest: GET '/view/req/'>
		"""
		print(request)
		return HttpResponse("ok")

"""
drf的请求和响应
"""
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.request import Request
class DemoAPIView(APIView):
	def get(self,request):
		print(request)
		"""打印效果
		<rest_framework.request.Request object at 0x00000212CE889AC8>
		"""
		print(request._request)
		"""打印效果
		<WSGIRequest: GET '/view/req2/'>
		"""
		return Response("ok")


"""
drf的request对象: rest_framework.request.Request
drf的request对象是一个新声明的对象,他在django的request对象基础上,进行扩充,而原来django的request对象作为了drf的request对象的属性_request
drf的request对象会自动根据客户端的http请求中的Content-Type来判断请求的数据格式,通过数据格式,在parsers类中进行自动接收数据并转换数据格式为dict字典
request.data  获取POST/PUT/PATCH请求提交过来的请求体数据
request.query_params  获取地址中的查询字符串,它是django的request.GET的别名属性
"""
from rest_framework.views import APIView
from rest_framework.response import Response
class Demo2APIView(APIView):
	def post(self,request):
		data = request.data
		print( data.get("name") )
		return Response("使用request对象获取数据")

"""
drf的response对象操作与原来django的response对象是继承关系,那么用法上面就没什么区别了.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class Demo3APIView(APIView):
	def get(self,request):
		# Response(data=返回数据格式,status=响应状态码,headers={响应头的名称:响应头的值},content_type="返回内容的格式声明")
		return Response("使用response对象返回数据",status=status.HTTP_200_OK,headers={"company":"it-qishi"})


"""基础视图类
APIView是drf中最基础的一个API视图类,主要实现了开发接口的基本操作,它继承于Django的View,所以使用上来说和View一模一样
APIView仅仅只是在View的基础上, 内部实现了API的相关异常处理,调用drf的request和response类以及增加了一些额外的API接口选项功能[流量控制、身份认证和权限检查]
"""
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
class Student1APIView(APIView):
	def get(self,request):
		"""学生列表数据"""
		# 获取数据
		student_list = Student.objects.all()
		# 调用序列化器
		serializer = StudentSerializer(instance=student_list, many=True)
		# 返回数据
		return Response(serializer.data)


"""通用视图类
GenericAPIView,它继承了APIView，所以APIView有的功能，通用视图都会有，同时通用视图类还在APIView的基础，提供了一些额外的属性和方法
使用通用视图类，必须声明一个类属性，queryset！！！否则报错
queryset 当前视图类中公用的查询数据集，可以在类方法中通过self.get_queryset()获取类属性的值
get_serializer 当前视图类中公共的序列化器，可以在类方法中通过self.get_serializer() 获取类属性的值
               如果类中使用了多个序列化器，可以通过重写 self.get_serializer_class()方法来返回不同的序列化器
"""
from rest_framework.generics import GenericAPIView
class Student1GenericAPIView(GenericAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	def get(self,request):
		"""列表数据"""
		# 获取数据
		queryset = self.get_queryset()
		# 调用序列化器
		serializer = self.get_serializer(queryset, many=True)
		# 返回数据
		return Response(serializer.data)

"""
GenericAPI可以和drf提供的视图扩展类，很方便的实现基本的5个API接口
获取多条数据 
获取一条数据
修改一条数据
添加一条数据
删除一条数据
"""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
class Student2GenericAPIView(GenericAPIView,ListModelMixin,CreateModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	def get(self,request):
		"""学生列表数据"""
		return self.list(request)

	def post(self,request):
		return self.create(request)

"""
5个基本API接口一般分2类型：
列表API
	获取多条数据 
	添加一条数据
详情API
	获取一条数据
	删除一条数据
	修改一条数据

划分的标准：地址上面是否需要指定ID(PK)

"""
from rest_framework.mixins import RetrieveModelMixin
class Student3GenericAPIView(GenericAPIView,RetrieveModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	def get(self,request,pk):
		"""获取一个学生数据"""
		return self.retrieve(request)


"""视图子类
drf还提供了通用视图类的子类，供我们直接提供基本API接口的实现方法，我们只需要继承
这些视图子类就不用声明类方法，视图子类已经默认帮我们写好了。
"""
from rest_framework.generics import ListAPIView,CreateAPIView
class Student4GenericAPIView(ListAPIView,CreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView
class Student5GenericAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


"""视图集
前面不管django或者drf提供的视图类，都是基于HTTP请求来执行不同视图类方法的，所以，在有些不明确是否是增删查改的操作中(例如：权限判断，流量控制，登录退出等等)，
此时，使用视图类就不得不方便和不伦不类了。
所以，drf提供了视图集，视图集不在依靠HTTP请求来自动执行对应的视图类方法，而使用在路由中把HTTP请求方法和类方法进行命名绑定的方式来完成类方法的调用执行。
def实现视图集的核心点就是as_view方法
"""
from rest_framework.viewsets import ViewSet
class Student1ViewSet(ViewSet):
	def get_all_student(self,request):
		"""获取所有学生数据"""
		# 获取数据
		student_list = Student.objects.all()
		# 调用序列化器
		serializer = StudentSerializer(instance=student_list, many=True)
		# 返回数据
		return Response(serializer.data)

	def create_student(self,request):
		"""添加一个学生数据"""
		serializer = StudentSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

	def get_one_student(self,request,pk):
		student = Student.objects.get(pk=pk)
		serializer = StudentSerializer(student)
		return Response(serializer.data)


"""
通用视图集,
继承了通用视图类GenericAPIView和ViewSetMixin

注意:通用视图集也可以配合视图扩展类提供5个基本API接口
"""

from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
class Student1GenericViewSet(GenericViewSet,ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


"""
路由类为视图集生成路由列表
"""
from rest_framework.viewsets import GenericViewSet,ModelViewSet
class Student1ModelViewSet(ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer