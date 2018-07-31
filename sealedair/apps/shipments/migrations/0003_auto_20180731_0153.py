# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 01:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sealedair_shipments', '0002_auto_20180730_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='arrival_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Llegada'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='current_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='current_status_shipments', to='sealedair_shipments.Status', verbose_name='Estado actual'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='delay_reason',
            field=models.CharField(blank=True, choices=[('HOL', 'Día festivo'), ('APP', 'Falta de cita'), ('CARR', 'Problema con carrier')], max_length=3, null=True, verbose_name='Razón de retraso'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='estimated_arrival_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='ETA'),
        ),
    ]