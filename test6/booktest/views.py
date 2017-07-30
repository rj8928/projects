# coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from models import *
from django.views.decorators.cache import  cache_page
from django.core.cache import cache
from task import *
# Create your views here.
# 省县市区查询处理
def index(request):
    return render(request,'booktest/index.html')
def getpro(request):
    prolist = AreaInfo.objects.filter(aParent__isnull=True)
    list = []
    for item in prolist:
        list.append([item.id,item.atitle])
    return JsonResponse({'data':list})

def city(request,pro):
    citylist = AreaInfo.objects.filter(aParent__id=pro)
    list = []
    #[{id:1,title:北京},{}]
    for item in citylist:
        list.append({'id':item.id,'title':item.atitle})
    return JsonResponse({'data':list})

# 富文本编辑器
def htmlEditor(request):
    return render(request,'booktest/htmlEditor.html')

def htmlEditorHandle(request):
    html = request.POST['hcontent']
    text1 = Test1()
    text1.content = html
    text1.save()
    content = {'content':html}
    return render(request,'booktest/htmlShow.html',content)

# 缓存
# @cache_page(60*10)
def cache1(request):
    # return HttpResponse('hello')
    # cache.set('key1','value21',600)
    # key = (cache.get('key1'))
    # cache.clear()
    # return HttpResponse(key)
    return render(request,'booktest/cache1.html')

#全文检索加中文分词

def mysearch(request):
    return render(request,'booktest/mysearch.html')

#celery异步
def celeryTest(request):
    show.delay()
    return HttpResponse('ok')