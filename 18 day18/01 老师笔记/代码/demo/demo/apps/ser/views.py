from django.shortcuts import render

# Create your views here.
"""
声明序列化器,并调用序列化器
序列化阶段: 服务器提供数据给客户端
	1. 创建序列化器,并使用序列化器对数据进行序列化

反序列化器阶段: 客户端提供数据给服务器
	2. 创建序列化器,并使用序列化器对数据进行验证[ 对客户端提交的数据进行验证 ]
	3. 创建序列化器,并使用序列化器对数据进行反序列化,转换数据成模型对象
"""

"""
1. 创建序列化器,并使用序列化器对数据进行序列化
"""
from django.views import View
from student.models import Student
from django.http.response import HttpResponse,JsonResponse
from .serializers import Student1Serializer
class StudentsView(View):
	def get(self,request):
		"""获取所有学生数据"""
		student_list = Student.objects.all()

		# 调用序列化器进行序列化
		# StudentSerializer(模型对象)            # 序列化转换单个模型对象
		# StudentSerializer(模型列表,many=True)  # 序列化转换多个模式对象
		# serializer = StudentSerializer(student_list)
		# 实例化序列化器类
		serializer = Student1Serializer(instance=student_list,many=True)  # 这里的instance可以省略,因为instance属于第一个位置参数
		# serializer内部就保存了数据转换后的内容以及布尔结果

		print(serializer.data) # 获取序列化转换以后的数据
		"""打印效果:
		[
			OrderedDict([('id', 1), ('name', '赵华'), ('sex', True), ('age', 22)]), 
			OrderedDict([('id', 2), ('name', '程星云'), ('sex', True), ('age', 20)]), 
			OrderedDict([('id', 3), ('name', '陈峰'), ('sex', True), ('age', 21)]), 
			OrderedDict([('id', 4), ('name', '苏礼就'), ('sex', True), ('age', 20)]), OrderedDict([('id', 5), ('name', '张小玉'), ('sex', True), ('age', 18)]), OrderedDict([('id', 6), ('name', '吴杰'), ('sex', True), ('age', 19)]), OrderedDict([('id', 7), ('name', '张小辰'), ('sex', True), ('age', 19)]), OrderedDict([('id', 8), ('name', '王丹丹'), ('sex', True), ('age', 22)]), OrderedDict([('id', 9), ('name', '苗俊伟'), ('sex', True), ('age', 22)]), OrderedDict([('id', 10), ('name', '娄镇明'), ('sex', True), ('age', 22)]), OrderedDict([('id', 11), ('name', '周梦琪'), ('sex', True), ('age', 19)]), OrderedDict([('id', 12), ('name', '欧阳博'), ('sex', True), ('age', 23)]), OrderedDict([('id', 13), ('name', '颜敏莉'), ('sex', True), ('age', 20)]), OrderedDict([('id', 14), ('name', '柳宗仁'), ('sex', True), ('age', 20)]), OrderedDict([('id', 15), ('name', '谢海龙'), ('sex', True), ('age', 22)]), OrderedDict([('id', 16), ('name', '邓士鹏'), ('sex', True), ('age', 22)]), OrderedDict([('id', 17), ('name', '宁静'), ('sex', True), ('age', 23)]), OrderedDict([('id', 18), ('name', '上官屏儿'), ('sex', True), ('age', 21)]), OrderedDict([('id', 19), ('name', '孙晓静'), ('sex', True), ('age', 20)]), OrderedDict([('id', 20), ('name', '刘承志'), ('sex', True), ('age', 20)]), OrderedDict([('id', 21), ('name', '王浩'), ('sex', True), ('age', 21)]), OrderedDict([('id', 22), ('name', '钟无艳'), ('sex', True), ('age', 19)]), OrderedDict([('id', 23), ('name', '莫荣轩'), ('sex', True), ('age', 22)]), OrderedDict([('id', 24), ('name', '张裕民'), ('sex', True), ('age', 21)]), OrderedDict([('id', 25), ('name', '江宸轩'), ('sex', True), ('age', 22)]), OrderedDict([('id', 26), ('name', '谭季同'), ('sex', True), ('age', 21)]), OrderedDict([('id', 27), ('name', '李松风'), ('sex', True), ('age', 19)]), OrderedDict([('id', 28), ('name', '叶宗政'), ('sex', True), ('age', 20)]), OrderedDict([('id', 29), ('name', '魏雪宁'), ('sex', True), ('age', 20)]), OrderedDict([('id', 30), ('name', '徐秋菱'), ('sex', True), ('age', 19)]), OrderedDict([('id', 31), ('name', '曾嘉慧'), ('sex', True), ('age', 19)]), OrderedDict([('id', 32), ('name', '欧阳镇安'), ('sex', True), ('age', 23)]), OrderedDict([('id', 33), ('name', '周子涵'), ('sex', True), ('age', 19)]), OrderedDict([('id', 34), ('name', '宋应诺'), ('sex', True), ('age', 23)]), OrderedDict([('id', 35), ('name', '白瀚文'), ('sex', True), ('age', 19)]), OrderedDict([('id', 36), ('name', '陈匡怡'), ('sex', True), ('age', 19)]), OrderedDict([('id', 37), ('name', '邵星芸'), ('sex', True), ('age', 22)]), OrderedDict([('id', 38), ('name', '王天歌'), ('sex', True), ('age', 21)]), OrderedDict([('id', 39), ('name', '王天龙'), ('sex', True), ('age', 22)]), OrderedDict([('id', 40), ('name', '方怡'), ('sex', True), ('age', 23)]), OrderedDict([('id', 41), ('name', '李伟'), ('sex', True), ('age', 19)]), OrderedDict([('id', 42), ('name', '李思玥'), ('sex', True), ('age', 22)]), OrderedDict([('id', 43), ('name', '赵思成'), ('sex', True), ('age', 18)]), OrderedDict([('id', 44), ('name', '蒋小媛'), ('sex', True), ('age', 22)]), OrderedDict([('id', 45), ('name', '龙华'), ('sex', True), ('age', 19)]), OrderedDict([('id', 46), ('name', '牧婧白夜'), ('sex', True), ('age', 21)]), OrderedDict([('id', 47), ('name', '江俊文'), ('sex', True), ('age', 19)]), OrderedDict([('id', 48), ('name', '李亚容'), ('sex', True), ('age', 18)]), OrderedDict([('id', 49), ('name', '王紫伊'), ('sex', True), ('age', 22)]), OrderedDict([('id', 50), ('name', '毛小宁'), ('sex', True), ('age', 19)]), OrderedDict([('id', 51), ('name', '董 晴'), ('sex', True), ('age', 19)]), OrderedDict([('id', 52), ('name', '严语'), ('sex', True), ('age', 18)]), OrderedDict([('id', 53), ('name', '陈都灵'), ('sex', True), ('age', 19)]), OrderedDict([('id', 54), ('name', '黄威'), ('sex', True), ('age', 23)]), OrderedDict([('id', 55), ('name', '林佳欣'), ('sex', True), ('age', 23)]), OrderedDict([('id', 56), ('name', '翁心颖'), ('sex', True), ('age', 19)]), OrderedDict([('id', 57), ('name', '蒙毅'), ('sex', True), ('age', 22)]), OrderedDict([('id', 58), ('name', '李小琳'), ('sex', True), ('age', 22)]), OrderedDict([('id', 59), ('name', '伍小龙'), ('sex', True), ('age', 19)]), OrderedDict([('id', 60), ('name', '晁然'), ('sex', True), ('age', 23)]), OrderedDict([('id', 61), ('name', '端木浩然'), ('sex', True), ('age', 18)]), OrderedDict([('id', 62), ('name', '姜沛佩'), ('sex', True), ('age', 21)]), OrderedDict([('id', 63), ('name', '李栋明'), ('sex', True), ('age', 19)]), OrderedDict([('id', 64), ('name', '柴柳依'), ('sex', True), ('age', 23)]), OrderedDict([('id', 65), ('name', '吴杰'), ('sex', True), ('age', 22)]), OrderedDict([('id', 66), ('name', '杜文华'), ('sex', True), ('age', 19)]), OrderedDict([('id', 67), ('name', '邓珊珊'), ('sex', True), ('age', 18)]), OrderedDict([('id', 68), ('name', '杜俊峰'), ('sex', True), ('age', 23)]), OrderedDict([('id', 69), ('name', '庄信杰'), ('sex', True), ('age', 22)]), OrderedDict([('id', 70), ('name', '宇文轩'), ('sex', True), ('age', 23)]), OrderedDict([('id', 71), ('name', '黄佳怿'), ('sex', True), ('age', 19)]), OrderedDict([('id', 72), ('name', '卫然'), ('sex', True), ('age', 18)]), OrderedDict([('id', 73), ('name', '耶律齐'), ('sex', True), ('age', 23)]), OrderedDict([('id', 74), ('name', '白素欣'), ('sex', True), ('age', 18)]), OrderedDict([('id', 75), ('name', '徐鸿'), ('sex', True), ('age', 23)]), OrderedDict([('id', 76), ('name', '上官杰'), ('sex', True), ('age', 19)]), OrderedDict([('id', 77), ('name', '吴兴国'), ('sex', True), ('age', 18)]), OrderedDict([('id', 78), ('name', '庄晓敏'), ('sex', True), ('age', 18)]), OrderedDict([('id', 79), ('name', '吴镇升'), ('sex', True), ('age', 18)]), OrderedDict([('id', 80), ('name', '朱文丰'), ('sex', True), ('age', 19)]), OrderedDict([('id', 81), ('name', '苟兴妍'), ('sex', True), ('age', 18)]), OrderedDict([('id', 82), ('name', '祝华生'), ('sex', True), ('age', 21)]), OrderedDict([('id', 83), ('name', '张美琪'), ('sex', True), ('age', 23)]), OrderedDict([('id', 84), ('name', '周永麟'), ('sex', True), ('age', 21)]), OrderedDict([('id', 85), ('name', '郑心'), ('sex', True), ('age', 21)]), OrderedDict([('id', 86), ('name', '公孙龙馨'), ('sex', True), ('age', 21)]), OrderedDict([('id', 87), ('name', '叶灵珑'), ('sex', True), ('age', 19)]), OrderedDict([('id', 88), ('name', '上官龙'), ('sex', True), ('age', 21)]), OrderedDict([('id', 89), ('name', '颜振超'), ('sex', True), ('age', 19)]), OrderedDict([('id', 90), ('name', '玛诗琪'), ('sex', True), ('age', 22)]), OrderedDict([('id', 91), ('name', '李哲生'), ('sex', True), ('age', 22)]), OrderedDict([('id', 92), ('name', '罗文华'), ('sex', True), ('age', 22)]), OrderedDict([('id', 93), ('name', '李康'), ('sex', True), ('age', 19)]), OrderedDict([('id', 94), ('name', '钟华强'), ('sex', True), ('age', 19)]), OrderedDict([('id', 95), ('name', '张今菁'), ('sex', True), ('age', 23)]), OrderedDict([('id', 96), ('name', '黄伟麟'), ('sex', True), ('age', 19)]), OrderedDict([('id', 97), ('name', '程荣泰'), ('sex', True), ('age', 22)]), OrderedDict([('id', 98), ('name', '范伟杰'), ('sex', True), ('age', 19)]), OrderedDict([('id', 99), ('name', '王俊凯'), ('sex', True), ('age', 21)]), OrderedDict([('id', 100), ('name', '白杨 '), ('sex', True), ('age', 19)]), OrderedDict([('id', 101), ('name', '刘德华'), ('sex', True), ('age', 18)]), OrderedDict([('id', 102), ('name', '周润发'), ('sex', True), ('age', 18)])]
		# OrderedDict 有序字典,是python基于默认字典是无序的情况,提供的一个高级数据类型.
		# 有序字典的操作,和无序字典是一模一样的
		# 要声明和使用有序字典:可以导包: from collections import OrderedDict
		"""

		# return HttpResponse("序列化器的使用:对多个数据进行序列化器")
		return JsonResponse(serializer.data)

