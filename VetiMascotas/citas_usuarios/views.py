from tkinter import Widget
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from citas_usuarios.forms import RolForm,UserForm,MascotaForm,CitaForm
from citas_usuarios.models import Rol,Persona,Mascota,CitaMedica,Persona

def inicio(request):
    
    return render(request,'inicio.html')


def busqueda_cita(request):
    if request.method == 'GET':
        busqueda = request.GET.get('header_input_busqueda_citas')
        citas_encontradas = CitaMedica.objects.filter(especialidad__contains=busqueda)
        return render(request,'busqueda_cita.html', {'citas_encontradas': citas_encontradas})
    else:
        return HttpResponseRedirect('./')
#----------------------------------------------------------------------------VISTAS DE MODELO MASCOTAS


def mascotas(request):

    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            mascota_agregada = Mascota(amo=info['amo'] ,nombre = info['nombre'],tipo_animal = info['tipo_animal'], edad=info['edad'])
            mascota_agregada.save()
            return HttpResponseRedirect('./')

    mascota_form = MascotaForm()
    lista_mascotas = Mascota.objects.all()

    return render(request,'mascotas.html', {'mascota_form':mascota_form,'lista_mascotas': lista_mascotas})

def eliminar_mascota(request, id):

    if request.method == 'POST':

        mascota = Mascota.objects.get(id=id)

        mascota.delete()

        mascotas = Mascota.objects.all()

        contexto = {"mascotas": mascotas}

        return HttpResponseRedirect('../mascotas')

def modificar_mascota(request, id):

    mascota = Mascota.objects.get(id=id)

    if request.method == "POST":

        miForm = MascotaForm(request.POST)

        if miForm.is_valid():
            data = miForm.cleaned_data
            
            mascota.amo = data["amo"]
            mascota.nombre = data["nombre"]
            mascota.tipo_animal = data["tipo_animal"]
            mascota.edad = data["edad"]
            
            mascota.save()

            return HttpResponseRedirect('../mascotas')
    else:
        miForm = MascotaForm(initial={
            "amo": mascota.amo,
            "nombre": mascota.nombre,
            "tipo_animal": mascota.tipo_animal,
            "edad": mascota.edad,
        })
        return render(request, "modificar_mascotas.html",{"miForm": miForm, "id": mascota.id})

#----------------------------------------------------------------------------VISTAS DE MODELO CITAS


def citas(request):

    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cita_agregada = CitaMedica(veterinario=info['veterinario'] ,fecha = info['fecha'],hora=info['hora'],especialidad=info['especialidad'])
            cita_agregada.save()
            return HttpResponseRedirect('../')

    cita_form = CitaForm()
    citas = CitaMedica.objects.all()

    return render(request,'citas.html', {'cita_form':cita_form,'lista_citas':citas})

def eliminar_cita(request, id):

    if request.method == 'POST':

        cita = CitaMedica.objects.get(id=id)

        cita.delete()

        citas = CitaMedica.objects.all()

        contexto = {"citas": citas}

        return HttpResponseRedirect('../citas')

def modificar_cita(request, id):

    cita = CitaMedica.objects.get(id=id)

    if request.method == "POST":

        miForm = CitaForm(request.POST)

        if miForm.is_valid():

            data = miForm.cleaned_data
            
            cita.veterinario = data["veterinario"]
            cita.fecha = data["fecha"]
            cita.hora = data["hora"]
            cita.especialidad = data["especialidad"]
            
            cita.save()

            return HttpResponseRedirect('../citas')
    else:
        miForm = CitaForm(initial={
            "veterinario": cita.veterinario,
            "paciente": cita.paciente,
            "fecha": cita.fecha,
            "hora": cita.hora,
            "mascota": cita.mascota,    
            "especialidad": cita.especialidad,
        })
        return render(request, "modificar_cita.html",{"miForm": miForm, "id": cita.id})

#----------------------------------------------------------------------------VISTAS DE MODELO USUARIOS


def usuarios(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario_agregado = Persona(cedula=info['cedula'] ,nombre = info['nombre'], edad=info['edad'], rol=info['rol'])
            usuario_agregado.save()
            return HttpResponseRedirect('../')

    usuarios_form = UserForm()
    usuarios = Persona.objects.all()

    return render(request,'usuario.html', {'usuarios_form':usuarios_form,'lista_usuario': usuarios})

def modificar_usuario(request, id):

    usuario = Persona.objects.get(cedula=id)

    if request.method == "POST":

        miForm = UserForm(request.POST)

        if miForm.is_valid():
            data = miForm.cleaned_data

            usuario.nombre = data["nombre"]
            usuario.edad = data["edad"]
            usuario.rol = data["rol"]

            usuario.save()

            return HttpResponseRedirect('../usuarios')
    else:
        miForm = UserForm(initial={
            "nombre": usuario.nombre,
            "edad": usuario.edad,
            "rol": usuario.rol,
            "cedula": usuario.cedula,
        })
        return render(request, "modificar_usuario.html",{"miForm": miForm, "id": usuario.cedula})

def eliminar_usuario(request, id):

     if request.method == 'POST':

        usuario = Persona.objects.get(cedula=id)

        usuario.delete()

        usuarios = Persona.objects.all()

        contexto = {"usuarios": usuarios}

        return HttpResponseRedirect ("../usuarios")


