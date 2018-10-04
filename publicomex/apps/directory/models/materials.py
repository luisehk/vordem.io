from django.db import models
from .categories import Category
from .files import File
from django.utils import timezone


class Material(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=264)
    description = models.TextField()
    files = models.ManyToManyField(File)
    expiration_date = models.DateField(null=True)
    publication_date = models.DateTimeField(default=timezone.now)
    downloads = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
