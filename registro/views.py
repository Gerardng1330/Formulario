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
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
import random
import smtplib
import uuid
from .models import Profile

def success(request):
    return render(request, 'success.html')

def send_token(request):
    return render(request, 'send_token.html')

def registros(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        username = request.POST['Usuario']
        password = request.POST['Contraseña']
        email = request.POST['Correo']

        try:
            if User.objects.filter(username=username).first():
                return redirect('/registro1', {'error': 'Nombre de usuario existente'})

            elif User.objects.filter(email=email).first():
                return redirect('/registro1', {'error': 'Este correo electrónico ya está registrado.'})

            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)

            profile_obj = Profile.objects.create(user=user_obj, token=str(uuid.uuid4))
            profile_obj.save()

            send_mail_after_registration(email, profile_obj.token)

            return redirect(reverse('send_token'))

        except IntegrityError:
            return redirect('/registro1', {'error': 'Error de integridad al crear usuario'})

        except ValidationError:
            return redirect('/registro1', {'error': 'Error de validación al crear usuario'})

    return render(request, 'registro1.html')

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            return redirect('/inicio', {'error': 'Tu cuenta ha sido verificada'})
        else:
            return redirect('/error')
    except Exception as e:
        print(e)

def error_page(request):
    return render(request, 'error.html')

def send_mail_after_registration(email, token):
    subject = "Tu cuenta necesita ser verificada"
    message = f'Hola, pega este enlace para verificar tu cuenta: http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def registros(request):
    # Verifica si el usuario ya ha iniciado sesión y, en caso afirmativo, lo desconecta.
    if request.user.is_authenticated:
        logout(request)
    
    # Verifica si la solicitud es de tipo POST (es decir, se ha enviado un formulario).
    if request.method == 'POST':
        # Obtiene los datos del formulario (nombre de usuario, contraseña y correo electrónico).
        username = request.POST['Usuario']
        password = request.POST['Contraseña']
        email = request.POST['Correo']

        try:
            # Verifica si ya existe un usuario con el mismo nombre de usuario.
            if User.objects.filter(username=username).first():
                # Redirige a la página de registro con un mensaje de error.
                return redirect('/registro1', {'error': 'Nombre de usuario existente'})

            # Verifica si ya existe un usuario con el mismo correo electrónico.
            elif User.objects.filter(email=email).first():
                # Redirige a la página de registro con un mensaje de error.
                return render(request, 'registro1.html', {
                    'error': 'Este correo electrónico ya está registrado.'
                })

            # Crea un nuevo objeto de usuario y lo guarda en la base de datos.
            user_obj = User.objects.create(username=username, email=email)
            # Establece la contraseña del usuario.
            user_obj.set_password(password)

            # Crea un objeto de perfil asociado al usuario y le asigna un token único.
            profile_obj = Profile.objects.create(user=user_obj, token=str(uuid.uuid4))
            profile_obj.save()

            # Envía un correo electrónico para verificar la cuenta del usuario.
            send_mail_after_registration(email, profile_obj.token)

            # Redirige a la página para enviar el token de verificación.
            return redirect('send-token')

        except IntegrityError:
            # Redirige a la página de registro con un mensaje de error.
            return render('registro1.html', {'error': 'Error de integridad al crear usuario'})

        except ValidationError:
            # Redirige a la página de registro con un mensaje de error.
            return render('registro1.html', {'error': 'Error de validación al crear usuario'})

    # Si la solicitud no es de tipo POST, renderiza la página de registro.
    return render(request, 'registro1.html')
