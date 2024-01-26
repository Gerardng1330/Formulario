from django.urls import path
from .views import home, formulario_view,exito,render_formulario

app_name = 'formularios'

urlpatterns = [
    #comentariosyhughgjhghjg
    path('formulario/', render_formulario, name='render_formulario'),
    path('exitoss/', formulario_view, name='formulario_view'),#prueba
    path('exito/', exito, name='exito'),

   

]