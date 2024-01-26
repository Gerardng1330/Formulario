# Generated by Django 5.0.1 on 2024-01-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=255, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=255, verbose_name='Correo Electrónico')),
                ('genero', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otros', 'Otros')], max_length=255, verbose_name='Género')),
                ('nacionalidad', models.CharField(blank=True, choices=[('Panama', 'Panamá'), ('Argentina', 'Argentina'), ('Chile', 'Chile'), ('Colombia', 'Colombia'), ('Cuba', 'Cuba'), ('Ecuador', 'Ecuador'), ('United-States', 'United States'), ('Guatemala', 'Guatemala'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Jamaica', 'Jamaica'), ('Mexico', 'Mexico'), ('Nicaragua', 'Nicaragua'), ('Peru', 'Peru'), ('Venezuela', 'Venezuela'), ('Otros', 'Otros')], max_length=255, verbose_name='Nacionalidad')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('alergia', models.TextField(blank=True, verbose_name='Alergia o Discapacidad')),
                ('identificacion', models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Identificación/Pasaporte')),
                ('hoja_vida', models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Hoja de Vida')),
                ('telefono1', models.CharField(max_length=20, verbose_name='Teléfono 1')),
                ('telefono2', models.CharField(max_length=20, verbose_name='Teléfono 2')),
                ('telefono3', models.CharField(max_length=20, verbose_name='Teléfono 3')),
                ('nombre_contacto', models.CharField(max_length=255, verbose_name='Nombre de Contacto')),
                ('direccion1', models.CharField(max_length=255, verbose_name='Dirección 1')),
                ('direccion2', models.CharField(blank=True, max_length=255, verbose_name='Dirección 2')),
                ('ciudad', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('estado_provincia', models.CharField(max_length=255, verbose_name='Estado/Provincia')),
                ('codigo_postal', models.CharField(max_length=20, verbose_name='Código Postal')),
                ('cargo_deseado1', models.CharField(blank=True, choices=[('Manager', 'Manager')], max_length=255, verbose_name='Cargo Deseado 1')),
                ('cargo_deseado2', models.CharField(blank=True, choices=[('Manager', 'Manager')], max_length=255, verbose_name='Cargo Deseado 2')),
                ('turno_deseado', models.CharField(blank=True, choices=[('En la mañana', 'En la mañana')], max_length=255, verbose_name='Turno Deseado')),
                ('nivel_ingles', models.CharField(blank=True, choices=[('Avanzado', 'Avanzado'), ('Intermedio', 'Intermedio'), ('Principiante', 'Principiante')], max_length=255, verbose_name='Nivel de Inglés')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('transporte_utilizado', models.CharField(blank=True, choices=[('Transporte publico', 'Transporte público')], max_length=255, verbose_name='Transporte Utilizado')),
                ('como_nos_conociste', models.CharField(blank=True, choices=[('Redes sociales', 'Redes sociales')], max_length=255, verbose_name='Cómo nos Conociste')),
                ('referido_por', models.CharField(max_length=255, verbose_name='Referido por')),
            ],
            options={
                'verbose_name_plural': 'Formularios de Usuarios',
            },
        ),
    ]
