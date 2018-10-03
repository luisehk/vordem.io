from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=264)
    subcategories = models.ManyToManyField(
        'Category')
    active = models.BooleanField(
        default=False)
