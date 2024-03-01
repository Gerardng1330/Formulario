from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.shortcuts import render, redirect
from backend.formularios.forms import UsuarioForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import login, logout, authenticate, views as auth_views
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
import random
from django.http import JsonResponse
import smtplib
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.core.mail import send_mail
import datetime
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import uuid
from backend.formularios.models import Politicas
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import capfirst
from backend.formularios.models import Usuario
from django.core.cache import cache
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
User = get_user_model()

def cerrado(request):
    return render(request, 'cerrado.html')

def prueba_page(request):
    return render(request,'pruebaPagina.html')

#Renderizar el formulario.html(prueba)
def render_formulario(request):
    return render(request,'formulario.html')

#Funcion para traducir las paginas
def traducir_paginas(request):
    #verifica el path para hacer la traducir la pagina correspondidad
    current_path = request.path
    if current_path == '/formulario_enviado/':
        url_para_traduccion = '/formulario_enviado/'
    elif current_path == '/prueba/':
        url_para_traduccion = '/prueba/'
    else:
        url_para_traduccion = '/'  # Otra opción por defecto

    return render(request, 'formulario.html', {'url_para_traduccion': url_para_traduccion})

# Función para obtener los correos registrados
def get_emails(request):
    if request.method == 'GET':
        emails_list = list(Usuario.objects.values_list('email', flat=True))
        return JsonResponse(emails_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})

# Formulario. Verifica que el form sea valido para despues enviarlo y envia un mensaje si se envió o no
def formulario_view(request):
    # Variables de estado
    form_activo = True
    enviado_correctamente = False
    politicas_aceptadas = False

    # Variables que necesitan inicialización
    politicas_aceptadas_uuid = None

    # Fetch a la BD. Párrafos de la tabla Politicas
    politicas_table = Politicas.objects.values('parrafo')

    # Verifica si 'politicas_aceptadas_cookie' existe
    if 'pltc' in request.COOKIES:
        # Quita el modal de políticas y no lo vuelve a mostrar (ver formulario.html)
        politicas_aceptadas = True
    else: 
        # Si no existe, genera un valor random para asignar a la cookie
        politicas_aceptadas_uuid = uuid.uuid4()

    # Verificar enviado_correctamente
    if request.method == 'POST' and form_activo:
        form = UsuarioForm(request.POST, request.FILES)
        #print(request.POST)
        
        if form.is_valid():
            # Obtiene el valor del campo email
            email_value = request.POST.get('email')

            # Verifica si el correo ya está registrado
            is_email_registrado = Usuario.objects.filter(email=email_value).exists()

            if not is_email_registrado:
                # El correo no está registrado, guarda el formulario.
                form.save()
                enviado_correctamente = True
        else:
            # Imprimir errores del formulario en la consola del servidor
            print(form.errors)
            messages.error(request, 'Hubo un error en el formulario. Por favor, verifica los campos.')
    else:
        form = UsuarioForm()

    return render(request, 'formulario.html', {'form': form,'form_activo':form_activo,'enviado_correctamente':enviado_correctamente, 'politicas_table':politicas_table, 'politicas_aceptadas':politicas_aceptadas, 'politicas_aceptadas_uuid':politicas_aceptadas_uuid, 'is_email_registrado':is_email_registrado})

#prueba
# def prueba(request):
    formulario_activo = True  # Puedes ajustar esta lógica según tus necesidades
    enviado_correctamente = False

    if request.method == 'POST' and formulario_activo:
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            enviado_correctamente = True

            messages.success(request, 'El formulario se envió satisfactoriamente.')
            return redirect('exito')  # Redirigir a la página de éxito (ajusta la URL según tu configuración)
        else:
            print(form.errors)
            messages.error(request, 'Hubo un error en el formulario. Por favor, verifica los campos.')

    else:
        form = UsuarioForm()

    return render(request, 'pruebaPagina.html', {'form': form, 'formulario_activo': formulario_activo,'enviado_correctamente':enviado_correctamente})

