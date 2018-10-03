from ...admin import site
from .models import Team, RegionalTeam, NationalTeam


site.register([Team, RegionalTeam, NationalTeam])
