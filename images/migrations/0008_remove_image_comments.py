# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-24 22:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comments',
        ),
    ]