from django.db import models
from django.urls import reverse


class Project(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	description = models.TextField(blank=True)
	image1 = models.ImageField(upload_to='projects/', blank=True, null=True)
	image2 = models.ImageField(upload_to='projects/', blank=True, null=True)
	image3 = models.ImageField(upload_to='projects/', blank=True, null=True)
	technologies = models.CharField(max_length=300, blank=True, help_text='Separar tecnologías por comas')
	github = models.URLField(blank=True)
	live = models.URLField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('proyecto_detalle', args=[self.slug])

	def tech_list(self):
		if not self.technologies:
			return []
		return [t.strip() for t in self.technologies.split(',') if t.strip()]


class Certificate(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='certificates/', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title


class ContactMessage(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField()
	subject = models.CharField(max_length=200, blank=True)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"{self.name} <{self.email}> - {self.subject}"
