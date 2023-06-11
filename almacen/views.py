from django.shortcuts import render,redirect



# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def listaProductos(request):
    return render(request, 'paginas/productos/listaProductos.html')

def nuevoProducto(request):
    return render(request, 'paginas/productos/nuevoProducto.html')

def editarProducto(request):
    return render(request, 'paginas/productos/editarProducto.html')

def eliminarProducto(request):
    return redirect('listaProductos')
