from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from main.urls import api

urlpatterns = [
    # path('api/import/', include(api)),
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='main.html'))

]
