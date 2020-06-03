# Generated by Django 2.2.12 on 2020-05-07 20:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentoUsuario', models.CharField(max_length=12)),
                ('fotoUsuario', models.ImageField(default='user.png', upload_to='', verbose_name='Foto de perfil')),
                ('telefonoUsuario', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreHabilidad', models.CharField(max_length=50)),
                ('descripcionHab', ckeditor.fields.RichTextField(default='Desarrollador', max_length=2000, verbose_name='Descripcion de la habilidad')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoleName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.DecimalField(decimal_places=1, max_digits=2)),
                ('udtHabili', models.DateTimeField(auto_now=True)),
                ('idHabilidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_de_usuario.Habilidades')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_de_usuario.DatosUser')),
            ],
        ),
        migrations.CreateModel(
            name='DetaRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addUser', models.DateTimeField(auto_now_add=True)),
                ('udtuser', models.DateTimeField(auto_now=True)),
                ('estadoRol', models.CharField(max_length=10)),
                ('idRol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_de_usuario.Roles', verbose_name='Identificador de rol')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_de_usuario.DatosUser')),
            ],
        ),
    ]