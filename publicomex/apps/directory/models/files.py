from versatileimagefield.fields import VersatileImageField, PPOIField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer
from versatileimagefield.placeholder import OnDiscPlaceholderImage
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
import os


User = get_user_model()


class File(models.Model):
    AUDIO = 'au'
    VIDEO = 'vi'
    IMAGE = 'im'
    DOCUMENT = 'do'

    FILE_TYPES = (
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
        (IMAGE, 'Imagen'),
        (DOCUMENT, 'Documento'),)

    name = models.CharField(
        max_length=264)
    file_type = models.CharField(
        max_length=2,
        choices=FILE_TYPES,
        default=IMAGE)
    upload_datetime = models.DateTimeField(
        auto_now_add=True)
    uploaded_by = models.ForeignKey(
        User, on_delete=models.PROTECT)
    active = models.BooleanField(
        default=False)

    # if using IMAGE as file_type, use the
    # image_file, if not use the other_file
    image_file = VersatileImageField(
        null=True, blank=True, ppoi_field='ppoi',
        placeholder_image=OnDiscPlaceholderImage(
            path=os.path.join(
                settings.BASE_DIR,
                'static/img/placeholder.gif'
            )))
    ppoi = PPOIField('Image PPOI', default=(0.5, 0.5))
    other_file = models.FileField(null=True)

    def warm_image_file(self):
        img_warmer = VersatileImageFieldWarmer(
            instance_or_queryset=self,
            rendition_key_set='image_file',
            image_attr='image_file')

        img_warmer.warm()