#Primera letra mayúscula a los campos de la bd.
@receiver(pre_save, sender=Usuario)
def normalize_fields(sender, instance, **kwargs):
    # Verifica si los campos existen y no son nulos
    fields_to_capitalize = ['nombre', 'apellido', 'alergia', 'nombre_contacto', 'direccion_principal', 'direccion_secundaria', 'ciudad', 'Estado_Provincia', 'referencia']

    for field in fields_to_capitalize:
        if hasattr(instance, field) and getattr(instance, field):
            # Aplica capitalización a cada palabra en el campo
            setattr(instance, field, getattr(instance, field).title())


        
def validar_nombre(request):
    
    nombre = request.GET.get('nombre', '')
    if len(nombre) < 3:
        return JsonResponse({'error': 'El nombre debe tener al menos 3 caracteress.'})
    return JsonResponse({'success': True})


def formacion(request):
    return render(request,'activacion_aviso.html')



#Login
def inicio_sesion(request):#Funcion de inicio de sesion
    if request.user.is_authenticated:#nos aseguramos de que el usuario siempre tenga que iniciar sesion o la sesion no este iniciada
        logout(request)
        
    if request.method == 'GET':
        return render(request, 'inicio.html')
    else:
        user = authenticate(request, username=request.POST['Usuario'],password=request.POST['Contraseña'])
        if user is None:
            return render(request, 'inicio.html',{
                    'error': 'Nombre de usuario o contraseña incorrectos'
                })
        else:
            login(request, user)
            return redirect('src_routes:home')
def home(request):
    return render (request, 'home.html')  
 
def recuperar_pass(request):
    # Funcion para recuperar la contraseña
    # Nos aseguramos de que el usuario siempre tenga que iniciar sesion o la sesion no este iniciada
    if request.user.is_authenticated:
        logout(request)
        
    if request.method == 'GET':
        return render(request, 'recuperar.html')
    else:
        user = authenticate(request, email=request.POST['Correo'])
        print(request.POST['Correo'])
        if user is None:
            return render(request, 'recuperar.html',{
                    'error': 'Este Correo electrónico no es válido'
                })

def generar_token():
    # Funcion para generar un token
    return uuid.uuid4().hex

def enviar_correo(destinatario, token):
    # Funcion para enviar un correo electrónico
    link_activacion = f"http://127.0.0.1:8000/activar-cuenta/{token}/"
    subject = "Token de Registro"
    message = f"Hola:\nhaz click en el siguiente enlace: {link_activacion} \nÚsalo para acceder a tu cuenta.\nSi no solicitaste esto, simplemente ignora este mensaje.\nSaludos,\nEl equipo de ARV System Corp."
    from_email = settings.EMAIL_HOST_USER
    print(f'{subject},\n {message},\n {from_email},\n{destinatario},\n{token},\n{link_activacion}')
    try:
        # Utiliza send_mail de Django para enviar el correo
        send_mail(subject, message, from_email, [destinatario], fail_silently=False)
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir al enviar el correo
        print(f"Error al enviar el correo: {e}")
        
# Esta vista maneja el registro de usuarios.
def registro(request):
    # Verifica si el usuario está autenticado y lo desconecta si es así.
    if request.user.is_authenticated:
        logout(request)
    # Si la solicitud es GET, renderiza la plantilla 'registro.html'.
    # Si es POST, intenta registrar al usuario con los datos proporcionados.
    if request.method == 'GET':
        return render(request, 'registro.html')
    elif request.method == 'POST':
        # Comprueba si las contraseñas coinciden.
        if request.POST['Contraseña'] != request.POST['Contraseña1']:
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden'})
        try:
            # Valida si el correo electrónico proporcionado es válido.
            validate_email(request.POST['Correo'])
            
            # Verifica si ya existe un usuario con el correo electrónico proporcionado.
            if User.objects.filter(email=request.POST['Correo']).exists():
                return render(request, 'registro.html', {'error': 'Este correo electrónico ya está registrado.'})
        except ValidationError:
            return render(request, 'registro.html', {'error': 'Correo electrónico no válido'})
        try:
            # Genera un token, crea un nuevo usuario con los datos proporcionados y guarda el token en la base de datos.
            token = generar_token()
            user = User.objects.create_user(
                username=request.POST['Usuario'],
                password=request.POST['Contraseña'],
                email=request.POST['Correo']
            )
            user.first_name = request.POST['Nombre']
            user.last_name = request.POST['Apellido']
            user.token_user = token
            user.save()
            # Envía un correo electrónico de activación al usuario con el token generado.
            enviar_correo(request.POST['Correo'], token)  # Corregir aquí, pasando el destinatario y el token
            
            # Redirige al usuario a la página de activación.
            return redirect('src_routes:activacion_aviso')
        except IntegrityError:
            return render(request, 'registro.html', {'error': 'Nombre de usuario existente'})
        
