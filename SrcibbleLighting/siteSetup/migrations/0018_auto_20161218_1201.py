# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-18 11:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteSetup', '0017_auto_20161218_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 18, 12, 1, 21, 936423)),
        ),
    ]
