from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from citas_usuarios.forms import Certificadoform
from citas_usuarios.models import Certificado
from veti_auth.models import Veterinario
from citas_usuarios.forms import Localform
from citas_usuarios.models import Local
from citas_usuarios.forms import UserEditFrom
from veti_auth.models import Usuario
from django.contrib.auth.models import User
from citas_usuarios.forms import UserForm,MascotaForm,CitaForm,PublicacionForm
from citas_usuarios.models import Mascota,Cita,Publicacion
from django.contrib.auth.decorators import login_required
import os

def inicio(request):
    return render(request,'inicio.html')

@login_required
def visita_perfil(request, idusuario):
    usuario = Usuario.objects.get(user_id=idusuario)

    if hasattr(usuario, 'veterinario'):
        return render(request,'perfil_veterinario.html',{"usuario":usuario})

    mascotas_usuario = Mascota.objects.filter(amo=usuario)
    return render(request,'perfil_usuario.html',{"usuario":usuario,"mascotas_usuario":mascotas_usuario})


@login_required
def sobre_nosotros(request):
    return render(request,'sobre_nosotros.html')
    

@login_required
def perfil(request):
    user = request.user.usuario

    if hasattr(user, 'veterinario'):
        return render(request,'perfil_veterinario.html',{"usuario":user})

    mascotas_usuario = Mascota.objects.filter(amo=request.user.id)
    mascota_form = MascotaForm()
    return render(request,'perfil.html',{"usuario":user,"mascotas_usuario":mascotas_usuario,"mascota_form":mascota_form})

    

#------------------------------------------------------------------------------------VISTAS DE MODELO PUBLICACIONES

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
            return HttpResponseRedirect('./')
    else:
        usuarios = Usuario.objects.all()
        publicaciones = Publicacion.objects.all()
        return render(request,"muro.html",{"usuarios":usuarios,"publicaciones":publicaciones,"publicacion_formulario":publicacion_formulario})


@login_required
def publicaciones_propias(request):
    publicaciones = Publicacion.objects.filter(autor=request.user.usuario)
    return render(request,"mis_publicaciones.html",{"publicaciones":publicaciones})



@login_required
def eliminar_publicacion(request,id):
    if request.method == 'POST':
        publicacion = Publicacion.objects.get(id=id)
        publicacion.delete()
        return HttpResponseRedirect('../mis_publicaciones')



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

@login_required
def editar_perfil(request):
    
    usuario = request.user
    cliente = request.user.usuario
    if request.method == 'POST':
        miForm = UserEditFrom( request.POST, request.FILES, instance=request.user)
        if miForm.is_valid():

            data = miForm.cleaned_data

            usuario.username= data['username']
            usuario.save()

            cliente.biografia = data['biografia']
            if data["avatar"] and cliente.avatar:
                image_path = cliente.avatar.path
                if os.path.exists(image_path):
                    os.remove(image_path)
                cliente.avatar = data["avatar"]
            elif data["avatar"]:
                cliente.avatar = data["avatar"]
            else:
                cliente.avatar = cliente.avatar
            cliente.save()

            return HttpResponseRedirect("../perfil")
        
        print(miForm.errors.get_json_data)
        return HttpResponseRedirect("./")
    else:
        miForm= UserEditFrom(initial={
            "username": request.user,
            "biografia" : usuario.usuario.biografia,
            "avatar" : usuario.usuario.avatar
        })
        return render(request, "editar_perfil.html",{"miForm":miForm, "usuario":usuario })

def eliminar_usuario(request, id):

     if request.method == 'POST':
        usuario = Usuario.objects.get(cedula=id)
        usuario.delete()
        usuarios = Usuario.objects.all()
        contexto = {"usuarios": usuarios}
        return HttpResponseRedirect ("../usuarios")


@login_required
def Locales(request):
    if request.user.usuario.veterinario:
        if request.method == 'POST':
            form = Localform(request.POST, request.FILES)
            veterinario = request.user.usuario.veterinario
            if form.is_valid() and veterinario:
                info = form.cleaned_data
                local_agregado = Local(veterinario=veterinario ,pais = info['pais'], ciudad=info['ciudad'], zona=info['zona'], direccion=info['direccion'], imagen=info['imagen'])
                local_agregado.save()
                return HttpResponseRedirect('../')

        local_form = Localform()
        local = Local.objects.all()

        return render(request,'locales.html', {'local_form':local_form,'lista_locales': local})
    else:
        return HttpResponseRedirect("../")

@login_required
def eliminar_local(request, id):

    if request.method == 'POST':
        local = Local.objects.get(id=id)
        local.delete()
        local = Local.objects.all()
        contexto = {"local": local}
        return HttpResponseRedirect('../locales')

@login_required
def modificar_local(request, id):

    local = Local.objects.get(id=id)
    if request.method == "POST":

        miForm = Localform(request.POST, request.FILES)
        if miForm.is_valid():
            data = miForm.cleaned_data

            local.veterinario = data["veterinario"]
            local.pais = data["pais"]
            local.ciudad = data["ciudad"]
            local.zona = data["zona"]
            local.direccion = data["direccion"]
            if data["imagen"]:
                image_path = local.imagen.path
                if os.path.exists(image_path):
                    os.remove(image_path)
                local.imagen = data["imagen"]
            else:
                local.imagen = local.imagen
            local.save()

            return HttpResponseRedirect('../locales')
    else:
        miForm = Localform(initial={
            "veterinario": local.veterinario,
            "pais": local.pais,
            "ciudad": local.ciudad,
            "zona": local.zona,   
            "direccion": local.direccion,
            "imagen":local.imagen
        })
        return render(request, "modificar_locales.html",{"miForm": miForm, "id": local.id})


@login_required
def certificados (request):
    certificados = request.user

    if request.method == 'POST':

        miForm = Certificadoform( request.POST, instance=request.user)
        if miForm.is_valid():
            data = miForm.cleaned_data

            certificados.veterinario = data['veterinario']
            certificados.imagen= data['imagen']
            certificados.fecha = data['fecha']

            certificados.save()
            return render(request, "certificados.html")
    else:
        miForm= Certificadoform(instance=request.user)
        return render(request, "certificados.html",{"miForm":miForm, "certificados":certificados })

@login_required
def eliminar_certificados(request, id):

     if request.method == 'POST':

        certificado = Certificado.objects.get(id=id)
        certificado.delete()
        certificados = Certificado.objects.all()
        contexto = {"certificados": certificados}

        return HttpResponseRedirect ("../certificados")

