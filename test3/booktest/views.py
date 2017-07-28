# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):
    return HttpResponse(request.path)

def detail(request,num):
    return HttpResponse(num)
# 展示链接页面
def getTest1(request):
    return render(request,'booktest/getTest1.html')
# 接收一键一值的情况
def getTest2(request):
    a1 =request.GET['a']
    b1 =request.GET['b']
    c1 =request.GET['c']
    content ={'a':a1,'b':b1,'c':c1}
    return render(request,'booktest/getTest2.html',content)
# 接收一键多值的情况
def getTest3(request):
    a1=request.GET.getlist('a')
    content={'a':a1}
    return render(request,'booktest/getTest3.html',content)

def postTest1(request):
    return render(request,'booktest/postTest1.html')


def postTest2(request):
    uname=request.POST['uname']
    upwd =request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    uaddress = request.POST['uaddress']
    content = {'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby,'uaddress':uaddress}
    return render(request,'booktest/postTest2.html',content)

# cookie联系
def cookieTest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if cookie.has_key('t1'):
        response.write(cookie['t1'])
    # response=HttpResponse()
    # response.set_cookie('t1','abc')
    return response
# 重定向
def redTest1(request):
    # return HttpResponseRedirect('/booktest/redTest2/')简写
    return redirect('/booktest/redTest2')

def redTest2(request):
    return HttpResponse('重定向的页面')

# 用户登录练习sessino

def session1(request):
    uname = request.session.get('uname','游客请登录')
    # uname = None

    content = {'uname':uname}
    return render(request,'booktest/session1.html',content)

def session2(request):
    return render(request,'booktest/session2.html')

def session2_handle(request):
    uname = request.POST['uname']
    request.session.set_expiry(0)
    request.session['uname']=uname
    return redirect('/booktest/session1/')

def session3(request):
    del request.session['uname']
    return redirect('/booktest/session1')

