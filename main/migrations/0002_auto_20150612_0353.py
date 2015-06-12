# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='cover',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookmark',
            name='is_trashed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date created'),
            preserve_default=True,
        ),
    ]
