from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from backend.auth_users.forms import change_password_form
""" Para servir archivos estáticos en desarrollo """
from django.conf import settings
from django.conf.urls.static import static

app_name = 'src_routes'

urlpatterns = [
    #Formularios
    path('', views.formulario_view,name='ver_formulario'),
    path('formulario_enviado/', views.formulario_view, name='envio_formulario'),
    path('obtener_emails/', views.get_emails, name='get_emails'),    

    # Login views
    path('home/', views.home,name='home'),
    path('inicio/', views.inicio_sesion,name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('logout/',views.signout, name='logout'),
    path('form/', views.formacion,name='form'),
    
    #Activacion de Token
    path('activacion/', views.activar_cuenta, name='activacion'),
    path('activacion_aviso/', views.activars, name='activacion_aviso'),
    path('activar-cuenta/<str:token>/', views.validar_token, name='activar_cuenta'),
    path('registro_exitoso/', views.succefully, name='registro_exitoso'),

    #Ayuda
    path('ayuda_contrasena/', views.ayuda_view , name='ayuda_contrasena'),
    path('proteccion_datos/', views.ayuda_view , name='proteccion_datos'),
    path('politica_actualizacion/', views.ayuda_view , name='politica_actualizacion'),
    path('terminos_actualizacion/', views.ayuda_view , name='terminos_actualizacion'),
    path('cuentas_inactivas/', views.ayuda_view , name='cuentas_inactivas'),
    path('tiempo_almacenamiento/', views.ayuda_view , name='tiempo_almacenamiento'),
    path('copia_datos/', views.ayuda_view , name='copia_datos'),
    path('derechos_autor/', views.ayuda_view , name='derechos_autor'),
    path('servicios_de_pago/', views.ayuda_view , name='servicios_de_pago'),
    path('empresas_relacionadas/', views.ayuda_view , name='empresas_relacionadas'),
    path('reembolso/', views.ayuda_view , name='reembolso'),
    
    # forgot password views
    path('recuperar/', auth_views.PasswordResetView.as_view(html_email_template_name='mail_template.html', template_name = 'recuperar.html'), name='recuperar'), #pantalla donde se ingresa el email para reestablecer contraseña
    #pantalla de correo enviado está en templates/accounts/password_reset_done.html
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),#pantalla donde se cambia las contraseñas
    #pantalla de contraseña cambiada con éxito está en templates/accounts/password_reset_complete.html
]

#ruta para descargar el cv 
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    #No hacer esto en producción. Esto es solo para el manejo local de archivos estáticos.
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
