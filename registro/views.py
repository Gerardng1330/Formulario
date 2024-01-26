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
from .models import Profile  
import uuid
#hola



def registro (request):
    if request.method == 'POST' :
        username = request.POST.get('Usuario')
        email = request.POST.get('Correo')
        password = request.POST.get('Contraseña')

        try:
            if User.objects.filter(username = username).first():
              messages.success(request,'Nombre de usuario existente.')
              return redirect('/register')
        
            elif User.objects.filter(email = email).first():
              messages.success(request, 'Este correo electrónico ya está registrado')
              return redirect('/register')
        
            user_obj = User.objects.create(username = username, email=email)
            user_obj.set_password(password)

            profile_obj = Profile.objects.create(user = user_obj , token = str(uuid.uuid4))
            profile_obj.save()

            return redirect('/token')

        except Exception as e:
            print(e)

        
    return render(request , 'Register.html')


def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Tu cuenta ha sido registrada')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)


def error_page(request):
    return render(request, 'error.html')   


def send_mail_after_registration(email,token):
    subject = "Your account needs to be verified"
    message = f'Hi paste your link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list)
# Create your views here.

