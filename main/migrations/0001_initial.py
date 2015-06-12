# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=50, verbose_name=b'title')),
                ('description', models.TextField(verbose_name=b'description', blank=True)),
                ('content', models.TextField(verbose_name=b'content', blank=True)),
                ('date_created', models.DateTimeField(verbose_name=b'date created')),
                ('date_updated', models.DateTimeField(verbose_name=b'date updated')),
                ('domain', models.CharField(max_length=40, verbose_name=b'domain', blank=True)),
                ('owner', models.ForeignKey(related_name='bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'bookmark',
                'verbose_name_plural': 'bookmarks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(to='main.Tag', blank=True),
            preserve_default=True,
        ),
    ]
