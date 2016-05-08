# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('isbn', models.CharField(blank=True, max_length=200)),
                ('info', models.CharField(blank=True, max_length=200)),
                ('summary', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Collection'),
        ),
    ]
