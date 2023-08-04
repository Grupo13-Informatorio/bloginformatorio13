from typing import Any, Dict
from django import http
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View   
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme


from apps.articulo.models import Articulo
from apps.comentario.models import Comentario
from apps.usuario.forms import UserCreationForm, UserEditionForm
from apps.usuario.models import Usuario



class registrarUsuario(CreateView):

    template_name = 'registration/registro.html'
    form_class = UserCreationForm
    model = Usuario

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['next'] = self.request.GET.get('next', '')
        return ctx

    def form_valid(self, form):
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = make_password(form.cleaned_data["password"])
            usuario.save()
            usuario = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            login(self.request, usuario)
            return super().form_valid(form)
        else:
            self.form_invalid(form)

    def get_success_url(self) -> str:
        redirect_to = self.request.POST.get('next', '')
        messages.warning(self.request, redirect_to)
        url_is_safe = url_has_allowed_host_and_scheme(redirect_to, '*')
        if redirect_to and url_is_safe:
            messages.success(self.request, "¡Usuario creado correctamente!")
            return redirect_to



class LoginUsuario(UserPassesTestMixin,LoginView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        else:
            return True

    def handle_no_permission(self):
        return redirect(reverse_lazy('usuario:logout'))

    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)
        else:
            self.form_invalid(form)

    def form_invalid(self, form: AuthenticationForm):
        messages.warning(self.request, "¡Usuario o contraseña incorrectos, intente nuevamente!")
        return super().form_invalid(form)

    def get_success_url(self) -> str:
        redirect_to = self.request.POST.get('next', '')
        url_is_safe = url_has_allowed_host_and_scheme(redirect_to, '*')
        if redirect_to != None and url_is_safe:
            messages.success(self.request, "¡Usuario logueado correctamente!")
            return redirect_to

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        next = self.request.GET.get('next','')
        context['next'] = next
        return context



class LogoutUsuario(LoginRequiredMixin, LogoutView):

    def handle_no_permission(self):
        return redirect(reverse_lazy('usuario:login'))

    def get(self, request, *args: Any, **kwargs) -> HttpResponse:
        messages.success(self.request, "¡Sesion cerrada correctamente!")
        return super().get(request, *args, **kwargs)



class UpdateUsuarioView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    template_name = "usuario/editarperfil.html"
    model = Usuario
    form_class = UserEditionForm

    def test_func(self):
        if self.request.user.is_active and (self.request.user.is_miembro or self.request.user.is_superuser or self.request.user == self.get_object()):
            return True
        else:
            return False

    def get_success_url(self) -> str:
        redirect_to = self.request.POST.get('next', '')
        url_is_safe = url_has_allowed_host_and_scheme(redirect_to, '*')
        if redirect_to != None and url_is_safe:
            messages.success(self.request, "¡Usuario actualizado correctamente!")
            return redirect_to

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.get_object(self.queryset)
        next = self.request.GET.get('next','')
        context['next'] = next
        return context

    def form_valid(self, form):
        if form.is_valid():
            messages.success(self.request, "¡Usuario actualizado correctamente!")
            return super().form_valid(form)
        else:
            self.form_invalid(form)




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
            titulo_comentarios = '1 Comentario'
        else:
            titulo_comentarios = str(cant_comentarios) + ' ' + 'Comentarios'
        if cant_articulos == 0:
            titulo_articulos = 'Sin articulos'
        elif cant_articulos == 1:
            titulo_articulos = '1 Articulo'
        else:
            titulo_articulos = str(cant_comentarios) + ' ' + 'Articulos'
        ctx['titulo_articulos'] = titulo_articulos
        ctx['titulo_comentarios'] = titulo_comentarios
        ctx['comentarios'] = comentarios
        ctx['articulos'] = articulos
        return ctx



class VerUsuariosView(LoginRequiredMixin, UserPassesTestMixin, ListView):

    model = Usuario
    template_name = 'usuario/usuarios.html'
    context_object_name = 'usuarios'
    paginate_by = 10
  

    def test_func(self):
        if self.request.user.is_active and (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False


class CambiarEstadoView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        if self.request.user.is_active and (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            usuario = Usuario.objects.get(id=kwargs['pk'])
            usuario.is_active = not usuario.is_active
            usuario.save()
            return redirect(reverse_lazy('usuario:usuarios'))
        else:
            return redirect(reverse_lazy('usuario:usuarios'))

class CambiarRolView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        if self.request.user.is_active and (self.request.user.is_miembro or self.request.user.is_superuser):
            return True
        else:
            return False

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            usuario = Usuario.objects.get(id=kwargs['pk'])
            if usuario != self.request.user:
                usuario.is_miembro = not usuario.is_miembro
                usuario.save()
            else:
                messages.warning(request, "Usted no puede cambiar su propio estado")
            return redirect(reverse_lazy('usuario:usuarios'))
        else:
            return redirect(reverse_lazy('usuario:usuarios'))