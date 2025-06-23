from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
from django.urls import reverse_lazy

def home(request):
    return render (request, 'homepage.html')

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('Product-list')
