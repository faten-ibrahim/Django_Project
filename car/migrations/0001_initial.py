# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-19 16:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarReservationRequest',
            fields=[
                ('car_requested', models.AutoField(primary_key=True, serialize=False)),
                ('pick_up_date', models.DateField(default=datetime.date.today)),
                ('Drop_off_date', models.DateField(default=datetime.date.today)),
                ('pick_up_time', models.TimeField(default='00:00')),
                ('Drop_off_time', models.TimeField(default='00:00')),
            ],
        ),
    ]
