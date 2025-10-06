from django.shortcuts import render
from .models import Certificado

def inicio(request):
    return render(request, 'nucleo/main.html')

def proyectos(request):
    return render(request, 'nucleo/proyectos.html')


def certificados(request):
    certificates = Certificate.objects.filter(published=True).order_by('-order', '-date')
    return render(request, 'nucleo/certificados.html', {'certificates': certificates})

