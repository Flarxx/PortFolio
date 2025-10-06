from django.contrib import admin
from .models import Certificado

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'emisor', 'fecha', 'publicado')
    list_filter = ('publicado', 'emisor')
    search_fields = ('titulo', 'emisor')
    ordering = ('-orden',)
