from django.db import models

from veti_auth.models import Usuario, Veterinario

class Mascota(models.Model):
    amo = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    tipo_animal = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="mascotas" )
    def __str__(self) -> str:
        return f'{self.nombre}'

class Publicacion(models.Model):
    autor = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.CharField(max_length=300,blank=True)
    imagen = models.ImageField(upload_to="publicaciones",blank=True)

class Local(models.Model):
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    pais = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=60)
    zona = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="locales",blank=True)

class Cita(models.Model):
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    cliente  = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, blank=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    especialidad = models.ImageField(max_length=100)

class Certificado(models.Model):
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="certificados",blank=True)
    fecha = models.DateField()