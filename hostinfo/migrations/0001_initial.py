# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.3 on 2017-08-10 14:10
=======
# Generated by Django 1.11.3 on 2017-08-09 22:52
>>>>>>> origin/master
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, null=True, verbose_name='机房')),
            ],
            options={
                'verbose_name_plural': '机房组',
                'db_table': 'Business',
                'verbose_name': '机房组',
            },
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_model', models.CharField(blank=True, max_length=128, verbose_name='CPU型号')),
                ('cpu_count', models.SmallIntegerField(verbose_name='物理CPU个数')),
                ('cpu_core_count', models.SmallIntegerField(verbose_name='CPU核心数')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name_plural': 'CPU部件',
                'db_table': 'Cpu',
                'verbose_name': 'CPU部件',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root', models.CharField(max_length=50, null=True, verbose_name='用户')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP')),
                ('port', models.CharField(max_length=50, null=True, verbose_name='端口')),
                ('cmd', models.CharField(max_length=50, null=True, verbose_name='命令')),
                ('user', models.CharField(max_length=50, null=True, verbose_name='操作者')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='时间')),
            ],
            options={
                'verbose_name_plural': '历史命令',
                'db_table': 'History',
                'verbose_name': '历史命令',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, verbose_name='主机编号')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP')),
                ('port', models.CharField(max_length=50, null=True, verbose_name='端口')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='登陆用户')),
                ('password', models.CharField(max_length=50, null=True, verbose_name='密码')),
                ('osversion', models.CharField(max_length=50, null=True, verbose_name='系统版本')),
                ('memory', models.CharField(max_length=50, null=True, verbose_name='内存')),
                ('disk', models.CharField(max_length=50, null=True, verbose_name='硬盘')),
                ('sn', models.CharField(max_length=50, null=True, verbose_name='SN')),
                ('model_name', models.CharField(max_length=50, null=True, verbose_name='型号')),
                ('cpu_core', models.CharField(max_length=50, null=True, verbose_name='CPU')),
                ('beizhu', models.CharField(max_length=1000, null=True, verbose_name='备注')),
                ('jifang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hostinfo.Business', verbose_name='机房')),
            ],
            options={
                'verbose_name_plural': '服务器',
                'db_table': 'Host',
                'verbose_name': '服务器',
            },
        ),
<<<<<<< HEAD
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_use', models.CharField(max_length=32, null=True, verbose_name='CPU使用率')),
                ('mem_use', models.CharField(max_length=32, null=True, verbose_name='内存使用率')),
                ('in_use', models.CharField(max_length=32, null=True, verbose_name='进流量')),
                ('out_use', models.CharField(max_length=32, null=True, verbose_name='出流量')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostinfo.Host')),
            ],
            options={
                'verbose_name': '监控状态',
                'verbose_name_plural': '监控状态',
                'db_table': 'Monitor',
            },
=======
        migrations.AddField(
            model_name='cpu',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostinfo.Host'),
>>>>>>> origin/master
        ),
    ]
