from django.apps import AppConfig


class ShipmentsConfig(AppConfig):
    name = 'sealedair.apps.shipments'
    label = 'sealedair_shipments'
    verbose_name = 'Embarques'

    def ready(self):
        pass
