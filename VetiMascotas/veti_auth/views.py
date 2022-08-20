from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario, Veterinario
from .forms import UserCreateForm,RegisterForm, VeterinarioForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def Login(request):
    if request.method=="POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            usuario = data['username']
            psw = data['password']

            user = authenticate(username=usuario,password=psw)

            if user:
                login(request,user)
                return HttpResponseRedirect("../../veti/")

        errores_login=login_form.errors.get_json_data()
        login_form=AuthenticationForm()
        for error in errores_login.values():
            for mensaje in error:
                mensajes_error = mensaje['message']
                return render(request,'login.html',{"errores":f"{mensajes_error}","login_form":login_form,"pagina":"Login"})
    else:

        login_form=AuthenticationForm()
        return render(request,"login.html",{"login_form":login_form,"pagina":"Login"})    



def Register(request):
    
    if request.method=="POST":

        user_form = UserCreateForm(request.POST)
        register_form = RegisterForm(request.POST)
        vet_form = VeterinarioForm(request.POST)

        if vet_form.is_valid() and user_form.is_valid() and register_form.is_valid():
            if vet_form.cleaned_data["nit"]:

                username = user_form.cleaned_data['username']
                edad = register_form.cleaned_data['edad']

                user = user_form.save()
                usuario_veti = Usuario(user_id=user,edad=edad)
                usuario_veti.save()
                usuario_veti = Usuario.objects.get(user_id=user)
                veterinario_veti = Veterinario(user_id=usuario_veti,nit=vet_form.cleaned_data["nit"])
                veterinario_veti.save()

                user_form = UserCreateForm()
                register_form = RegisterForm()

                return render(request,'register.html',{"mensaje":f"Veterinario {username} creado","register_form":register_form,"user_form":user_form,"pagina":"Register"})
                 

        if user_form.is_valid() and register_form.is_valid():

            username = user_form.cleaned_data['username']
            edad = register_form.cleaned_data['edad']

            user = user_form.save()
            usuario_veti = Usuario(user_id=user,edad=edad)
            usuario_veti.save()

            user_form = UserCreateForm()
            register_form = RegisterForm()

            return render(request,'register.html',{"mensaje":f"Usuario {username} creado","register_form":register_form,"user_form":user_form,"pagina":"Register"})
        

        errores_user=user_form.errors.get_json_data()
        errores_user.update(register_form.errors.get_json_data())
        errores_user.update(vet_form.errors.get_json_data())

        user_form = UserCreateForm()
        register_form = RegisterForm()

        for error in errores_user.values():
            for mensaje in error:
                mensajes_error = mensaje['message']
                return render(request,'register.html',{"errores":f"{mensajes_error}","register_form":register_form,"user_form":user_form,"pagina":"Register"})
            
    user_form = UserCreateForm()
    register_form = RegisterForm()
    
    return render(request,'register.html',{"register_form":register_form,"user_form":user_form,"pagina":"Register"})
