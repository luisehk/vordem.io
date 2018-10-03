from versatileimagefield.serializers import VersatileImageFieldSerializer
from django.core.files.base import ContentFile
import base64


class BetterVersatileImageFieldSerializer(VersatileImageFieldSerializer):
    def to_native(self, value):
        self.context = {}
        return super().to_native(value)


class Base64ImageField(BetterVersatileImageFieldSerializer):
    def to_internal_value(self, data):
        if data and isinstance(data, str) and data.startswith('data:image'):  # noqa
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)
