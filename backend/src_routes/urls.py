from django.urls import path
from . import views
""" Para servir archivos estáticos en desarrollo """
from django.conf import settings
from django.conf.urls.static import static

app_name = 'src_routes'

urlpatterns = [
    #Formularios
    path('', views.formulario_view, name='ver_formulario'),
    #path('formulario/', views.render_formulario, name='ver_formulario'),
    path('formulario_enviado/', views.formulario_view, name='envio_formulario'),#prueba
    #path('exito/', views.exito, name='pagina_exito'),
    path('cerrado/', views.cerrado, name='pagina_cerrado}'),
    path('prueba/', views.prueba_page, name='pagina_prueba'),
    path('obtener_emails/', views.get_emails, name='get_emails'),

    # Login views
    path('home/', views.home,name='home'),
    path('inicio/', views.inicio_sesion,name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('logout/',views.signout, name='logout'),
    path('form/', views.formacion,name='form'),
    
    #Recuperacion de usuario
    path('recuperar/', views.recuperar_pass,name='recuperar'),    
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
]

if settings.DEBUG:
    #No hacer esto en producción. Esto es solo para el manejo local de archivos estáticos.
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
