# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-18 02:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_orderlineitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='user',
        ),
    ]
