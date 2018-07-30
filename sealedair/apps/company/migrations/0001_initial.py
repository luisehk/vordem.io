# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 04:54
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('code', models.CharField(max_length=4, verbose_name='Código')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=10, verbose_name='Color')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]