# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user_name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(20, '20'), (19, '19'), (18, '18'), (17, '17'), (16, '16'), (15, 'I would buy (again)'), (14, '14'), (13, '13'), (12, '12'), (11, '11'), (10, 'Average, considering cost'), (9, '9'), (8, '8'), (7, '7'), (6, '6'), (5, 'Not good at this price'), (4, '4'), (3, '3'), (2, '2'), (1, '1')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vintage', models.PositiveIntegerField(default=2016)),
                ('name', models.CharField(max_length=200)),
                ('producer', models.CharField(default=' ', max_length=50)),
                ('country', models.CharField(default=' ', max_length=50)),
                ('region', models.CharField(default=' ', max_length=50)),
                ('appellation', models.CharField(default=' ', max_length=50)),
                ('subregion', models.CharField(blank=True, default='', max_length=50)),
                ('dominant_variety', models.CharField(default=' ', max_length=50)),
                ('secondary_variety', models.CharField(blank=True, default='', max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('R', 'Red'), ('W', 'White'), ('P', 'Rose'), ('S', 'Sparkling'), ('F', 'Fortified')], default=' ', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='wine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.Wine'),
        ),
    ]
