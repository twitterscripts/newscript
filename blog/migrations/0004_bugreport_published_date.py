# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-30 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_bugreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugreport',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
