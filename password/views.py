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
import random
import smtplib



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
        return render(request, 'Register.html')
    else:#si es POST entonces compara las contraseñas ingresadas
        if request.POST['Contraseña'] == request.POST['Contraseña1']:
            #si las contraseñas son iguales entonces entra a el try
            try:
                validate_email(request.POST['Correo'])

                if User.objects.filter(email=request.POST['Correo']).exists():
                    return render(request, 'Register.html', {
                        'error': 'Este correo electrónico ya está registrado.'
                    })
            except ValidationError:
                return render(request, 'Register.html', {
                    'error': 'Correo electrónico no válido'
                })

            try:
                # Genera un token y lo envía por correo
                token = generar_token()
                enviar_correo(request.POST['Correo'], token)

                # Almacena el correo y token en la sesión para usarlo en la validación
                request.session['user_email'] = request.POST['Correo']
                request.session['registration_token'] = token

                # Agrega el token al contexto para mostrarlo en la plantilla (opcional)
                context = {'token': token}
                return render(request, 'password_send.html', context)   

            except IntegrityError:
                return render(request, 'Register.html',{
                    'error': 'Nombre de usuario existente'
                })
        else:
            return render(request, 'Register.html', {
                'error': 'Las Contraseñas no coinciden'
            })


def validar_token(request):
    if request.method == 'GET':
        return render(request, 'validar_token.html')
    if request.method == 'POST':
        token_ingresado = request.POST.get('token')
        correo_ingresado = request.POST.get('Correo')

        try:
            # Verifica si el token es válido y si coincide con el correo proporcionado
            stored_email = request.session.get('user_email')
            stored_token = request.session.get('registration_token')

            if correo_ingresado == stored_email and token_ingresado == stored_token:
                # Autentica al usuario
                user = authenticate(request, username=stored_email, password=request.POST.get('Contraseña'))
                
                if user is not None:
                    # Loguea al usuario
                    login(request, user)
                    return redirect('registro_exitoso')
                else:
                    # Si el usuario no pudo ser autenticado, muestra un mensaje de error
                    return render(request, 'validar_token.html', {'error': 'Error al autenticar al usuario'})
            else:
                # Si el token no es válido, muestra un mensaje de error
                return render(request, 'validar_token.html', {'error': 'Token no válido'})
        except Exception as e:
            # Maneja cualquier otra excepción que pueda ocurrir
            print(f"Error al validar el token: {e}")
            return render(request, 'validar_token.html', {'error': 'Error al validar el token'})

    # Si la solicitud no es de tipo POST, redirige a otra página o muestra un mensaje de error
    return redirect('login')

