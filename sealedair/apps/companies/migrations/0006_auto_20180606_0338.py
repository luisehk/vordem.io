# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-06 03:38
from __future__ import unicode_literals

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sealedair_companies', '0005_auto_20180529_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='avatar',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='company',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
    ]