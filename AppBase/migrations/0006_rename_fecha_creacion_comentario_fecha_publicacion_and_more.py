# Generated by Django 4.2.1 on 2023-05-29 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBase', '0005_alter_libro_genero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='fecha_creacion',
            new_name='fecha_publicacion',
        ),
        migrations.RenameField(
            model_name='tema',
            old_name='fecha_creacion',
            new_name='fecha_publicacion',
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.CharField(choices=[('agricultura', 'Agricultura'), ('autobiografia', 'Autobiografia'), ('aventura', 'Aventura'), ('botanica', 'Botanica'), ('cienciaficcion', 'Cienciaficcion'), ('deportes', 'Deportes'), ('detective', 'Detective'), ('educativa', 'Educativa'), ('estrategia', 'Estrategia'), ('fantastica', 'Fantastica'), ('gotica', 'Gotica'), ('guerra', 'Guerra'), ('hadas', 'Hadas'), ('humor', 'Humor'), ('infantil', 'Infantil'), ('ingenio', 'Ingenio'), ('juegos', 'Juegos'), ('juvenil', 'Juvenil'), ('paranormal', 'Paranormal'), ('policial', 'Policial'), ('recetas', 'Recetas'), ('thriller', 'Thriller'), ('viajes', 'Viajes')], max_length=255),
        ),
    ]