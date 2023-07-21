from django.shortcuts import render, redirect, get_object_or_404
from .models import Articulo, Categoria
from apps.comentario.models import Comentario
from django.views import View
from .forms import ArticuloForm
from apps.comentario.forms import ComentarioForm
from django.views.generic import DeleteView
from django.urls import reverse


# ##Vista basada en clases
class DeleteArticulo(DeleteView):
    model = Articulo
    template_name = "articulo/eliminarArticulo.html"
    def get_success_url(self):
        return reverse('apps.articulo:articulos')

class ArticuloView(View):
    template_name = 'articulo.html'

    def get(self, request, categoria=None):
        if categoria:
            articulos = Articulo.objects.filter(categoria__nombre=categoria)
        else:
            articulos = Articulo.objects.all()

        categorias = Categoria.objects.all()

        return render(request, 'articulo/articulo.html',{'articulos' : articulos,'categorias': categorias}) ##

def articulo_crear(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            print(f'form is valid: {form.is_valid()}')
            form.save()
            return redirect('apps.articulo:articulos')

    else:
        form = ArticuloForm()
    return render(request, 'articulo/articulo_form.html', {'form':form})

def articulo_actualizar(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('apps.articulo:articulos')
        
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'articulo/articulo_form.html', {'form':form, 'articulo': articulo})
    
def existe_articulo(id):
    for i in Articulo:
        if i.id == id:
            return i
    return None

def leer_articulo(request, id):
    try:
        articulos = existe_articulo(id)
    except Exception:
        articulos = Articulo.objects.get(id = id)
        comentarios = Comentario.objects.filter(articulo=id) 

    form = ComentarioForm(request.POST or None) 
    if form.is_valid():

        if not form.is_valid():
            print(form.errors)
        if request.user.is_authenticated:
            aux         = form.save(commit=False)
            aux.articulo = articulos
            aux.usuario = request.user
            aux.save()
            form        = ComentarioForm()################ ACÄ PUEDE QUE LE HAYA ERRADO, si no es este es ComentarioForm
        
        else:

            return redirect('usuario.login')
        
    context = {

         'articulos': articulos,
         'form': form,
         'comentarios': comentarios,

        }
    return render(request, 'articulo/articulo_individual.html', context)




