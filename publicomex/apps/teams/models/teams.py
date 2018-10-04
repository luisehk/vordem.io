from django.db import models
from django.contrib.auth import get_user_model
from ...core.models import Zone


User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=264)
    members = models.ManyToManyField(User)
    active = models.BooleanField(default=False)


class RegionalTeam(Team):
    zones = models.ManyToManyField(Zone)


class NationalTeam(Team):
    pass


class Business(NationalTeam):
    pass


class RegionalMarketing(RegionalTeam):
    pass


# agencia (todas las demás)
class Agency(NationalTeam):
    pass


# despacho (aguinaga)
class Firm(NationalTeam):
    pass


class Licensee(RegionalTeam):
    pass
