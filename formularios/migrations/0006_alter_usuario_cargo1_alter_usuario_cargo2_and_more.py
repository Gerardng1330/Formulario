# Generated by Django 5.0.1 on 2024-02-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0005_alter_usuario_codigo1_alter_usuario_codigo2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Cargo1',
            field=models.CharField(choices=[('Limpieza', 'Limpieza'), ('Mantenimiento', 'Mantenimiento'), ('Ayudante-cocina', 'Ayudante-cocina'), ('Recepcion', 'Recepcion')], default='nombre', max_length=255, verbose_name='Cargo Deseado 1'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Cargo2',
            field=models.CharField(choices=[('Limpieza', 'Limpieza'), ('Mantenimiento', 'Mantenimiento'), ('Ayudante-cocina', 'Ayudante-cocina'), ('Recepcion', 'Recepcion')], default='nombre', max_length=255, verbose_name='Cargo Deseado 2'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Ciudad',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Codigo1',
            field=models.CharField(blank=True, choices=[('+507', '+507'), ('+1', '+1')], default='507', max_length=20, null=True, verbose_name='Codigo1'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Codigo2',
            field=models.CharField(blank=True, choices=[('+507', '+507'), ('+1', '+1')], default='507', max_length=20, null=True, verbose_name='Codigo2'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Codigo3',
            field=models.CharField(blank=True, default='507', max_length=20, null=True, verbose_name='Codigo3'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Estado_Provincia',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Estado/Provincia'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Telefono1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono 1'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Telefono2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono 2'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='codigo_postal',
            field=models.CharField(blank=True, default='507', max_length=20, null=True, verbose_name='Codigo4'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Hoja de Vida'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion_principal',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección 1'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion_secundaria',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección 2'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nacionalidad',
            field=models.CharField(blank=True, choices=[('Panama', 'Panamá'), ('Argentina', 'Argentina'), ('Chile', 'Chile'), ('Colombia', 'Colombia'), ('Cuba', 'Cuba'), ('Ecuador', 'Ecuador'), ('United-States', 'United States'), ('Guatemala', 'Guatemala'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Jamaica', 'Jamaica'), ('Mexico', 'Mexico'), ('Nicaragua', 'Nicaragua'), ('Peru', 'Peru'), ('Venezuela', 'Venezuela'), ('Otros', 'Otros')], max_length=255, null=True, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_contacto',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre de Contacto'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='referencia',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Referido por'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono_emergencia',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono 3'),
        ),
    ]
