from django.shortcuts import render
from .models import Certificado, Proyecto

def inicio(request):
    return render(request, 'nucleo/main.html')

def proyectos(request):
    proyectos = Proyecto.objects.all().order_by('-fecha')
    return render(request, 'nucleo/proyectos.html', {'proyectos': proyectos})


def certificados(request):
    certificates = Certificado.objects.filter(publicado=True).order_by('-orden', '-fecha')
    return render(request, 'nucleo/certificados.html', {'certificates': certificates})

def formulario_contacto(request):
    return render(request, 'nucleo/formulario.html')


