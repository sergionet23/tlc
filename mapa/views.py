from django.http import HttpResponse
from django.template import loader
#import sqlite3


def index(request):
    template = loader.get_template('mapa/indexTLC.html')
    return HttpResponse(template.render({}, request))


def lugarocupado(request):
    template = loader.get_template('mapa/lugarocupado.html')
    return HttpResponse(template.render({}, request))
# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
#conexion = sqlite3.connect('db.sqlite3')
#latitud = conexion.cursor()
#longitud = conexion.cursor()
#ci = conexion.cursor()

#latitud.execute("select latitud from TeLoCuido_lugar_trabajo")
#longitud.execute("select longitud from TeLoCuido_lugar_trabajo")
#ci.execute("select ci from TeLoCuido_lugar_trabajo")

# Cerramos la conexión, si no la cerramos quedará abierta
# y no podremos gestionar el fichero
#conexion.close()