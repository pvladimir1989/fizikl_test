from django.urls import path
from django.contrib import admin

from main import views

urlpatterns = [
    path('', views.ImageView.as_view()),
    path('upload/', views.ImageCreateView.as_view(), name='upload'),
    path('admin/', admin.site.urls),
]
