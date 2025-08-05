from django.shortcuts import render

def inicio(request):
    return render(request, 'nucleo/layout.html')


def inicio(request):
    return render(request, 'nucleo/main.html')