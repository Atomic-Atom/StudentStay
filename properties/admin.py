from django.contrib import admin
from properties.models import Property, PropertyImage
from django.utils.safestring import mark_safe


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active', 'name', 'bedroom_type', 'bathroom_type', 'kitchen_type']
    list_filter = ['bedroom_type', 'bathroom_type', 'kitchen_type']


class PropertyImageAdmin(admin.ModelAdmin):
    read_only_fields = ['image_preview']  # this is the field you're defining below

    @staticmethod
    def image_preview(obj):
        return mark_safe(
            f'<img src={{"{obj.image.url}"}} width={{"{obj.image.width}"}} height={{"{obj.image.height}"}} />')

    list_display = ['property', 'is_active', 'image_preview']


# Register your models here.
admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage, PropertyImageAdmin)
