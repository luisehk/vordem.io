from ...admin import site
from .models import Carrier, Truck


site.register([Carrier, Truck])
