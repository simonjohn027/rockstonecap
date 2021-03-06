# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-11 19:56
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdrawdate', models.DateField(default=datetime.datetime(2018, 7, 11, 19, 56, 19, 254867, tzinfo=utc))),
                ('goal', models.CharField(blank=True, choices=[('Major Savings', 'Saving for major expenses or purchase (education, vacation, debt etc.) '), ('Wealth', 'Building long term wealth and preparing for retirement'), ('Testing', 'Testing the digital currency market.')], default='Testing the digital currency market.', max_length=500)),
                ('portfolio', models.CharField(blank=True, choices=[('M', 'Momentum'), ('C', 'Consecutive')], default='Consecutive', max_length=100)),
                ('investmentAmount', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=12)),
                ('currency_understand', models.CharField(blank=True, choices=[('None', 'None'), ('Some', 'Some'), ('Good', 'Good'), ('Extensive', 'Extensive')], default='Good', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
