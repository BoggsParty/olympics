# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2018-01-07 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20170919_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='extended_user',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='extended_user',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
