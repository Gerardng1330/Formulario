# Generated by Django 5.0.1 on 2024-02-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0012_alter_usuario_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Ciudad',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ciudad'),
        ),
    ]
