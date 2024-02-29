# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from backend.formularios.models import Usuario

#panel de django
class usuarioInfo(admin.ModelAdmin):
    #campos a mostrar
    list_display=("nombre","apellido","email","fecha_nacimiento","nacionalidad","Telefono1","Cargo1")
    #buscar los capos
    search_fields=("nombre","nacionalidad")
    #filtrar los campos
    list_filter=("nombre","fecha_nacimiento",)
    #filtrar las fechas
    date_hierarchy = "fecha_nacimiento"



# Registramps el modelo de usuario personalizado
admin.site.register(User, UserAdmin)
admin.site.register(Usuario,usuarioInfo)





