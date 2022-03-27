from django.conf import settings
from django.db import models


# Create your models here.

class Property(models.Model):
    BEDROOM_TYPE = (
        ('SHARING', 'SHARING'),
        ('PRIVATE', 'PRIVATE'),
    )

    BATHROOM_TYPE = (
        ('SHARING', 'SHARING'),
        ('PRIVATE', 'PRIVATE'),
        ('COMMUNAL', 'COMMUNAL'),
    )

    KITCHEN_TYPE = (
        ('SHARING', 'SHARING'),
        ('PRIVATE', 'PRIVATE'),
        ('COMMUNAL', 'COMMUNAL'),
    )

    CAMPUS_CHOICES = (
        ('DURBAN', 'DBN'),
        ('JOHANNESBURG', 'JHB'),
        ('CAPE TOWN', 'CPT'),
    )

    name = models.CharField(max_length=256)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    price = models.FloatField(help_text="Per month")
    bedroom_type = models.CharField(max_length=256, choices=BEDROOM_TYPE, default='PRIVATE')
    bathroom_type = models.CharField(max_length=256, choices=BATHROOM_TYPE, default='PRIVATE')
    kitchen_type = models.CharField(max_length=256, choices=KITCHEN_TYPE, default='PRIVATE')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    campus = models.CharField(max_length=256, choices=CAMPUS_CHOICES, default='JHB')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def get_display_image_url(self):
        # TODO: fix image url resolve
        # try:
        #     url = PropertyImage.objects.get(property_id=self.id).image.url
        #     return f'{url}'
        # except Exception:
        #     return 'https://via.placeholder.com/300&text="image not found"'
        return 'https://via.placeholder.com/300&text="image not found"'

    def __str__(self):
        return self.name


class PropertyImage(models.Model):
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def get_image_url(self):
        # TODO: fix image url resolve
        return 'https://via.placeholder.com/300&text="image not found"'
