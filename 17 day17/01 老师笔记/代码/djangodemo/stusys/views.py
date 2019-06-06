from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
"""
针对一个功能的实现，基本要完成5个方法：
1. 获取所有数据  students/
3. 添加一条数据  students/

2. 获取一条数据  students/10/
4. 修改一条数据  students/10/
5. 删除一条数据  students/10/
"""
from users.models import Student
class StudentListView(View):
	def get(self,request):
		"""获取所有数据"""
		# 1. 获取数据库里面的所有学生信息
		student_list = Student.objects.filter(is_delete=False).all()
		# 2. 渲染模板
		return render(request,"sys/list.html",{
			"students_list":student_list,
		})

	def post(self,request):
		"""添加一条数据"""
		pass

class StudentView(View):
	def get(self,request):
		"""获取一条数据"""
		pass

class StudentDeleteView(View):
	def get(self,request):
		"""删除一条数据"""
		pass
from users.models import Student
from .forms import StudentForm
class StudentUpdateView(View):
	def get(self,request,pk):
		"""获取要更新的数据"""

		# 根据ID获取学生信息
		try:
			student = Student.objects.get(pk=pk)
		except Student.DoesNotExist:
			return redirect("对不起,参数有误!")

		data = {}
		data["name"] = student.name
		data["sex"] = student.sex
		data["age"] = student.age
		data["class_no"] = student.class_no
		data["born"] = student.born
		data["money"] = student.money
		data["description"] = student.description

		# 把表单类显示到模板中
		return render(request,"sys/update.html",{
			"forms": StudentForm(data)
		})

	def post(self,request,pk):
		"""更新数据"""
		# 调用表单类进行验证
		form = StudentForm(request.POST)

		if form.is_valid():
			# 验证通过
			data = form.cleaned_data
			# 数据库操作
			try:
				student = Student.objects.get(pk=pk)
				student.name = data.get("name")
				student.class_no = data.get("class_no")
				student.sex = data.get("sex")
				student.age = data.get("age")
				student.money = data.get("money")
				student.born = data.get("born")
				student.description = data.get("description")
				student.save()
				return redirect("/sys/students/")
			except Student.DoesNotExist:
				return render(request, "sys/update.html", {
					"forms": form,
				})
		else:
			# 验证失败
			return render(request,"sys/update.html",{
				"forms":form,
			})