# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-11 20:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capital', '0002_auto_20180611_2218'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RCPortfolio',
            new_name='CapitalPortfolio',
        ),
        migrations.RenameModel(
            old_name='ClientsPort',
            new_name='ClientPortfolio',
        ),
    ]
