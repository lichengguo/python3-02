from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views import View
import json


def login(request):
    if request.method == 'POST':
        ret = {'status': 1200, 'msg': None}
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alnk' and pwd == '123':
            ret['msg'] = '登录成功'
        else:
            ret['status'] = 1404
            ret['msg'] = '账号或者密码错误'
        return JsonResponse(ret)
    else:
        return render(request, 'login/login.html')


def index(request):
    return render(request, 'login/index.html')