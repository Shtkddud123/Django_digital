# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0003_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='startups',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AlterField(
            model_name='newslink',
            name='link',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=31, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(help_text='A label for URL config', max_length=31, unique=True),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
