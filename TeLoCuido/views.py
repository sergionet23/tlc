from django.shortcuts import render
from django.http import HttpResponse
from .models import Datos_personales, Lugar_trabajo, Monedero, Puntuacion, Datos_bancarios, Woow


def index(request):
    equipo = Woow.objects.all()
    return render(request, 'index.html', {'equipo': equipo})


def datos_personales(request):
    datos_personales = Datos_personales.objects.all()
    return render(request, 'datos_personales.html', {'datos_personales': datos_personales})


def lugar_trabajo(request):
    lugar_trabajo = Lugar_trabajo.objects.all()
    return render(request, 'lugar_trabajo.html', {'lugar_trabajo': lugar_trabajo})


def monedero(request):
    monedero = Monedero.objects.all()
    return render(request, 'monedero.html', {'mondero': monedero})


def puntuacion(request):
    puntuacion = Puntuacion.objects.all()
    return render(request, 'puntacion.html',{'punutacion': puntuacion})


def datos_bancarios(request):
    datos_bancarios = Datos_bancarios.objects.all()
    return render(request, 'datos_bancarios.html', {'datos_bancarios': datos_bancarios})