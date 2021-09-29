# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import include, path
#
# from rest_framework.routers import DefaultRouter
#
# from main.views import FileImportViewSet
#
# router = DefaultRouter()
#
# router.register(r'file', FileImportViewSet)
#
# urlpatterns = [
#                   path('v1/file/', include(router.urls)),
#                   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
