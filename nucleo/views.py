from django.shortcuts import render

def inicio(request):
    return render(request, 'nucleo/main.html')

def proyectos(request):
    return render(request, 'nucleo/proyectos.html')

