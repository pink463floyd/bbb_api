# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160509_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=8)),
                ('agency_id', models.CharField(max_length=8)),
                ('route_short_name', models.CharField(max_length=8)),
                ('route_long_name', models.CharField(max_length=80)),
                ('route_desc', models.CharField(max_length=8, null=True)),
                ('route_type', models.CharField(max_length=8, null=True)),
                ('route_url', models.CharField(max_length=120, null=True)),
                ('route_color', models.CharField(max_length=8, null=True)),
                ('route_text_color', models.CharField(max_length=8, null=True)),
            ],
        ),
    ]