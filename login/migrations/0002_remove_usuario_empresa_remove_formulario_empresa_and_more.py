# Generated by Django 5.0.1 on 2024-01-25 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='respuestas',
            name='id_formulario',
        ),
        migrations.RemoveField(
            model_name='preguntas',
            name='id_formulario',
        ),
        migrations.RemoveField(
            model_name='opciones',
            name='id_pregunta',
        ),
        migrations.RemoveField(
            model_name='respuestas',
            name='id_opcion',
        ),
        migrations.DeleteModel(
            name='PapeleraReciclaje',
        ),
        migrations.RemoveField(
            model_name='preguntas',
            name='id_tipo_pregunta',
        ),
        migrations.RemoveField(
            model_name='respuestas',
            name='id_pregunta',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id_rol',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='Formulario',
        ),
        migrations.DeleteModel(
            name='Opciones',
        ),
        migrations.DeleteModel(
            name='TipoPregunta',
        ),
        migrations.DeleteModel(
            name='Preguntas',
        ),
        migrations.DeleteModel(
            name='Respuestas',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
