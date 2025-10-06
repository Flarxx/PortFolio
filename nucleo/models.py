from django.db import models

class Certificado(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    emisor = models.CharField(max_length=255, blank=True, verbose_name="Emisor")
    fecha = models.DateField(null=True, blank=True, verbose_name="Fecha")
    imagen = models.ImageField(upload_to='certificados/imagenes/', blank=True, null=True, verbose_name="Imagen")
    enlace_externo = models.URLField(blank=True, null=True, verbose_name="Enlace externo")
    archivo = models.FileField(upload_to='certificados/archivos/', blank=True, null=True, verbose_name="Archivo")
    orden = models.PositiveIntegerField(default=0, help_text="Orden (mayor valor primero)")
    publicado = models.BooleanField(default=True, verbose_name="Publicado")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-orden', '-fecha']
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"

    def __str__(self):
        return f"{self.titulo} — {self.emisor}"

    def obtener_url_certificado(self):
        if self.enlace_externo:
            return self.enlace_externo
        if self.archivo:
            return self.archivo.url
        return '#'
