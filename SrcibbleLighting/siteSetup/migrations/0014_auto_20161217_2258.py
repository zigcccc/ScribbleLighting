# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-17 21:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteSetup', '0013_auto_20161217_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 17, 22, 58, 32, 281431)),
        ),
    ]
