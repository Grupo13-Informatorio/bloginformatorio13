from django.views.generic import CreateView
from .forms import ContactoForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


class ContactoUsuario(CreateView):
    template_name = "contacto.html"
    form_class = ContactoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)