from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        formulario = UserCreationForm()

    return render(request, 'usuarios/registro.html', {
        'formulario': formulario
    })
    
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def inicio(request):
    return render(request, 'inicio.html')
# Create your views here.
