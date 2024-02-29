from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Modelo para las políticas
class Politicas(models.Model):
    parrafo = models.TextField()

# Creamos el modelo para la bd
class Usuario(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre',default='nombre')
    apellido = models.CharField(max_length=255,  verbose_name='Apellido',default='apellido')
    email = models.EmailField(max_length=255, verbose_name='Correo Electrónico',default='email@exampl.ecom')
    genero = models.CharField(max_length=255, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')],  verbose_name='Género',default='genero')
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
    alergia = models.TextField(verbose_name='Alergia o Discapacidad',default='alergia')
    id_file = models.FileField(upload_to='archivos/',  verbose_name='Identificación/Pasaporte',default='id-file')
    cv_file = models.FileField(upload_to='archivos/', verbose_name='Hoja de Vida',default='cv-file')
    codigo1= models.CharField(max_length=20, choices=[('507','507'),('1','1')],verbose_name='Codigo1',default='codigo1')
    Telefono1 = models.IntegerField(verbose_name='Teléfono 1',default='telefono1')
    codigo2= models.CharField(max_length=20,choices=[('507','507'),('1','1')], verbose_name='Codigo2',default='codigo2')
    Telefono2 = models.IntegerField(verbose_name='Teléfono 2',default='telefono2')
    codigo3= models.CharField(max_length=20,choices=[('507','507'),('1','1')], verbose_name='Codigo3',default='codigo3')
    telefono_emergencia = models.IntegerField(verbose_name='Teléfono emergencia',default='telefono emergencia')
    nombre_contacto = models.CharField(max_length=255, verbose_name='Nombre de Contacto',default='nombre contacto')
    direccion_principal = models.CharField(max_length=255, verbose_name='Dirección principal',default='direccion principal')
    #no requerido
    direccion_secundaria = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección secundaria',default='direccion secundaria')
    ciudad = models.CharField(max_length=255,  verbose_name='Ciudad ',default='ciudad')
    Estado_Provincia = models.CharField(max_length=255,verbose_name='Estado/Provincia',default='estado/provincia')
    #codigo_postal= models.CharField(max_length=20, verbose_name='Codigo postal',default='507')
    Cargo1 = models.CharField(max_length=255, choices=[('Limpieza','Limpieza'), ('Mantenimiento','Mantenimiento'),('Ayudante-cocina','Ayudante-cocina'),('Recepcion','Recepcion')],  verbose_name='Cargo Deseado 1',default='cargo 1')
    Cargo2 = models.CharField(max_length=255, choices=[('Limpieza','Limpieza'), ('Mantenimiento','Mantenimiento'),('Ayudante-cocina','Ayudante-cocina'),('Recepcion','Recepcion')],  verbose_name='Cargo Deseado 2',default='cargo 2')
    turno = models.CharField(max_length=255,choices=[('mañana','mañana'), ('tarde','tarde'),('noche','noche'),('madrugada','madrugada')],  verbose_name='Turno Deseado',default='turno')
    nivel_ingles = models.CharField(max_length=255, choices=[('nulo', 'nulo'),
        ('basico', 'basico'),
        ('medio', 'medio'),('avanzado','avanzado'),('nativo','nativo')], verbose_name='Nivel de Inglés',default='nivel ingles')
    fecha_inicio = models.DateField( verbose_name='Fecha de Inicio',default='2012-12-12')
    Transporte = models.CharField(max_length=255, choices=[('bus','bus'), ('vehiculo-propio','vehiculo-propio'),('uber','uber'),('OTRO','OTRO')],  verbose_name='Transporte Utilizado',default='transporte')
    Conociste = models.CharField(max_length=255, choices=[('referencia','referencia'),('sticker-qr','sticker-qr'),('volante','volante'),('oficina','oficina'), ('google','google'),('otro','otro')],  verbose_name='Cómo nos Conociste',default='como nos conociste')
    #no requerido
    referencia = models.CharField(max_length=255,blank=True, null=True, verbose_name='Referido por',default='referencia')

    # Método que devuelve una representación en cadena del objeto
    def __str__(self):
        return f"{self.nombre}"

    # Configuración adicional del modelo (en este caso, nombre plural)
    class Meta:
        verbose_name_plural = 'Formularios de Usuarios'