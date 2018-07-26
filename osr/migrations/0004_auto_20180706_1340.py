# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-06 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osr', '0003_auto_20180705_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='types_of_service_providers',
        ),
        migrations.AddField(
            model_name='program',
            name='types_of_sps',
            field=models.TextField(blank=True, default=b'', max_length=600, verbose_name='types of service providers'),
        ),
        migrations.AlterField(
            model_name='program',
            name='eligible_immigration_status',
            field=models.ManyToManyField(blank=True, to='osr.ImmigrationStatus'),
        ),
        migrations.AlterField(
            model_name='program',
            name='support',
            field=models.TextField(blank=True, default=b'', max_length=600, verbose_name='support'),
        ),
        migrations.AlterField(
            model_name='program',
            name='support_en',
            field=models.TextField(blank=True, default=b'', max_length=600, null=True, verbose_name='support'),
        ),
        migrations.AlterField(
            model_name='program',
            name='support_fr',
            field=models.TextField(blank=True, default=b'', max_length=600, null=True, verbose_name='support'),
        ),
        migrations.DeleteModel(
            name='ServiceProviderType',
        ),
    ]
