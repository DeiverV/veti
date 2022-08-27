from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,)
    biografia = models.CharField(blank=True,null=True,max_length=300)
    avatar = models.ImageField(upload_to="avatares",blank=True,null=True)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.user_id}'

class Veterinario(models.Model):
    user_id = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True,)
    nit = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.user_id}'