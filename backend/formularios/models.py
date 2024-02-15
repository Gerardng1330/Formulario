from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Creamos el modelo para la bd
class Usuario(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre', default='nombre')
    apellido = models.CharField(max_length=255, blank=True, null=True, verbose_name='Apellido')
    email = models.EmailField(max_length=255,blank=True, null=True, verbose_name='Correo Electrónico')
    genero = models.CharField(max_length=255,blank=True, null=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')],  verbose_name='Género')
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
        ('Otros', 'Otros')],blank=True, null=True, verbose_name='Nacionalidad')
    fecha_nacimiento = models.TextField(blank=True, null=True,verbose_name='Fecha de Nacimiento')
    alergia = models.TextField(blank=True, null=True,verbose_name='Alergia o Discapacidad')
    id_file = models.FileField(upload_to='archivos/', null=True, blank=True, verbose_name='Identificación/Pasaporte')
    cv_file = models.FileField(upload_to='archivos/', blank=True, null=True,  verbose_name='Hoja de Vida')
    Telefono1 = models.CharField(max_length=20, blank=True, null=True,verbose_name='Teléfono 1')
    Telefono2 = models.CharField(max_length=20, blank=True, null=True,verbose_name='Teléfono 2')
    telefono_emergencia = models.CharField(max_length=20,blank=True, null=True, verbose_name='Teléfono 3')
    nombre_contacto = models.CharField(max_length=255,blank=True, null=True, verbose_name='Nombre de Contacto')
    direccion_principal = models.CharField(max_length=255, blank=True, null=True,verbose_name='Dirección 1')
    direccion_secundaria = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección 2')
    ciudad = models.CharField(max_length=255,blank=True,  verbose_name='Ciudad cliente',default='cid')
    Estado_Provincia = models.CharField(max_length=255,blank=True, null=True, verbose_name='Estado/Provincia')
    Codigo1= models.CharField(max_length=20,blank=True, null=True, choices=[('507','507'),('1','1')],verbose_name='Codigo1',default='507')
    Codigo2= models.CharField(max_length=20,blank=True, null=True,choices=[('507','507'),('1','1')], verbose_name='Codigo2',default='507')
    Codigo3= models.CharField(max_length=20,blank=True, null=True, verbose_name='Codigo3',default='507')
    codigo_postal= models.CharField(max_length=20,blank=True, null=True, verbose_name='Codigo4',default='507')
    Cargo1 = models.CharField(max_length=255, choices=[('Limpieza','Limpieza'), ('Mantenimiento','Mantenimiento'),('Ayudante-cocina','Ayudante-cocina'),('Recepcion','Recepcion')],blank=True, null=True,  verbose_name='Cargo Deseado 1',default='nombre')
    Cargo2 = models.CharField(max_length=255, choices=[('Limpieza','Limpieza'), ('Mantenimiento','Mantenimiento'),('Ayudante-cocina','Ayudante-cocina'),('Recepcion','Recepcion')],  verbose_name='Cargo Deseado 2',default='nombre')
    turno = models.CharField(max_length=255,blank=True, null=True, choices=[('mañana','mañana'), ('Tarde','Tarde'),('Noche','Noche'),('Madrugada','Madrugada')],  verbose_name='Turno Deseado')
    nivel_ingles = models.CharField(max_length=255,blank=True, null=True, choices=[('nulo', 'nulo'),
        ('basico', 'basico'),
        ('medio', 'medio'),('avanzado','avanzado'),('nativo','nativo')], verbose_name='Nivel de Inglés')
    fecha_inicio = models.TextField(blank=True, null=True, verbose_name='Fecha de Inicio')
    Transporte = models.CharField(max_length=255,blank=True, null=True, choices=[('bus','bus'), ('vehiculo-propio','vehiculo-propio'),('uber','uber'),('OTRO','OTRO')],  verbose_name='Transporte Utilizado')
    Conociste = models.CharField(max_length=255, blank=True, null=True,choices=[('referencia','referencia'),('sticker-qr','sticker-qr'),('volante','volante'),('oficina','oficina'), ('google','google'),('otro','otro')],  verbose_name='Cómo nos Conociste')
    referencia = models.CharField(max_length=255,blank=True, null=True, verbose_name='Referido por')

    # Método que devuelve una representación en cadena del objeto
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    # Configuración adicional del modelo (en este caso, nombre plural)
    class Meta:
        verbose_name_plural = 'Formularios de Usuarios'
