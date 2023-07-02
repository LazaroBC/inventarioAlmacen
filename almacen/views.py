from django.shortcuts import render,redirect
from .models import Producto
from .forms import ProductoForm
from pdf2image import convert_from_path

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

# def mostrarProducto(request, id):
#     # producto2 = Producto.objects.get(id=id)
#     producto = Producto.objects.all().filter(id=id)
# 
#     if producto.manualInstrucciones:
#         ruta_pdf = producto.manualInstrucciones.path
#         
#         imagenes = convert_from_path(ruta_pdf, first_page=0, last_page=1)
#         
#         ruta_imagen_temporal = "almacen/static/files/imagen.png"
#         imagenes[0].save(ruta_imagen_temporal, "png")
#         
#         return render(request, 'paginas/productos/mostrarProducto.html', {'producto': producto, 'ruta_imagen': ruta_imagen_temporal})
#     
#     return render(request, 'paginas/productos/mostrarProducto.html', {'producto': producto})