# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningco_content', '0011_auto_20180709_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='score_range',
            field=models.CharField(choices=[('L', 'Bajo'), ('A', 'Medio'), ('H', 'Alta')], default='L', max_length=1),
        ),
        migrations.AlterUniqueTogether(
            name='bundle',
            unique_together=set([('skill', 'generation', 'level_of_hierarchy', 'score_range')]),
        ),
    ]
