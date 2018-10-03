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
