# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pw', models.CharField(max_length=10, blank=True)),
                ('reward', models.IntegerField(null=True, blank=True)),
                ('address', models.CharField(max_length=300, blank=True)),
                ('verification_status', models.CharField(default=b'p', max_length=2, choices=[(b'a', b'active'), (b'd', b'deactive'), (b'o', b'other'), (b'p', b'pending'), (b's', b'suspended')])),
                ('verification_code', models.CharField(default=b'123456', max_length=128)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
