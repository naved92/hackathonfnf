# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0003_auto_20160405_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('driver_name', models.CharField(max_length=50, null=True, blank=True)),
                ('driver_address', models.CharField(max_length=300, null=True, blank=True)),
                ('driver_employer', models.ForeignKey(to='carpool.UserProfile')),
            ],
        ),
    ]
