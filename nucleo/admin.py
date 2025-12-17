from django.contrib import admin
from django.utils.html import format_html
from .models import Project

from .models import Certificate, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'github', 'live', 'preview')
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ('title', 'description', 'technologies')
	readonly_fields = ('preview',)
	fieldsets = (
		(None, {
			'fields': ('title', 'slug', 'description', 'technologies')
		}),
		('Imágenes', {
			'fields': ('image1', 'image2', 'image3', 'preview')
		}),
		('Enlaces', {
			'fields': ('github', 'live')
		}),
	)

	def preview(self, obj):
		img = obj.image1 or obj.image2 or obj.image3
		if not img:
			return '(sin imagen)'
		return format_html('<img src="{}" style="max-height:200px;" />', img.url)

	preview.short_description = 'Vista previa'


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'preview')
	readonly_fields = ('preview',)

	def preview(self, obj):
		if not obj.image:
			return '(sin imagen)'
		return format_html('<img src="{}" style="max-height:120px;" />', obj.image.url)

	preview.short_description = 'Imagen'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'subject', 'created_at')
	readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
	search_fields = ('name', 'email', 'subject')
