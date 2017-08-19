# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 11:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('username', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u7528\u6237\u540d')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='\u90ae\u7bb1\u5730\u5740')),
                ('url', models.URLField(blank=True, max_length=100, null=True, verbose_name='\u4e2a\u4eba\u7f51\u9875\u5730\u5740')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='two.Article', verbose_name='\u6587\u7ae0'),
        ),
        migrations.AddField(
            model_name='comment',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='two.Comment', verbose_name='\u7236\u7ea7\u8bc4\u8bba'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
        ),
    ]