from django.urls import path
from . import views


urlpatterns = [
    path('mapa/', views.index, name='index'),
]
