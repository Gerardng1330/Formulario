# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from backend.formularios.models import Usuario

class usuarioInfo(admin.ModelAdmin):
    list_display=("nombre","apellido","email","fecha_nacimiento","nacionalidad","Telefono1","Cargo1")
    search_fields=("nombre","nacionalidad")
    list_filter=("nombre","fecha_nacimiento",)
    date_hierarchy = "fecha_nacimiento"



# Registra tu modelo de usuario personalizado
admin.site.register(User, UserAdmin)
admin.site.register(Usuario,usuarioInfo)





