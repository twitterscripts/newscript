# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-30 10:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_bugreport_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bugreport',
            name='published_date',
        ),
    ]