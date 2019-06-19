from rest_framework import serializers

from drfdemo.models import Student


class Student1Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    sex = serializers.IntegerField()
    age = serializers.IntegerField()


def check_name(data):
    if data == 'null':
        raise serializers.ValidationError('名字不能为null')
    return data


class Student2Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50,validators=[check_name, ])
    age = serializers.IntegerField(required=True, min_value=0, max_value=100)
    description = serializers.CharField()
    sex = serializers.IntegerField(required=True)

    def validate_name(self, data):
        print('===========', data)

        if data == 'root':
            raise serializers.ValidationError("名字不能是root")

        return data


class Student3Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField(required=True, min_value=0, max_value=100)
    description = serializers.CharField()
    sex = serializers.IntegerField(required=True)
    class_no = serializers.IntegerField()

    def create(self, validated_data):
        name = validated_data.get("name")
        age = validated_data.get("age")
        description = validated_data.get("description")
        sex = validated_data.get("sex")
        class_no = validated_data.get('class_no')

        student = Student.objects.create(
            name=name,
            age=age,
            description=description,
            sex=sex,
            class_no=class_no,
        )
        return student

    def update(self, instance, validated_data):
        name = validated_data.get("name")
        age = validated_data.get("age")
        description = validated_data.get("description")
        sex = validated_data.get("sex")
        class_no = validated_data.get('class_no')

        instance.name = name
        instance.age = age
        instance.description = description
        instance.sex = sex
        instance.class_no = class_no

        instance.save()
        return instance


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField(required=True, min_value=0, max_value=100)
    description = serializers.CharField()
    sex = serializers.IntegerField(required=True)
    class_no = serializers.IntegerField()

    def validate_name(self, data):
        if data == 'root':
            raise serializers.ValidationError("名字不能是root!!!")
        return data

    def create(self, validated_data):
        name = validated_data.get("name")
        age = validated_data.get("age")
        description = validated_data.get("description")
        sex = validated_data.get("sex")
        class_no = validated_data.get('class_no')

        student = Student.objects.create(
            name=name,
            age=age,
            description=description,
            sex=sex,
            class_no=class_no,
        )
        return student

    def update(self, instance, validated_data):
        name = validated_data.get("name")
        age = validated_data.get("age")
        description = validated_data.get("description")
        sex = validated_data.get("sex")
        class_no = validated_data.get('class_no')

        instance.name = name
        instance.age = age
        instance.description = description
        instance.sex = sex
        instance.class_no = class_no

        instance.save()
        return instance


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_name(self, data):
        if data == 'root':
            raise serializers.ValidationError('NO root!!')
        return data
