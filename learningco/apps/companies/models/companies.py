from django.contrib.auth import get_user_model
from django.db import models
from .industries import Industry


User = get_user_model()


class Company(models.Model):
    COMPANY_SIZE_UNKNOWN = '0'
    COMPANY_SIZE_SMALL = 'A'
    COMPANY_SIZE_MEDIUM = 'B'
    COMPANY_SIZE_LARGE = 'C'
    COMPANY_SIZES = (
        (COMPANY_SIZE_UNKNOWN, 'No especificado'),
        (COMPANY_SIZE_SMALL, '50-500 empleados'),
        (COMPANY_SIZE_MEDIUM, '500-5,000 empleados'),
        (COMPANY_SIZE_LARGE, '+5,000 empleados'),
    )

    name = models.CharField(
        max_length=150)
    industry = models.ForeignKey(
        Industry, null=True, blank=True, on_delete=models.SET_NULL)
    size = models.CharField(
        max_length=1, choices=COMPANY_SIZES, default=COMPANY_SIZE_UNKNOWN)
    human_resources = models.ManyToManyField(
        User, blank=True, related_name='hr_companies')
    leaders = models.ManyToManyField(
        User, blank=True, related_name='leader_companies')
