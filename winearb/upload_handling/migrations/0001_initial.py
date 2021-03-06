# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import winearb.upload_handling.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot', models.ImageField(upload_to=winearb.upload_handling.models.image_upload_path, validators=[winearb.upload_handling.models.validate_image_size])),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wineimages', to='reviews.Review')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
