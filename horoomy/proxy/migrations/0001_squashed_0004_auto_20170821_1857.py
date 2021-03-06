# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('proxy', '0001_initial'), ('proxy', '0002_auto_20170821_1845'), ('proxy', '0003_auto_20170821_1853'), ('proxy', '0004_auto_20170821_1857')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('0', 'HTTP'), ('1', 'HTTPS'), ('2', 'HTTP / HTTPS')], max_length=1, verbose_name='type')),
                ('address', models.CharField(max_length=30, unique=True, verbose_name='address')),
                ('speed', models.PositiveSmallIntegerField(verbose_name='speed')),
                ('stability', models.PositiveSmallIntegerField(verbose_name='stability')),
                ('rating', models.PositiveSmallIntegerField(editable=False, verbose_name='rating')),
            ],
            options={
                'ordering': ('-rating',),
                'verbose_name': 'Proxy',
                'verbose_name_plural': 'Proxies',
            },
        ),
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
