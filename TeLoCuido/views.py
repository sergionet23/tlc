from django.shortcuts import render
from django.http import HttpResponse
from .models import Datos_personales,  Monedero, Puntuacion, Datos_bancarios, Woow
from django.contrib.auth.decorators import login_required


def index(request):
    equipo = Woow.objects.all()
    return render(request, 'index.html', {'equipo': equipo})


@login_required(login_url='/login')
def datos_personales(request):
    datos_personales = Datos_personales.objects.all()
    return render(request, 'datos_personales.html', {'datos_personales': datos_personales})


@login_required(login_url='/login')
def monedero(request):
    monedero = Monedero.objects.all()
    return render(request, 'monedero.html', {'monedero': monedero})


def puntuacion(request):
    puntuacion = Puntuacion.objects.all()
    return render(request, 'puntuacion.html',{'puntuacion': puntuacion})


@login_required(login_url='/login')
def datos_bancarios(request):
    datos_bancarios = Datos_bancarios.objects.all()
    return render(request, 'datos_bancarios.html', {'datos_bancarios': datos_bancarios})


def dar_propina(request):
    dar_propina = Monedero.objects.all()
    return render(request, 'dar_propina.html',{'dar_propina': dar_propina})