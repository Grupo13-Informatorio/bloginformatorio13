from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


from apps.usuario.mixins import IsMiembroRequiredMixin
from apps.articulo.models import Articulo
from apps.comentario.models import Comentario
from apps.usuario.forms import UserCreationForm
from apps.usuario.models import Usuario

class registrarUsuario(CreateView):
    
    template_name = 'registration/registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            response_form = super().form_valid(form)
            usuario = form.save(commit=False)
            next = self.request.POST.get('next')
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
        next = self.request.GET.get('next')
        context['next'] = next
        return context
  
  
  
class LogoutUsuario(LoginRequiredMixin, LogoutView):
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        messages.success(self.request, "¡Sesion cerrada correctamente!")
        return super().get(request, *args, **kwargs)



class UpdateUsuarioView(LoginRequiredMixin, IsMiembroRequiredMixin, UpdateView):
    
    template_name = "usuario/editar_perfil.html"
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

class VerPerfilUsuario(DetailView):
    model = Usuario
    template_name = 'usuario/perfil.html'
    context_object_name = 'usuario'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        articulos = Articulo.objects.filter(creado_por=kwargs['object'])
        comentarios = Comentario.objects.filter(creado_por=kwargs['object'])
        cant_comentarios = comentarios.count()
        cant_articulos = articulos.count()
        if cant_comentarios == 0:
            titulo_comentarios = 'Sin comentarios'
        elif cant_comentarios == 1:
            titulo_comentarios = 'Comentario'
        else:
            titulo_comentarios = str(cant_comentarios) + ' ' + 'Comentarios'
        if cant_articulos == 0:
            titulo_articulos = 'Sin articulos'
        elif cant_articulos == 1:
            titulo_articulos = 'Articulo'
        else:
            titulo_articulos = str(cant_comentarios) + ' ' + 'Articulos'
        ctx['titulo_articulos'] = titulo_articulos
        ctx['titulo_comentarios'] = titulo_comentarios
        ctx['comentarios'] = comentarios
        ctx['articulos'] = articulos
        return ctx

       
