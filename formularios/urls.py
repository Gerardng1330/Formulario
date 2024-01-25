from django.urls import path
from .views import *

app_name = 'formularios'

urlpatterns = [
    #path('', home, name='home'),
    path('formulario/', formulario, name='formulario'),
    path('exitoss/', formulario_view, name='formulario_view'),
    path('exito/', exito, name='exito'),

   

]