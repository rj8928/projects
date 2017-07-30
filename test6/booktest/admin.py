from django.contrib import admin
from models import *

# Register your models here.
class Test1Manager(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(Test1,Test1Manager)