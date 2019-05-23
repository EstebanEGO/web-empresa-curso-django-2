from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail  import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            email = EmailMessage(
                "La cafeteria: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.oi",
                ["bangogarcia@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact') + "?fial")
    return render(request, 'contact/contact.html', {'form': form})