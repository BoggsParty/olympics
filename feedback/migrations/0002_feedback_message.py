# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-09-20 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
