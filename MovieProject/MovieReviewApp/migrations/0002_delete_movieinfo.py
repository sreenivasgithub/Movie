# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-12-14 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieReviewApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MovieInfo',
        ),
    ]