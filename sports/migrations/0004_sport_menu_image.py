# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-02-24 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_auto_20170220_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='menu_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
