import ssl
from django.shortcuts import render, redirect
from .forms import ContactoForm
import smtplib
from django.conf import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib import messages
# Create your views here.


def enviar_correo(user, asunto, mensaje):
    print("Iniciando el envío del correo...")
    remitente = settings.EMAIL_HOST_USER
    destinatario = settings.EMAIL_HOST_USER
    
    try:
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=ssl.SSLContext(ssl.PROTOCOL_TLS))as smtp:
            print("Conectado al servidor SMTP...")
            smtp.login(remitente,settings.EMAIL_HOST_PASSWORD)
            print("Autenticado en el servidor SMTP...")
            email = MIMEMultipart()
            email["From"] = remitente
            email["To"] = destinatario
            email["Subject"] = asunto
            email.attach(MIMEText(mensaje, "plain"))
            
            smtp.send_message(email)
            print("Correo enviado!") 
        return True
    except Exception as e:
        print(f"Error al enviar el mnanesaje {e}")
        return False

def index(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            asunto = 'Nuevo mensaje de contacto'
            mensaje = f'Mensaje de {first_name} {last_name} ({email}): {message}'
            enviar_correo(email, asunto, mensaje)
            messages.success(request, '!Gracias por ponerte en contacto, prontamente me comunicare contigo!')
            return redirect ('index')
    return render(request, 'app_portafolio/index.html')
