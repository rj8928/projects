# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateTimeField()
    # def __str__(self):
    #     return self.btitle.encode('utf-8')

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook=models.ForeignKey(BookInfo)
    # def __str__(self):
    #     return self.hname.encode('utf-8')

    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'
