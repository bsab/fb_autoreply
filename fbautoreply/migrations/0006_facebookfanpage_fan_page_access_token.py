# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-14 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbautoreply', '0005_auto_20160812_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookfanpage',
            name='fan_page_access_token',
            field=models.CharField(max_length=500, null=True),
        ),
    ]