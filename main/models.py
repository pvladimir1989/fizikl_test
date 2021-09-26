from django.db import models
from django.contrib.auth.models import User


class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now=True)
    # uploaded_by = models.ForeignKey(User, blank=True, null=True)
