# coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.

class goodsAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','click','kucun','type']
    search_fields = ['gtitle']
    list_filter = ['gtype']

class typeAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle',]
admin.site.register(TypeInfo,typeAdmin)
admin.site.register(GoodsInfo,goodsAdmin)