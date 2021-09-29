from rest_framework.serializers import ModelSerializer
from .models import ImageUpload


class ImportImageSerializer(ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = '__all__'
