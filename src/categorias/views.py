from django.shortcuts import render , redirect , get_object_or_404 
from .models import Categoria
from .forms import CategoriaForm
from django.db.models.functions import Lower

def lista_categorias(request):
    query = request.GET.get('q', '')
    categorias = Categoria.objects.all().order_by(Lower('nombre'))
    if query:
        categorias = categorias.filter(nombre__icontains=query)
    return render(request, 'categorias/lista_categorias.html', {
        'categorias': categorias,
        'query': query
    })

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias:lista')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/crear_categoria.html', {'form': form})

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias:lista')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/editar_categoria.html', {'form': form})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias:lista')
    return render(request, 'categorias/eliminar_categoria.html', {'categoria': categoria})


