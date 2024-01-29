from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import views as auth_views

def home(request ):
    return render (request, 'home.html')

def formacion(request):
    return render(request,'formulario.html')


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
            return redirect('home')
    
    
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

                #guardamos los datos en la base de datos
                user.save()
                #creo una cookie de sesion para el usuario con login y tomo el valor ingresado e usuario
                #se utiliza para autenticar a un usuario en el sistema y establecer una sesión de usuario. 
                login(request, user)
                #redirecciono a la pantalla de login una vez pasa por el return no sigue el codigo hacia abajo
                return redirect('home')
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
        
def signout (request):
    logout(request)
    return redirect('inicio')    




