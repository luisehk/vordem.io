# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealedair_users', '0002_auto_20180529_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='preferred_language',
        ),
        migrations.AddField(
            model_name='profile',
            name='generation',
            field=models.CharField(choices=[('GZ', 'Generación Z'), ('GY', 'Millenial'), ('GX', 'Generación X'), ('BB', 'Baby Boomer'), ('GS', 'Generación Silenciosa')], default='GY', max_length=2),
        ),
    ]