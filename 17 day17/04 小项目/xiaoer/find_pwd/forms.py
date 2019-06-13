from django import forms


class LoginForm(forms.Form):
    # 登录页表单类
    username = forms.CharField(max_length=6, required=True, label='账号')
    password = forms.CharField(widget=forms.PasswordInput, max_length=16, required=True, label='密码')


class FindForm(forms.Form):
    # 查询表单类
    find_use = forms.CharField(required=True, label='输入玩家账号')
