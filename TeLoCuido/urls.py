from django.urls import path
from . import views


urlpatterns = [
    path ('',views.index),
    path('Datos_Personales/', views.Datos_personales),
    path('Lugar_trabajo/', views.Lugar_trabajo),
    path('Monedero/', views.Monedero),
    path('Puntuacion/', views.Puntuacion),
    path ('Datos_Bancarios', views.Datos_bancarios)
]