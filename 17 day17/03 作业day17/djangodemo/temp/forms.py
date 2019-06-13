from django import forms
from django.core.exceptions import ValidationError


def checkusername(data):
    if data == "None":
        raise ValidationError("用户名不能为None")
    return data


class LoginForm(forms.Form):
    username = forms.CharField(validators=[checkusername, ], max_length=6, required=True, help_text="账号不能为空", label='账号')
    password = forms.CharField(max_length=6, required=True, help_text="密码不能为空", label='密码')


from students.models import Student


class UserForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ["is_delete", ]

    def clean_name(self):
        data = self.cleaned_data.get("data")
        if data == "alnk":
            raise ValidationError("用户名不能是：%s" % data)
        else:
            return data