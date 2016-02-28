# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160122_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together=set([('url', 'owner')]),
        ),
    ]
