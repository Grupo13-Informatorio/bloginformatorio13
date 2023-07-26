# Generated by Django 4.2.2 on 2023-07-26 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='contenido',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, default='../static/default-articulo.jpg', null=True, upload_to='articulo'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='resumen',
            field=models.TextField(verbose_name='Resumen'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]
