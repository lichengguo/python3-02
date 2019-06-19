from django.http import JsonResponse, HttpResponse
from django.views import View
from drfdemo.models import Student
from ser.serializers import Student1Serializer, Student2Serializer, StudentSerializer, StudentModelSerializer


class StudentsView(View):
    def get(self, request):
        student_list = Student.objects.all()
        serializer = Student1Serializer(instance=student_list, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)


class StudentView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = Student1Serializer(instance=student)
        print(serializer.data)
        return JsonResponse(serializer.data)


class Student2View(View):
    def post(self, request):
        data1 = {
            'name': 'null',
            'age': 19,
            'sex': 2,
            'description': '没有个性签名',
        }
        serializer = Student2Serializer(data=data1)
        result = serializer.is_valid(raise_exception=True)
        print('验证结果 %s' % result)

        if not result:
            print(serializer.error_messages)

        return HttpResponse("序列化器的使用:对客户端提交的数据进行验证")


from .serializers import Student3Serializer


class Student3View(View):
    def post(self, request):
        data = {
            'name': '周末2期',
            'age': 30,
            'sex': 2,
            'class_no': 306,
            'description': '没有个性签名',
        }
        serializer = Student3Serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        print(instance)
        return HttpResponse("序列化器的使用:对客户端提交的数据进行反序列化")


class Student4View(View):
    def put(self, request, pk):
        data = {
            'name': '周末2期aaa',
            'age': 30,
            'sex': 2,
            'class_no': 306,
            'description': '没有个性签名',
        }
        student = Student.objects.get(pk=pk)

        serializer = Student3Serializer(instance=student, data=data)

        serializer.is_valid(raise_exception=True)

        instance = serializer.save()

        print(instance)

        return HttpResponse("序列化器的使用:对客户端提交的数据进行反序列化")


class Student5View(View):
    def get(self, request):
        student_list = Student.objects.all()
        serializer = StudentSerializer(instance=student_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = {
            'name': '周末2期xxx',
            'age': 30,
            'sex': 2,
            'class_no': 306,
            'description': '没有个性签名',
        }
        serializer = StudentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)


class Student6View(View):
    def get(self, request):
        student_list = Student.objects.all()
        serializer = StudentModelSerializer(instance=student_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = {
            'name': 'root',
            'age': 30,
            'sex': 2,
            'class_no': 306,
            'description': '没有个性签名',
        }
        serializer = StudentModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data)
