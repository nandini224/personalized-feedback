# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-11 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_answermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answermodel',
            name='sessionfive',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='answermodel',
            name='sessionfour',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='answermodel',
            name='sessionone',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='answermodel',
            name='sessionthree',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='answermodel',
            name='sessiontwo',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]