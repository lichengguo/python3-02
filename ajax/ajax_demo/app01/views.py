from django.shortcuts import render, HttpResponse
import json
import os
from django.http import JsonResponse


def test(request):
    if request.method == "GET":
        return render(request, 'test.html')
    else:
        return HttpResponse('okokokok!')


def total(request, num):
    print('===', num)  # 接收传递过来的参数
    ret = {'status': True, "msg": None}
    try:
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        total1 = float(num1) + float(num2)
        ret['total'] = total1
    except Exception as e:
        ret['status'] = False
        ret['msg'] = "输入有误"

    return HttpResponse(json.dumps(ret))
    # return JsonResponse(ret)


def json_upload(request):
    print('11111111', request.method, type(request.method))
    print('22222222', request.POST)
    print('33333333', request.body)

    data = json.loads(request.body.decode('utf-8'))
    print(data, type(data))

    return HttpResponse('jjjjjjjj')


def upload_file(request):
    print('xxxxxx', request.POST)
    print('ggggggg', request.FILES)
    file_obj = request.FILES.get('file_name')
    print('aaaaaaaa', file_obj, type(file_obj))
    with open(os.path.join('medio', file_obj.name), 'wb') as f:
        for line in file_obj:
            f.write(line)

    return HttpResponse('kkkkkk')
