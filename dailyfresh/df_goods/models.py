# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
import sys
reload(sys)
sys.setdefaultencoding("utf8")
# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20,default='500g')
    gclick = models.IntegerField()
    gjianjie = models.CharField(max_length=1000)
    gkucun = models.IntegerField()
    gcontent = HTMLField()
    gtype = models.ForeignKey(TypeInfo)
    # gadv = models.BooleanField()
    def __str__(self):
        return self.gtitle
    def title(self):
        return self.gtitle
    gtitle.short_description = '名称'
    def price(self):
        return self.gprice
    price.short_description = '价格'
    def click(self):
        return self.gclick
    click.short_description = '点击量'
    def kucun(self):
        return self.gkucun
    kucun.short_description = '库存'
    def type(self):
        return self.gtype
    type.short_description = '类型'
