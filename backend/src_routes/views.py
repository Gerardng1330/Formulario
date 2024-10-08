from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.shortcuts import render, redirect
from backend.formularios.forms import UsuarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
import time
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
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.utils.encoding import force_bytes   
import smtplib
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.core.mail import send_mail,BadHeaderError
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
#from backend.auth_users.forms import  PasswordChangingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.core.cache import cache
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.shortcuts import resolve_url
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps
#-----------
from django.shortcuts import render
from urllib.parse import urlparse

""" from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, AuthenticationForm """
User = get_user_model()

#Funcion para traducir las paginas

def verificar_correo(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Asegúrate de reemplazar 'email' con el nombre real del campo en tu formulario.
        print("Correo electrónico:", email)

        if Usuario.objects.filter(email=email).exists():
            print("Este correo electrónico ya está registrado.")
            return render(request, 'formulario.html', {'error': 'Este correo electrónico ya está registrado.'})

    # Resto de la lógica del formulario o redirección si no hay error
    return render(request, 'formulario.html', {})

        
# Función para obtener los correos registrados
def get_emails(request):
    if request.method == 'GET':
        app_name = request.GET.get('app')  # Obtener el nombre del modelo de la solicitud
        model_name = request.GET.get('model')  # Obtener el nombre del modelo de la solicitud
        model = apps.get_model(app_label=app_name, model_name=model_name) #Obtener el modelo con nombres de modelo y app
        emails_list = list(model.objects.values_list('email', flat=True)) #Busca la lista de emails en el la app y modelo que se le envió
        return JsonResponse(emails_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})

# Formulario. Verifica que el form sea valido para despues enviarlo y envia un mensaje si se envió o no
def formulario_view(request):
    url_para_traduccion = ''  # Asigna la URL por defecto
    
    # Variables de estado
    form_activo = True
    enviado_correctamente = False
    politicas_aceptadas = False

    # Variables que necesitan inicialización
    politicas_aceptadas_uuid = None
    is_email_registrado = None
    datos_formulario = {}  # Inicializa datos_formulario como un diccionario vacío

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
        nombre = request.POST.get('nombre')
        print(nombre)  
        form = UsuarioForm(request.POST, request.FILES)
        
        datos_formulario = {
            'nombre': nombre,
        }
        # Almacenar los datos del formulario en la sesión
        request.session['datos_formulario'] = datos_formulario

        if form.is_valid():
            # Obtiene el valor del campo email
            email_value = request.POST.get('email')

            # Verifica si el correo ya está registrado
            is_email_registrado = Usuario.objects.filter(email=email_value).exists()

            if not is_email_registrado:
                # El correo no está registrado, guarda el formulario.
                form.save()
                enviado_correctamente = True
                url_para_traduccion = 'formulario_enviado'  # Asigna la URL por defecto
                return render(request,'exito.html')
            
        else:
            # Si el formulario no es válido, imprime los errores
            print(form.errors)
            messages.error(request, 'Hubo un error en el formulario. Por favor, verifica los campos.')
    elif url_para_traduccion == 'formulario_enviado': # mejor verifica si es post 
        datos_formulario = request.session.get('datos_formulario', {})
        if datos_formulario:
            enviado_correctamente = True
        url_para_traduccion = 'formulario_enviado'
    else:
        form = UsuarioForm()
    return render(request, 'formulario.html', {'form': form,'form_activo':form_activo,'enviado_correctamente':enviado_correctamente, 'politicas_table':politicas_table, 'politicas_aceptadas':politicas_aceptadas, 'politicas_aceptadas_uuid':politicas_aceptadas_uuid, 'is_email_registrado':is_email_registrado, 'url_para_traduccion': url_para_traduccion,'datos_formulario':datos_formulario})

#Primera letra mayúscula a los campos de la bd.
@receiver(pre_save, sender=Usuario)
def normalize_fields(sender, instance, **kwargs):
    # Verifica si los campos existen y no son nulos
    fields_to_capitalize = ['nombre', 'apellido', 'alergia', 'nombre_contacto', 'direccion_principal', 'direccion_secundaria', 'ciudad', 'Estado_Provincia', 'referencia']

    for field in fields_to_capitalize:
        if hasattr(instance, field) and getattr(instance, field):
            # Aplica capitalización a cada palabra en el campo
            setattr(instance, field, getattr(instance, field).title())
            
#----------------------------fin de formulario -----------------------------------------------


def formacion(request):
    return render(request,'activacion_aviso.html')



#Login
def inicio_sesion(request):#Funcion de inicio de sesion
    url_para_traduccion = 'inicio/'
    if request.user.is_authenticated:#nos aseguramos de que el usuario siempre tenga que iniciar sesion o la sesion no este iniciada
        logout(request)
        
    if request.method == 'GET':
        return render(request, 'inicio.html',{'url_para_traduccion':url_para_traduccion})
    else:
        user = authenticate(request, username=request.POST['Usuario'],password=request.POST['Contraseña'])
        if user is None:
            return render(request, 'inicio.html',{
                    'error': 'Invalid username or password','url_para_traduccion':url_para_traduccion
                })
        else:
            login(request, user)
            return redirect('admin:index')
def home(request):
    return render (request, 'home.html')  
