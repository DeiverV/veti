from django import forms

from citas_usuarios.models import Rol,Persona

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
    queryset=Persona.objects.all(),
    label='amo',
    widget=forms.Select
)