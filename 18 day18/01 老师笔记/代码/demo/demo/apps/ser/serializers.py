from rest_framework import serializers

"""
1. 创建序列化器,并使用序列化器对数据进行序列化
"""
# class 资源名称+Serializer(serializers.Serializer):
# 	"""xxx数据序列化器"""
# 	# 1. 数据转换时字段[这里的声明类似于模型的字段声明]
#
# 	# 2. [可选]如果序列化器中大部分字段和模型的字段保持一致,可以通过过引用模型中的字段声明
#
#   # 3. [可选]数据验证方法[这里的所有方法名: 必须以"vilidate_"开头]
#
# 	# 4. [可选]当使用序列化器用于进行反序列化,需要调用操作数据模型对象
# 	# 一般是 create或者save

# 例如,创建一个序列化器,转换用于提供给学生表的
class Student1Serializer(serializers.Serializer):
	id = serializers.IntegerField()
	name=serializers.CharField()
	sex=serializers.IntegerField()
	age=serializers.IntegerField()
	status=serializers.BooleanField()


"""
2. 创建序列化器,并使用序列化器对数据进行验证[ 对客户端提交的数据进行验证 ]
# 在使用序列化器进行验证的时候，drf框架一共提供了三个方式，给我们编写验证代码：
	验证规则: 
		书写位置: 序列化器字段声明后面的小圆括号里面,多个规则使用逗号隔开
	验证方法:
		书写位置: 作为序列化器的类方法存在,方法名必须是以 "validate_" 开头
	验证函数:
		书写位置: 在序列化器类外部声明的验证函数，在字段声明后面的小圆括号中通过 validators来进行调用
		验证函数的代码类似于 验证方法，同时验证函数只能用于当前序列化器类中，而验证函数可以被多个序列化器引入并调用

在调用is_valid的时候，上面三个方式都会被依次调用。
最先被调用的就是验证规则，其次到验证方法，最后到验证函数
逐个字段验证！
"""

def check_name(data): # data 就是当前验证的字段值,是视图中实例化序列化器时,传递的data数据的其中一个成员
	if data == "null":
		raise serializers.ValidationError("名字不能是关键字null!")

	# 验证函数也需要有返回值
	return data

class Student2Serializer(serializers.Serializer):
	# max_length=50 验证选项,字符串的最大长度是50
	# name = serializers.CharField(max_length=50,validators=[函数名1,函数名2,.....])  # validators可以调用多个验证函数，格式是第一个列表
	name = serializers.CharField(max_length=50,validators=[check_name])
	# required=True 验证选项,必填,不能为没有字段
	# min_value=0,max_value=100 验证选项, 字段最大值 和 最小值
	age = serializers.IntegerField(required=True,min_value=0,max_value=100)
	description = serializers.CharField()
	sex = serializers.IntegerField(required=True)

	# 验证方法
	# 1. 验证一个字段   方法名格式:   validate_字段名()
	# 2. 验证所有字段   方法名必须就叫做:   validate()

	def validate_name(self,data): # data 就是当前验证的字段值,是视图中实例化序列化器时,传递的data数据的其中一个成员
		"""验证单个字段的值"""
		print(data)
		if data == "root":
			# 抛出错误
			raise serializers.ValidationError("名字不能是root!!!")

		# 为了保证验证完成以后,可以得到当前这个验证的字段值,必须要返回数据
		# 当然,在返回数据之前,你可以对数据进行加工处理!
		return "<"+data+">"

	def validate(self,data): # data 就是当前验证的字段值,是视图中实例化序列化器时,传递的data数据
		"""验证多个字段"""
		print(data)

		sex = data.get("sex")
		age = data.get("age")

		if sex != 2 or age > 30:
			raise serializers.ValidationError("本女装店不招收大叔或者高龄大妈！")

		# 为了保证验证完成以后,可以得到字段值,必须要返回数据
		# 不返回则报错！
		return data

	def validate_mobile(self,data):
		# 获取手机信息
		mobile = data.get("mobile")
		import re
		if not re.match("^1\d{10}$",data):
			raise serializers.ValidationError("手机号码格式不正确！")

		return data


