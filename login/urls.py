from django.urls import path
from . import views

urlpatterns  = [

    #path('home/', views.home,name='home'),
    path('login/', views.inicio_sesion,name='Login'),
    #path('register/', views.registro, name='Register'),
    path('logout/',views.signout, name='logout'),
    path('form/', views.formacion,name='form'),

]
#si a la url del main le pongo un prefijo ya sea home/ le tengo que poner eso
#a todas las urls que agregue en cualquier aplicacion