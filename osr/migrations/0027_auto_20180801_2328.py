# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-02 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osr', '0026_auto_20180801_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Timestamp'),
        ),
    ]
