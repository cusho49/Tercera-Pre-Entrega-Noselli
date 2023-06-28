from django.contrib import admin
from django.urls import path, include
from django_entregable import views

urlpatterns = [
    path('', include('inicio.urls')),
    path('admin/', admin.site.urls),
]
