# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 04:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sealedair_providers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sealedair_company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150, verbose_name='Código')),
                ('start_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Salida')),
                ('arrival_datetime', models.DateTimeField(null=True, verbose_name='Llegada')),
                ('estimated_arrival_datetime', models.DateTimeField(null=True, verbose_name='ETA')),
                ('delay_reason', models.CharField(choices=[('HOL', 'Día festivo'), ('APP', 'Falta de cita'), ('CARR', 'Problema con carrier')], max_length=3, verbose_name='Razón de retraso')),
                ('carrier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='sealedair_providers.Carrier', verbose_name='Carrier')),
            ],
            options={
                'ordering': ['start_datetime'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkpoint', models.CharField(choices=[('MTR', 'México: En tránsito'), ('MCA', 'México: Carrier mexicano'), ('BCR', 'Laredo: Cruzando'), ('BCA', 'Laredo: US Carrier'), ('UTR', 'Destino: En tránsito'), ('UDE', 'Destino: Entregado')], default='MTR', max_length=3, verbose_name='Checkpoint')),
                ('time_status', models.CharField(choices=[('TOT', 'A tiempo'), ('TDE', 'En riesgo'), ('TLA', 'Retrasado')], default='TOT', max_length=3, verbose_name='Estatus')),
                ('start_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Inicio')),
                ('end_datetime', models.DateTimeField(null=True, verbose_name='Fin')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_history', to='sealedair_shipments.Shipment', verbose_name='Embarque')),
            ],
        ),
        migrations.AddField(
            model_name='shipment',
            name='current_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='current_status_shipments', to='sealedair_shipments.Status', verbose_name='Estado actual'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='sealedair_company.Plant', verbose_name='Planta destino'),
        ),
        migrations.AddField(
            model_name='comment',
            name='shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sealedair_shipments.Shipment', verbose_name='Embarque'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipment_comments', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
