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
    fecha_nacimiento = models.CharField(max_length=25)
    numero_registro = models.IntegerField()
    vigencia = models.CharField(max_length=25)
    estado = models.CharField(max_length=25)
    password = models.CharField(max_length=255)
    promedio = models.FloatField()
    cantidad_votos = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Lugar_trabajo(models.Model):
    ci = models.IntegerField()
    lugar_trabajo = models.CharField(max_length=255)
    horario = models.IntegerField()


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
