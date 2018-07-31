# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 03:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')),
                ('message', models.TextField(max_length=150, verbose_name='Mensaje')),
                ('reason', models.CharField(choices=[('NSH', 'Nuevo embarque'), ('LSH', 'Retraso'), ('DSH', 'Entrega')], max_length=3, verbose_name='Razón')),
                ('processed', models.BooleanField(default=False, verbose_name='Procesada')),
                ('notified_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Usuarios notificados')),
            ],
            options={
                'verbose_name': 'notificacion',
                'verbose_name_plural': 'notificaciones',
                'ordering': ['datetime'],
            },
        ),
        migrations.CreateModel(
            name='UserNotificationsConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_shipment', models.BooleanField(default=False, verbose_name='Nuevo embarque')),
                ('late_shipment', models.BooleanField(default=False, verbose_name='Retraso')),
                ('delivered_shipment', models.BooleanField(default=False, verbose_name='Entrega')),
                ('email', models.BooleanField(default=False, verbose_name='Por correo')),
                ('sms', models.BooleanField(default=False, verbose_name='Por SMS')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_config', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Configuración de alertas',
                'verbose_name_plural': 'Configuraciones de alertas',
            },
        ),
    ]
