from django.urls import path
from django_entregable import views

urlpatterns = [
    path('', views.inicio),
    path('segunda-vista/', views.segunda_vista),
    path('fecha-actual/', views.fecha_actual),
    path('saludar/', views.saludar),
    path('saludos/<str:nombre>/<str:apellido>/', views.saludos),
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('cursoFormulario/', views.cursoFormulario, name='formulario_curso'),
    path('profes/', views.profes, name='profes'),
]