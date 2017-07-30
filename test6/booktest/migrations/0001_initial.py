# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atitle', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(blank=True, to='booktest.AreaInfo', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]
