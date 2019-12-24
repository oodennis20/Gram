# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-24 21:58
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20191225_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
