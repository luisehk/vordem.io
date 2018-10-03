from django.db import models
from ...teams.models import Team
from ...core.models import Zone


class Category(models.Model):
    name = models.CharField(max_length=264)
    subcategories = models.ManyToManyField('Category')
    owners = models.ManyToManyField(Team)
    zones = models.ManyToManyField(Zone)
    active = models.BooleanField(default=False)
