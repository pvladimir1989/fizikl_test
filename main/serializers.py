from rest_framework.serializers import ModelSerializer
from .models import ImageUpload


class ImportImageSerializer(ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ('title', 'image', 'date_uploaded')
        # file = serializers.FileField()

    def save(self, *args, **kwargs):
        if self.instance.image:
            self.instance.avatar.delete()
        return super().save(*args, **kwargs)