# Esta vista valida el token de activación proporcionado por el usuario.
def validar_token(request, token):
    # Busca al usuario con el token proporcionado en la base de datos.
    user = User.objects.get(token_user=token)
    try:
        if user.token_user == None:
            return render (request,'registro_existoso.html',{'email_confirmed':user.email_confirmed,'error': f'Este Token ya ha caducado.'})
        if user.email_confirmed == True:
            return render (request,'registro_existoso.html',{'email_confirmed':user.email_confirmed,'error': f'Este Token ya ha sido utilizado.'})
        try:
                # Si el token coincide, marca el correo electrónico como confirmado y redirige al usuario a la página de registro exitoso.
            if token == user.token_user:
                user.email_confirmed = True
                user.save()
                return redirect('src_routes:registro_exitoso')
            else:
                return render(request, 'activacion_aviso.html', {'error': 'Token no válido'})
        except User.DoesNotExist:
                return render(request, 'activacion_aviso.html', {'error': 'Usuario no encontrado'})
        except Exception as e:
                return render(request, 'activacion_aviso.html', {'error': f'Error al validar el token: {e}'})
    except Exception as e:
            return render(request, 'activacion_aviso.html', {'error': f'Error al validar el token: {e}'}) 

 # Esta vista renderiza la plantilla 'activacion.html'.


def activar_cuenta(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'GET':
        return render(request, 'activacion.html')
    elif request.method == 'POST':
        # Verifica si la función se ha llamado recientemente
        ultima_llamada = cache.get('activar_cuenta_ultima_llamada')
        if ultima_llamada is not None:
            tiempo_transcurrido = timezone.now() - ultima_llamada
            if tiempo_transcurrido.total_seconds() < 60:
                return render(request, 'activacion.html', {'error': 'Solamente se puede enviar el token una vez por minuto. Por favor, inténtelo de nuevo más tarde.'})
        correo = request.POST.get('Correo')
        try:
            # Valida si el correo electrónico proporcionado es válido.
            validate_email(correo)
        except ValidationError:
            return render(request, 'activacion.html', {'error': 'Correo electrónico no válido'})
        
        try:
            # Verifica si el correo electrónico está asociado a una cuenta
            usuario = User.objects.get(email=correo)
            # Genera un nuevo token
            User.limpiar_tokens()
            token = generar_token()
            # Guarda el nuevo token en la base de datos
            usuario.token_user = token
            usuario.save()
            # Envía el correo electrónico con el nuevo token
            enviar_correo(correo, token)
            # Guarda la marca de tiempo de la última llamada
            cache.set('activar_cuenta_ultima_llamada', timezone.now(), timeout=60)  # Guarda la marca de tiempo durante 60 segundos
            # Redirige a la página de aviso de reenvío de token
            return redirect('src_routes:activacion_aviso')
        except User.DoesNotExist:
            return render(request, 'activacion.html', {'error': 'No se encontró ninguna cuenta asociada a este correo electrónico'})

def activars(request):
    return render(request, 'activacion_aviso.html')   

def signout (request):
    logout(request)
    return redirect('src_routes:inicio')
        
def succefully(request):
    return render (request, 'registro_existoso.html') 