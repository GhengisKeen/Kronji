# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RaceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='dicts',
            field=models.TextField(max_length=5000000),
        ),
    ]
