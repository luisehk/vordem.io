from versatileimagefield.fields import VersatileImageField, PPOIField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer
from versatileimagefield.placeholder import OnDiscPlaceholderImage
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from .industries import Industry
import os


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
        verbose_name='Nombre',
        max_length=150)
    industry = models.ForeignKey(
        Industry, verbose_name='Industria',
        null=True, blank=True,
        on_delete=models.SET_NULL)
    size = models.CharField(
        verbose_name='Tamaño', max_length=1,
        choices=COMPANY_SIZES,
        default=COMPANY_SIZE_UNKNOWN)
    human_resources = models.ManyToManyField(
        User, verbose_name='Recursos humanos',
        blank=True, related_name='hr_companies')
    leaders = models.ManyToManyField(
        User, verbose_name='Líderes',
        blank=True, related_name='leader_companies')

    avatar = VersatileImageField(
        null=True, blank=True, ppoi_field='ppoi',
        placeholder_image=OnDiscPlaceholderImage(
            path=os.path.join(
                settings.BASE_DIR,
                'static/imgs/profile-neutral.png'
            )))
    ppoi = PPOIField('Image PPOI', default=(0.5, 0.5))

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def warm_avatar(self):
        img_warmer = VersatileImageFieldWarmer(
            instance_or_queryset=self,
            rendition_key_set='company_avatar',
            image_attr='avatar')

        img_warmer.warm()

    def get_avatar_update_url(self):
        return '/companies/companies/{}/'.format(self.id)
