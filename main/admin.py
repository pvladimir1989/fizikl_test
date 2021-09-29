from django.contrib import admin

from main.models import ImageUpload


@admin.register(ImageUpload)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('file',)
