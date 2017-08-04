# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToolsScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='工具名称')),
                ('tool_script', models.TextField(verbose_name='脚本')),
                ('tool_run_type', models.IntegerField(choices=[(0, 'Shell'), (1, 'Python')], default=0, verbose_name='脚本类型')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='工具说明')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '工具',
                'verbose_name_plural': '工具',
            },
        ),
    ]
