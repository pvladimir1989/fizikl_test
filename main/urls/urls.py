from django.contrib import admin
from django.urls import path, include

from main.urls import api

urlpatterns = [
    path('api/import/', include((api,), namespace='api_import')),
    path('admin/', admin.site.urls),

]
