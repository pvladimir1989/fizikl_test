from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView, Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import action

from rest_framework import viewsets

from main.custom_renderers import JPEGRenderer
from main.models import ImageUpload
from main.serializers import ImportImageSerializer


# class FileImportView(APIView):
#     parser_classes = (MultiPartParser, FormParser,)
#     serializer = ImportImageSerializer
#
#     def post(self, request, format=None):
#         upload = self.serializer(data=request.FILES)
#
#         if upload.is_valid():
#             file = ImageUpload(image=upload.validated_data['api_import'], uploaded_by=request.user.profile)
#             file.save()
#             return Response({'success': 'Imported successfully'})
#         else:
#             return Response(upload.errors, status=400)


# class FileImportViewSet(viewsets.ModelViewSet):
#     queryset = ImageUpload.objects.all()
#     serializer_class = ImportImageSerializer
#     permission_classes = [AllowAny]
#     parser_classes = (FormParser, MultiPartParser,)
#
#     @detail_route
#
#     renderer_classes = [JPEGRenderer]
#
#     def get(self, request, *args, **kwargs):
#         renderer_classes = [JPEGRenderer]
#         queryset = ImageUpload.objects.get(id=self.kwargs['id']).image
#         data = queryset
#         return Response(data, content_type='image/jpg')


class FileImportViewSet(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ImportImageSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
