from django.shortcuts import render,redirect ,get_object_or_404
from .models import Producto , ListaCompras
from .forms import ProductoForm , ListaComprasForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:lista')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos:lista')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})


def lista_compras(request):
    items = ListaCompras.objects.all()
    return render(request, 'productos/lista_compras.html', {'items': items})

def crear_compra(request):
    if request.method == 'POST':
        form = ListaComprasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:lista_compras')
    else:
        form = ListaComprasForm()
    return render(request, 'productos/crear_compra.html', {'form': form})

def editar_compra(request, pk):
    item = get_object_or_404(ListaCompras, pk=pk)
    if request.method == 'POST':
        form = ListaComprasForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('productos:lista_compras')
    else:
        form = ListaComprasForm(instance=item)
    return render(request, 'productos/editar_compra.html', {'form': form})

def eliminar_compra(request, pk):
    item = get_object_or_404(ListaCompras, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('productos:lista_compras')
    return render(request, 'productos/eliminar_compra.html', {'item': item})