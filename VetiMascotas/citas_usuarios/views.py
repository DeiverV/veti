from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from citas_usuarios.forms import RolForm,UserForm,MascotaForm,CitaForm
from citas_usuarios.models import Rol,Persona,Mascota,CitaMedica,Persona

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

def leermascotas(request):
    mascotas = Mascota.objects.all()
    contexto = {"mascotas": mascotas}
    return render(request, "lista_mascotas.html", contexto)


def eliminarMascota(request, id):

    if request.method == 'POST':

        mascota = Mascota.objects.get(id=id)

        mascota.delete()

        mascotas = Mascota.objects.all()

        contexto = {"mascotas": mascotas}

        return render(request, "lista_mascotas.html", contexto)



def modificarMascota(request, id):

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

            return render(request, "inicio.html")
    else:
        miForm = MascotaForm(initial={
            "amo": mascota.amo,
            "nombre": mascota.nombre,
            "tipo_animal": mascota.tipo_animal,
            "edad": mascota.edad,
        })
        return render(request, "modificar_mascotas.html",{"miForm": miForm, "id": mascota.id})
