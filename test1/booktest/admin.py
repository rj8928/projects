from django.contrib import admin

# Register your models here.

from models import *
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcontent','hbook']
    search_fields = ['hname']
    list_per_page = 10


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_data']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_data']})
    ]
    inlines = [HeroInfoInline]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
