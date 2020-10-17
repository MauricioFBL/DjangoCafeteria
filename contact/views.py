from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de CONTACTO", # asunto ,
                "De {} <{}> \n\n Escribio: \n\n{}".format(name,email,content), # cuerpo,
                "No contestar@inbox.mailtrap.io", # email_origen,
                ["mauricio.fernando_sic@tesco.edu.mx"], # email_destino,
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')

    return render(request,"contact/contact.html",{'form':contact_form})