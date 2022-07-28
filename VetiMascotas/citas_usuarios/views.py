from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from citas_usuarios.forms import RolForm,UserForm,MascotaForm
from citas_usuarios.models import Rol,Persona,Mascota

def inicio(request):
    
    return render(request,'base.html')

def roles(request):

    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            rol_agregado = Rol(nombre = info['nombre'])
            rol_agregado.save()
            return HttpResponseRedirect('../')
    
    rol_form = RolForm()

    return render(request,'rol.html', {'rol_form':rol_form})

def usuarios(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario_agregado = Persona(cedula=info['cedula'] ,nombre = info['nombre'], edad=info['edad'], rol=info['rol'])
            usuario_agregado.save()
            return HttpResponseRedirect('../')

    rol_form = UserForm()

    return render(request,'rol.html', {'rol_form':rol_form})

def mascotas(request):

    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            mascota_agregada = Mascota(amo=info['amo'] ,nombre = info['nombre'],tipo_animal = info['tipo_animal'], edad=info['edad'])
            mascota_agregada.save()
            return HttpResponseRedirect('../')

    rol_form = MascotaForm()

    return render(request,'rol.html', {'rol_form':rol_form})