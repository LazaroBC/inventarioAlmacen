from django.shortcuts import render,redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def listaProductos(request):
    productos = Producto.objects.all()
    return render(request, 'paginas/productos/listaProductos.html', {'productos':productos})

def nuevoProducto(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listaProductos')
    return render(request, 'paginas/productos/nuevoProducto.html', {'formulario':formulario})

def editarProducto(request):
    return render(request, 'paginas/productos/editarProducto.html')

def eliminarProducto(request):
    return redirect('listaProductos')

def producto(request):
    productos = Producto.objects.all()
    return render(request,'paginas/productos/producto.html', {'productos':productos})