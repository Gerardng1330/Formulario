from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.shortcuts import render, redirect
from backend.formularios.forms import UsuarioForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.http import HttpResponse
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
from django.contrib.auth.models import User
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
User = get_user_model()

def exito(request):
    return render(request, 'exito.html')

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

# verifica que el form sea valido para despues enviarlo y envia
#un mensaje si se envio o no
def formulario_view(request):
    # Variables de estado
    form_activo = True
    enviado_correctamente = False
    politicas_aceptadas = False
    politicas_aceptadas_uuid = None

    # Fetch a la BD. Párrafos de la tabla Politicas
    politicas_table = Politicas.objects.values('parrafo')

    # Verifica si 'politicas_aceptadas_cookie' existe
    if 'politicas_aceptadas_cookie' in request.COOKIES:
        # Quita el modal de políticas y no lo vuelve a mostrar (ver formulario.html)
        politicas_aceptadas = True
    else: 
        # Si no existe, genera un valor random para asignar a la cookie
        politicas_aceptadas_uuid = uuid.uuid4()

    # Verificar enviado_correctamente
    if request.method == 'POST' and form_activo:
        form = UsuarioForm(request.POST, request.FILES)
        print(request.POST) 
        if form.is_valid():
            form.save()
            #messages.success(request, 'El formulario se envió satisfactoriamente.')
            enviado_correctamente = True
            #return render(request, 'exito.html')
        else:
            # Imprimir errores del formulario en la consola del servidor
            print(form.errors)
            messages.error(request, 'Hubo un error en el formulario. Por favor, verifica los campos.')
    else:
        form = UsuarioForm()

    return render(request, 'formulario.html', {'form': form,'form_activo':form_activo,'enviado_correctamente':enviado_correctamente, 'politicas_table':politicas_table, 'politicas_aceptadas':politicas_aceptadas, 'politicas_aceptadas_uuid':politicas_aceptadas_uuid})

#prueba
def prueba(request):
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

@receiver(pre_save, sender=Usuario)
def normalize_fields(sender, instance, **kwargs):
    # Verifica si el campo 'nombre' existe y no es nulo
    print(f"Before normalization: {instance.apellido}")
    if hasattr(instance, 'nombre') and instance.nombre and instance.apellido :
        # Convierte el nombre a mayúsculas y luego aplica capitalización
        print(f"Nombre before normalization: {instance.nombre}")
        instance.nombre = capfirst(instance.nombre.lower())
        instance.apellido = capfirst(instance.apellido.lower())
        print(f"Ciudad after normalization: {instance.apellido}")

        print(f"Nombre after normalization: {instance.nombre}")
    # Verifica si el campo 'ciudad' existe y no es nulo
    




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
    try:
        # Busca al usuario con el token proporcionado en la base de datos.
        user = User.objects.get(token_user=token)
        
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


 # Esta vista renderiza la plantilla 'activacion.html'.
def activar_cuenta(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'GET':
        return render(request, 'activacion.html')
    elif request.method == 'POST':
        try:
            # Valida si el correo electrónico proporcionado es válido.
            validate_email(request.POST['Correo'])
        except ValidationError:
            return render(request, 'registro.html', {'error': 'Correo electrónico no válido'})
        
        correo = request.POST['Correo']
        
        # Verifica si el correo electrónico está asociado a una cuenta
        if User.objects.filter(email=correo).exists():
            # Genera un nuevo token
            token = generar_token()
            # Guarda el nuevo token en la base de datos
            usuario = User.objects.get(email=correo)
            usuario.token_user = token
            usuario.save()
            # Envía el correo electrónico con el nuevo token
            enviar_correo(correo, token)
            # Redirige a la página de aviso de reenvío de token
            return redirect('src_routes:aviso_reenvio_token')
        else:
            return render(request, 'registro.html', {'error': 'No se encontró ninguna cuenta asociada a este correo electrónico'})

def activars(request):
    return render(request, 'activacion_aviso.html')   

def signout (request):
    logout(request)
    return redirect('src_routes:inicio')
        
def succefully(request):
    return render (request, 'registro_existoso.html') 