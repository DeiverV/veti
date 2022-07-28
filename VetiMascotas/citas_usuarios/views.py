from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from citas_usuarios.forms import RolForm,UserForm,MascotaForm,CitaForm
from citas_usuarios.models import Rol,Persona,Mascota,CitaMedica

def inicio(request):
    
    return render(request,'inicio.html')

def roles(request):

    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            rol_agregado = Rol(nombre = info['nombre'])
            rol_agregado.save()
            return HttpResponseRedirect('../')
    
    usuarios_form = RolForm()

    return render(request,'usuario.html', {'usuarios_form':usuarios_form})

def usuarios(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario_agregado = Persona(cedula=info['cedula'] ,nombre = info['nombre'], edad=info['edad'], rol=info['rol'])
            usuario_agregado.save()
            return HttpResponseRedirect('../')

    usuarios_form = UserForm()

    return render(request,'usuario.html', {'usuarios_form':usuarios_form})

def mascotas(request):

    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            mascota_agregada = Mascota(amo=info['amo'] ,nombre = info['nombre'],tipo_animal = info['tipo_animal'], edad=info['edad'])
            mascota_agregada.save()
            return HttpResponseRedirect('../')

    mascota_form = MascotaForm()

    return render(request,'mascotas.html', {'mascota_form':mascota_form})

def citas(request):

    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cita_agregada = CitaMedica(veterinario=info['veterinario'] ,fecha = info['fecha'],hora=info['hora'],especialidad=info['especialidad'])
            cita_agregada.save()
            return HttpResponseRedirect('../')

    cita_form = CitaForm()

    return render(request,'citas.html', {'cita_form':cita_form})