"""

"""
from student.models import Student
class Student3Serializer(serializers.Serializer):
	name = serializers.CharField(max_length=50,validators=[check_name])
	age = serializers.IntegerField(required=True,min_value=0,max_value=100)
	description = serializers.CharField()
	sex = serializers.IntegerField(required=True)


	"""
	反序列化： 保存数据，把字典转换成模型对象
	Serializer会默认提供两个方法，给我们完成添加数据或者编辑数据功能实现，我们需要在里面补充代码，返回模型对象
	那么，在视图中调用序列化器时，就可以实现把字段转换成模型对象了
	def create(self, validated_data) # validated_data 序列化器验证通过以后的数据
	def update(self, instance, validated_data) # instance 就是要修改数据的模型对象; validated_data 序列化器验证通过以后的数据
	pycharm提供了多行编辑的功能，可以通过Alt+鼠标左键，可以选中多行数据进行编辑
	pycharm还提供了选中单词或者代码块的功能，可以通过ctrl+shift+左右方向键进行选中
	"""

	def create(self, validated_data):
		"""添加数据"""
		name = validated_data.get("name")
		age = validated_data.get("age")
		description = validated_data.get("description")
		sex = validated_data.get("sex")

		student = Student.objects.create(
			name=name,
			age=age,
			description=description,
			sex=sex
		)

		return student

	def update(self, instance, validated_data):
		"""更新数据"""
		name = validated_data.get("name")
		age = validated_data.get("age")
		description = validated_data.get("description")
		sex = validated_data.get("sex")

		instance.name = name
		instance.age = age
		instance.description = description
		instance.sex = sex
		instance.save()
		return instance


"""
上面因为我们分功能对序列化器进行了学习，所以创建了三个序列化器，但是，事实上，我们开发中只会声明一个序列化器就可以完成上面三个阶段的使用。
"""
class StudentSerializer(serializers.Serializer):
	"""学生信息的序列化器"""
	#  1. 数据转换时字段[这里的声明类似于模型的字段声明]
	id = serializers.IntegerField(read_only=True) # read_only=True 表示设置当前字段只会在序列化的时候使用
	name = serializers.CharField(max_length=50)
	age = serializers.IntegerField(required=True, min_value=0, max_value=100)
	description = serializers.CharField()
	sex = serializers.IntegerField(required=True)
	status = serializers.BooleanField()

	# 2. 数据验证方法
	def validate_name(self,data):
		if data == "root":
			raise serializers.ValidationError("名字不能是root!!!")
		return "<"+data+">"

	# 3. 反序列化的方法
	def create(self, validated_data):
		"""添加数据"""
		name = validated_data.get("name")
		age = validated_data.get("age")
		description = validated_data.get("description")
		sex = validated_data.get("sex")
		status = validated_data.get("status")

		student = Student.objects.create(
			name=name,
			age=age,
			description=description,
			sex=sex,
			status=status
		)
		return student

	def update(self, instance, validated_data):
		"""更新数据"""
		name = validated_data.get("name")
		age = validated_data.get("age")
		description = validated_data.get("description")
		sex = validated_data.get("sex")

		instance.name = name
		instance.age = age
		instance.description = description
		instance.sex = sex
		instance.save()
		return instance


"""
由 Serializer基类下面还提供了一个子类，ModelSerializer模型类序列化器
- 基于模型类自动生成一系列序列化器字段
- 基于模型类自动为Serializer生成validators，比如unique_together
- 默认实现了create()和update()功能
"""
from student.models import Student
class StudentModelSerializer(serializers.ModelSerializer):
	# 1. 字段声明
	# 确认密码，不需要保存到数据库，但是一定要客户端提交的数据，也需要验证
	#  password2 = serializer.CharField(required=True)

	# 2. 引用数据模型的声明
	class Meta:
		model = Student
		# fields = ("id","name","sex","age","class_no","description","status","password2")
		# fields = ("id","name","sex","age","class_no","description","status")
		# fields = ["id","name","sex","age","class_no","description","status"]
		fields = "__all__" # 两个下划线，表示全部
	# 3. 数据验证方法
	def validate_name(self,data):
		if data == "root":
			raise serializers.ValidationError("名字不能是root!!!")
		return "<"+data+">"

	# 4. 反序列化的方法【ModelSerializer默认提供了】
