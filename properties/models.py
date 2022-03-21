from django.db import models
from django.conf import settings


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

    name = models.CharField(max_length=256)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    price = models.FloatField(help_text="Per month")
    bedroom_type = models.CharField(max_length=256, choices=BEDROOM_TYPE, default='PRIVATE')
    bathroom_type = models.CharField(max_length=256, choices=BATHROOM_TYPE, default='PRIVATE')
    kitchen_type = models.CharField(max_length=256, choices=KITCHEN_TYPE, default='PRIVATE')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PropertyImage(models.Model):
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE)
    image = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
