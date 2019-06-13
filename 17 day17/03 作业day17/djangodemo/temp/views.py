from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # context = {'city': '北京'}
    # return render(request, 'index.html', context)
    return render(request, 'index.html', {'city': '北京1'})  # 也可以这样写


from django.views import View


class HomeView(View):
    def get1(self, request):

        return render(request, 'index.html', {
            "title": '新的标题',
            'tuple': (1, 2, 3, 4,),
            'list1': ['a', 'b', 'c', ],
            'dict1': {'name': 'alnk', 'age': 18, },
            'num': 100,
        })


    def get2(self, request):

        return render(request, 'index2.html', {
            'tuple': (1, 2, 3, 4,),
            'list1': ['a', 'b', 'c', ],
            'dict1': {'name': 'alnk', 'age': 18, },
        })

    def get3(self, request):

        return render(request, 'index3.html', {
            'book_list': [
                {'name': 'python', 'price': 99},
                {'name': 'go', 'price': 69},
                {'name': 'go', 'price': 69},
                {'name': 'go', 'price': 69},
                {'name': 'go', 'price': 69},
            ]
        })

    # def get(self, request):
    #     # forloop.parentloop.counter 会继承上一个for循环的计数规则
    #     return render(request, 'index4.html', {
    #         'people': [
    #             {'name':'alnk', 'age': 19, 'love': ['睡觉', '吃饭', '打豆豆']},
    #             {'name':'alnk', 'age': 19, 'love': ['睡觉', '吃饭', '打豆豆']},
    #             {'name':'alnk', 'age': 19, 'love': ['睡觉', '吃饭', '打豆豆']},
    #             {'name':'alnk', 'age': 19, 'love': ['睡觉', '吃饭', '打豆豆']},
    #             {'name':'alnk', 'age': 19, 'love': ['睡觉', '吃饭', '打豆豆']},
    #         ]
    #     })

    def get(self, request):
        """过滤器"""
        from datetime import datetime
        return render(request, "index5.html", {
            "title": "welcome to django",
            'title2': '<h1>大标题</h1>',
            'title3': "小可爱",
            'date_time': datetime.now(),
            'str1': 'welcome to django',
            'str2': '我爱中国 welcome to django'
        })


# class IndexView(View):
#     """模板继承"""
#     def get(self, request):
#         return render(request, "index/index.html")
#
#
# class List(View):
#     def get(self, request):
#         return render(request, "index/list.html")


class IndexView(View):
    """模板继承"""
    def get(self, request):
        return render(request, "exten/index.html")


class List(View):
    def get(self, request):
        return render(request, "exten/list.html")


"""表单系统"""
from . forms import LoginForm

class LoginView(View):
    def get(self, request):
        return render(request, 'form.html', {
            'forms': LoginForm(),
        })

    def post(self, request):
        # print(request.POST)
        # print(request.POST.get("user"))
        # print(request.POST.get("pwd"))
        # 提交表单
        # 使用表单系统提供的验证流程
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print('到数据库查询账号密码，进行对比')
            print(form)
            return HttpResponse('OK')
        else:
            print(form)
            # return HttpResponse('NO')
            return render(request, 'form.html', {
                'forms': form
            })



from .forms import UserForm
class FormModelView(View):
    def get(self, request):
        return render(request, 'form_model.html', {
            'form_content': UserForm(),
        })

    def post(self, request):
        forms_mode = UserForm(request.POST)
        if forms_mode.is_valid():
            print(forms_mode.data)
            print('查询数据库账号密码')
            return HttpResponse('OK')
        else:
            print(forms_mode.cleaned_data)
            return render(request, 'form_model.html', {
                'form_content': forms_mode,
            })