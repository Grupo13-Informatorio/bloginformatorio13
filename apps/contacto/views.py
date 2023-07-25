from typing import Any, Dict
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Contacto
# Create your views here.


class ContactoView(CreateView):
    model = Contacto
    template_name = 'contacto/contacto.html'
    form_class = ContactForm
    def form_valid(self, form):
        messages.success(self.request, 'Consulta enviada.')
        return super().form_valid(form)
    