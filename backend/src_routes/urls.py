from django.urls import path
from . import views

app_name = 'src_routes'

urlpatterns = [
#Formularios
    path('', views.formulario_view, name='ver_formulario'),
    #path('formulario/', views.render_formulario, name='ver_formulario'),
    #path('formulario_enviado/', views.formulario_view, name='envio_formulario'),#prueba
    path('exito/', views.exito, name='pagina_exito'),
    path('cerrado/', views.cerrado, name='pagina_cerrado}'),
    path('prueba/', views.prueba, name='pagina_prueba'),


# Login views
    path('home/', views.home,name='home'),
    path('inicio/', views.inicio_sesion,name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('logout/',views.signout, name='logout'),
    path('form/', views.formacion,name='form'),
    
#Recuperacion de usuario
    path('recuperar/', views.recuperar_pass,name='recuperar'),    
    path('registro/', views.registro, name='registro'),
    path('activacion/', views.validar_token, name='activacion'),
    path('succefully/', views.succefully, name= 'succefully'),
    path('password-email/', views.password_email,name='passwordemail'),
    path('password-send/', views.password_send,name='passwordsend'),
    path('password-complete/', views.password_complete,name='passwordcomplete'),
    path('verify/<str:token>/', views.password_send, name='passwordcambiado')
]
