from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from veti_auth.models import Usuario
from django.contrib.auth.models import User
from citas_usuarios.forms import UserForm,MascotaForm,CitaForm,PublicacionForm
from citas_usuarios.models import Mascota,Cita,Publicacion
from django.contrib.auth.decorators import login_required
import os

def inicio(request):
    if request.user:
        usuario = request.user.usuario
        return render(request,"inicio.html",{"user":usuario})
    return render(request,'inicio.html')

@login_required
def sobre_nosotros(request):
    return render(request,'sobre_nosotros.html')

@login_required
def perfil(request):
    user = request.user
    mascotas_usuario = Mascota.objects.filter(amo=request.user.id)
    mascota_form = MascotaForm()
    return render(request,'perfil.html',{"usuario":user,"mascotas_usuario":mascotas_usuario,"mascota_form":mascota_form})

@login_required
def muro(request):
    publicacion_formulario=PublicacionForm()

    if request.method=="POST":

        publicacion_formulario=PublicacionForm(request.POST,request.FILES)
        if publicacion_formulario.is_valid():
            data = publicacion_formulario.cleaned_data
            publicacion_nueva = Publicacion(
                autor=request.user.usuario,
                texto=data["texto"],
                imagen=data["imagen"]
                )

            publicacion_nueva.save()
            return HttpResponseRedirect('../perfil')

    else:
        usuarios = Usuario.objects.all()
        publicaciones = Publicacion.objects.all()
        return render(request,"muro.html",{"usuarios":usuarios,"publicaciones":publicaciones,"publicacion_formulario":publicacion_formulario})


def busqueda_cita(request):
    if request.method == 'GET':
        busqueda = request.GET.get('header_input_busqueda_citas')
        citas_encontradas = Cita.objects.filter(especialidad__contains=busqueda)
        return render(request,'busqueda_cita.html', {'citas_encontradas': citas_encontradas})
    else:
        return HttpResponseRedirect('./')
#----------------------------------------------------------------------------VISTAS DE MODELO MASCOTAS

@login_required
def mascotas(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            usuario = Usuario.objects.get(user_id = request.user)
            mascota_agregada = Mascota(
                amo= usuario ,
                nombre = info['Nombre'],
                edad = info['Edad'], 
                tipo_animal = info['Tipo_animal'], 
                raza=info['Raza'], 
                imagen=info['Foto']
                )
                
            mascota_agregada.save()
            return HttpResponseRedirect('../perfil')

@login_required
def eliminar_mascota(request, id):
    if request.method == 'POST':
        mascota = Mascota.objects.get(id=id)
        mascota.delete()
        mascotas = Mascota.objects.all()
        return HttpResponseRedirect('../perfil')

@login_required
def modificar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    if request.method == "POST":
        miForm = MascotaForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = Usuario.objects.get(user_id = request.user)
            data = miForm.cleaned_data
            
            mascota.amo = usuario
            mascota.nombre = data["Nombre"]
            mascota.edad = data["Edad"] 
            mascota.tipo_animal = data["Tipo_animal"]
            mascota.raza = data["Raza"]
            if data["Foto"]:
                image_path = mascota.imagen.path
                if os.path.exists(image_path):
                    os.remove(image_path)
                mascota.imagen = data["Foto"]
            else:
                mascota.imagen = mascota.imagen
            mascota.save()

            return HttpResponseRedirect('../perfil')
    else:
        usuario = Usuario.objects.get(user_id = request.user)
        miForm = MascotaForm(initial={
            "Amo": usuario,
            "Nombre": mascota.nombre,
            "Tipo_animal": mascota.tipo_animal,
            "Raza": mascota.raza,
            "Edad": mascota.edad,
            "Foto": mascota.imagen,
        })
        return render(request, "modificar_mascotas.html",{"miForm": miForm, "id": mascota.id,"nombre_mascota":mascota.nombre})

#----------------------------------------------------------------------------VISTAS DE MODELO CITAS

@login_required
def citas(request):
        #VALIDAR SI EL USUARIO ES VETERINARIO request.user.usuario.veterinario
        #veterinario=request.user.usuario.veterinario
        #verificar que el local.veterinario == veterinario
    if request.method == 'POST':
        form = CitaForm(request.POST)
        veterinario = request.user.usuario.veterinario
        if form.is_valid() and veterinario:
            info = form.cleaned_data    
            if info['local'].veterinario == veterinario:
                cita_agregada = Cita(veterinario = veterinario ,local=info['local'] ,fecha=info['fecha'] ,especialidad=info['especialidad'])
                cita_agregada.save()
                return HttpResponse

    cita_form = CitaForm()
    citas = Cita.objects.all
    return render(request,'citas.html', {'cita_form':cita_form,'lista_citas':citas})

@login_required
def eliminar_cita(request, id):

    if request.method == 'POST':

        cita = Cita.objects.get(id=id)

        cita.delete()

        citas = Cita.objects.all()

        contexto = {"citas": citas}

        return HttpResponseRedirect('../citas')
        
@login_required
def modificar_cita(request, id):

    cita = Cita.objects.get(id=id)

    if request.method == "POST":

        miForm = CitaForm(request.POST)

        if miForm.is_valid():

            data = miForm.cleaned_data
            
            cita.veterinario = data["veterinario"]
            cita.local = data["local"]
            cita.fecha = data["fecha"]
            cita.especialidad = data["especialidad"]
            
            cita.save()

            return HttpResponseRedirect('../citas')
    else:
        miForm = CitaForm(initial={
            "veterinario": cita.veterinario,
            "local": cita.local,
            "fecha": cita.fecha,
            "hora": cita.hora,   
            "especialidad": cita.especialidad,
        })
        return render(request, "modificar_cita.html",{"miForm": miForm, "id": cita.id})

#----------------------------------------------------------------------------VISTAS DE MODELO USUARIOS


def usuarios(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario_agregado = Usuario(cedula=info['cedula'] ,nombre = info['nombre'], edad=info['edad'], rol=info['rol'])
            usuario_agregado.save()
            return HttpResponseRedirect('../')

    usuarios_form = UserForm()
    usuarios = Usuario.objects.all()

    return render(request,'usuario.html', {'usuarios_form':usuarios_form,'lista_usuario': usuarios})

def modificar_usuario(request, id):

    usuario = Usuario.objects.get(cedula=id)

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

        usuario = Usuario.objects.get(cedula=id)

        usuario.delete()

        usuarios = Usuario.objects.all()

        contexto = {"usuarios": usuarios}

        return HttpResponseRedirect ("../usuarios")
