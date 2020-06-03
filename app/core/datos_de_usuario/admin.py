from django.contrib import admin

#Importamos las clases desde los modelos
from .models import Roles, DatosUser, DetaRoles, Habilidades, Rates

# Register your models here.

# Registro el modelo de roles

class RolModel(admin.ModelAdmin):
    list_display = ["NombreRol"]

    class Meta: 
        model = Roles

admin.site.register(Roles)

# Registro el modelo de DatosUser

class DatosUsuModel(admin.ModelAdmin):
    list_display = ["NombreUsuario"]

    class Meta:
        model = DatosUser

admin.site.register(DatosUser)

# Registro el modelo de Detaroles

class DetalleRolModel(admin.ModelAdmin):
    list_display = ["IdUsuario"]

    class Meta:
        model = DetaRoles

admin.site.register(DetaRoles)

# Registro el modelo de Habilidades

class HabilidadesModel(admin.ModelAdmin):
    list_display = ["NombreHabilidad"]

    class Meta:
        model = Habilidades

admin.site.register(Habilidades)

# Registro el modelo de Calificaciones - Rates

class RatesModel(admin.ModelAdmin):
    list_display = ["IdUsuario"]

    class Meta:
        model = Rates

admin.site.register(Rates)


