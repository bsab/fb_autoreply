# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-12 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fbautoreply', '0002_auto_20160802_0643'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoresponderType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='autoresponder_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fbautoreply.AutoresponderType'),
        ),
    ]
