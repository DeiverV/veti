from dataclasses import field
from urllib import request
from django import forms
from citas_usuarios.widget import DatePickerInput,TimePickerInput

from citas_usuarios.models import Mascota,Publicacion
from dataclasses import Field, field
from django import forms
from citas_usuarios.widget import DatePickerInput,TimePickerInput

from citas_usuarios.models import Cita, Mascota


class UserForm(forms.Form):
    cedula = forms.IntegerField()   
    nombre = forms.CharField(max_length=20)   
    edad = forms.IntegerField()

class MascotaForm(forms.Form):
    Nombre = forms.CharField(max_length=20)   
    Edad = forms.IntegerField()
    Tipo_animal = forms.CharField(max_length=20)
    Raza = forms.CharField(max_length=20) 
    Foto = forms.ImageField(required=False) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Foto'].widget.clear_checkbox = 'Borrar'
        self.fields['Foto'].widget.initial_text = "Actual"
        self.fields['Foto'].widget.input_text = "Cambiar Imagen"


class CitaForm(forms.Form):
    veterinario = forms.CharField(max_length=30)
    local = forms.CharField()
    fecha = forms.DateTimeField(widget=DatePickerInput)
    hora = forms.TimeField(widget=TimePickerInput) 
    especialidad = forms.CharField(max_length=30)


class PublicacionForm(forms.Form):
    texto = forms.CharField(max_length=300)
    imagen = forms.ImageField(required=False)

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('fecha', 'especialidad', 'local')

