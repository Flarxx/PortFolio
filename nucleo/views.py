from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail
from django.conf import settings
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
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            email_body = (
                f"Mensaje de Contacto del Portafolio:\n\n"
                f"De: {name}\n"
                f"Email: {email}\n"
                f"Asunto: {subject}\n\n"
                f"Cuerpo del Mensaje:\n{message}"
            )
            
            try:
                send_mail(
                    subject=f"PORTAFOLIO - Nuevo mensaje: {subject}",
                    message=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL_RECEIVER],
                    fail_silently=False,
                )
                
                form.save() 
                
                messages.success(request, '✅ ¡Mensaje enviado con éxito! Te responderé lo antes posible.')
                return redirect('contacto')
                
            except Exception as e:
                print(f"Error al enviar correo: {e}")
                messages.error(request, '❌ Hubo un error al enviar tu mensaje. Por favor, inténtalo de nuevo o revisa la configuración del correo.')
                
    else:
        form = ContactForm()
        
    return render(request, 'nucleo/contact.html', {'form': form})

