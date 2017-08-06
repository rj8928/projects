from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from models import *
import sys
sys.path.append('../')
from df_goods.models import *
from df_user.models import *
import user_decorator
# Create your views here.


@user_decorator.login
def cart(request):
    userid = request.session.get('userid')
    goodslist = CartInfo.objects.filter(user_id=userid)
    list = []

    for i in goodslist:
        list.append(i.goods_id)

    list1 = []
    for i in list:
        goods= GoodsInfo.objects.get(id=int(i))
        list1.append(goods)
    list2 = []
    k = 0
    for i in list1:

        list3 = []
        list3.append(i)
        list3.append(goodslist[k])

        list2.append(list3)
        k +=1
    content = {
        'pwd':'user','goodslist':list2,
    }
    return render(request,'df_cart/cart.html',content)


@user_decorator.login
def addtocart(request,id,num):
    userid = request.session.get('userid')
    # print userid
    # userid = UserInfo.objects.get(uname=username)

    # goods = GoodsInfo.objects.get(id=int(id))

    # cart = CartInfo.objects.filter(user=username)
    # print cart
    # if len(cart)==0:
    #     print 9999
    userid = int(userid)
    goodsid = int(id)
    num = int(num)
    goodid = CartInfo.objects.filter(user_id=userid, goods_id=id)
    if len(goodid)==0:
        cart = CartInfo()
        cart.user_id = userid
        cart.goods_id = goodsid
        cart.count = num
        cart.save()
    else:
        goodid[0].count +=1
        goodid[0].save()
    return JsonResponse({})

    # cart.user = int(userid)
    # cart.goods = int(goods.id)
    # cart.count = int(num)
    # cart.save()
    # return JsonResponse({})
def buy_now(request):
    userid = request.session.get('userid')
    if userid:
        return JsonResponse({"stu":1})
    else:
        return JsonResponse({"stu":0})

def del_cart_goods(request,goods_id):
    userid = request.session.get('userid')
    goods_id = int(goods_id)
    userid = int(userid)
    print (goods_id)
    print (userid)
    goods = CartInfo.objects.filter(user_id=userid).filter(goods_id=goods_id)
    print goods
    goods[0].delete()
    return  JsonResponse({})