class StudentView(View):
	def get(self,request,pk):
		"""获取指定ID的一个成员信息"""
		# 获取数据
		student = Student.objects.get(pk=pk)
		# 使用序列化器进行序列化器
		serializer = Student1Serializer(instance=student)
		print(serializer.data)  # 获取序列化转换以后的数据
		"""打印效果:
		{'id': 2, 'name': '程星云', 'sex': 3, 'age': 20, 'status': False}
		"""
		return HttpResponse("序列化器的使用:对单个数据进行序列化器")


"""
2. 创建序列化器,并使用序列化器对数据进行验证[ 对客户端提交的数据进行验证 ]
"""
from .serializers import Student2Serializer
class Student2View(View):
	def post(self,request):

		# request.body用于获取客户端提交过来的数据不识别情况,
		# print(request.body) # bytes类型
		# """打印效果:
		# b'{\n\t"name":"\xe9\xaa\x91\xe5\xa3\xab\xe5\x91\xa8\xe6\x9c\xab",\n\t"age":16,\n\t"sex":1,\n\t"description":"\xe6\xb2\xa1\xe6\x9c\x89\xe4\xb8\xaa\xe6\x80\xa7\xe7\xad\xbe\xe5\x90\x8d"\n}'
		# """
		# 获取数据的步骤：
		# data_json_str = request.body.decode()
		# import json
		# data_dict = json.loads(data_json_str) # json字符串转成 字典
		# print(data_dict) # {'name': '骑士周末', 'age': 16, 'sex': 1, 'description': '没有个性签名'}
		data = {
			'name': 'null',
			'age': 30,
			'sex': 2,
			'description': '没有个性签名',
		}
		# 调用序列化器进行数据验证
		# Serializer(data=客户端提供的数据) # 验证所有字段
		# Serializer(data=客户端提供的数据,partial=True) # 验证部分字段, partial=True 表示没有的字段不会去验证
		serailizer = Student2Serializer(data=data)
		# 对数据进行验证, 获取验证结果
		# 使用is_vald对数据进行验证,raise_exception=True 表示直接抛出错误!后面的代码不会被执行
		result = serailizer.is_valid(raise_exception=True) # is_valid 会内部调用序列化器中的验证代码
		print("验证结果: %s" % result)

		# 获取验证失败以后的错误信息
		if not result:
			print(serailizer.error_messages)

		# 获取经过验证后的数据
		print( serailizer.validated_data ) # 如果验证结果为False,则validated_data的值为空字典,

		return HttpResponse("序列化器的使用:对客户端提交的数据进行验证")

