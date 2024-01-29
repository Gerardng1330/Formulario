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
