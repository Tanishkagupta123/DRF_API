from rest_framework import serializers
from .models import Student

class Stu_serializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=50)
    age=serializers.IntegerField()
    city=serializers.CharField(max_length=30)
    email=serializers.EmailField()

    class Meta:
        model = Student
        fields = '__all__'