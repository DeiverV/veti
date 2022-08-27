from dataclasses import field
from django import forms
from citas_usuarios.widget import DatePickerInput,TimePickerInput
from django.contrib.auth.forms import UserCreationForm
from citas_usuarios.models import Mascota
from django.contrib.auth.models import User

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


class UserEditFrom(UserCreationForm):

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita su Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields =['email', 'first_name', 'last_name']

    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if  password2 != self.cleaned_data["password2"]:
            raise forms.ValidationError("Las contraseñas no coicinden..")

        return password2
    
    biografia = forms.CharField(label="Biografia")
    
    avatar =forms.ImageField(label="Avatar")

class Localform(forms.Form):
    pais = forms.CharField(max_length=60)
    ciudad = forms.CharField(max_length=60)
    zona = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=100)
    imagen = forms.ImageField()
