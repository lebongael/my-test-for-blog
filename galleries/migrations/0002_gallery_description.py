# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]