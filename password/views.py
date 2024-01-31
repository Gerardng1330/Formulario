from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, views as auth_views
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
import random
import smtplib
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError

#GG

def recuperar_pass(request ):
    return render (request, 'recuperar.html')

def password_send(request):
    return render (request, 'password_send.html')

def password_cambiado(request):
    return render (request, 'password_cambiado.html')

def password_complete(request):
    return render (request, 'password_complete.html')

def password_email(request):
    return render (request, 'password_email.html')
def succefully(request):
    return render (request, 'registro_exitoso.html')
def generar_token():
    # Genera un token numérico de 6 dígitos
    return random.randint(100000, 999999)

def enviar_correo(destinatario, token):
    subject = "Token de Registro"
    message = f"Su token de veificacion es: {token}"
    from_email = settings.EMAIL_HOST_USER

    try:
        # Utiliza send_mail de Django para enviar el correo
        send_mail(subject, message, from_email, [destinatario], fail_silently=False)
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir al enviar el correo
        print(f"Error al enviar el correo: {e}")

def registro(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'GET':
        return render(request, 'registro.html')
    else:  # Si es POST, compara las contraseñas ingresadas
        try:
            contraseña = request.POST['Contraseña']
            contraseña1 = request.POST['Contraseña1']
        except MultiValueDictKeyError:
            return render(request, 'registro.html', {'error': 'Las contraseñas no se proporcionaron correctamente'})

        if contraseña == contraseña1:
            print(contraseña,'y',contraseña1)
            try:
                validate_email(request.POST['Correo'])

                if User.objects.filter(email=request.POST['Correo']).exists():
                    return render(request, 'registro.html', {'error': 'Este correo electrónico ya está registrado.'})
            except ValidationError:
                return render(request, 'registro.html', {'error': 'Correo electrónico no válido'})

            try:
                
                # Genera un token y lo envía por correo
                token = generar_token()
                enviar_correo(request.POST['Correo'], token)

                # Almacena el correo y token en la sesión para usarlo en la validación
                request.session['correo-registro'] = request.POST['Correo']
                request.session['token-registro'] = token
                request.session['usuario-registro']= request.POST['Usuario']
                request.session['contra-registro']= request.POST['Contraseña']
                request.session['nombre-registro']= request.POST['Nombre']
                request.session['apellido-registro']= request.POST['Apellido']



                # Agrega el token al contexto para mostrarlo en la plantilla (opcional)
                '''context = {'token': token}
                print(context)'''
                print(request.POST['Correo'],token,request.POST['Contraseña'],request.POST['Usuario'])
                return redirect('activacion')

            except IntegrityError:
                return render(request, 'registro.html', {'error': 'Nombre de usuario existente'})
        else:
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden'})



def validar_token(request):
    if request.method == 'GET':
        return render(request, 'activacion.html')
    else: 
        request.method == 'POST'
        token_ingresado = request.POST.get('token')
        print("Tipo de token_ingresado:", type(token_ingresado))
        try:
            # Verifica si el token es válido
            stored_token = request.session.get('token-registro')
            print("Tipo de stored_token:", type(stored_token),stored_token,token_ingresado)
            if token_ingresado == str(stored_token):
                # Obtén el correo electrónico almacenado en la sesión
                stored_email = request.session.get('correo-registro')
                usuario_guardado = (request.session.get('usuario-registro'))
                contra_guardado = (request.session.get('contra-registro'))
                nombre_guardado = (request.session.get('nombre-registro'))
                apellido_guardado = (request.session.get('apellido-registro'))
                print(nombre_guardado,apellido_guardado,stored_email,usuario_guardado,contra_guardado)
                # Verifica si el usuario ya existe en la base de datos
                if not request.user.is_authenticated:
                    if User.objects.filter(email=stored_email).exists():
                        user = authenticate(request, username=usuario_guardado)
                        login(request, user)
                
                try:
                    # Si el usuario no existe, crea un nuevo usuario y guárdalo en la base de datos
                    user = User.objects.create_user(
                        username=usuario_guardado,
                        password=contra_guardado,
                        email=stored_email
                    )
                    # Agregamos los datos adicionales al usuario
                    user.first_name = nombre_guardado
                    user.last_name = apellido_guardado
                    user.save()
                    
                    # Autentica al nuevo usuario
                    if not request.user.is_authenticated:
                        login(request, user)

                    return redirect('home')
                except IntegrityError:#en tal caso el username ya este registrado en la bd le mostramos el error de nombre de usuario existente
                #e un except epecifico
                #renderizamos la pagina y mostramos el error
                    return render(request, 'registro.html',{
                        'error': 'Nombre de usuario existente'
                    })
            else:
                # Si el token no es válido, muestra un mensaje de error
                return render(request, 'activacion.html', {'error': 'Token no válido'})
        except Exception as e:
            # Maneja cualquier otra excepción que pueda ocurrir
            print(f"Error al validar el token: {e}")
            return render(request, 'activacion.html', {'error': 'Error al validar el token'})
    # Si la solicitud no es de tipo POST, redirige a otra página o muestra un mensaje de error
    return redirect('inicio')

