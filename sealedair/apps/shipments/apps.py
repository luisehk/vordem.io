from django.apps import AppConfig


class ShipmentsConfig(AppConfig):
    name = 'sealedair.apps.shipments'
    label = 'sealedair_shipments'

    def ready(self):
        pass
