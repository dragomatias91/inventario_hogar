from django.shortcuts import render , redirect
from .models import Categoria
from .forms import CategoriaForm

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias:lista')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/crear_categoria.html', {'form': form})