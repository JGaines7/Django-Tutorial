# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='priority',
            field=models.IntegerField(default=3, verbose_name='question priority'),
        ),
    ]
