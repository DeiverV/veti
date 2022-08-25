from django.contrib import admin

from citas_usuarios.models import Certificado, Cita, Local, Mascota, Publicacion

# Register your models here.

admin.site.register(Mascota)
admin.site.register(Publicacion)
admin.site.register(Local)
admin.site.register(Cita)
admin.site.register(Certificado)