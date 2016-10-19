# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 04:26
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
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot', models.ImageField(upload_to=winearb.upload_handling.models.image_upload_path)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WineImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot', models.ImageField(upload_to=winearb.upload_handling.models.image_upload_path)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='reviews.Review')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]