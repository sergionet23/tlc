from django.contrib import admin
from .models import Datos_personales,  Monedero, Puntuacion, Datos_bancarios, Woow

admin.site.register(Datos_personales)
admin.site.register(Monedero)
admin.site.register(Puntuacion)
admin.site.register(Datos_bancarios)
admin.site.register(Woow)
