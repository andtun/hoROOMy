# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0002_delete_useragent'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=512, verbose_name='value')),
            ],
        ),
    ]