''' 
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
                })'''

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
    url_para_traduccion = 'registro'  # Asigna la URL por defecto
    
    # Verifica si el usuario está autenticado y lo desconecta si es así.
    if request.user.is_authenticated:
        logout(request)
    # Si la solicitud es GET, renderiza la plantilla 'registro.html'.
    # Si es POST, intenta registrar al usuario con los datos proporcionados.
    if request.method == 'GET':
        return render(request, 'registro.html',{'url_para_traduccion':url_para_traduccion})
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
    url = request.build_absolute_uri()
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')  # Dividir la ruta en partes usando '/'

    # Obtener la última parte de la ruta sin la barra inicial
    url_para_traduccion = path_parts[2]
    # Busca al usuario con el token proporcionado en la base de datos.
    try:
        user = User.objects.get(token_user=token)

        if user.email_confirmed == True:
            return render (request,'registro_exitoso.html',{'email_confirmed':user.email_confirmed,'error': f'Esta cuenta ya ha sido activada.'})
           # Si el token coincide, marca el correo electrónico como confirmado y redirige al usuario a la página de registro exitoso.
        if token == user.token_user:
            user.email_confirmed = True
            user.save()
            return redirect('src_routes:registro_exitoso')
        else:
            return render(request, 'activacion_aviso.html', {'error': 'Usuario no encontrado'})
    except User.DoesNotExist:
        print(f'paso aqui caducao')
        return render (request,'registro_exitoso.html', {'url_para_traduccion':url_para_traduccion,'noexiste':User.DoesNotExist,'error': 'Este Token ha caducado'})
    except Exception as e:
        return render(request, 'registro_exitoso.html', {'url_para_traduccion':url_para_traduccion,'error': f'Error al validar el token: {e}'}) 

 # Esta vista renderiza la plantilla 'activacion.html'.


def activar_cuenta(request):
    url_para_traduccion = 'activacion'  # Asigna la URL por defecto
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'GET':
        url_para_traduccion = 'activacion'  # Asigna la URL por defecto
        return render(request, 'activacion.html',{'url_para_traduccion':url_para_traduccion})
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
            return render(request, 'activacion.html', {'url_para_traduccion':url_para_traduccion,'error': 'No se encontró ninguna cuenta asociada a este correo electrónico'})

def activars(request):
    url_para_traduccion ='activacion_aviso'
    if request.method == 'GET':
        return render(request, 'activacion_aviso.html',{'url_para_traduccion':url_para_traduccion})
    elif request.method == 'POST':
    # zi no hay una llamada reciente, o si han pasado más de 60 segundos, continúa con la vista normalmente
        cache.set('activar_cuenta_ultima_llamada', timezone.now(), timeout=60)
        ultima_llamada = cache.get('activar_cuenta_ultima_llamada')
        if ultima_llamada is not None:
            tiempo_transcurrido = timezone.now() - ultima_llamada
            if tiempo_transcurrido.total_seconds() < 60:
                tiempo_restante = 60 - tiempo_transcurrido.total_seconds()
                return render(request, 'activacion_aviso.html', {'error': f'Solamente se puede enviar el token una vez por minuto. Espere {int(tiempo_restante)} segundos antes de intentarlo de nuevo.'})
        cache.set('activar_cuenta_ultima_llamada', timezone.now(), timeout=60)        
    return render(request, 'activacion_aviso.html')

def signout (request):
    logout(request)
    return redirect('src_routes:inicio')
        
def succefully(request):
    url_para_traduccion='registro_exitoso'
    return render (request, 'registro_exitoso.html',{'url_para_traduccion':url_para_traduccion})

def ayuda_view(request):
    url = request.build_absolute_uri()
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')  # Dividir la ruta en partes usando '/'

    # Obtener la última parte de la ruta sin la barra inicial
    url_para_traduccion = path_parts[2]  # Acceder a la parte que necesitas
    pathname = request.path[4:]
    politicas_table = Politicas.objects.values('parrafo')
    return render(request, 'ayuda.html', {'pathname': pathname,'url_para_traduccion': url_para_traduccion, 'politicas_table': politicas_table})

#def password_reset_request(request):
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = "Recuperacion de Contraseña"
                    email_template= 'mensaje_envio.html'
                    parameters = {
                        'email': user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'F2F',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email= render_to_string(email_template,parameters)
                    try:
                        send_mail(subject, email, 'noreply@arvcloud.com', [user.email], fail_silently=False)
                        print(f'paso por aqui')
                        return redirect('src_routes:recuperar_aviso')
                    except Exception as e:
                        print("Error al enviar el correo electrónico:", e)
                        return HttpResponse('Error al enviar el correo electrónico: {}'.format(e))
            else:
               return render(request, 'recuperar.html', {'error': 'No se encontró ninguna cuenta asociada a este correo electrónico'})

    else:
        password_form = PasswordResetForm()
    context = { 
        'password_form': password_form,
            
    }
    return render(request, 'recuperar.html',context)



def recuperar_aviso_view(request):
    url_para_traduccion = 'adminpaneldjango/accounts/password-reset-done/'
    return render (request, 'recuperar_aviso.html',{'url_para_traduccion':url_para_traduccion})