from django.db import models
from django.conf import settings


# Create your models here.

class UserProfile(models.Model):
    is_wtc_student = models.BooleanField(default=False, help_text="Approved WTC Student")
    is_wtc_staff = models.BooleanField(default=False, help_text="Approved WTC Staff member")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
