from django.views.generic import TemplateView
from rest_framework.generics import CreateAPIView

from main.models import ImageUpload
from main.serializers import ImportImageSerializer


class ImageCreateView(CreateAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImportImageSerializer


class ImageView(TemplateView):
    template_name = 'main.html'
