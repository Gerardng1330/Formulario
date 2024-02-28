from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Creamos el modelo para la bd
class Usuario(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    apellido = models.CharField(max_length=255,  verbose_name='Apellido')
    email = models.EmailField(max_length=255, verbose_name='Correo Electrónico')
    genero = models.CharField(max_length=255, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')],  verbose_name='Género')
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
        ('Otros', 'Otros')], verbose_name='Nacionalidad')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    alergia = models.TextField(verbose_name='Alergia o Discapacidad')
    id_file = models.FileField(upload_to='archivos/',  verbose_name='Identificación/Pasaporte')
    cv_file = models.FileField(upload_to='archivos/', verbose_name='Hoja de Vida')
    Codigo1= models.CharField(max_length=20, choices=[('507','507'),('1','1')],verbose_name='Codigo1',default='507')
    Telefono1 = models.IntegerField(verbose_name='Teléfono 1')
    Codigo2= models.CharField(max_length=20,choices=[('507','507'),('1','1')], verbose_name='Codigo2',default='507')
    Telefono2 = models.IntegerField(verbose_name='Teléfono 2')
    Codigo3= models.CharField(max_length=20,choices=[('507','507'),('1','1')], verbose_name='Codigo3',default='507')
    telefono_emergencia = models.IntegerField(verbose_name='Teléfono emergencia')
    nombre_contacto = models.CharField(max_length=255, verbose_name='Nombre de Contacto')
    direccion_principal = models.CharField(max_length=255, verbose_name='Dirección principal')
    #no requerido
    direccion_secundaria = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección secundaria')
    ciudad = models.CharField(max_length=255,  verbose_name='Ciudad ')
    Estado_Provincia = models.CharField(max_length=255,verbose_name='Estado/Provincia')
    codigo_postal= models.CharField(max_length=20, verbose_name='Codigo postal',default='507')
    Cargo1 = models.CharField(max_length=255, choices=[('Limpieza','Limpieza'), ('Mantenimiento','Mantenimiento'),('Ayudante-cocina','Ayudante-cocina'),('Recepcion','Recepcion')],  verbose_name='Cargo Deseado 1')
    Cargo2 = models.CharField(max_length=255, choices=[('Limpieza','Limpieza'), ('Mantenimiento','Mantenimiento'),('Ayudante-cocina','Ayudante-cocina'),('Recepcion','Recepcion')],  verbose_name='Cargo Deseado 2')
    turno = models.CharField(max_length=255,choices=[('mañana','mañana'), ('Tarde','Tarde'),('Noche','Noche'),('Madrugada','Madrugada')],  verbose_name='Turno Deseado')
    nivel_ingles = models.CharField(max_length=255, choices=[('nulo', 'nulo'),
        ('basico', 'basico'),
        ('medio', 'medio'),('avanzado','avanzado'),('nativo','nativo')], verbose_name='Nivel de Inglés')
    fecha_inicio = models.DateField( verbose_name='Fecha de Inicio')
    Transporte = models.CharField(max_length=255, choices=[('bus','bus'), ('vehiculo-propio','vehiculo-propio'),('uber','uber'),('OTRO','OTRO')],  verbose_name='Transporte Utilizado')
    Conociste = models.CharField(max_length=255, choices=[('referencia','referencia'),('sticker-qr','sticker-qr'),('volante','volante'),('oficina','oficina'), ('google','google'),('otro','otro')],  verbose_name='Cómo nos Conociste')
    #no requerido
    referencia = models.CharField(max_length=255,blank=True, null=True, verbose_name='Referido por')

    # Método que devuelve una representación en cadena del objeto
    def __str__(self):
        return f"{self.nombre}"

    # Configuración adicional del modelo (en este caso, nombre plural)
    class Meta:
        verbose_name_plural = 'Formularios de Usuarios'
