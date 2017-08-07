# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jiguidx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xuan', models.CharField(max_length=64, verbose_name='多选选项')),
            ],
            options={
                'verbose_name': '多选',
                'verbose_name_plural': '多选',
                'db_table': 'Jiguidx',
            },
        ),
        migrations.CreateModel(
            name='JiguiInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名字')),
                ('jq', models.CharField(max_length=64, verbose_name='总数')),
                ('zy', models.CharField(max_length=64, null=True, verbose_name='自用')),
                ('ziy', models.CharField(max_length=64, null=True, verbose_name='在用')),
                ('zs', models.CharField(max_length=64, null=True, verbose_name='自用')),
                ('zb', models.CharField(max_length=64, null=True, verbose_name='在售')),
                ('sh', models.CharField(max_length=64, null=True, verbose_name='整包')),
                ('xz', models.CharField(max_length=64, null=True, verbose_name='闲置')),
                ('yong', models.BooleanField(verbose_name='是否在用')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('dx', models.ManyToManyField(to='jigui.Jiguidx', verbose_name='多选')),
            ],
            options={
                'verbose_name': '机柜',
                'verbose_name_plural': '机柜中心',
                'db_table': 'JiguiInfo',
            },
        ),
    ]
