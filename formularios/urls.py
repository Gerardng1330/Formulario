from django.urls import path
from . import views

app_name = 'formularios'

urlpatterns = [
    #comentariosyhughgjhghjg
    path('', views.render_formulario, name='ver_formulario'),
    path('formulario/', views.render_formulario, name='ver_formulario'),
    path('formulario_enviado/', views.formulario_view, name='envio_formulario'),#prueba
    path('exito/', views.exito, name='pagina_exito'),
    path('cerrado/', views.cerrado, name='pagina_cerrado}'),
    path('validar-nombre/', views.validar_nombre, name='validar_nombre'),
    path('prueba/', views.prueba, name='prueba'),


    

   

]
