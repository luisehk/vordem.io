from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=264)
