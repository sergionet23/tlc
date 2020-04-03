from django.db import models


class Woow(models.Model):
    nombre = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    foto = models.CharField(max_length=2083)


class Datos_personales(models.Model):
    ci = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()
    numero_registro = models.IntegerField()
    vigencia = models.DateTimeField()
    estado = models.CharField(max_length=25)
    password = models.CharField(max_length=255)
    promedio = models.FloatField(null=True)
    cantidad_votos = models.IntegerField(null=True)
    image_url = models.CharField(max_length=2083, null=True)
    nombre_lugar_trabajo = models.CharField(max_length=255, null=True)
    horario_inicio = models.IntegerField(null=True)
    horario_fin = models.IntegerField(null=True)
    direccion_trabajo = models.CharField(max_length=255, null=True)
    latitud_trabajo = models.FloatField(null=True)
    longitud_trabajo = models.FloatField(null=True)
    lugares_libres = models.IntegerField(null=True)


class Monedero(models.Model):
    ci = models.IntegerField()
    fecha_mov = models.FloatField()
    monto = models.IntegerField()
    origen = models.CharField(max_length=255)


class Puntuacion(models.Model):
    ci = models.IntegerField()
    puntuacion = models.FloatField()
    comentarios = models.CharField(max_length=255)
    reclamos = models.CharField(max_length=255)


class Datos_bancarios(models.Model):
    ci = models.IntegerField()
    cuenta_banco = models.IntegerField()
    banco = models.CharField(max_length=25)