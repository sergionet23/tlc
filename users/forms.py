from django import forms
from TeLoCuido.models import Datos_personales


class CuidacochesForm(forms.ModelForm):

    class Meta:
        model = Datos_personales


        fields = [
            'ci',
            'nombre',
            'apellido',
            'direccion',
            'telefono',
            'fecha_nacimiento',
            'numero_registro',
            'vigencia',
            'estado',
            'password',
            #'promedio',
            #'cantidad_votos',
            'image_url',
            'nombre_lugar_trabajo',
            #'horario_inicio',
            #'horario_fin',
            'direccion_trabajo',
            #'latitud_trabajo',
            #'longitud_trabajo',
            #'lugares_libres',
        ]


        labels = {
            'ci': 'Ci',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'fecha_nacimiento': 'Fecha Nacimiento Ej: 2000-01-01',
            'numero_registro': 'Numero Registro',
            'vigencia': 'Vigencia Ej: 2022-01-01',
            'estado': 'Estado',
            'password': 'Password',
            #'promedio': 'Promedio',
            #'cantidad_votos': 'Cantidad Votos',
            'image_url': 'Imagen URL',
            'nombre_lugar_trabajo': 'Nombre Lugar Trabajo',
            #'horario_inicio': 'Horario Inicio',
            #'horario_fin': 'Horario Fin',
            'direccion_trabajo': 'Direccion Trabajo',
            #'latitud_trabajo': 'Latitud Trabajo',
            #'longitud_trabajo': 'Longitud Trabajo',
            #'lugares_libres': 'Lugares Libres',
        }


        widgets = {
            'ci': forms.NumberInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control'}),
            'numero_registro': forms.NumberInput(attrs={'class':'form-control'}),
            'vigencia': forms.DateInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            #'promedio': forms.TextInput(attrs={'class':'form-control'}),
            #'cantidad_votos': forms.NumberInput(attrs={'class':'form-control'}),
            'image_url': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_lugar_trabajo': forms.TextInput(attrs={'class':'form-control'}),
            #'horario_inicio': forms.TimeInput(attrs={'class':'form-control'}),
            #'horario_fin': forms.TimeInput(attrs={'class':'form-control'}),
            'direccion_trabajo': forms.TextInput(attrs={'class':'form-control'}),
            #'latitud_trabajo': forms.TextInput(attrs={'class':'form-control'}),
            #'longitud_trabajo': forms.TextInput(attrs={'class':'form-control'}),
            #'lugares_libres': forms.NumberInput(attrs={'class':'form-control'}),
        }
