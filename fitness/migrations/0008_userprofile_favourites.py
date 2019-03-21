# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-21 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0007_workout_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourites', to='fitness.Workout'),
        ),
    ]