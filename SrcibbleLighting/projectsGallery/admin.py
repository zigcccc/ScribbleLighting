from django.contrib import admin

from .models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Images', {'fields': ['image_title', 'image']}),
    ]
    list_display = ('image_title', 'image')
    search_fields = ['image_title']


admin.site.register(Image, ImageAdmin)
