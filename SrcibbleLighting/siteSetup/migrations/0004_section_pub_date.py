# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-17 21:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteSetup', '0003_paragraph'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 17, 22, 12, 52, 451498)),
        ),
    ]
