# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170929_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mark_down',
            field=models.BooleanField(default=False, verbose_name='显示方式'),
        ),
    ]