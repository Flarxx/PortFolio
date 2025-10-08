from django.contrib import admin
from .models import Certificado, Proyecto       

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'emisor', 'fecha', 'publicado')
    list_filter = ('publicado', 'emisor')
    search_fields = ('titulo', 'emisor')
    ordering = ('-orden',)

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'tecnologias')