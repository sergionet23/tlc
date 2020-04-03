from django.urls import path, include
from . import views



urlpatterns=[
    path ('',views.bienvenido, name ='bienvenido'),
    path('login/', include('django.contrib.auth.urls')),
    path('logout/', include('django.contrib.auth.urls')),
    path('users/nuevo', views.cudiacoches_view, name='cuidacoches_crear'),
]