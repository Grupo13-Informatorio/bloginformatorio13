from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.usuario.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.contrib import messages

# Create your views here.


class registrarUsuario(CreateView):
    template_name = 'registration/registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('registration_success')
    
    def form_valid(self, form):
        if form.is_valid():
            response_form = super().form_valid(form)
            usuario = form.save(commit=False)
            print(usuario.password)
            print(form.clean())
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
            messages.error(self.request, "¡Usuario logueado correctamente!")
    

    def get_success_url(self) -> str:
        messages.success(self.request, "¡Usuario logueado correctamente!")
        return super().get_success_url()
