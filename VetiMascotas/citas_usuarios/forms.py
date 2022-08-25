from dataclasses import field
from django import forms
from citas_usuarios.widget import DatePickerInput,TimePickerInput

from citas_usuarios.models import Mascota

class UserForm(forms.Form):
    cedula = forms.IntegerField()   
    nombre = forms.CharField(max_length=20)   
    edad = forms.IntegerField()

class MascotaForm(forms.Form):
    Nombre = forms.CharField(max_length=20)   
    Edad = forms.IntegerField()
    Tipo_animal = forms.CharField(max_length=20)
    Raza = forms.CharField(max_length=20) 
    Foto = forms.ImageField() 


class CitaForm(forms.Form):
    veterinario = forms.CharField(max_length=30)
    local = forms.CharField()
    fecha = forms.DateTimeField(widget=DatePickerInput)
    hora = forms.TimeField(widget=TimePickerInput) 
    especialidad = forms.CharField(max_length=30)