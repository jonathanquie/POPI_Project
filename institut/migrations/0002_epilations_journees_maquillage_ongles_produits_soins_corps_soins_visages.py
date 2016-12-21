# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institut', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epilations',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=42)),
                ('price', models.FloatField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Journees',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('jour', models.DateTimeField(auto_now_add=True, verbose_name='Date de la journée')),
                ('ca', models.FloatField()),
                ('costs', models.FloatField()),
                ('result', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Maquillage',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=42)),
                ('price', models.FloatField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Ongles',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=42)),
                ('price', models.FloatField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=42)),
                ('price', models.FloatField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Soins_Corps',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=42)),
                ('price', models.FloatField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Soins_Visages',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=42)),
                ('price', models.FloatField()),
                ('cost', models.FloatField()),
            ],
        ),
    ]
