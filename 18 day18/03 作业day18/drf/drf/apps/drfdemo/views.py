from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student


class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
