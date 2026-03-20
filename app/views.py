from django.shortcuts import render,redirect
from .serializers import *
from .models import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response


# Create your views here.
 

def student(req):
    data=Student.objects.all()
    serializer=Stu_serializer(data,many=True)
    print(serializer)
    print(serializer.data)

# def student(req):
#     data=Student.objects.get(id=1)
#     serializer=Stu_serializer(data)
#     print(serializer)
#     print(serializer.data)


    json = JSONRenderer().render(serializer.data)
    print(json)
    return HttpResponse(json,content_type='application/json')

