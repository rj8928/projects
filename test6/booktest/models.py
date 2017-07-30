from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True)

class Test1(models.Model):
    content = HTMLField()