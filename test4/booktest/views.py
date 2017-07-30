# coding=utf-8
from django.shortcuts import render
from models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    # hero = HeroInfo.objects.get(pk=1)
    # content = {'hero':hero}
    list = HeroInfo.objects.filter(isDelete=False)
    content = {'list':list}
    return render(request,'booktest/index.html',content)

def show(request,id,id2):
    content = {'show':id}
    return render(request,'booktest/show.html',content)


# 模板继承
def index2(request):
    return render(request,'booktest/index2.html')


def user1(request):
    return  render(request,'booktest/user1.html')
def user2(request):
    return  render(request,'booktest/user2.html')

# html转义
def htmlTest(request):
    content = {'html':'<h1>998</h1>'}
    return render(request,'booktest/htmlTset.html',content)

# cstf 跨站伪造

def csrf1(request):
    return render(request,'booktest/csrf1.html')

def csrf2(request):
    uname= request.POST['uname']
    # return render(request,'booktest/csrf1.html',{'uname':uname})
    return HttpResponse(uname)

def verifyCode(request):
    from PIL import Image,ImageDraw,ImageFont
    import random
    import cStringIO
    # 创建背景色
    bgcolor = (random.randrange(50,100),random.randrange(50,100),0)
    # 规定宽高
    width = 80
    height = 20
    # 创建画布
    image = Image.new('RGB',(width,height),bgcolor)
    # 构造字体对象
    font = ImageFont.truetype('FreeMono.ttf',20)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    # 创建文本内容
    text = 'ABCD78953'
    textTemp=''
    for i in range(4):
        textTemp1 = text[random.randrange(0,len(text))]
        textTemp += textTemp1
        draw.text(
            (i*15,0),
            textTemp1,
            (255,255,255),
            font
        )
        request.session['code']=textTemp
    # draw.text((0,0),text,(255,255,255),font)
    # 保存到内存流中
    buf = cStringIO.StringIO()
    image.save(buf,'png')
    # 将内存流中的内容输出到客户端
    return HttpResponse(buf.getvalue(),'image/png')

def verifyTest1(request):
    return render(request,'booktest/verifyTest1.html')

def verifyTest2(request):
    code1 = request.POST['code1']
    code2 = request.session['code']
    if code1==code2:
        request.session['code']='jxust'
        return HttpResponse('ok')
    else:
        request.session['code']='jxust'
        return HttpResponse('no')
