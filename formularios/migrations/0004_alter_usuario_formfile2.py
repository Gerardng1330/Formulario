# Generated by Django 5.0.1 on 2024-01-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0003_rename_fechanacimiento_usuario_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='formFile2',
            field=models.FileField(null=True, upload_to='archivos/', verbose_name='Hoja de Vida'),
        ),
    ]
