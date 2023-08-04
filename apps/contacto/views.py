from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from apps.contacto.forms import ContactoForm
from apps.contacto.models import Contacto



class ContactoUsuario(CreateView):
    
    form_class = ContactoForm
    success_url = reverse_lazy('inicio')
    template_name = 'contacto/contacto.html'
    def form_valid(self, form):
        messages.success(self.request, "Mensaje enviado exitosamente!")
        return super().form_valid(form)
    


class ListarContactosView(UserPassesTestMixin, LoginRequiredMixin, ListView):

    model = Contacto
    template_name = 'contacto/contacto_lista.html'
    context_object_name = 'contactos'
    
    def test_func(self):
        if self.request.user.is_active and (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False



class DetalleContactoView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    
    model = Contacto
    template_name = 'contacto/contacto_detalle.html'
    context_object_name = 'contacto'
    
    def test_func(self):
        if self.request.user.is_active and (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False


class BorrarContactoView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Contacto
    template_name = 'contacto/contacto_borrar.html'
    success_url = reverse_lazy('contacto:verContactos')

    def test_func(self):
        if self.request.user.is_active and (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False

    def get_success_url(self) -> str:
        messages.success(self.request, "Contacto borrado exitosamente")
        return super().get_success_url()   
        
   