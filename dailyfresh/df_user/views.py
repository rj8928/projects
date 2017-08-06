# coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from models import *
import sys
sys.path.append('../')
from df_goods.models import *
from df_order.models import *
from hashlib import sha1
import user_decorator
from django.core.paginator import Paginator
# Create your views here.

def register(request):
    return render(request,'df_user/register.html')

def register_handle(requset):
    # 接受用户输入
    post = requset.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    uemail = post.get('email')
    upwd2 = post.get('cpwd')
    user = UserInfo.objects.filter(uname=uname)
    # 判断两次密码
    if upwd != upwd2 and uname==user:
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    # 注册成功，跳转
    return  redirect('/user/login/')

# 判断用户名是否已存在
def check_user(requset,val):
    user = UserInfo.objects.filter(uname=val)
    print (val)
    if user:
        return JsonResponse({"val":'1'})
    else:
        return JsonResponse({"val":'0'})

    #登录
def login(request,uname=''):
    content = {'error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',content)

# 登录处理
def login_handle(request):

    check_u = False
    check_p = False
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    checkbox = request.POST.get('check')
    user = UserInfo.objects.filter(uname=username)
    if user:

        check_u = True
    else:
        content = {'error_name': 0, 'error_pwd': 1, 'uname': username}
        return render(request,'df_user/login.html',content)
    # 密码加密查询
    s1 = sha1()
    s1.update(pwd)
    upwd2 = s1.hexdigest()
    user1 = UserInfo.objects.get(uname=username)
    if upwd2 == user1.upwd:

        check_p = True
    else:
        content = {'error_name': 1, 'error_pwd': 0, 'uname': username}
        return render(request,'df_user/login.html',content)

    if check_u==True and check_p == True:
        url = request.COOKIES.get('url', '/')

        red = HttpResponseRedirect(url)

        if checkbox=='1':
            red.set_cookie('jizhuuname',username)

        else:
            red.set_cookie('jizhuuname', '',max_age=-1)

        request.session['user'] = user1.uname
        request.session['userid']=user1.id
        red.set_cookie('uemail', user1.uemail)
        red.set_cookie('uname', user1.uname)
        red.set_cookie('uphone', user1.uphone)
        # red.set_cookie('uyoubian', user1.uyoubian)
        # red.set_cookie('ushou', user1.ushou)
        return red

@user_decorator.login
def usercenterinfo(request):
     uname =request.session.get('user')
     # print (uname)
     user = UserInfo.objects.get(uname=uname)
     goods_ids = request.COOKIES.get('goods_ids','')
     list = []
     if goods_ids !='':
         goods_id = goods_ids.split(',')
         for i in goods_id:
             name = 'goods'+i
             name = GoodsInfo.objects.filter(id=int(i))
             if len(name)>0:
                list.append(name[0])
     content = {'uaddress':user.uaddress,'pwd':'user','list':list,'uname':user.uname}
     return render(request,'df_user/user_center_info.html',content)

@user_decorator.login
def usercenterorder(request,index):
    userid = request.session.get('userid')
    order = OrderInfo.objects.filter(user_id=int(userid))
    print order
    list =[]
    if len(order)>0:
        for order1 in order:
            list2 = []
            list3 = []
            list4 = []
            list2.append(order1)
            detail = order1.orderdetailinfo_set.all()
            # list3.append(detail)
            for goods1 in detail:
                goods =GoodsInfo.objects.get(id=goods1.goods_id)
                list3.append(goods1)
                list3.append(goods)
                list4.append(list3)
                list3 = []


            list2.append(list4)
            list.append(list2)


    p = Paginator(order,5)
    if index == '':
        index = '1'
    pindex = int(index)
    list2 = p.page(pindex)
    plist = p.page_range

            # list2.append(detail)
            # list.append(list2)
    print plist
    print pindex
    content = {'pwd':'user','order':order,'list':list,'list2':list2,'plist':plist,'pIndex':pindex}
    return render(request,'df_user/user_center_order.html',content)

@user_decorator.login
def usercentersite(request):
    uname = request.session.get('user')
    # print (uname)
    user = UserInfo.objects.get(uname=uname)
    content = {'uaddress': user.uaddress,'uyoubian':user.uyoubian,'ushou':user.ushou,'uphone':user.uphone
               ,'pwd':'user'}
    return render(request,'df_user/user_center_site.html',content)

def editorinfo(request):
    ushou = request.POST.get('ushou')
    uaddress = request.POST.get('uaddress')
    uyoubian = request.POST.get('uyoubian')
    uphone = request.POST.get('uphone')
    uname = request.session.get('user')
    user = UserInfo.objects.get(uname=uname)
    user.ushou = ushou
    user.uaddress = uaddress
    user.uyoubian = uyoubian
    user.uphone = uphone
    user.save()
    red = HttpResponseRedirect('/user/site/')
    # red.set_cookie('uaddress',uaddress)
    red.set_cookie('uphone', uphone)
    # red.set_cookie('uyoubian',uyoubian)
    # red.set_cookie('ushou', ushou)

    return red

def logout(request):
    request.session.flush()
    return redirect('/')




