# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-03 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0004_remove_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
