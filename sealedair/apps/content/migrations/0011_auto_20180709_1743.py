# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sealedair_content', '0010_auto_20180709_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='options',
        ),
        migrations.AlterField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='sealedair_content.Question', verbose_name='Pregunta'),
        ),
    ]