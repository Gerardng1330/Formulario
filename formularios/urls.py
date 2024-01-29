from django.urls import path
from .views import home, formulario_view,exito,render_formulario,cerrado

app_name = 'formularios'

urlpatterns = [
    #comentariosyhughgjhghjg
    path('formulario/', render_formulario, name='render_formulario'),
    path('xs', formulario_view, name='formulario_view'),#prueba
    path('', exito, name='exito'),
    path('cerrado/', cerrado, name='cerrado'),

   

]
