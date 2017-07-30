# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import os
from models import *
from  django.conf import settings
from django.core.paginator import *
# Create your views here.

def index(request):
    return render(request,'booktest/index.html')

def uploadPic(request):
    return render(request,'booktest/uploadPic.html')

def uploadHandel(request):
    pic1 = request.FILES['pic1']
    picName = os.path.join(settings.MEDIA_ROOT,pic1.name)
    with open(picName,'w') as pic:
        for c in pic1.chunks():
            pic.write(c)
        pic.close()
    return HttpResponse('<img src="/abc2/media/%s">'%pic1.name)

def herolist(request,pindex=1):
    if pindex=='':
        pindex=1
    list = HeroInfo.objects.all()
    paginator = Paginator(list,5)
    page = paginator.page(int(pindex))
    content = {'page':page}
    return render(request,'booktest/herolist.html',content)

# 省市区选择
def area(request):
    return render(request,'booktest/area.html')

def area2(request,id):
    id1=int(id)
    if id1==0:
        data = AreaInfo.objects.filter(aParent__isnull=True)
    else:
        data = {[]}
    list = []
    for area9 in data:
        list.append([area9.id,area9.atitle])
    return JsonResponse({'data':list})





