# Generated by Django 5.0.1 on 2024-02-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0006_alter_usuario_cargo1_alter_usuario_cargo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='turno',
            field=models.CharField(blank=True, choices=[('Mañana', 'mañana'), ('Tarde', 'Tarde'), ('Noche', 'Noche'), ('Madrugada', 'Madrugada')], max_length=255, null=True, verbose_name='Turno Deseado'),
        ),
    ]
