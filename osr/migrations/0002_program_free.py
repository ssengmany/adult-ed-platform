# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='free',
            field=models.BooleanField(default=False, verbose_name='free'),
        ),
    ]
