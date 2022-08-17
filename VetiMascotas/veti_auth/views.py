from distutils.log import error
from django.shortcuts import render

from .models import Usuario
from .forms import UserCreateForm,RegisterForm

def Register(request):
    
    if request.method=="POST":

        user_form = UserCreateForm(request.POST)
        register_form = RegisterForm(request.POST)
        if user_form.is_valid() and user_form.is_valid():
            username = user_form.cleaned_data['username']
            edad = register_form.cleaned_data['edad']
            user = user_form.save()
            usuario_veti = Usuario(user_id=user,edad=edad)
            usuario_veti.save()
            return render(request,'register.html',{"mensaje":f"Usuario {username} creado"})
        else:
            errores=[]
            errores.extend(user_form.error_messages.values())
            return render(request,'register.html',{"errores":f"{errores}"})


    
    user_form = UserCreateForm()
    register_form = RegisterForm()
    
    return render(request,'register.html',{"register_form":register_form,"user_form":user_form})
