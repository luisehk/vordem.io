from django.contrib.auth import get_user_model
from crum import get_current_request
from django.db import models
from django.utils import timezone
from ...messaging.email.helpers import send_email
from ...providers.models import Truck
from ...company.models import Plant


User = get_user_model()


class DelayReason(models.Model):
    reason = models.CharField(
        verbose_name='Razón de retraso',
        max_length=100)

    class Meta:
        verbose_name = 'Razón de retraso'
        verbose_name_plural = 'Razones de retraso'

    def __str__(self):
        return self.reason


class Shipment(models.Model):
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
    cpm_number = models.CharField(
        verbose_name='CPM number',
        max_length=150,
        default='')
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
    delay_reason = models.ForeignKey(
        DelayReason,
        on_delete=models.PROTECT,
        related_name='delay_reason_shipments',
        null=True,
        blank=True)

    class Meta:
        verbose_name = 'embarque'
        verbose_name_plural = 'embarques'
        ordering = ['start_datetime']

    def __str__(self):
        return self.truck.carrier.code + self.code

    def next_checkpoint(self):
        next_checkpoint = self.current_status.get_next_checkpoint()

        if next_checkpoint:
            print(
                'NUEVO CHECKPOINT',
                self.current_status.checkpoint,
                next_checkpoint)
            return Status.objects.create(
                shipment=self,
                checkpoint=next_checkpoint)

    def previous_status(self):
        previous_checkpoint = self.current_status.get_previous_checkpoint()

        if previous_checkpoint:
            return Status.objects.filter(
                shipment=self,
                checkpoint=previous_checkpoint
            ).first()

    def email_notification_create_new_shipment(self, user):
        send_email(
            subject='Nuevo embarque creado',
            to_email=[user.email],
            template='emails/shipments/new_shipment.html',
            ctx={
                'user': user.first_name,
                'shipment': self,
                'truck': self.truck,
                'plant': self.plant,
                'carrier': self.truck.carrier.name,
                'request': get_current_request()})

    def email_notification_delivered_shipment(self, user):
        send_email(
            subject='Embarque entregado',
            to_email=[user.email],
            template='emails/shipments/delivered_shipment.html',
            ctx={
                'user': user.first_name,
                'shipment': self,
                'truck': self.truck,
                'plant': self.plant,
                'carrier': self.truck.carrier.name,
                'status': self.current_status.get_checkpoint_display,
                'request': get_current_request()})

    def notification_risk_shipment(self, user):
        send_email(
            subject='Embarque en riesgo',
            to_email=[user.email],
            template='emails/shipments/shipment_at_risk.html',
            ctx={
                'user': user.first_name,
                'shipment': self,
                'truck': self.truck,
                'plant': self.plant,
                'carrier': self.truck.carrier.name,
                'request': get_current_request()})

    def notification_late_shipment(self, user):
        send_email(
            subject='Embarque retrasado',
            to_email=[user.email],
            template='emails/shipments/late_shipment.html',
            ctx={
                'user': user.first_name,
                'shipment': self,
                'truck': self.truck,
                'plant': self.plant,
                'carrier': self.truck.carrier.name,
                'request': get_current_request()})

    def change_to_delayed(self):
        status = self.current_status
        hours_spent = status.get_hours_since_start()

        if hours_spent > 5:
            status.time_status = Status.TIME_DELAYED
            status.save()

            users_to_notify = User.objects.filter(
                notifications_config__email=True,
                notifications_config__late_shipment=True)

            for user in users_to_notify:
                self.notification_late_shipment(user)

    def change_to_late(self):
        status = self.current_status
        hours_spent = status.get_hours_since_start()

        if hours_spent > 7:
            status.time_status = Status.TIME_LATE
            status.save()

            users_to_notify = User.objects.filter(
                notifications_config__email=True,
                notifications_config__late_shipment=True)

            for user in users_to_notify:
                self.notification_late_shipment(user)


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
        ordering = ('-datetime',)


class Status(models.Model):
    MEX_TRANSIT = 'MTR'
    MEX_CARRIER = 'MCA'
    BORDER_CROSSING = 'BCR'
    BORDER_CARRIER = 'BCA'
    USA_TRANSIT = 'UTR'
    USA_DELIVERED = 'UDE'
    CHECKPOINTS = (
        (MEX_TRANSIT, 'Tránsito MX',),
        (MEX_CARRIER, 'Carrier MX',),
        (BORDER_CROSSING, 'En cruce',),
        (BORDER_CARRIER, 'Carrier US',),
        (USA_TRANSIT, 'Tránsito US',),
        (USA_DELIVERED, 'Entregado',),
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
        ordering = ('-start_datetime',)
        verbose_name = 'estatus'
        verbose_name_plural = 'estatus'
        unique_together = ('shipment', 'checkpoint')

    def __str__(self):
        return str(self.shipment) + ' - ' + self.get_checkpoint_display()

    def get_hours_since_start(self):
        time = self.end_datetime or timezone.now()
        delta = time - self.start_datetime
        return int(delta.total_seconds() // 3600)

    def get_next_checkpoint(self):
        if self.checkpoint == self.MEX_TRANSIT:
            return self.MEX_CARRIER

        if self.checkpoint == self.MEX_CARRIER:
            return self.BORDER_CROSSING

        if self.checkpoint == self.BORDER_CROSSING:
            return self.BORDER_CARRIER

        if self.checkpoint == self.BORDER_CARRIER:
            return self.USA_TRANSIT

        if self.checkpoint == self.USA_TRANSIT:
            return self.USA_DELIVERED

        if self.checkpoint == self.USA_DELIVERED:
            return None

    def get_previous_checkpoint(self):
        if self.checkpoint == self.MEX_TRANSIT:
            return None

        if self.checkpoint == self.MEX_CARRIER:
            return self.MEX_TRANSIT

        if self.checkpoint == self.BORDER_CROSSING:
            return self.MEX_CARRIER

        if self.checkpoint == self.BORDER_CARRIER:
            return self.BORDER_CROSSING

        if self.checkpoint == self.USA_TRANSIT:
            return self.BORDER_CARRIER

        if self.checkpoint == self.USA_DELIVERED:
            return self.USA_TRANSIT
