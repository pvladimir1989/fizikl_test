from django.contrib import admin
from django.contrib.admin import ModelAdmin

from main.models import ImageUpload


@admin.register(ImageUpload)
class BookAdmin(ModelAdmin):
    pass
