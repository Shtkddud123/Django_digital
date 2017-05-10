# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
            ],
        ),
    ]