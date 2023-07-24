from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.usuario.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

from apps.usuario.models import Usuario

# Create your views here.


class registrarUsuario(CreateView):
    template_name = 'registration/registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('registration_success')
    
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
        else:
            form.is_invalid(form)
            messages.error(self.request, "Error de validacion")
    
    def get_success_url(self) -> str:
        messages.success(self.request, "¡Usuario logueado correctamente!")
        return super().get_success_url()
  
    
class LogoutUsuario(LogoutView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        messages.success(self.request, "¡Sesion cerrada correctamente!")
        return super().get(request, *args, **kwargs)
    
class UpdateUsuarioView(UpdateView):
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
       
