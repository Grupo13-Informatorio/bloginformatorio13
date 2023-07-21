# Generated by Django 4.2.2 on 2023-07-20 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='articulo.articulo')),
            ],
        ),
    ]
