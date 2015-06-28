# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150622_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='cover',
            field=models.ImageField(null=True, blank=True, upload_to=''),
        ),
    ]
