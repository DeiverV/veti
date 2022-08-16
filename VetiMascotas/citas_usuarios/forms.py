from dataclasses import field
from django import forms
from citas_usuarios.widget import DatePickerInput,TimePickerInput

from citas_usuarios.models import Mascota

class UserForm(forms.Form):
    cedula = forms.IntegerField()   
    nombre = forms.CharField(max_length=20)   
    edad = forms.IntegerField()

class MascotaForm(forms.Form):
    nombre = forms.CharField(max_length=20)   
    tipo_animal = forms.CharField(max_length=20)   
    edad = forms.IntegerField()


class CitaForm(forms.Form):
    fecha = forms.DateTimeField(widget=DatePickerInput)
    hora = forms.TimeField(widget=TimePickerInput) 
    especialidad = forms.CharField(max_length=30)   