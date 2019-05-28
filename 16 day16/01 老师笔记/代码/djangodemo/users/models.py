from django.db import models
# 模型类
# Create your models here.
class Student(models.Model):
	# 字段声明
	SEX_CHOICES = (
		(1,"男"),
		(2,"女"),
		(3,"保密"),
	)
	# ID[主键，django系统会自动声明这个字段，我们可以手动声明，但是不推荐]
	# user_id = models.AutoField(primary_key=True,verbose_name="主键")
	name = models.CharField(max_length=15, verbose_name="姓名")
	sex  = models.SmallIntegerField(choices=SEX_CHOICES,default=3,verbose_name="性别")
	class_no = models.IntegerField(verbose_name='班级')
	age = models.IntegerField(verbose_name='年龄')
	born = models.DateField(null=True, verbose_name="生日")
	money = models.DecimalField(default=0.0, max_digits=8, decimal_places=2,verbose_name="账户余额")
	description = models.TextField(null=True,verbose_name='个性签名')
	is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

	# 表相关信息
	class Meta:
		db_table="tb_student" # 如果不设置db_table，则系统自定生成表名为“users_Student”
		verbose_name="学生信息表"
		verbose_name_plural= verbose_name

	# 自定义模型字段[ 这里的不是表的结构，而是操作数据时的新增字段 ]
	def __str__(self):
		return "学生：%s;ID:%s;年龄:%s" % (self.name,self.id,self.age)
