from django.contrib.auth import get_user_model
from django.db import models
from ...providers.models import Truck
from ...company.models import Plant


User = get_user_model()


class Shipment(models.Model):
    DELAY_HOLIDAYS = 'HOL'
    DELAY_APPOINTMENT = 'APP'
    DELAY_CARRIER = 'CARR'
    DELAY_REASONS = (
        (DELAY_HOLIDAYS, 'Día festivo',),
        (DELAY_APPOINTMENT, 'Falta de cita',),
        (DELAY_CARRIER, 'Problema con carrier',),
    )

    truck = models.ForeignKey(
        Truck,
        verbose_name='Trailer',
        on_delete=models.PROTECT,
        related_name='shipments',)
    plant = models.ForeignKey(
        Plant,
        verbose_name='Planta destino',
        on_delete=models.PROTECT,
        related_name='shipments')
    code = models.CharField(
        verbose_name='Código',
        max_length=150)
    current_status = models.ForeignKey(
        'Status',
        verbose_name='Estado actual',
        on_delete=models.PROTECT,
        related_name='current_status_shipments',
        null=True,
        blank=True)
    start_datetime = models.DateTimeField(
        verbose_name='Salida',
        auto_now_add=True)
    arrival_datetime = models.DateTimeField(
        verbose_name='Llegada',
        null=True,
        blank=True)
    estimated_arrival_datetime = models.DateTimeField(
        verbose_name='ETA',
        null=True,
        blank=True)
    delay_reason = models.CharField(
        verbose_name='Razón de retraso',
        max_length=3,
        choices=DELAY_REASONS,
        null=True,
        blank=True)

    class Meta:
        verbose_name = 'embarque'
        verbose_name_plural = 'embarques'
        ordering = ['start_datetime']

    def __str__(self):
        return self.truck.carrier.code + self.code


class Comment(models.Model):
    shipment = models.ForeignKey(
        Shipment,
        verbose_name='Embarque',
        related_name='comments',
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        verbose_name='Usuario',
        related_name='shipment_comments',
        on_delete=models.CASCADE)
    datetime = models.DateTimeField(
        verbose_name='Fecha y hora',
        auto_now_add=True)
    body = models.TextField()

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'


class Status(models.Model):
    MEX_TRANSIT = 'MTR'
    MEX_CARRIER = 'MCA'
    BORDER_CROSSING = 'BCR'
    BORDER_CARRIER = 'BCA'
    USA_TRANSIT = 'UTR'
    USA_DELIVERED = 'UDE'
    CHECKPOINTS = (
        (MEX_TRANSIT, 'México: En tránsito',),
        (MEX_CARRIER, 'México: Carrier mexicano',),
        (BORDER_CROSSING, 'Laredo: Cruzando',),
        (BORDER_CARRIER, 'Laredo: US Carrier',),
        (USA_TRANSIT, 'Destino: En tránsito',),
        (USA_DELIVERED, 'Destino: Entregado',),
    )

    TIME_ONTIME = 'TOT'
    TIME_DELAYED = 'TDE'
    TIME_LATE = 'TLA'
    TIME_STATUSES = (
        (TIME_ONTIME, 'A tiempo',),
        (TIME_DELAYED, 'En riesgo',),
        (TIME_LATE, 'Retrasado',),
    )

    shipment = models.ForeignKey(
        Shipment,
        verbose_name='Embarque',
        related_name='status_history',
        on_delete=models.CASCADE)
    checkpoint = models.CharField(
        verbose_name='Checkpoint',
        max_length=3, choices=CHECKPOINTS,
        default=MEX_TRANSIT)
    time_status = models.CharField(
        verbose_name='Estatus',
        max_length=3, choices=TIME_STATUSES,
        default=TIME_ONTIME)
    start_datetime = models.DateTimeField(
        verbose_name='Inicio',
        auto_now_add=True)
    end_datetime = models.DateTimeField(
        verbose_name='Fin',
        null=True,
        blank=True)

    class Meta:
        verbose_name = 'estatus'
        verbose_name_plural = 'estatus'
        unique_together = ('shipment', 'checkpoint')

    def __str__(self):
        return str(self.shipment) + ' - ' + self.get_checkpoint_display()
