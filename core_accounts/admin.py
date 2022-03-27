from django.contrib import admin
from core_accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_wtc_student', 'is_wtc_staff', 'is_active']


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
