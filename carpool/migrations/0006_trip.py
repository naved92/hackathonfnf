# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0005_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trip_time', models.DateTimeField(blank=True)),
                ('destination', models.ForeignKey(related_name='destination', to='carpool.Location')),
                ('driver_of_trip', models.ForeignKey(to='carpool.Driver')),
                ('source', models.ForeignKey(related_name='source', to='carpool.Location')),
            ],
        ),
    ]
