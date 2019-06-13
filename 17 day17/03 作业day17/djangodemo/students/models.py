from django.db import models


class Student(models.Model):
    # 字段声明
    SEX_CHOICES = (
        (1, '男'),
        (2, '女'),
        (3, '保密'),
    )
    name = models.CharField(max_length=15, verbose_name='姓名')
    sex = models.SmallIntegerField(choices=SEX_CHOICES, default=3, verbose_name='性别')
    class_no = models.IntegerField(verbose_name='班级')
    age = models.IntegerField(verbose_name='年龄')
    born = models.DateField(null=True, verbose_name='生日')
    money = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, verbose_name='账户余额')
    description = models.TextField(null=True, verbose_name='个性签名')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    # 表相关信息
    class Meta:
        db_table = 'tb_student'
        verbose_name = '学生信息表'
        verbose_name_plural = verbose_name

    # 自定义模型
    def __str__(self):
        return "学生：%s ID：%s 年龄：%s " % (self.name, self.id, self.age)

    #  自定义模型字段
    def sex_text(self):
        return self.SEX_CHOICES[self.sex-1][1]
