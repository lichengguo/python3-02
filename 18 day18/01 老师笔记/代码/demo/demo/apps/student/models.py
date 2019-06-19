from django.db import models

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
	class_no = models.IntegerField(db_column="class",verbose_name='班级')
	age = models.IntegerField(verbose_name='年龄')
	description = models.TextField(null=True,verbose_name='个性签名')
	status = models.SmallIntegerField(verbose_name="是否删除")
	orders = models.IntegerField(default=None, null=True, verbose_name="排序")
	# 表相关信息
	class Meta:
		db_table="student" # 如果不设置db_table，则系统自定生成表名为“users_Student”
		verbose_name="学生信息表"
		verbose_name_plural= verbose_name

	# 自定义模型字段[ 这里的不是表的结构，而是操作数据时的新增字段 ]
	def __str__(self):
		return "学生：%s;ID:%s;年龄:%s" % (self.name,self.id,self.age)

	# 自定义模型字段
	def sex_text(self):
		return self.SEX_CHOICES[self.sex-1][1]