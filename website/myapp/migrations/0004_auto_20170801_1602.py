# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170720_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(default='a.png', upload_to='avatar/%Y/%m', verbose_name='\u7528\u6237\u5934\u50cf')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u4e66\u540d'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(verbose_name='\u7f51\u5740'),
        ),
    ]
