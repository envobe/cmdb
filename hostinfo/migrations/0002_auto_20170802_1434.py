# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='cpu_use',
            field=models.CharField(max_length=50, null=True, verbose_name='CPU使用率'),
        ),
        migrations.AddField(
            model_name='host',
            name='mem_use',
            field=models.CharField(max_length=50, null=True, verbose_name='内存使用率'),
        ),
        migrations.AlterField(
            model_name='host',
            name='jifang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hostinfo.Business', verbose_name='机房'),
        ),
    ]
