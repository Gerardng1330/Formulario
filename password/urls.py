from django.urls import path
from . import views

urlpatterns  = [
    path('recuperar/', views.recuperar_pass,name='recuperar'),    
    #path('registro/', views.registro, name='registro'),
    path('validar-token/', views.validar_token, name='validartoken'),
    path('succefully/', views.succefully, name= 'succefully'),
    path('password-email/', views.password_email,name='passwordemail'),
    path('password-send/', views.password_send,name='passwordsend'),
    path('password-complete/', views.password_complete,name='passwordcomplete'),
    path('verify/<str:token>/', views.password_send, name='passwordcambiado'),
    
]
#si a la url del main le pongo un prefijo ya sea home/ le tengo que poner eso
#a todas las urls que agregue en cualquier aplicacion