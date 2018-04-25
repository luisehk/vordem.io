from versatileimagefield.fields import VersatileImageField, PPOIField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer
from versatileimagefield.placeholder import OnDiscPlaceholderImage
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from .languages import LANGUAGE, ENGLISH_CODE
from django.conf import settings
from django.db import models
import os


User = get_user_model()


class Profile(models.Model):
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
                settings.BASE_DIR, 'users/static/img/profile-neutral.png')))
    ppoi = PPOIField('Image PPOI', default=(0.5, 0.5))

    # contact info
    phone = models.CharField(_('Phone'), max_length=100, blank=True)
    linkedin = models.URLField(_('Linkedin'), blank=True)
    twitter = models.URLField(_('Twitter'), blank=True)
    facebook = models.URLField(_('Facebook'), blank=True)
    github = models.URLField(_('Github'), blank=True)

    # settings
    preferred_language = models.CharField(
        max_length=10,
        default=ENGLISH_CODE,
        choices=LANGUAGE)

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

    def populate_social_info(self, social):
        if social.provider == 'twitter':
            self.twitter = social.get_profile_url()
            self.save()
        elif social.provider == 'facebook':
            self.facebook = social.get_profile_url()
            self.save()
        elif social.provider == 'linkedin':
            self.linkedin = social.get_profile_url()
            self.save()
