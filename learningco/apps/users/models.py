from versatileimagefield.fields import VersatileImageField, PPOIField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer
from versatileimagefield.placeholder import OnDiscPlaceholderImage
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
import os


User = get_user_model()


class Profile(models.Model):
    GENERATION_Z = 'GZ'
    MILLENIALS = 'GY'
    GENERATION_X = 'GX'
    BABY_BOOMERS = 'BB'
    SILENT_GENERATION = 'GS'
    GENERATIONS = (
        (GENERATION_Z, 'Generación Z',),
        (MILLENIALS, 'Millenial',),
        (GENERATION_X, 'Generación X',),
        (BABY_BOOMERS, 'Baby Boomer',),
        (SILENT_GENERATION, 'Generación Silenciosa',),
    )

    TOP_LEVEL_MANAGEMENT = 'TLM'
    MIDDLE_LEVEL_MANAGEMENT = 'MLM'
    OPERATION_LEVEL_EMPLOYEE = 'OLE'
    LEVELS_OF_HIERARCHY = (
        (TOP_LEVEL_MANAGEMENT, 'Directivo'),
        (MIDDLE_LEVEL_MANAGEMENT, 'Gerencial'),
        (OPERATION_LEVEL_EMPLOYEE, 'Operativo'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile')

    # profile
    bio = models.TextField(_('Extract'), blank=True)
    avatar = VersatileImageField(
        null=True, blank=True, ppoi_field='ppoi',
        placeholder_image=OnDiscPlaceholderImage(
            path=os.path.join(
                settings.BASE_DIR,
                'static/imgs/profile-neutral.png'
            )))
    ppoi = PPOIField('Image PPOI', default=(0.5, 0.5))

    # contact info
    phone = models.CharField(_('Phone'), max_length=100, blank=True)

    # company leader attributes
    generation = models.CharField(
        max_length=2, choices=GENERATIONS,
        default=MILLENIALS)
    level_of_hierarchy = models.CharField(
        max_length=3, choices=LEVELS_OF_HIERARCHY,
        default=OPERATION_LEVEL_EMPLOYEE)

    def __str__(self):
        return self.get_full_name() or self.user.email

    def get_full_name(self):
        return self.user.get_full_name()

    def warm_avatar(self):
        img_warmer = VersatileImageFieldWarmer(
            instance_or_queryset=self,
            rendition_key_set='profile_avatar',
            image_attr='avatar')

        img_warmer.warm()
