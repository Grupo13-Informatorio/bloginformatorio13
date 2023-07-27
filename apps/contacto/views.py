from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from apps.contacto.forms import ContactoForm
# Create your views here.

class ContactoUsuario(CreateView):
    
    form_class = ContactoForm
    success_url = reverse_lazy('inicio')
    template_name = 'contacto/contacto.html'
    def form_valid(self, form):
        messages.success(self.request, "Mensaje enviado exitosamente!")
        return super().form_valid(form)
    
