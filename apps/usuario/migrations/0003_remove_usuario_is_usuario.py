# Generated by Django 4.2.2 on 2023-07-27 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_foto_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='is_usuario',
        ),
    ]
