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
User = get_user_model()

def exito(request):
    trans = translate(language='es')
    return render(request, 'exito.html',{'trans': trans})

def cerrado(request):
    return render(request, 'cerrado.html')

#Renderizar el formulario.html(prueba)
def render_formulario(request):
    transe = translate(language='en')
    return render(request,'formulario.html',{'transe': transe})

# La funcion nos permite traducir el texto en pantalla
def translate(language):
    cur_languaje = get_language()
    try:
        activate(language)
        #prueba de traduccion
        text= gettext('Language')
    finally:
        activate(cur_languaje)
    return text     

# verifica que el form sea valido para despues enviarlo y envia
#un mensaje si se envio o no
def formulario_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se envió satisfactoriamente.')
            return render(request, 'exito.html')
        else:
            # Imprimir errores del formulario en la consola del servidor
            print(form.errors)

            # Manejar mensaje de error específico para el campo 'nombre'
            if 'nombre' in form.errors:
                messages.error(request, 'El nombre debe tener al menos 3 caracteres.')
            else:
                messages.error(request, 'Hubo un error en el formulario. Por favor, verifica los campos.')
    else:
        form = UsuarioForm()

    return render(request, 'formulario.html', {'form': form})

def prueba(request):
    return render('prueba.html')

def validar_nombre(request):
    
    nombre = request.GET.get('nombre', '')
    if len(nombre) < 3:
        return JsonResponse({'error': 'El nombre debe tener al menos 3 caracteress.'})
    return JsonResponse({'success': True})

def home(request):
    return render (request, 'home.html')

def formacion(request):
    return render(request,'activacion.html')
#Login
def inicio_sesion(request):#Funcion de inicio de sesion
    if request.user.is_authenticated:#nos aseguramos de que el usuario siempre tenga que iniciar sesion o la sesion no este iniciada
        logout(request)
        
    if request.method == 'GET':
        return render(request, 'inicio.html')
    else:
        user = authenticate(request, username=request.POST['Usuario'],password=request.POST['Contraseña'])
        if user is not None:
            return render(request, 'inicio.html',{
                    'error': 'Nombre de usuario o contraseña incorrectos'
                })
        else:
            login(request, user)
            return redirect('home')
   
def recuperar_pass(request ):
    if request.user.is_authenticated:#nos aseguramos de que el usuario siempre tenga que iniciar sesion o la sesion no este iniciada
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

def enviar_correo(destinatario,token):
    subject = "Token de Registro"
    message = f"Hola:\nTu código es: {token} \nÚsalo para acceder a tu cuenta.\nSi no solicitaste esto, simplemente ignora este mensaje.\nSaludos,\nEl equipo de ARV System Corp."
    from_email = settings.EMAIL_HOST_USER
    print(subject,message,from_email,destinatario)
    try:
        # Utiliza send_mail de Django para enviar el correo
        send_mail(subject, message, from_email, [destinatario], fail_silently=False)
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir al enviar el correo
        print(f"Error al enviar el correo: {e}")
       

def registro(request):#creo la funcion del registro
    if request.user.is_authenticated:#nos aseguramos de que el usuario siempre tenga que iniciar sesion o la sesion no este iniciada
        logout(request)
    #si el request es GET ose que necesita datos ingresados en la URL entonces renderiza la pagina
    if request.method == 'GET':
        return render(request, 'registro.html')
    else:#si es POST entonces compara las contraseñas ingresadas
        if request.POST['Contraseña'] == request.POST['Contraseña1']:
            #si las contraseñas son iguales entonces entra a el try
            try:
                validate_email(request.POST['Correo'])
                print(f'Email valido.')
                
                if User.objects.filter(email=request.POST['Correo']).exists():
                    return render(request, 'registro.html', {
                    'error': 'Este correo electrónico ya está registrado.'
                })
            except ValidationError:
                return render(request, 'registro.html', {
                    'error': 'Correo electrónico no válido'
                })
            try:#intentamos creal el usuario y guardarlo en los campos que le estamos dando
                user = User.objects.create_user(
                    username=request.POST['Usuario'], 
                    password=request.POST['Contraseña'],
                    email=request.POST['Correo']
                )
                #la funcion user.objects.create nos permite crear un usuario con username contraseña y email eliminamos el campo de email
                #Agregamos 2 datos mas que pedimos en el Registro nombre y apellido
                user.first_name = request.POST['Nombre']
                user.last_name = request.POST['Apellido']
                #guardamos los datos en la base de datos
                user.save()
                #creo una cookie de sesion para el usuario con login y tomo el valor ingresado e usuario
                #se utiliza para autenticar a un usuario en el sistema y establecer una sesión de usuario. 
                token = user.token_user
                enviar_correo(request.POST['Correo'],token)
                print(enviar_correo)
                
                # Agrega el token al contexto para mostrarlo en la plantilla (opcional)
                print(request.POST['Correo'],request.POST['Contraseña'],request.POST['Usuario'])
                return redirect('src_routes:activacion')
            except IntegrityError:#en tal caso el username ya este registrado en la bd le mostramos el error de nombre de usuario existente
                #e un except epecifico
                #renderizamos la pagina y mostramos el error
                return render(request, 'registro.html',{
                    'error': 'Nombre de usuario existente'
                })
        #si las contraseñas no coinciden entoces le mostramos el error al usuario         
        return render(request, 'registro.html',{
            'error': 'Las Contraseñas no coinciden'
        })
#datos introducidos son incorrectos
#me equivoque de correo

def validar_token(request):
    if request.method == 'GET':
        return render(request, 'activacion.html')
    else:
        token_ingresado = request.POST.get('token')
        try:
            user = User.objects.get(token_user=token_ingresado)
            print(f'este es el token del usuario: {user}')
            print(token_ingresado)
            if token_ingresado == user.token_user:
                # Obtenemos el nombre de usuario y contraseña del usuario asociado al token
                username = user.username
                password = user.password
                print(username,password)
                # Autenticar al usuario utilizando el nombre de usuario y la contraseña
                autenticacion = authenticate(request, username=username, password=password)
                print(f'esto es una autenticacion: {autenticacion}')
                try:
                    if autenticacion is None:
                        user.email_confirmed = True
                        user.save()
                        return render (request, 'registro_existoso.html')
                except Exception as e:
                        return render(request, 'activacion.html', {'error': f'Error al validar el token: {e}'})
            else:
                return render(request, 'activacion.html', {'error': f'Token no válido'})
        except User.DoesNotExist as e:
            return render(request, 'activacion.html', {'error': f'Usuario no encontrado: {e}'})
        except Exception as e:
            return render(request, 'activacion.html', {'error': f'Error al validar el token: {e}'})

def signout (request):
    logout(request)
    return redirect('inicio')
        
def succefully(request):
    return render (request, 'registro_existoso.html')