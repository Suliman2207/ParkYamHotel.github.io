# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-10 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParkYamManagerApp', '0009_auto_20170610_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_room_being_cleaned',
            field=models.BooleanField(default=False, verbose_name='Is Room Being Cleaned'),
        ),
    ]
