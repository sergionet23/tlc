from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from TeLoCuido.models import  Lugar_trabajo, Datos_personales
import json


def mapa(request):
    template = loader.get_template('mapa.html')
    coordenadas = Datos_personales.objects.all()
    return render(request, 'mapa.html', {'coordenadas': coordenadas})


def lugarocupado(request):
    template = loader.get_template('mapa/lugarocupado.html')
    return HttpResponse(template.render({}, request))


def propina(request):
    template = loader.get_template('mapa/propina.html')
    return HttpResponse(template.render({}, request))



