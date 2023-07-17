from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.usuario.forms import UserCreationForm
from django.contrib.auth.hashers import make_password


# Create your views here.


class registrarUsuario(CreateView):
    template_name = 'registro.html'
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
            return response_form
        else:
            form.is_invalid(form)

    
