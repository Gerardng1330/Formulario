from django.urls import path
from . import views

urlpatterns  = [
    path('', views.inicio_sesion,name='inicio'),
    path('home/', views.home,name='home'),
    path('inicio/', views.inicio_sesion,name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('logout/',views.signout, name='logout'),
    path('form/', views.formacion,name='form'),

]
#si a la url del main le pongo un prefijo ya sea home/ le tengo que poner eso
#a todas las urls que agregue en cualquier aplicacion