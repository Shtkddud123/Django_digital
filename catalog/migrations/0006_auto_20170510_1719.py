# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_book_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('d', 'Maintenence'), ('o', 'On Loan'), ('a', 'Avaliable'), ('r', 'Reserved')], default='d', help_text='Book avaliability', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='due_back',
        ),
        migrations.RemoveField(
            model_name='book',
            name='imprint',
        ),
        migrations.RemoveField(
            model_name='book',
            name='status',
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=1, help_text='13 Character <a href "https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='catalog.Genre'),
        ),
    ]
