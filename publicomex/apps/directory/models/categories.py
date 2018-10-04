from django.db import models
from ...teams.models import Team, Agency
from ...core.models import Zone


class Category(models.Model):
    name = models.CharField(max_length=264)
    subcategories = models.ManyToManyField('Category')
    owners = models.ManyToManyField(Team)
    agency = models.ForeignKey(
        Agency, null=True,
        on_delete=models.SET_NULL,
        related_name='categories')
    zones = models.ManyToManyField(Zone)
    active = models.BooleanField(default=False)
