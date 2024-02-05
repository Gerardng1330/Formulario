# Generated by Django 5.0.1 on 2024-02-02 16:42

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
                ('nombre', models.CharField(default='nombre', max_length=255, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=255, null=True, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=255, null=True, verbose_name='Correo Electrónico')),
                ('genero', models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otros', 'Otros')], max_length=255, null=True, verbose_name='Género')),
                ('nacionalidad', models.CharField(choices=[('Panama', 'Panamá'), ('Argentina', 'Argentina'), ('Chile', 'Chile'), ('Colombia', 'Colombia'), ('Cuba', 'Cuba'), ('Ecuador', 'Ecuador'), ('United-States', 'United States'), ('Guatemala', 'Guatemala'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Jamaica', 'Jamaica'), ('Mexico', 'Mexico'), ('Nicaragua', 'Nicaragua'), ('Peru', 'Peru'), ('Venezuela', 'Venezuela'), ('Otros', 'Otros')], max_length=255, null=True, verbose_name='Nacionalidad')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('alergia', models.TextField(blank=True, null=True, verbose_name='Alergia o Discapacidad')),
                ('formFile', models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Identificación/Pasaporte')),
                ('formFile2', models.FileField(null=True, upload_to='archivos/', verbose_name='Hoja de Vida')),
                ('Telefono1', models.CharField(max_length=20, null=True, verbose_name='Teléfono 1')),
                ('Telefono2', models.CharField(max_length=20, null=True, verbose_name='Teléfono 2')),
                ('Telefono3', models.CharField(max_length=20, null=True, verbose_name='Teléfono 3')),
                ('nombre_contacto', models.CharField(max_length=255, null=True, verbose_name='Nombre de Contacto')),
                ('Direccion1', models.CharField(max_length=255, null=True, verbose_name='Dirección 1')),
                ('Direccion2', models.CharField(max_length=255, null=True, verbose_name='Dirección 2')),
                ('Ciudad', models.CharField(max_length=255, null=True, verbose_name='Ciudad')),
                ('Estado_Provincia', models.CharField(max_length=255, null=True, verbose_name='Estado/Provincia')),
                ('Codigo1', models.CharField(default='507', max_length=20, null=True, verbose_name='Codigo1')),
                ('Codigo2', models.CharField(default='507', max_length=20, null=True, verbose_name='Codigo2')),
                ('Codigo3', models.CharField(default='507', max_length=20, null=True, verbose_name='Codigo3')),
                ('Codigo4', models.CharField(default='507', max_length=20, null=True, verbose_name='Codigo4')),
                ('Cargo1', models.CharField(blank=True, choices=[('Manager', 'Manager')], max_length=255, null=True, verbose_name='Cargo Deseado 1')),
                ('Cargo2', models.CharField(blank=True, choices=[('Manager', 'Manager')], max_length=255, null=True, verbose_name='Cargo Deseado 2')),
                ('turno', models.CharField(blank=True, choices=[('En la mañana', 'En la mañana')], max_length=255, null=True, verbose_name='Turno Deseado')),
                ('Ingles', models.CharField(blank=True, choices=[('Avanzado', 'Avanzado'), ('Intermedio', 'Intermedio'), ('Principiante', 'Principiante')], max_length=255, null=True, verbose_name='Nivel de Inglés')),
                ('Iniciar', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('Transporte', models.CharField(blank=True, choices=[('Transporte publico', 'Transporte público')], max_length=255, null=True, verbose_name='Transporte Utilizado')),
                ('Conociste', models.CharField(blank=True, choices=[('Redes sociales', 'Redes sociales')], max_length=255, null=True, verbose_name='Cómo nos Conociste')),
                ('Referido', models.CharField(max_length=255, null=True, verbose_name='Referido por')),
            ],
            options={
                'verbose_name_plural': 'Formularios de Usuarios',
            },
        ),
    ]
