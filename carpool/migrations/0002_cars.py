# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_number', models.CharField(max_length=300, null=True, blank=True)),
                ('car_model', models.CharField(max_length=300, null=True, blank=True)),
                ('number_of_seats', models.IntegerField(null=True, blank=True)),
                ('car_availablity_status', models.CharField(default=b'p', max_length=2, choices=[(b'a', b'active'), (b'd', b'deactive'), (b'o', b'other'), (b'p', b'pending'), (b's', b'suspended')])),
                ('owner', models.ForeignKey(to='carpool.UserProfile')),
            ],
        ),
    ]
