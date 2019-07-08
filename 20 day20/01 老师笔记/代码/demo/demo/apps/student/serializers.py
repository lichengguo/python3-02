from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    """学生数据序列化器"""
    class Meta:
        model = Student
        fields = '__all__'