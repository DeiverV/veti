from dataclasses import field
from tkinter import Widget
from turtle import width
from django import forms
from citas_usuarios.widget import DatePickerInput,TimePickerInput
from django.contrib.auth.forms import UserCreationForm
from citas_usuarios.models import Mascota
from django.contrib.auth.models import User
from citas_usuarios.models import Mascota,Publicacion,Certificado,Local,Asignacion
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


class UserEditFrom(UserCreationForm):

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput,required=False)
    password2 = forms.CharField(label="Repita su Contraseña", widget=forms.PasswordInput,required=False)
    biografia = forms.CharField(label="Biografia",required=False)
    avatar =forms.ImageField(label="Avatar",required=False)
    
    class Meta:
        model = User
        fields =('username',)
        widget = {
            "username":forms.CharField(required=False, help_text=False)
        }

    def clean_password2(self):
        password2 = self.cleaned_data["password2"]
        if  password2 != self.cleaned_data["password2"]:
            raise forms.ValidationError("Las contraseñas no coicinden..")
        return password2
    

class Localform(forms.ModelForm):
    class Meta:
        model = Local
        fields = ('nombre', 'pais', 'ciudad','zona','direccion','imagen')

class Certificadoform(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = ('nombre', 'fecha', 'imagen')

class PublicacionForm(forms.Form):
    texto = forms.CharField(max_length=300,label=False, widget=forms.Textarea(attrs={'placeholder':"Que vas a compartir hoy? :D"}))
    imagen = forms.ImageField(required=False)

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('fecha', 'especialidad', 'local')

class AsignacionForm(forms.ModelForm):
    class Meta:
        model=Asignacion
        fields = ('mascota',)
