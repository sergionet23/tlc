from django.urls import path
from . import views

urlpatterns = [
    path('mapa/', views.index, name='index'),
    path('mapa/lugarocupado/', views.lugarocupado, name='lugarocupado'),
    path('mapa/propina/', views.propina, name='propina'),
]
