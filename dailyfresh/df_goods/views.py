# coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60*15)
def index(request):
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    context = {
        'type0':type0,'type01':type01,'pwd':'goods',
    }
    return render(request,'df_goods/index.html',context)
@cache_page(60*15)
def list(request,id,sort,Pindex=''):
    id = int(id)

    if sort == '0':
        list = TypeInfo.objects.get(id=id).goodsinfo_set.order_by('-id')
    elif sort == '1':
        list = TypeInfo.objects.get(id=id).goodsinfo_set.order_by('-gprice')
    elif sort== '2':
        list = TypeInfo.objects.get(id=id).goodsinfo_set.order_by('-gclick')
    # print (list)
    # 分页
    p = Paginator(list,20)

    if Pindex == '':
        Pindex = '1'
    Pindex = int(Pindex)
    list2 = p.page(Pindex)
    # print (list2)
    plist = p.page_range
    typelist = TypeInfo.objects.all()
    news1 = typelist[0].goodsinfo_set.order_by('-id')[0:2]
    content = {
        'list':list2,'plist':plist,'pindex':Pindex,'type':id,'pwd':'goods','news':news1
    }
    return render(request,'df_goods/list.html',content)

def detail(request,id):
    id = int(id)
    detail = GoodsInfo.objects.get(id=id)
    detail.gclick +=1
    detail.save()
    typelist = TypeInfo.objects.all()
    news1 = typelist[0].goodsinfo_set.order_by('-id')[0:2]
    type = TypeInfo.objects.get(id=detail.gtype_id)
    context = {
        'detail':detail,'news':news1,'pwd':'goods','type':type.ttitle
    }
    response =  render(request,'df_goods/detail.html',context)

    # 记录最近浏览，在用户中心使用
    goods_ids = request.COOKIES.get('goods_ids','')

    if goods_ids != '':
        id ='%d'%id
        goods_ids1=goods_ids.split(',')
        if goods_ids1.count(id)>=1:
            goods_ids1.remove(id)
        goods_ids1.insert(0,id)
        if len(goods_ids1)>5:
            del goods_ids1[5]
        goods_ids=','.join(goods_ids1)
    else:
        goods_ids=id
    response.set_cookie('goods_ids',goods_ids)

    return response