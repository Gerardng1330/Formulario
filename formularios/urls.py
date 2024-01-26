from django.urls import path
from .views import home, formulario_view,exito,formulario

app_name = 'formularios'

urlpatterns = [
    #comentariosyhughgjhghjg
    path('', formulario, name='formulario'),
    path('exitoss/', formulario_view, name='formulario_view'),
    path('exito/', exito, name='exito'),

   

]