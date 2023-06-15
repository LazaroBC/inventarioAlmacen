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

def editarProducto(request, id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listaProductos')
    return render(request, 'paginas/productos/editarProducto.html', {'formulario':formulario})

def eliminarProducto(request,id):
    Producto.objects.filter(id=id).delete()
    return redirect('listaProductos')

def mostrarProducto(request,id):
    producto = Producto.objects.all().filter(id=id)
    return render(request,'paginas/productos/mostrarProducto.html', {'producto':producto})