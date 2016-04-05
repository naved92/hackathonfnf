# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0006_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rider', models.ForeignKey(to='carpool.UserProfile')),
                ('trip', models.ForeignKey(to='carpool.Trip')),
            ],
        ),
        migrations.CreateModel(
            name='TripRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trip_requested', models.ForeignKey(to='carpool.Trip')),
                ('user_requested', models.ForeignKey(to='carpool.UserProfile')),
            ],
        ),
    ]
