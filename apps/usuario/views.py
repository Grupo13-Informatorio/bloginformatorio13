from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from apps.usuario.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from apps.usuario.mixins import IsMiembroRequiredMixin

from apps.usuario.models import Usuario

class registrarUsuario(CreateView):
    
    template_name = 'registration/registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('registration_success')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            response_form = super().form_valid(form)
            usuario = form.save(commit=False)
            usuario.password = make_password(form.cleaned_data["password"])
            usuario.save()
            messages.success(self.request, "¡Usuario creado correctamente!")
            return response_form
        else:
            form.is_invalid(form)

class LoginUsuario(LoginView):
    
    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)
        
    def get_success_url(self) -> str:
        messages.success(self.request, "¡Usuario logueado correctamente!")
        return super().get_success_url()
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        return context
  
  
  
class LogoutUsuario(LogoutView):
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        messages.success(self.request, "¡Sesion cerrada correctamente!")
        return super().get(request, *args, **kwargs)



class UpdateUsuarioView(IsMiembroRequiredMixin, UpdateView):
    
    template_name = "usuario/perfil.html"
    model = Usuario
    form_class = UserCreationForm
    success_url = reverse_lazy('inicio')
    
    def form_valid(self, form):
        if form.is_valid():
            response_form = super().form_valid(form)
            usuario = form.save(commit=False)
            usuario.password = make_password(form.cleaned_data["password"])
            usuario.save()
            messages.success(self.request, "Usuario actualizado correctamente")
            return response_form
        else:
            form.is_invalid(form)
<<<<<<< HEAD

class VerPerfilUsuario(DetailView):
    model = Usuario
    template_name = 'usuario/ver_perfil.html'
    context_object_name = 'usuario'

=======
            
>>>>>>> darian
       
