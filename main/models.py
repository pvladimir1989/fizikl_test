from django.db import models

from PIL import Image as img


class ImageUpload(models.Model):
    file = models.ImageField(upload_to='pictures/')

    def save(self, *args, **kwargs):
        super(ImageUpload, self).save(*args, **kwargs)
        image = img.open(self.file.path)
        image.save(self.file.path, quality=20, optimize=True)