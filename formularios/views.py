from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext
from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UsuarioForm
from django.http import JsonResponse
#Renderizar el formulario.html
def home(request):
    #trans es la palabra clave para asignarle la traduccion
    trans = translate(language='es')
    return render(request,'formulario.html',{'trans': trans})

#Renderizar el exti.html(prueba)

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

