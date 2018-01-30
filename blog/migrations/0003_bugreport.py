# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-30 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180123_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorr', models.CharField(max_length=20)),
                ('titler', models.CharField(max_length=200)),
                ('textr', models.TextField()),
                ('created_dater', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_dater', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
