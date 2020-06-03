# Generated by Django 2.2.12 on 2020-05-13 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_de_usuario', '0002_auto_20200507_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosuser',
            name='adddata',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='apellidoUsuario',
            field=models.CharField(max_length=100, null=True, verbose_name='Apellidos'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='generoUsuario',
            field=models.CharField(choices=[('Femenino', 'F'), ('Masculino', 'M'), ('Otro', 'O')], default='Otro', max_length=20, null=True, verbose_name='Genero'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='modifiat',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado el'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='nombreUsuario',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombres'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='profesionUsu',
            field=models.CharField(max_length=100, null=True, verbose_name='Profesión'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='documentoUsuario',
            field=models.CharField(max_length=12, null=True, verbose_name='Identificación'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='fotoUsuario',
            field=models.ImageField(default='user.png', null=True, upload_to='', verbose_name='Foto de perfil'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='telefonoUsuario',
            field=models.CharField(max_length=20, null=True, verbose_name='Numero de teléfono'),
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='nombreHabilidad',
            field=models.CharField(max_length=50, verbose_name='Nombre de la habilidad'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='RoleName',
            field=models.CharField(max_length=50, verbose_name='Nombre de rol'),
        ),
    ]