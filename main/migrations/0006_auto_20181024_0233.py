# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181024_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='deleted',
        ),
        migrations.AddField(
            model_name='store',
            name='reset_list',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='reset_played',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
