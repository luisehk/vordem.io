# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-10 06:06
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('learningco_content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='thumbnail',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to=''),
        ),
    ]
