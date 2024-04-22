from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from backend.formularios.models import Usuario
from django.http import HttpResponse
from django.urls import path
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from django.utils.translation import gettext_lazy as _
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter, landscape, legal


class UsuarioInfo(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "fecha_nacimiento", "nacionalidad", "Telefono1", "Cargo1","cv_file","id_file")
    search_fields = ("nombre", "nacionalidad")
    list_filter = ("nombre", "fecha_nacimiento",)
    date_hierarchy = "fecha_nacimiento"

    actions = ['download_pdf']

    def download_pdf_dropdown(self, request, queryset):
        model_name = self.model.__name__
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={model_name}.pdf'

        pdf = SimpleDocTemplate(response, pagesize=landscape(legal))
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

    def get_urls_dropdown(self):
        urls = super().get_urls()
        return [
            path('download-pdf-dropdown/', self.admin_site.admin_view(self.download_pdf_dropdown), name='app_label_usuario_download_pdf_dropdown')
        ] + urls
    
    def download_pdf(self, request):
        queryset = self.get_queryset(request)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=Usuario.pdf'

        doc = SimpleDocTemplate(response, pagesize=landscape(legal))
        elements = []

        data = [["nombre", "apellido", "email", "fecha_nacimiento", "nacionalidad", "Telefono1", "Cargo1","cv_file","id_file"]]
        for usuario in queryset:
            data.append([usuario.nombre, usuario.apellido,usuario.email,usuario.fecha_nacimiento,usuario.nacionalidad,usuario.Telefono1,usuario.Cargo1,usuario.cv_file,usuario.id_file])

        usuario_table = Table(data)
        usuario_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ]))
        elements.append(usuario_table)

        doc.build(elements)
        return response

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('download-pdf/', self.admin_site.admin_view(self.download_pdf), name='formularios_usuario_download_pdf')
        ]
        return custom_urls + urls

admin.site.register(User, UserAdmin)
admin.site.register(Usuario, UsuarioInfo)

