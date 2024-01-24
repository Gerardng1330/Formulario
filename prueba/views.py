from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request ):
    return render (request, 'home.html')

def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'Login.html')
    else:
        print(f'Obteniendo datos')

        
    return render(request, 'Login.html')
def registro(request):
    if request.method == 'GET':
        return render(request, 'Register.html')
    else:
        if request.POST['Contraseña'] == request.POST['Contraseña1']:
            try:
                user = User.objects.create_user(
                    username=request.POST['Usuario'], 
                    password=request.POST['Contraseña']
                )

                # Puedes agregar más campos al usuario si es necesario
                user.first_name = request.POST['Nombre']
                user.last_name = request.POST['Apellido']
                
                user.save()
                
                return render(request, 'Register.html',{
                    'error': 'Las Contrseñas no coinciden'
                })
            except:
                return HttpResponse(f'Este nombre de usuario ya existe')

        return render(request, 'Register.html',{
            'error': 'Las Contrseñas no coinciden'
        })
            


def prueba(request):
    
    return render(request, 'muestra.html',{
        'form':UserCreationForm
        })
    

def muestra(request):
    print(request.POST)
    return render(request, 'muestra.html')