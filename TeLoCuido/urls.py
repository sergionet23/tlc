from django.urls import path, include
from . import views


urlpatterns = [
    path ('',views.index),
    path('Datos_Personales/', views.Datos_personales),
    path('Lugar_trabajo/', views.Lugar_trabajo),
    path('Monedero/', views.Monedero),
    path('dar_propina', views.dar_propina),
    path('puntuacion/', views.puntuacion),
    path ('Datos_Bancarios', views.Datos_bancarios),
    path('login/', include('django.contrib.auth.urls')),
    path('logout/', include('django.contrib.auth.urls')),
]