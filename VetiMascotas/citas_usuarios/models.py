from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} - {self.cedula}'


class Mascota(models.Model):
    amo = models.ForeignKey(Persona,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    tipo_animal = models.CharField(max_length=50)
    edad = models.IntegerField()
        
class CitaMedica(models.Model):
    veterinario = models.ForeignKey(Persona,on_delete=models.CASCADE,related_name='veterinario_requerido')
    paciente = models.ForeignKey(Persona,on_delete=models.CASCADE,related_name='usuario_requerido')
    fecha = models.DateTimeField()
    mascota= models.ForeignKey(Mascota,on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)