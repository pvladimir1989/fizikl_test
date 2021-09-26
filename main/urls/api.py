from django.urls import include, path

from main.views import FileImportView

urlpatterns = [
    path('v1/file/', FileImportView.as_view(), name="file"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
