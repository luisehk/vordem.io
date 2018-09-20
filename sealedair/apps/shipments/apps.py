from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save


class ShipmentsConfig(AppConfig):
    name = 'sealedair.apps.shipments'
    label = 'sealedair_shipments'
    verbose_name = 'Embarques'

    def ready(self):
        from sealedair.apps.shipments.models import (
            Shipment, Status)
        from sealedair.apps.shipments.signals import (
            create_shipment_status, set_status_as_current,
            check_if_eta_changed)

        post_save.connect(set_status_as_current, sender=Status)
        post_save.connect(create_shipment_status, sender=Shipment)
        pre_save.connect(check_if_eta_changed, sender=Shipment)
