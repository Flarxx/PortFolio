from django.shortcuts import render
from .models import Project
from .models import Certificate, ContactMessage
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect


def inicio(request):
    return render(request, 'nucleo/main.html')


def proyectos(request):
    projects = Project.objects.all()
    return render(request, 'nucleo/Proyectos.html', {'projects': projects})


def certificados(request):
    certs = Certificate.objects.all()
    return render(request, 'nucleo/certificados.html', {'certificates': certs})


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado. Gracias!')
            return redirect('contacto')
    else:
        form = ContactForm()
    return render(request, 'nucleo/contact.html', {'form': form})

