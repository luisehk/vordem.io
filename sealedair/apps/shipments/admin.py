from ...admin import site
from .models import Shipment, Comment, Status


site.register([Shipment, Comment, Status])
