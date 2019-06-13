from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import View

# def index(request):
#     return HttpResponse('<h1>hello django</h1>')
#
#
# def list(request):
#     return HttpResponse("列表页")
#
#
# def imgs(request):
#     return HttpResponse("<img src=/static/imgs/1.jpg />")
#
#
# def index2(request):
#     return HttpResponse('登录成功')
#
#
# def index3(request, number):
#     return HttpResponse('%s 正则表达式333' % number)
#
#
# def index4(request, n):
#     return HttpResponse('%s 正则表达式444' % n)
#
#
# def index5(request):
#     url = reverse("stu_space:index_rev")
#     return redirect(url)
#
#
# def login(request):
#     if request.method == "POST":
#         usernmae = request.POST.get("user")
#         pwd = request.POST.get("pwd")
#         if usernmae == "alex" and pwd == "123":
#             return redirect(reverse("stu_space:index_rev"))
#         else:
#             return HttpResponse('登录失败')
#
#     return render(request, 'login.html')
#
#
# def register(request):
#     if request.method == 'GET':
#         return HttpResponse('注册页面')
#     else:
#         return HttpResponse('登录逻辑')


# class UserView(View):
#     def post(self, request):
#         return HttpResponse('post')
#
#     def get(self, request):
#         return HttpResponse('get')
#
#     def put(self, request):
#         return HttpResponse('put')
#
#     def delete(self, request):
#         return HttpResponse('delete')

from django.utils.decorators import method_decorator


def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)

    return wrapper


# @method_decorator(my_decorator, name='get')
# @method_decorator(my_decorator, name='post')
# @method_decorator(my_decorator, name='dispatch')
# class Uapi2(View):
#     # @method_decorator(my_decorator)
#     def get(self, request):
#         return HttpResponse('类视图使用装饰器')
#
#     def post(self, request):
#         return HttpResponse('类视图 post')


# @method_decorator(my_decorator, name='dispatch')
# class BaseView(View):
#     pass
#
#
# class Uapi2(BaseView):
#     def get(self, request):
#         return HttpResponse('类视图使用装饰器')
#
#     def post(self, request):
#         return HttpResponse('类视图 post')

class MyDecoratorMixin(object):

    @classmethod
    def as_view(cls, *args, **kwargs):
        print('===', super())
        view = super().as_view(*args, **kwargs)
        view = my_decorator(view)
        return view


class Uapi2(MyDecoratorMixin, View):
    def get(self, request):
        print('get方法')
        return HttpResponse('getok')

    def post(self, request):
        print('post方法')
        return HttpResponse('postok')


from .models import Student


class StudentView(View):
    #
    # def post(self, request):
    #     stu = Student(
    #         name='alnk',
    #         age=17,
    #         sex=1,
    #         class_no=305,
    #         money=100,
    #         born='1991-07-21',
    #         description='啦啦啦',
    #     )
    #     stu.save()
    #     print(stu)
    #     return HttpResponse('post %s ' % request)
    # def post(self, request):
    #     stu = Student.objects.create(
    #         name='周星星',
    #         age=17,
    #         sex=1,
    #         class_no=305,
    #         money=100,
    #         born='1961-07-21',
    #         description='哆啦咪',
    #     )
    #     print(stu)
    #     return HttpResponse('post %s ' % request)
    # def get(self, request):
    #     # stu = Student.objects.get(id=104)
    #     try:
    #         stu = Student.objects.get(pk=103)
    #         print(stu)
    #     except Student.DoesNotExist:
    #         print('查无此人')
    #
    #     return HttpResponse('get')

    def get(self, request):
        # stu_list = Student.objects.all()
        # print(stu_list)
        #
        # for stu in stu_list:
        #     print(stu.name,stu.id)

        # count = Student.objects.count()
        # print(count)
        # stu = Student.objects.filter(pk__exact=1)
        # stu = Student.objects.filter(name__contains='a')
        # stu = Student.objects.filter(name__startswith='李')
        # stu = Student.objects.filter(name__endswith='明')
        # stu = Student.objects.filter(description__isnull=True)
        # stu = Student.objects.get(pk=103)
        # stu = Student.objects.all()

        # stu = Student.objects.filter(pk=103)  # 这是一个列表
        # for i in stu:
        #     print(i.pk, i.name, i.description)

        # stu = Student.objects.filter(description__isnull=True)
        # stu = Student.objects.filter(id__gte=100)
        from datetime import date
        stu = Student.objects.filter(born__gt=date(1990, 1, 1))
        from django.db.models import F
        stu = Student.objects.filter(age__gt=F('id'))

        stu = Student.objects.filter(age__gt=20,id__lt=30)
        from django.db.models import Q
        stu = Student.objects.filter(Q(age__gt=20) | Q(pk__lt=30))
        stu = Student.objects.filter(~Q(pk=2))
        stu = Student.objects.exclude(pk=2)


        from django.db.models import aggregates
        from django.db.models import Sum, Count, Max, Min, Avg
        stu = Student.objects.aggregate(Sum('age'))
        stu = Student.objects.aggregate(Count('age'))

        stu = Student.objects.all().order_by('age')
        stu = Student.objects.all().order_by('-age')
        stu = Student.objects.filter(description__isnull=True)
        stu = Student.objects.all()[0:2]
        print(stu)
        return HttpResponse('get')

