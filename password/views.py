from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
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
from django.contrib.auth import get_user_model

User = get_user_model()
#GG

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
        
        
def password_send(request):
    return render (request, 'password_send.html')

def password_cambiado(request):
    return render (request, 'password_cambiado.html')

def password_complete(request):
    return render (request, 'password_complete.html')

def password_email(request):
    return render (request, 'password_email.html')
def succefully(request):
    return render (request, 'registro_existoso.html')

'''def generar_token():
    # Genera un token numérico de 6 dígitos
    return random.randint(100000, 999999)

def enviar_correo(destinatario, token):
    subject = "Token de Registro"
    message = f"Su token de veificacion es: {token}"
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

                #guardamos los datos en la base de datos}
                user.is_active = False
                
                user.save()
            
                
                # Genera un token y lo envía por correo
                token = generar_token()
                enviar_correo(request.POST['Correo'], token)
                print(enviar_correo)

                # Almacena el correo y token en la sesión para usarlo en la validación
                request.session['correo-registro'] = request.POST['Correo']
                request.session['token-registro'] = token
                request.session['usuario-registro']= request.POST['Usuario']
                request.session['contra-registro']= request.POST['Contraseña']
                request.session['nombre-registro']= request.POST['Nombre']
                request.session['apellido-registro']= request.POST['Apellido']
                # Agrega el token al contexto para mostrarlo en la plantilla (opcional)
                print(request.POST['Correo'],token,request.POST['Contraseña'],request.POST['Usuario'])
                return redirect('activacion')

            except IntegrityError:
                return render(request, 'registro.html', {'error': 'Nombre de usuario no es válido.'})
        else:
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden'})

#datos introducidos son incorrectos
#me equivoque de correo'''

def validar_token(request):
    if request.method == 'GET':
        return render(request, 'activacion.html')
    else: 
        request.method == 'POST'
        token_ingresado = request.POST.get('token')
        
        try:
            # Verifica si el token es válido
            stored_token = request.session.get('token-registro')
            
            if token_ingresado == str(stored_token):
                print("Tipo de stored_token:", type(stored_token),stored_token,token_ingresado)
                # Obtén el correo electrónico almacenado en la sesión
                stored_email = request.session.get('correo-registro')
                usuario_guardado = (request.session.get('usuario-registro'))
                contra_guardado = (request.session.get('contra-registro'))
                nombre_guardado = (request.session.get('nombre-registro'))
                apellido_guardado = (request.session.get('apellido-registro'))
                print(nombre_guardado,apellido_guardado,stored_email,usuario_guardado,contra_guardado)
                # Verifica si el usuario ya existe en la base de datos
                try:
                    if not request.user.is_authenticated:
                        if User.objects.filter(email=stored_email).exists():
                            user = authenticate(request, username=usuario_guardado) 
                            if user is None:
                                print(user)
                                return render(request, 'activacion.html', {'error': 'Error al validar el token'})
                            else:
                                return redirect('succefully')
                    #Si el usuario no existe, crea un nuevo usuario y guárdalo en la base de datos
                    else:
                        print(f'algo')
                        #Autentica al nuevo usuario
                except IntegrityError:#en tal caso el username ya este registrado en la bd le mostramos el error de nombre de usuario existente
                #e un except epecifico
                #renderizamos la pagina y mostramos el error
                    return render(request, 'registro.html',{
                        'error': 'El nombre de usuario no es válido.'
                    })
            else:
                # Si el token no es válido, muestra un mensaje de error
                return render(request, 'activacion.html', {'error': 'Token no válido'})
        except Exception as e:
            # Maneja cualquier otra excepción que pueda ocurrir
            print(f"Error al validar el token: {e}")
            return render(request, 'activacion.html', {'error': 'Error al validar el token'})
    # Si la solicitud no es de tipo POST, redirige a otra página o muestra un mensaje de error
    

