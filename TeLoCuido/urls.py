from django.urls import path, include
from . import views


urlpatterns = [
    path ('',views.index),
    path('Datos_Personales/', views.Datos_personales),
    path('Lugar_trabajo/', views.Lugar_trabajo),
    path('Monedero/', views.Monedero),
    path('Puntuacion/', views.Puntuacion),
    path ('Datos_Bancarios', views.Datos_bancarios),
    path('login/', include('django.contrib.auth.urls')),
    path('logout/', include('django.contrib.auth.urls')),
]