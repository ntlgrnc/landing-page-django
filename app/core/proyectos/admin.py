from django.contrib import admin

#Importamos las clases desde los modelos
from .models import CateProyecto, TipoDocu, Proyectos, Documentos

# Register your models here.

# Registro el modelo de CategoriaProyecto

class CategoriaModel(admin.ModelAdmin):
    list_display = ["Lenguaje"]

    class Meta:
        model = CateProyecto

admin.site.register(CateProyecto)

# Registro el modelo de Proyectos

class ProyectosModel(admin.ModelAdmin):
    list_display = ["NombreProyecto"]

    class Meta:
        model = Proyectos

admin.site.register(Proyectos)

# Registro el modelo de TipoDocumento

class TipoDocumentoModel(admin.ModelAdmin):
    list_display = ["NombreTipoDocu"]

    class Meta:
        model = TipoDocu

admin.site.register(TipoDocu)

# Registro el modelo de Documentos

class DocumentosModel(admin.ModelAdmin):
    list_display = ["NombreDocumento"]

    class Meta:
        model = Documentos
        
admin.site.register(Documentos)

