#coding=utf8
from django.shortcuts import render
from  models import *
from django.db.models import Max,F,Q,Min,Avg
# Create your views here.

def index(request):
    list = BookInfo.books1.aggregate(Avg('bread'))
    content = {"list":'list'}
    return render(request,'booktest/index.html',content)

def area(request):
    area = AreaInfo.objects.get(pk=130100)
    content = {"area":area}
    return render(request,'booktest/area.html',content)
