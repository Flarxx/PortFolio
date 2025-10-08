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

class Proyecto(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    tecnologias = models.CharField(max_length=200, help_text="Ejemplo: HTML, CSS, JS, Django")
    enlace_codigo = models.URLField(blank=True, null=True)
    enlace_proyecto = models.URLField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    
    # imágenes del carrusel
    imagen1 = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    imagen3 = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    def imagenes(self):
        return [img for img in [self.imagen1, self.imagen2, self.imagen3] if img]

    def lista_tecnologias(self):
        """Convierte la cadena en lista separada por comas"""
        return [t.strip() for t in self.tecnologias.split(',') if t.strip()]