"""
3. 创建序列化器,并使用序列化器对数据进行反序列化,转换数据成模型对象
"""
from .serializers import  Student3Serializer
class Student3View(View):
	def post(self,request):
		"""添加一个学生信息"""
		# 接受客户端数据
		data = {
			'name': '骑士周末',
			'age': 30,
			'sex': 2,
			'description': '没有个性签名',
		}

		serializer = Student3Serializer(data=data)
		# 调用序列化器的验证功能
		serializer.is_valid(raise_exception=True)
		# 进行反序列化
		# save执行时，会自动调用序列化器内部的create或者update方法来完成数据的添加或者功能，但是最终的返回值都是模型对象
		instance = serializer.save() # 调用了save以后，就可以得到模型对象

		print(instance)

		return HttpResponse("序列化器的使用:对客户端提交的数据进行反序列化")

from .serializers import  Student3Serializer
class Student4View(View):
	def put(self,request,pk):
		"""更新数据"""
		# 接受客户端数据
		data = {
			'name': '周氏周末2期',
			'age': 30,
			'sex': 2,
			'description': '没有个性签名',
		}

		# 获取当前更新的模型对象
		student = Student.objects.get(pk=pk)

		# 调用序列化器进行更新操作，必须在实例化的时候传递2个参数，instance 和 data
		serializer = Student3Serializer(instance=student,data=data)
		# 调用序列化器的验证功能
		serializer.is_valid(raise_exception=True)
		# 进行反序列化起
		instance = serializer.save()  # 调用了save以后，就可以得到模型对象
		print(instance) # 修改后的模型对象

		return HttpResponse("序列化器的使用:对客户端提交的数据进行反序列化")

