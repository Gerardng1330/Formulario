# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from backend.formularios.models import Usuario
from django.http import HttpResponse

from django.urls import path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape
from reportlab.platypus import Table, TableStyle,SimpleDocTemplate
from reportlab.lib import colors
from django.utils.html import format_html
from django.urls import reverse


#panel de django
class UsuarioInfo(admin.ModelAdmin):
    #muestra los campos en el panel
    list_display = ("nombre", "apellido", "email", "fecha_nacimiento", "nacionalidad", "Telefono1", "Cargo1","cv_file","id_file")
    # los campos de busqueda
    search_fields = ("nombre", "nacionalidad")
    #filtro 
    list_filter = ("nombre", "fecha_nacimiento",)
    #que aparezca la fecha con su jerarquia
    date_hierarchy = "fecha_nacimiento"
    
    actions = ['download_pdf']

    
    #descargar la informacion de los usuarios
    def download_pdf(self, request, queryset):
        model_name = self.model.__name__
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={model_name}.pdf'

        pdf = SimpleDocTemplate(response, pagesize=landscape(letter))
        elements = []

        header = [self.model._meta.get_field(field).verbose_name for field in self.list_display]
        data = [header]

        for obj in queryset:
            data_row = [str(getattr(obj, field)) for field in self.list_display]
            data.append(data_row)

        style = TableStyle(
            [
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ]
        )

        table = Table(data)
        table.setStyle(style)
        elements.append(table)

        pdf.build(elements)
        return response

    def get_urls(self):
        urls = super().get_urls()
        return [
            path('download-pdf/', self.admin_site.admin_view(self.download_pdf), name='app_label_usuario_download_pdf')
        ] + urls




# Registramps el modelo de usuario personalizado
admin.site.register(User, UserAdmin)
admin.site.register(Usuario,UsuarioInfo)





