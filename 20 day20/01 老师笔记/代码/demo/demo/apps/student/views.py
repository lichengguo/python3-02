from django.views import View
from django.http.response import JsonResponse
from .models import Student
"""
原生django编写API接口代码:
"""
class StudentsView(View):
	def get(self,request):
		"""获取所有的学生信息"""
		# 获取数据
		student_list = Student.objects.all()
		# print(student_list)
		# 返回json数据给客户端,通过 JsonResponse
		# return JsonResponse({"name":"zhagnsan","age":17})
		# json的语法可以使用花括号,也可以是中括号,还可以支持字符串[双引号]和数值[整数\浮点数\布尔值],
		# return JsonResponse([{"name":"zhagnsan","age":17},{"name":"zhagnsan","age":17}],safe=False)

		# 手动序列化转换数据
		student_data_list = []
		for student in student_list:
			student_data_list.append({
				"id":student.id,
				"name":student.name,
				"age":student.age,
				"sex":student.sex,
				"class_no":student.class_no,
			})

		return JsonResponse(student_data_list,safe=False)

	def post(self):
		"""获取所有的学生信息"""
		# 接收数据

		# 数据库操作

		# 返回结果.把新增的模型对象返回给客户端
		pass

class StudentView(View):
	def get(self,request,pk):
		"""获取一条学生信息"""
		pass

	def put(self,request,pk):
		"""更新学生信息"""
		pass

	def delete(self,request,pk):
		"""删除学生信息"""
		pass

"""
drf框架提供api接口操作
"""
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student

class Students2ViewSet(ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer