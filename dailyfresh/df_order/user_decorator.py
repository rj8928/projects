# coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect


# 登录验证
def login(func):
    def login_fun(request,*args,**kwargs):
        if request.session.has_key('user'):
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url',request.get_full_path())
            return red
    return login_fun