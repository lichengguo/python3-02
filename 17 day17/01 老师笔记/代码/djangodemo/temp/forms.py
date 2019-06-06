from django import forms
from django.core.exceptions import ValidationError

# 自定义验证函数
def checkusername(data):
	if data == "None":
		# 抛出异常
		raise ValidationError("用户名不能是None!")
	# 验证函数里面如果通过了验证，必须返回数据!
	return data

class LoginForm(forms.Form):
	username = forms.CharField(validators=[checkusername], max_length=6, required=True, help_text="账号不能为空，并且长度必须在6-16个字符之间", label="账号")
	password = forms.CharField(required=True, help_text="密码不能为空，并且长度必须在6-16个字符之间", label="密码")
	remember = forms.BooleanField(required=False,label="是否记住密码")

	# 验证单个字段 方法的命名规范必须是 clean_<字段名>(self):
	def clean_username(self):
		"""自定义验证表单字段的方法"""
		# cleaned_data 字典类型，用户提交过来的数据
		data = self.cleaned_data.get("username")
		if data == "老男孩":
			raise ValidationError("用户名不能是老男孩！")
		else:
			# 验证函数里面如果通过了验证，必须返回数据!
			return data

	# 验证所有字段，方法名必须是 clean(self)
	def clean(self):
		password = self.cleaned_data.get("password")
		if not password:
			raise ValidationError("登录密码不能为空！")
		return self.cleaned_data


"""From 基本表单类
	    所有的字段和验证选项，都需要我们手动声明
	    
   ModelForm 模型表单类
		可以支持我们声明表单中的字段，从指定的模型中进行生成
"""
from users.models import Student
class UserForm(forms.ModelForm):
	class Meta:
		model = Student
		# fields = "__all__"  # 这里表示从模型中继承所有的字段过来,作为表单项显示到页面那种
		# fields = ["name","sex","class_no"] # 这里表示从模型中继承列表中指定的字段作为表单项
		exclude = ["is_delete"]   # 这里表示从模型中继承除了列表中以外的字段作为表单项,这个选项和fields相反