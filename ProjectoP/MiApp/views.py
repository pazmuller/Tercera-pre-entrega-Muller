from django.shortcuts import render, redirect
from .models import Producto, Categoria, Cliente
from .forms import ProductoForm, CategoriaForm, ClienteForm, BusquedaForm

def index(request):
    return render(request, 'index.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'agregarProducto.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'agregarCategoria.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            resultados = Producto.objects.filter(nombre__icontains=busqueda)
            return render(request, 'resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})


def administrador(request):
    productos = Producto.objects.all()  
    categorias = Categoria.objects.all()  
    clientes = Cliente.objects.all() 
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'clientes': clientes,
    }
    
    return render(request, 'administrador.html', context)