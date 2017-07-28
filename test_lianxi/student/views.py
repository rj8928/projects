# -*- coding=utf-8 -*-
from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    claclist = ClassInfo.objects.all()
    content = {'list':claclist}
    return render(request,'students/index.html',content)

def show(request,id):
    classinfo = ClassInfo.objects.get(pk=id)
    stulist = classinfo.studentinfo_set.all()
    content = {'list':stulist}
    return render(request,'students/show.html',content)
