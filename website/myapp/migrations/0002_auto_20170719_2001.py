# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Publisher',
            new_name='publisher',
        ),
    ]