from rest_framework import serializers
from .models import ImageUpload


class ImportImageSerializer(serializers.Serializer):
    class Meta:
        model = ImageUpload
        fields = '__all__'
        # file = serializers.FileField()
