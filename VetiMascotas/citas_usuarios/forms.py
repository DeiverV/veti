from dataclasses import field
from django import forms
from citas_usuarios.widget import DatePickerInput,TimePickerInput

from citas_usuarios.models import Rol,Persona,Mascota

class RolForm(forms.Form):
    nombre = forms.CharField(max_length=20)

class UserForm(forms.Form):
    cedula = forms.IntegerField()   
    nombre = forms.CharField(max_length=20)   
    edad = forms.IntegerField()

    rol = forms.ModelChoiceField(
    queryset=Rol.objects.all(),
    label='rol',
    widget=forms.Select
)

class MascotaForm(forms.Form):
    nombre = forms.CharField(max_length=20)   
    tipo_animal = forms.CharField(max_length=20)   
    edad = forms.IntegerField()
    
    amo = forms.ModelChoiceField(
    queryset=Persona.objects.filter(rol=2),
    label='Amo',
    widget=forms.Select
)

class CitaForm(forms.Form):
    fecha = forms.DateTimeField(widget=DatePickerInput)
    hora = forms.TimeField(widget=TimePickerInput) 
    especialidad = forms.CharField(max_length=30)   
    
    veterinario = forms.ModelChoiceField(
    queryset=Persona.objects.filter(rol=1),
    label='Veterinario',
    widget=forms.Select
    )