# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-13 07:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accs', '0003_auto_20180611_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='withdrawdate',
            field=models.DateField(default=datetime.datetime(2018, 7, 13, 7, 37, 38, 833282, tzinfo=utc)),
        ),
    ]