"""面试题：序列化器在完成发序列化的时候，调用save，序列化器知道该调用的是create或者update？
   问题的关键就是序列化器的实例化参数上面！
   drf内部会自动根据实例化序列化器时，如果有同时传入 instance 和 data，则默认本次操作是更新数据操作
   如果只传递了data，则默认本次操作是添加数据操作
   # 查看 save内部的源码，可以发现在 BaseSerializer的__init__方法，instance作为对象属性
   # 在save中使用if判断是否有 self.instance
"""

"""
通过一个序列化器完成序列化、验证和反序列化效果
"""
from .serializers import StudentSerializer
class Student5View(View):
	def get(self,request):
		"""获取所有学生信息"""
		student_list = Student.objects.all()
		serializer = StudentSerializer(instance=student_list, many=True)
		return JsonResponse(serializer.data,safe=False)

	def post(self,request):
		"""添加学生信息"""
		# 接受数据
		data_json_str = request.body.decode()
		import json
		data_dict = json.loads(data_json_str)
		# 实例化序列化器
		serializer = StudentSerializer(data=data_dict)
		# 验证
		serializer.is_valid(raise_exception=True)
		# 反序列化
		instance = serializer.save()

		return JsonResponse(serializer.data)


"""使用模型类序列化器缩进字段声明的代码和发序列化的代码"""
from .serializers import StudentModelSerializer
class Student6View(View):
	def get(self, request):
		"""获取所有学生信息"""
		student_list = Student.objects.all()
		serializer = StudentModelSerializer(instance=student_list, many=True)
		print(serializer)
		return JsonResponse(serializer.data, safe=False)

	def post(self, request):
		"""添加学生信息"""
		# 接受数据
		data_json_str = request.body.decode()
		import json
		data_dict = json.loads(data_json_str)
		# 实例化序列化器
		serializer = StudentModelSerializer(data=data_dict)
		# 验证
		serializer.is_valid(raise_exception=True)
		# 反序列化
		instance = serializer.save()

		return JsonResponse(serializer.data)
