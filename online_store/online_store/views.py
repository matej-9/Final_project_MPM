from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    return render (request, 'homepage.html')

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        name = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        email = form.cleaned_data['email']
        message = form.cleaned_data['content']

        send_mail(f'From{name}{lastname}',
                    f'Message:{message}', email, [settings.ADMIN_EMAIL], fail_silently=False)
        messages.success(self.request, "Thank you for contacting us.")
        return super().form_valid(form)      