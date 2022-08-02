"""VetiMascotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import eliminar_cita, eliminar_mascota, eliminar_usuario, inicio, leer_mascotas, lista_citas, lista_usuarios, mascotas, modificar_cita, modificar_mascota, modificar_usuario, roles, usuarios,citas

urlpatterns = [
    path('', inicio, name='inicio'),
    path('usuarios/', usuarios, name='usuarios'),
    path('mascotas/', mascotas, name='mascotas'),
    path('citas/', citas, name='citas'),
    path('leer_mascotas/', leer_mascotas, name='leermascotas'),
    path('elimina_mascota/<int:id>', eliminar_mascota, name='elimina_mascota'),
    path('modifica_mascota/<int:id>', modificar_mascota, name='modifica_mascota'),
    path('lista_citas', lista_citas, name='lista_citas'),
    path('elimina_cita/<int:id>', eliminar_cita, name='elimina_cita'),
    path('modifica_cita/<int:id>', modificar_cita, name='modifica_cita'),
    path('lista_usuarios/', lista_usuarios, name='listausuarios'),
    path('modifica_usuario/<int:id>', modificar_usuario, name='modifica_usuario'),
    path('elimina_usuario/<int:id>', eliminar_usuario, name='elimina_usuario'),
    
]
