from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.inicio, name='home'),
    path('', views.inicio, name='inicio'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('certificados/', views.certificados, name='certificados'),
    path('contacto/', views.formulario_contacto, name='contacto'),
]

