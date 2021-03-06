# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-10 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picsart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['pub_date']},
        ),
        migrations.RenameField(
            model_name='location',
            old_name='image_location',
            new_name='location',
        ),
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.TextField(blank=True),
        ),
    ]
