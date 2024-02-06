# Generated by Django 5.0.1 on 2024-02-06 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0008_alter_usuario_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Codigo1',
            field=models.CharField(blank=True, choices=[('507', '507'), ('1', '1')], default='507', max_length=20, null=True, verbose_name='Codigo1'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Codigo2',
            field=models.CharField(blank=True, choices=[('507', '507'), ('1', '1')], default='507', max_length=20, null=True, verbose_name='Codigo2'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('femenino', 'femenino'), ('otros', 'Otros')], max_length=255, null=True, verbose_name='Género'),
        ),
    ]
