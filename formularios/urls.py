from django.urls import path
from .views import *

app_name = 'formularios'

urlpatterns = [
    
    path('', formulario, name='formulario'),
    path('exitoss/', formulario_view, name='formulario_view'),
    path('exito/', exito, name='exito'),

   

]