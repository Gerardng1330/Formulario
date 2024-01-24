from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
class Usuarios(models.Model):
    name = models.CharField(max_length=200)

class TipoPregunta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=255)

class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=255)

class Usuario(models.Model):
    correo = models.EmailField(max_length=80)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    num_telefono = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha_inicio_sesion = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    ip_secundary = models.GenericIPAddressField(null=True, blank=True)

class Formulario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField()
    fecha_papelera = models.DateTimeField(null=True, blank=True)

class Preguntas(models.Model):
    id_formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    enunciado = models.CharField(max_length=255)
    id_tipo_pregunta = models.ForeignKey(TipoPregunta, on_delete=models.CASCADE)

class Opciones(models.Model):
    id_pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    valor = models.CharField(max_length=255)

class Respuestas(models.Model):
    id_pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    id_opcion = models.ForeignKey(Opciones, on_delete=models.CASCADE)
    id_formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

class PapeleraReciclaje(models.Model):
    id_elemento = models.AutoField(primary_key=True)
    tipo_elemento = models.CharField(max_length=255, help_text='Tipo de elemento: Formulario, Pregunta, Respuesta, etc.')
    id_elemento_original = models.IntegerField(help_text='ID del elemento original antes de ser eliminado')
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
