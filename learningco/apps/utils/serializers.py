from versatileimagefield.serializers import VersatileImageFieldSerializer


class BetterVersatileImageFieldSerializer(VersatileImageFieldSerializer):
    def to_native(self, value):
        self.context = {}
        return super().to_native(value)
