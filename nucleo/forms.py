from django import forms
from .models import Project, ContactMessage


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'slug', 'description', 'image1', 'image2', 'image3', 'technologies', 'github', 'live']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'technologies': forms.TextInput(attrs={'placeholder': 'HTML, CSS, Django, ...'}),
            'slug': forms.TextInput(attrs={'placeholder': 'url-friendly-slug'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Escribe tu mensaje...'}),
            'name': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'tu@ejemplo.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Asunto'}),
        }
