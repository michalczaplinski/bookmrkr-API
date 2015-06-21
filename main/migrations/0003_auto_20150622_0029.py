# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150612_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='content',
            field=models.TextField(verbose_name='content', blank=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='cover',
            field=models.ImageField(upload_to='', null=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.TextField(verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='domain',
            field=models.CharField(verbose_name='domain', max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(verbose_name='title', max_length=50),
        ),
    ]
