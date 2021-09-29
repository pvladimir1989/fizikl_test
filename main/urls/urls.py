from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from main.urls import api

# urlpatterns = [
#     # path('api/import/', include(api)),
#     path('admin/', admin.site.urls),
#     path('',TemplateView.as_view(template_name='main.html'))
#
# ]
from main.views import FileImportViewSet

urlpatterns = [
    path("", TemplateView.as_view(template_name="main.html")),
    # path("api/auth-token/", obtain_auth_token, name="rest_auth_token"),
    path("api/user-avatar/", FileImportViewSet.as_view(), name="api_import"),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
