# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanager', '0007_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='lender',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]