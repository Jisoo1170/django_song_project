# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181024_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='site',
            field=models.CharField(choices=[('1', '멜론'), ('2', '지니'), ('3', '벅스')], max_length=1),
        ),
    ]
