from django.contrib.auth import get_user_model
from django.db import models
from ...shipments.models import Shipment


User = get_user_model()


class UserNotificationsConfig(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='notifications_config')
    new_shipment = models.BooleanField(
        verbose_name='Nuevo embarque',
        default=False)
    late_shipment = models.BooleanField(
        verbose_name='Retraso',
        default=False)
    delivered_shipment = models.BooleanField(
        verbose_name='Entrega',
        default=False)
    email = models.BooleanField(
        verbose_name='Por correo',
        default=False)
    sms = models.BooleanField(
        verbose_name='Por SMS',
        default=False)

    class Meta:
        verbose_name = 'Configuración de alertas'
        verbose_name_plural = 'Configuraciones de alertas'


class Notification(models.Model):
    NEW_SHIPMENT = 'NSH'
    LATE_SHIPMENT = 'LSH'
    DELIVERED_SHIPMENT = 'DSH'
    NOTIFICATION_REASONS = (
        (NEW_SHIPMENT, 'Nuevo embarque',),
        (LATE_SHIPMENT, 'Retraso',),
        (DELIVERED_SHIPMENT, 'Entrega',),
    )

    user = models.ForeignKey(
        User,
        verbose_name='Usuario',
        on_delete=models.CASCADE,
        related_name='notifications')
    shipment = models.ForeignKey(
        Shipment,
        verbose_name='Embarque',
        on_delete=models.CASCADE)
    datetime = models.DateTimeField(
        verbose_name='Fecha y hora',
        auto_now_add=True)
    message = models.TextField(
        verbose_name='Mensaje',
        max_length=150)
    reason = models.CharField(
        verbose_name='Razón',
        max_length=3, choices=NOTIFICATION_REASONS)
    notified_users = models.ManyToManyField(
        User,
        verbose_name='Usuarios notificados')
    processed = models.BooleanField(
        verbose_name='Procesada',
        default=False)

    class Meta:
        verbose_name = 'notificacion'
        verbose_name_plural = 'notificaciones'
        ordering = ['datetime']

    def __str__(self):
        return self.message
