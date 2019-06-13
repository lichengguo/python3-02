from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.views import View
from .forms import LoginForm, FindForm  # 表单类
from .models import Account  # 数据库模型类


class Login(View):
    """登录验证"""

    def __init__(self):
        """预设登录的账号密码"""
        self.use = 'leju'
        self.pwd = 'Leju123456'

    def get(self, request):
        """获取登录页面"""
        return render(request, 'xiaoer/login.html', {
            'forms': LoginForm(),
        })

    def post(self, request):
        """验证登录账号密码"""
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")  # 输入的登录账号
            password = form.cleaned_data.get('password')  # 输入的登录密码
            if username == self.use and password == self.pwd:  # 验证账号密码
                # 账号密码正确返回查询玩家密码的页面
                return render(request, 'xiaoer/find_pwd.html', {
                    'forms': FindForm(),
                })
            else:
                # return HttpResponse('账号或密码错误')
                return render(request, 'xiaoer/error.html', {
                    'error': '登录账号或密码错误!'
                })

        else:
            return render(request, 'xiaoer/login.html', {
                'forms': form
            })


class Find(View):
    """查找玩家密码"""

    def post(self, request):
        """查找页面"""
        form = FindForm(request.POST)
        if form.is_valid():
            name = request.POST.get("find_use")  # 玩家账号
            # 去数据库查询玩家密码
            try:
                use_pwd = Account.objects.get(username=name)
                return render(request, 'xiaoer/result.html', {
                    'username': use_pwd.username,
                    'password': use_pwd.password
                })

            except Account.DoesNotExist:
                return render(request, 'xiaoer/error.html', {
                    'error': '不存在该玩家!'
                })
        else:
            return render(request, 'xiaoer/find_pwd.html', {
                'forms': form,
            })
