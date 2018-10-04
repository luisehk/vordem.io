from django.db import models


class Size(models.Model):
    CENTIMETER = 'cm'
    METER = 'me'

    UNITS_OF_LENGTH = (
        (CENTIMETER, 'Centimetros'),
        (METER, 'Metros'),)

    # NOTE: all units are stored in centimeters
    # the unit_of_length field is only for
    # display purposes
    name = models.CharField(max_length=264)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    unit_of_length = models.CharField(
        max_length=2,
        choices=UNITS_OF_LENGTH,
        default=CENTIMETER)
