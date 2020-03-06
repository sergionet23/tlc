from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm


def bienvenido(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "bienvenido.html")
    # En otro caso redireccionamos al login
    return redirect("/login")


def usuarios(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "iniciousuario.html")
    # En otro caso redireccionamos al login
    return redirect("/login")


def cuidacoches(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "iniciocuidacoches.html")
    # En otro caso redireccionamos al login
    return redirect("/login")


def registro(request):
    # Creamos el formulario de autenticacion vacio
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es valido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "registro.html", {'form': form})
#Cambiar cuando se cree el registro de usuarios


def login(request):
    # creamos el formulario de autenticacion vacio
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es valido...
        if form.is_valid():
            # Recuoperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                if request.user.username == "cuidacochesapp":
#                if request.user.groups.name == "cuidacoches":
                    return redirect('/cuidacoches')
#                elif request.user.groups.name == "usuarios":
                elif request.user.username == "usuarioapp":
                    return redirect('/usuarios')
                else:
                    return redirect('TeLoCuido/')
    # Si llegaos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


def logout(request):
    # Finalizamos la sesion
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
