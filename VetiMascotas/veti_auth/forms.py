from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Usuario

class UserCreateForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','password1','password2']
        help_texts={k:"" for k in fields}

    def Duplicado(self):
        username = self.cleaned_data['username']
        if User.objects.get(username=username):
            raise forms.ValidationError("Usuario ya existe")
        return username

        
class RegisterForm(ModelForm):
    class Meta:
        model=Usuario
        fields=["edad"]