from django.shortcuts import render,redirect
from .serializers import *
from .models import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def student(req):
    if req.method=="POST":
        data=req.body
        stream= io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        serializer=Stu_serializer(data=p_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse({"msg":"object created"},content_type='application/json')
        else:
            data=JSONRenderer().render(serializer.errors)
            return HttpResponse(data,content_type='application/json')

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


#Deserializer

