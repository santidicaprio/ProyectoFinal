# Generated by Django 4.0.4 on 2022-08-09 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0004_contacto_usuario_alter_empleado_imagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='apellido',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
