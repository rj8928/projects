# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sname', models.CharField(max_length=20)),
                ('sgender', models.BooleanField()),
                ('snum', models.IntegerField(max_length=10)),
                ('sclass', models.ForeignKey(to='student.ClassInfo')),
            ],
        ),
    ]
