from django.contrib import admin
from .models import Student

# 配置模型管理类
class StudentModelAdmin(admin.ModelAdmin):
	# 站点当中，对于数据的显示字段进行设置
	list_display = ["name","sex","age"]

admin.site.register(Student,StudentModelAdmin)