# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0004_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=300, blank=True)),
                ('location_lat', models.FloatField(null=True, blank=True)),
                ('location_long', models.FloatField(null=True, blank=True)),
            ],
        ),
    ]
