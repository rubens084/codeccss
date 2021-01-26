from django.contrib import admin
from .models import *

# Register your models here.

class regPerfil(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at"]
    search_display = ["nombre", "modulo"]

    class Meta:
        Model = Perfil


admin.site.register(Perfil, regPerfil)

class regModulo(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at"]
    search_display = ["tipo"]

    class Meta:
        Model = Modulo


admin.site.register(Modulo, regModulo)

class regExpediente(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at"]
    search_display = ["matricula"]

    class Meta:
        Model = Expediente

admin.site.register(Expediente, regExpediente)


class regCredito(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at"]
    search_display = ["matricula"]

    class Meta:
        Model = Credito

admin.site.register(Credito, regCredito)

class regPlantilla(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at"]
    search_display = ["__str__"]

    class Meta:
        Model = Plantilla

admin.site.register(Plantilla, regPlantilla)

class regHistorialCredito(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at"]
    search_display = ["__str__"]

    class Meta:
        Model = Historial_Redaccion

admin.site.register(Historial_Redaccion, regHistorialCredito)

class regExpedienteServicio(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at"]
    search_display = ["matricula"]

    class Meta:
        Model = Expediente_Servicio

admin.site.register(Expediente_Servicio, regExpedienteServicio)

class regDocumentoServicio(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "updated_at"]
    search_display = ["matricula"]

    class Meta:
        Model = Documento_Servicio

admin.site.register(Documento_Servicio, regDocumentoServicio)
