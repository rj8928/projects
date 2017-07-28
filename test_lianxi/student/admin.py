from django.contrib import admin
from models import *

# Register your models here.
class StudentInfoInlines(admin.TabularInline):
    model = StudentInfo
    extra = 5

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['sname','gender','snum','sclass']
    search_fields = ['sname']

class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ['cname']
    inlines = [StudentInfoInlines]

admin.site.register(StudentInfo,StudentInfoAdmin)
admin.site.register(ClassInfo,ClassInfoAdmin)