# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 17:40
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sealedair_content', '0009_remove_lesson_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='options',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options_list', to='sealedair_content.Question', verbose_name='Pregunta'),
        ),
    ]