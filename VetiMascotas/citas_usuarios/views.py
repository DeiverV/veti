from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from veti_auth.models import Usuario
from citas_usuarios.forms import UserForm,MascotaForm,CitaForm
from citas_usuarios.models import Mascota,Cita
from django.contrib.auth.decorators import login_required

def inicio(request):
    if request.user:
        username = request.user.username.capitalize()
        return render(request,"inicio.html",{"user":username})
    return render(request,'inicio.html')

@login_required
def sobre_nosotros(request):
    return render(request,'sobre_nosotros.html')

@login_required
def perfil(request):
    return render(request,'perfil.html')


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
        print(form)
        if form.is_valid():
            print("123")
            info = form.cleaned_data
            usuario = Usuario.objects.get(user_id = request.user)
            mascota_agregada = Mascota(amo= usuario ,nombre = info['Nombre'],edad = info['Edad'], tipo_animal = info['Tipo_animal'], raza=info['Raza'], imagen=info['Foto'])
            mascota_agregada.save()
            return HttpResponseRedirect('./')

    mascota_form = MascotaForm()
    lista_mascotas = Mascota.objects.all()

    return render(request,'mascotas.html', {'mascota_form': mascota_form, 'lista_mascotas': lista_mascotas})


@login_required
def eliminar_mascota(request, id):

    if request.method == 'POST':

        mascota = Mascota.objects.get(id=id)

        mascota.delete()

        mascotas = Mascota.objects.all()

        contexto = {"mascotas": mascotas}

        return HttpResponseRedirect('../mascotas')

@login_required
def modificar_mascota(request, id):

    mascota = Mascota.objects.get(id=id)

    if request.method == "POST":

        miForm = MascotaForm(request.POST)

        if miForm.is_valid():
            usuario = Usuario.objects.get(user_id = request.user)
            data = miForm.cleaned_data
            
            mascota.amo = data[usuario]
            mascota.nombre = data["nombre"]
            mascota.tipo_animal = data["tipo_animal"]
            mascota.raza = data["raza"]
            mascota.edad = data["edad"]
            mascota.imagen = data["imagen"]
            
            mascota.save()

            return HttpResponseRedirect('../mascotas')
    else:
        usuario = Usuario.objects.get(user_id = request.user)
        miForm = MascotaForm(initial={
            "amo": usuario,
            "nombre": mascota.nombre,
            "tipo_animal": mascota.tipo_animal,
            "raza": mascota.raza,
            "edad": mascota.edad,
            "imagen": mascota.imagen,
        })
        return render(request, "modificar_mascotas.html",{"miForm": miForm, "id": mascota.id})

#----------------------------------------------------------------------------VISTAS DE MODELO CITAS


def citas(request):

    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cita_agregada = Cita(veterinario=info['veterinario'] ,local = info['local'] ,fecha=info['fecha'] ,hora=info['hora'] ,especialidad=info['especialidad'])
            cita_agregada.save()
            return HttpResponse

    cita_form = CitaForm()
    citas = Cita.objects.all
    return render(request,'citas.html', {'cita_form':cita_form,'lista_citas':citas})

def eliminar_cita(request, id):

    if request.method == 'POST':

        cita = Cita.objects.get(id=id)

        cita.delete()

        citas = Cita.objects.all()

        contexto = {"citas": citas}

        return HttpResponseRedirect('../citas')

def modificar_cita(request, id):

    cita = Cita.objects.get(id=id)

    if request.method == "POST":

        miForm = CitaForm(request.POST)

        if miForm.is_valid():

            data = miForm.cleaned_data
            
            cita.veterinario = data["veterinario"]
            cita.local = data["local"]
            cita.fecha = data["fecha"]
            cita.hora = data["hora"]
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


