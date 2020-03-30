from django.urls import path, include
from . import views

urlpatterns = [
    path('mapa/', views.mapa, name='mapa'),
    path('mapa/lugarocupado/', views.lugarocupado, name='lugarocupado'),
    path('mapa/propina/', views.propina, name='propina'),
]
