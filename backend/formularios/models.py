from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Modelo para las políticas
class Politicas(models.Model):
    parrafo = models.TextField()

# Creamos el modelo para la bd
from django.utils.translation import gettext_lazy as _

class Usuario(models.Model):
    nombre = models.CharField(max_length=255, verbose_name=_('Nombre'), default='nombre')
    apellido = models.CharField(max_length=255, verbose_name=_('Apellido'), default='apellido')
    email = models.EmailField(max_length=255, verbose_name=_('Correo Electrónico'), default='email@exampl.ecom')
    genero = models.CharField(max_length=255, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], verbose_name=_('Género'), default='genero')
    nacionalidad = models.CharField(max_length=255, choices=[
        ('Panama', 'Panamá'),
        ('Argentina', 'Argentina'),
        ('Chile', 'Chile'),
        ('Colombia', 'Colombia'),
        ('Cuba', 'Cuba'),
        ('Ecuador', 'Ecuador'),
        ('United-States', 'United States'),
        ('Guatemala', 'Guatemala'),
        ('Haiti', 'Haiti'),
        ('Honduras', 'Honduras'),
        ('Jamaica', 'Jamaica'),
        ('Mexico', 'Mexico'),
        ('Nicaragua', 'Nicaragua'),
        ('Peru', 'Peru'),
        ('Venezuela', 'Venezuela'),
        ('Otro', 'Otro')],
        verbose_name=_('Nacionalidad'), default='507')
    fecha_nacimiento = models.DateField(verbose_name=_('Fecha de Nacimiento'), default='2012-12-12')
    alergia = models.TextField(verbose_name=_('Alergia o Discapacidad'), default='alergia')
    id_file = models.FileField(verbose_name=_('Identificación/Pasaporte'), default='id-file', upload_to="media/id_usuarios")
    cv_file = models.FileField(verbose_name=_('Hoja de Vida'), default='cv-file', upload_to="media/cv_usuarios/")
    codigo1 = models.CharField(max_length=20, choices=[('507', '507'), ('1', '1')], verbose_name=_('Codigo1'), default='codigo1')
    Telefono1 = models.IntegerField(verbose_name=_('Teléfono 1'), default='telefono1')
    codigo2 = models.CharField(max_length=20, choices=[('507', '507'), ('1', '1')], verbose_name=_('Codigo2'), default='codigo2')
    Telefono2 = models.IntegerField(verbose_name=_('Teléfono 2'), default='telefono2')
    codigo3 = models.CharField(max_length=20, choices=[('507', '507'), ('1', '1')], verbose_name=_('Codigo3'), default='codigo3')
    telefono_emergencia = models.IntegerField(verbose_name=_('Teléfono emergencia'), default='telefono emergencia')
    nombre_contacto = models.CharField(max_length=255, verbose_name=_('Nombre de Contacto'), default='nombre contacto')
    direccion_principal = models.CharField(max_length=255, verbose_name=_('Dirección principal'), default='direccion principal')
    direccion_secundaria = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Dirección secundaria'), default='direccion secundaria')
    ciudad = models.CharField(max_length=255, verbose_name=_('Ciudad'), default='ciudad')
    Estado_Provincia = models.CharField(max_length=255, verbose_name=_('Estado/Provincia'), default='estado/provincia')
    Cargo1 = models.CharField(max_length=255, choices=[('Limpieza', 'Limpieza'), ('Mantenimiento', 'Mantenimiento'), ('Ayudante-cocina', 'Ayudante-cocina'), ('Recepcion', 'Recepcion')], verbose_name=_('Cargo Deseado 1'), default='cargo 1')
    Cargo2 = models.CharField(max_length=255, choices=[('Limpieza', 'Limpieza'), ('Mantenimiento', 'Mantenimiento'), ('Ayudante-cocina', 'Ayudante-cocina'), ('Recepcion', 'Recepcion')], verbose_name=_('Cargo Deseado 2'), default='cargo 2')
    turno = models.CharField(max_length=255, choices=[('mañana', 'mañana'), ('tarde', 'tarde'), ('noche', 'noche'), ('madrugada', 'madrugada')], verbose_name=_('Turno Deseado'), default='turno')
    nivel_ingles = models.CharField(max_length=255, choices=[('nulo', 'nulo'), ('basico', 'basico'), ('medio', 'medio'), ('avanzado', 'avanzado'), ('nativo', 'nativo')], verbose_name=_('Nivel de Inglés'), default='nivel ingles')
    fecha_inicio = models.DateField(verbose_name=_('Fecha de Inicio'), default='2012-12-12')
    Transporte = models.CharField(max_length=255, choices=[('bus', 'bus'), ('vehiculo-propio', 'vehiculo-propio'), ('uber', 'uber'), ('otro', 'otro')], verbose_name=_('Transporte Utilizado'), default='transporte')
    Conociste = models.CharField(max_length=255, choices=[('referencia', 'referencia'), ('sticker-qr', 'sticker-qr'), ('volante', 'volante'), ('oficina', 'oficina'), ('google', 'google'), ('otro', 'otro')], verbose_name=_('Cómo nos Conociste'), default='como nos conociste')
    referencia = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Referido por'), default='referencia')


    # Método que devuelve una representación en cadena del objeto
    def __str__(self):
        return f"{self.nombre}"

    # Configuración adicional del modelo (en este caso, nombre plural)
    class Meta:
        verbose_name_plural = 'Formularios de Usuarios'