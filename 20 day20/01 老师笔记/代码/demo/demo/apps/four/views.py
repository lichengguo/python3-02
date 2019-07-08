"""
身份认证和权限检查
"""
# from student.models import Student
# from .serializers import StudentSerializer
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
# class Student1ModelViewSet(ModelViewSet):
# 	queryset = Student.objects.all()[:2]
# 	serializer_class = StudentSerializer
# 	permission_classes = [IsAuthenticated]


"""
自定义权限
has_permission(self,request, view)             判断用户是否有访问视图的权限，返回值为True则表示有权限
has_object_permission(self,request,view,obj)   判断用户访问视图时，是否有操作数据模型的权限，返回值为True则表示有权限
"""
# from student.models import Student
# from .serializers import StudentSerializer
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import BasePermission
#
# # 自定义权限类
# class MyPermission(BasePermission):
# 	def has_permission(self, request, view):
# 		name = request.query_params.get("name")
# 		if name == 'zimakaimen':
# 			return True
#
# class Student1ModelViewSet(ModelViewSet):
# 	queryset = Student.objects.all()[:2]
# 	serializer_class = StudentSerializer
# 	permission_classes = [MyPermission]


"""限流"""
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
class Student1ModelViewSet(ModelViewSet):
	"""
	create:
	创建学生信息
	read:
	查询一条数据

	"""
	queryset = Student.objects.all()[:2]
	serializer_class = StudentSerializer
	# 限流的局部
	throttle_classes = [UserRateThrottle,AnonRateThrottle]


"""
过滤、排序 和 分页
上面这几个功能，必须在列表页视图使用，也就是ListAPIView，或者ListModelMixin
"""


"""自定义分页器"""
from rest_framework.pagination import PageNumberPagination
class StandardPageNumberPagination(PageNumberPagination):
	page_query_param = "page"  # 设置表示页码的变量名
	page_size = 2


from student.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
class StudentListAPIView(ListAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	filter_backends = [DjangoFilterBackend,OrderingFilter]
	filter_fields = ["class_no","sex","age"]
	ordering_fields = ["id"]
	pagination_class = StandardPageNumberPagination


"""
自定义异常
"""
from rest_framework.views import APIView
from rest_framework.response import Response
class Demo1APIView(APIView):
	def get(self,request):
		"""
		测试自定义异常的API接口
		"""
		1/0
		return Response("ok")