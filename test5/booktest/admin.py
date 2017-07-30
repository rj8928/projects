# coding=utf-8
from django.contrib import admin
from models import *

# Register your models here.
@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle']


admin.site.register(UserInfo)
# admin.site.register(BookInfo,BookInfoAdmin)装饰器注册
admin.site.register(HeroInfo)
admin.site.register(AreaInfo)
