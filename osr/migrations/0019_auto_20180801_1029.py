# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osr', '0018_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['created'], 'verbose_name': 'feedback', 'verbose_name_plural': 'feedback'},
        ),
        migrations.AlterField(
            model_name='feedback',
            name='content_or_feature_request',
            field=models.CharField(max_length=2000, verbose_name='What other information or feature would make this website more useful for you?'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Timestamp'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='found_what_i_was_looking_for',
            field=models.CharField(max_length=10, verbose_name='Did you find what you were looking for?'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='general_comment',
            field=models.CharField(max_length=2000, verbose_name='Share any comment you have about the adult learning website'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='information_easy_to_understand',
            field=models.CharField(max_length=10, verbose_name='Is the information easy to understand?'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='matchmaker_easy_to_use',
            field=models.CharField(max_length=10, verbose_name='If you used the matchmaker, was it easy to use?'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='matchmaker_helpful',
            field=models.CharField(max_length=10, verbose_name='If you used the matchmaker, did it help you find a program?'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='most_useful_feature',
            field=models.CharField(max_length=50, verbose_name='What feature helped you find a program?'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='purpose_of_visit',
            field=models.CharField(max_length=50, verbose_name='What was the purpose of your visit today?'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.CharField(max_length=50, verbose_name='Please rate the overall experience you had with the adult learning website'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='type_of_user',
            field=models.CharField(max_length=50, verbose_name='You are visiting the adult learning website as a:'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='website_easy_to_navigate',
            field=models.CharField(max_length=10, verbose_name='Is the adult learning website easy to navigate?'),
        ),
    ]
