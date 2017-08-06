# coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from models import *
import sys
sys.path.append('../')
from df_goods.models import *
from df_user.models import *
from df_cart.models import *
import user_decorator
import random
import time
from django.db import transaction
# Create your views here.
@user_decorator.login
def order(request):
    list = request.GET['List']
    list = list.split(',')
    # print len(list)
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    for temp in range(len(list) - 1):
        # print temp
        if temp % 2 == 0:
            goods = GoodsInfo.objects.filter(id=int(list[temp]))
            list2.append(goods[0])
            list4.append(goods[0].id)
        else:
            count = int(list[temp])
            list2.append(count)
            list4.append(count)
        if len(list2) >= 2:
            list3.append(list2)
            list5.append(list4)
            list2 = []
            list4 = []

    # print list3
    request.session['orderinfo']=list5
    userid = request.session.get('userid')
    user = UserInfo.objects.get(id=userid)
    content = {'pwd':'user','list3':list3,'address':user.uaddress,'phone':user.uphone,
               'name':user.ushou}
    return render(request,'df_order/place_order.html',content)

# def addorder(request,list):
#     pass
@transaction.atomic()
@user_decorator.login
def suborder(request):
    tran_id = transaction.savepoint()
    userid = request.session.get('userid')
    print userid
    user = UserInfo.objects.get(id=userid)
    address = user.uaddress+' '+'('+user.ushou+' 收)'+'  '+user.uphone
    print address
    list = request.session.get('orderinfo')
    total_price = 0
    list_price = []
    for temp in list:
        goods_id,count = temp
        goods1 = GoodsInfo.objects.get(id=int(goods_id))
        price = goods1.gprice
        if goods1.gkucun<count:
            transaction.savepoint_rollback(tran_id)
            return redirect('/cart/')
        list_price.append(price)

        price1 = price*count
        total_price =total_price+price1

    total_price = total_price+10
    print total_price
    oid = str(random.randint(1000,9999))+str(int(time.time()))
    try:
        neworder = OrderInfo()
        neworder.oid = oid
        neworder.user_id = int(userid)
        neworder.ototal = total_price
        neworder.oaddress = address
        neworder.save()
        i = 0
        for temp in list:
            goods_id,count = temp
            price = list_price[i]
            orderdetail = OrderDetailInfo()
            orderdetail.goods_id = goods_id
            orderdetail.price = price
            orderdetail.count = count
            orderdetail.order_id = oid
            orderdetail.save()
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print '-------------------%s'%e
        transaction.savepoint_rollback(tran_id)
    for temp in list:
        goods_id,count = temp
        goods = CartInfo.objects.get(goods_id=int(goods_id))
        goods.delete()

    return HttpResponse('成功啦')




    # list = request.GET['List']
    # list = list.split(',')
    # print len(list)
    # list2 = []
    # list3 = []
    # for temp in range(len(list)-1):
    #     print temp
    #     if temp%2 == 0:
    #         goods = GoodsInfo.objects.filter(id = int(list[temp]))
    #         list2.append(goods)
    #     else:
    #         count = list[temp]
    #         list2.append(count)
    #     if len(list2)>=2:
    #         list3.append(list2)
    #         list2 = []
    #
    # print list3
    # content = {'list':list3}
    # return HttpResponse(content)