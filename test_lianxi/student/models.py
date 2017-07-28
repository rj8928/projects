# -*- coding=utf-8 -*-
from django.db import models

# Create your models here.



class ClassInfo(models.Model):
    cname = models.CharField(max_length=20)
    def __str__(self):
        return self.cname.encode('utf-8')


class StudentInfo(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField()
    snum = models.IntegerField(max_length=10)
    sclass = models.ForeignKey(ClassInfo)
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'