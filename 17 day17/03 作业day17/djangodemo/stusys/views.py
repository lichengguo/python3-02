from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from students.models import Student  # 导入数据模型
from .forms import StudentForm  # 导入表单类


class StudentListView(View):
    """展示全部数据"""

    def get(self, request):
        # 获取所有数据
        stu_list = Student.objects.filter(is_delete=False).all()
        # print(stu_list)
        # 渲染模板
        return render(request, 'stusys/list.html', {
            "forms": stu_list,
        })


class StudentUpdateView(View):
    """更新一条数据"""

    def get(self, request, pk):
        # 获取一条数据
        try:
            stu = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return redirect('对不起参数有误')
        data = dict()
        data["name"] = stu.name
        data["sex"] = stu.sex
        data["age"] = stu.age
        data["class_no"] = stu.class_no
        data["born"] = stu.born
        data["money"] = stu.money
        data["description"] = stu.description

        return render(request, 'stusys/list_one.html', {
            'info': StudentForm(data),
        })

    def post(self, request, pk):
        # 更新个人信息
        # 获取表单提交过来的全部信息
        form = StudentForm(request.POST)
        print(form.clean)
        if form.is_valid():
            data = form.cleaned_data
            try:
                student = Student.objects.get(pk=pk)
                student.name = data.get("name")
                student.class_no = data.get("class_no")
                student.sex = data.get("sex")
                student.age = data.get("age")
                student.money = data.get("money")
                student.born = data.get("born")
                student.description = data.get("description")
                student.save()
                return redirect('/stusys/list/')
            except Student.DoesNotExist:
                return render(request, 'stusys/list_one.html', {
                    "info": form
                })
        else:
            return render(request, 'stusys/list_one.html', {
                "info": form
            })


class StudentAddView(View):
    """添加一条数据"""

    def get(self, request):
        # 获取form表单
        return render(request, 'stusys/add.html', {
            'infoadd': StudentForm()
        })

    def post(self, requset):
        form_info = StudentForm(requset.POST)
        if form_info.is_valid():
            data = form_info.cleaned_data  # 数据为字典
            try:
                Student.objects.create(
                    name=data.get('name'),
                    sex=data.get('sex'),
                    class_no=data.get('class_no'),
                    age=data.get('age'),
                    born=data.get('born'),
                    money=data.get('money'),
                    description=data.get('description')
                )
                return redirect('/stusys/list/')
            except:
                pass
        else:
            return render(requset, 'stusys/add.html', {
                "infoadd": form_info
            })


class StudentDeleteView(View):
    """删除一条数据"""

    def get(self, request, pk):
        try:
            Student.objects.get(pk=pk).delete()
        except Student.DoesNotExist:
            print('当前数据已经被删除')
        return redirect('/stusys/list/')
