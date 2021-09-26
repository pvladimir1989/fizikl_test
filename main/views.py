from rest_framework.views import APIView,Response
from rest_framework.parsers import MultiPartParser,FormParser


from main.models import ImageUpload
from main.serializers import ImportImageSerializer


class FileImportView(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer = ImportImageSerializer

    def post(self, request, format=None):
        upload = self.serializer(data=request.FILES)

        if upload.is_valid():
            file = ImageUpload(image=upload.validated_data['api_import'], uploaded_by=request.user.profile)
            file.save()
            return Response({'success': 'Imported successfully'})
        else:
            return Response(upload.errors, status=400)
