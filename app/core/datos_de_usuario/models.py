from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos

# Create your models here.
#Crear la estructura de la aplicacion en el modelo de datos:

class Roles(models.Model):
    RoleName = models.CharField(max_length=50, verbose_name="Nombre de rol")

    #Creo la funcion para llamar atributos 
    def __str__(self):
        return self.RoleName

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles"

class DatosUser(models.Model):
    documentoUsuario = models.CharField(max_length=12,null=True, verbose_name="Identificación")
    nombreUsuario = models.CharField(max_length=100,null=True, verbose_name="Nombres")
    apellidoUsuario = models.CharField(max_length=100,null=True, verbose_name="Apellidos")
    profesionUsu = models.CharField(max_length=100, null=True,verbose_name="Profesión")
    fotoUsuario = models.ImageField(default='user.png',null=True, verbose_name="Foto de perfil", upload_to = "img/perfiles")
    telefonoUsuario = models.CharField(max_length=20,null=True, verbose_name="Numero de teléfono")
    generoUsuario = models.CharField(max_length=20, null=True,choices=Generos, default="Otro", verbose_name="Genero")
    adddata = models.DateTimeField(auto_now_add= True, null=True, verbose_name="Creado el")
    modifiat = models.DateTimeField(auto_now= True, null=True, verbose_name="Modificado el")

    def __str__(self):
        return self.documentoUsuario
    
    class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Información"

class Habilidades(models.Model):
    nombreHabilidad = models.CharField(max_length=50, verbose_name="Nombre de la habilidad")
    descripcionHab = models.TextField(default="Desarrollador",
     verbose_name= "Descripcion de la habilidad")


    def __str__(self):
        return self.nombreHabilidad

    class Meta:
        verbose_name = "Habilidades del Usuario"
        verbose_name_plural = "Competencias"

#Modelos de detalle
class DetaRoles(models.Model):
    idRol = models.ForeignKey(Roles, on_delete= models.CASCADE, verbose_name = "Identificador de rol")
    idUsuario = models.ForeignKey(DatosUser, on_delete = models.CASCADE) 
    addUser = models.DateTimeField(auto_now_add= True, auto_now= False)
    udtuser = models.DateTimeField(auto_now= True)
    estadoRol = models.CharField(max_length=10)

    #funcion de mostrar

    def __str__(self):
        return self.estadoRol

    class Meta:
        verbose_name = "Detalles del rol"
        verbose_name_plural = "Roles"

#Tabla rates
      

class Rates(models.Model):
    idHabilidad = models.ForeignKey(Habilidades, on_delete = models.CASCADE)
    idUsuario = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    porcentaje = models.DecimalField(max_digits=2, decimal_places=1)
    udtHabili = models.DateTimeField(auto_now= True)

    #Función para mostrar 
    def __str__(self):
        self.idUsuario

    class Meta:
        verbose_name = "Nivel de habilidad"
        verbose_name_plural = "Niveles"
