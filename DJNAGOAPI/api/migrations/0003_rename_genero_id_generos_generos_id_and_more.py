# Generated by Django 5.1.2 on 2024-10-28 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usuarios_fk_generos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generos',
            old_name='genero_id',
            new_name='generos_id',
        ),
        migrations.RenameField(
            model_name='generos',
            old_name='tipo_genero',
            new_name='nombre_genero',
        ),
        migrations.RenameField(
            model_name='usuarios',
            old_name='nombre_completo',
            new_name='nombre_usuario',
        ),
        migrations.RenameField(
            model_name='usuarios',
            old_name='usuarios_id',
            new_name='usuario_id',
        ),
    ]
