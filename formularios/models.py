from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Creamos el modelo para la bd
class Usuario(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre', default='nombre')
    apellido = models.CharField(max_length=255, null=True, verbose_name='Apellido')
    email = models.EmailField(max_length=255,null=True, verbose_name='Correo Electrónico')
    genero = models.CharField(max_length=255,null=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otros', 'Otros')], blank=True, verbose_name='Género')
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
        ('Otros', 'Otros')], null=True, verbose_name='Nacionalidad')
    fecha_nacimiento = models.DateField(blank=True, null=True,verbose_name='Fecha de Nacimiento')
    alergia = models.TextField(blank=True, null=True,verbose_name='Alergia o Discapacidad')
    formFile = models.FileField(upload_to='archivos/', null=True, blank=True, verbose_name='Identificación/Pasaporte')
    formFile2 = models.FileField(upload_to='archivos/', null=True,  verbose_name='Hoja de Vida')
    Telefono1 = models.CharField(max_length=20, null=True,verbose_name='Teléfono 1')
    Telefono2 = models.CharField(max_length=20, null=True,verbose_name='Teléfono 2')
    Telefono3 = models.CharField(max_length=20,null=True, verbose_name='Teléfono 3')
    nombre_contacto = models.CharField(max_length=255,null=True, verbose_name='Nombre de Contacto')
    Direccion1 = models.CharField(max_length=255, null=True,verbose_name='Dirección 1')
    Direccion2 = models.CharField(max_length=255, null=True, verbose_name='Dirección 2')
    Ciudad = models.CharField(max_length=255,null=True, verbose_name='Ciudad')
    Estado_Provincia = models.CharField(max_length=255,null=True, verbose_name='Estado/Provincia')
    Codigo1= models.CharField(max_length=20,null=True, verbose_name='Codigo1',default='507')
    Codigo2= models.CharField(max_length=20,null=True, verbose_name='Codigo2',default='507')
    Codigo3= models.CharField(max_length=20,null=True, verbose_name='Codigo3',default='507')
    Codigo4= models.CharField(max_length=20,null=True, verbose_name='Codigo4',default='507')
    Cargo1 = models.CharField(max_length=255, choices=[('Manager', 'Manager')], blank=True,null=True, verbose_name='Cargo Deseado 1')
    Cargo2 = models.CharField(max_length=255, choices=[('Manager', 'Manager')], blank=True,null=True, verbose_name='Cargo Deseado 2')
    turno = models.CharField(max_length=255,null=True, choices=[('En la mañana', 'En la mañana')], blank=True, verbose_name='Turno Deseado')
    Ingles = models.CharField(max_length=255,null=True, choices=[('Avanzado', 'Avanzado'),
        ('Intermedio', 'Intermedio'),
        ('Principiante', 'Principiante')], blank=True, verbose_name='Nivel de Inglés')
    Iniciar = models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')
    Transporte = models.CharField(max_length=255,null=True, choices=[('Transporte publico', 'Transporte público')], blank=True, verbose_name='Transporte Utilizado')
    Conociste = models.CharField(max_length=255, null=True,choices=[('Redes sociales', 'Redes sociales')], blank=True, verbose_name='Cómo nos Conociste')
    Referido = models.CharField(max_length=255,null=True, verbose_name='Referido por')

    # Método que devuelve una representación en cadena del objeto
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    # Configuración adicional del modelo (en este caso, nombre plural)
    class Meta:
        verbose_name_plural = 'Formularios de Usuarios'
