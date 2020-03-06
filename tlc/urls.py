from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('TeLoCuido/',include('TeLoCuido.urls')),
    path('', views.bienvenido),
    path('registro', views.registro),
    path('login', views.login),
    path('logout', views.logout),
    path('usuarios/', views.usuarios),
    path('cuidacoches/', views.cuidacoches),
]
