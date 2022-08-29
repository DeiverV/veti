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
from .views import Locales, asignacion_cita,busqueda_cita, certificados, editar_perfil,eliminar_certificado, eliminar_cita, eliminar_local, eliminar_mascota, eliminar_publicacion, eliminar_usuario, inicio, mascotas, mis_citas, modificar_cita, modificar_local, modificar_mascota, muro, perfil, publicaciones_propias, sobre_nosotros,citas, visita_perfil


urlpatterns = [
    path('', inicio, name='inicio'),
    path('about-us', sobre_nosotros, name='sobre_nosotros'),
    path('perfil', perfil, name='perfil'),
    path('perfil-usuario/<int:idusuario>', visita_perfil, name='perfil-usuario'),
    path('muro/', muro, name='muro'),
    path('mis_publicaciones/', publicaciones_propias, name='mis_publicaciones'),
    path('eliminar_publicacion/<int:id>', eliminar_publicacion, name='eliminar_publicaciones'),
    path('mascotas/', mascotas, name='mascotas'),
    path('elimina_mascota/<int:id>', eliminar_mascota, name='elimina_mascota'),
    path('modifica_mascota/<int:id>', modificar_mascota, name='modifica_mascota'),
    path('editarperfil/', editar_perfil, name="editar_perfil"),
    path('citas/', citas, name='citas'),
    path('mis_citas/', mis_citas, name='mis_citas'),
    path('elimina_cita/<int:id>', eliminar_cita, name='elimina_cita'),
    path('asignacion_cita/<int:idcita>', asignacion_cita, name='asignacion_cita'),
    path('locales/', Locales, name='locales'),

    path('modifica_cita/<int:id>', modificar_cita, name='modifica_cita'),
    path('elimina_usuario/<int:id>', eliminar_usuario, name='elimina_usuario'),
    path('busqueda/>', busqueda_cita, name='busqueda_cita'),
    path('elimina_local/<int:id>', eliminar_local, name='elimina_local'),
    path('modifica_local/<int:id>', modificar_local, name='modifica_local'),
    path('certificados/', certificados, name='certificados'),
    path('elimina_certificado/<int:id>', eliminar_certificado, name='elimina_certificado'),

    
]
