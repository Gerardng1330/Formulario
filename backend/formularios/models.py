from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Modelo para las políticas
class Politicas(models.Model):
    parrafo = models.TextField()

# Creamos el modelo para la bd
class Usuario(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre',default='507')
    apellido = models.CharField(max_length=255,  verbose_name='Apellido',default='507')
    email = models.EmailField(max_length=255, verbose_name='Correo Electrónico',default='507')
    genero = models.CharField(max_length=255, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')],  verbose_name='Género',default='507')
    nacionalidad = models.CharField(max_length=255, choices=[ ('Panama', 'Panamá'),
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
        ('Otro', 'Otro')], verbose_name='Nacionalidad',default='507')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento',default='2012-12-12')
    alergia = models.TextField(verbose_name='Alergia o Discapacidad',default='507')
    id_file = models.FileField(upload_to='archivos/',  verbose_name='Identificación/Pasaporte',default='507')
    cv_file = models.FileField(upload_to='archivos/', verbose_name='Hoja de Vida',default='507')
    codigo1= models.CharField(max_length=20, choices=[('507','507'),('1','1')],verbose_name='Codigo1',default='507')
    Telefono1 = models.IntegerField(verbose_name='Teléfono 1',default='507')
    codigo2= models.CharField(max_length=20,choices=[('507','507'),('1','1')], verbose_name='Codigo2',default='507')
    Telefono2 = models.IntegerField(verbose_name='Teléfono 2',default='507')
    codigo3= models.CharField(max_length=20,choices=[('507','507'),('1','1')], verbose_name='Codigo3',default='507')
    telefono_emergencia = models.IntegerField(verbose_name='Teléfono emergencia',default='507')
    nombre_contacto = models.CharField(max_length=255, verbose_name='Nombre de Contacto',default='507')
    direccion_principal = models.CharField(max_length=255, verbose_name='Dirección principal',default='507')
    #no requerido
    direccion_secundaria = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección secundaria',default='507')
    ciudad = models.CharField(max_length=255,  verbose_name='Ciudad ',default='507')
    Estado_Provincia = models.CharField(max_length=255,verbose_name='Estado/Provincia',default='507')
    #codigo_postal= models.CharField(max_length=20, verbose_name='Codigo postal',default='507')
    Cargo1 = models.CharField(max_length=255, choices=[('Limpieza','Limpieza'), ('Mantenimiento','Mantenimiento'),('Ayudante-cocina','Ayudante-cocina'),('Recepcion','Recepcion')],  verbose_name='Cargo Deseado 1')
    Cargo2 = models.CharField(max_length=255, choices=[('Limpieza','Limpieza'), ('Mantenimiento','Mantenimiento'),('Ayudante-cocina','Ayudante-cocina'),('Recepcion','Recepcion')],  verbose_name='Cargo Deseado 2',default='507')
    turno = models.CharField(max_length=255,choices=[('mañana','mañana'), ('Tarde','Tarde'),('Noche','Noche'),('Madrugada','Madrugada')],  verbose_name='Turno Deseado',default='507')
    nivel_ingles = models.CharField(max_length=255, choices=[('nulo', 'nulo'),
        ('basico', 'basico'),
        ('medio', 'medio'),('avanzado','avanzado'),('nativo','nativo')], verbose_name='Nivel de Inglés',default='507')
    fecha_inicio = models.DateField( verbose_name='Fecha de Inicio',default='2012-12-12')
    Transporte = models.CharField(max_length=255, choices=[('bus','bus'), ('vehiculo-propio','vehiculo-propio'),('uber','uber'),('OTRO','OTRO')],  verbose_name='Transporte Utilizado',default='507')
    Conociste = models.CharField(max_length=255, choices=[('referencia','referencia'),('sticker-qr','sticker-qr'),('volante','volante'),('oficina','oficina'), ('google','google'),('otro','otro')],  verbose_name='Cómo nos Conociste',default='507')
    #no requerido
    referencia = models.CharField(max_length=255,blank=True, null=True, verbose_name='Referido por',default='507')

    # Método que devuelve una representación en cadena del objeto
    def __str__(self):
        return f"{self.nombre}"

    # Configuración adicional del modelo (en este caso, nombre plural)
    class Meta:
        verbose_name_plural = 'Formularios de Usuarios'