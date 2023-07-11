from django.shortcuts import render,redirect
from .models import Producto
from .forms import ProductoForm
import logging
import os

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
    nombre_archivo = os.path.basename(producto.manualInstrucciones.name)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listaProductos')
    return render(request, 'paginas/productos/editarProducto.html', {'formulario':formulario, 'nombre_archivo': nombre_archivo})

def eliminarProducto(request,id):
    Producto.objects.filter(id=id).delete()
    return redirect('listaProductos')

def mostrarProducto(request,id):
    producto = Producto.objects.all().filter(id=id)
    ruta_miniatura = "/static/files/miniaturaPDF.png"
    return render(request,'paginas/productos/mostrarProducto.html', {'producto':producto, 'ruta_miniatura':ruta_miniatura})

# def mostrarProducto(request, id):
#     # producto2 = Producto.objects.get(id=id)
#     producto = Producto.objects.all().filter(id=id)

#     if producto.manualInstrucciones:
#         ruta_pdf = producto.manualInstrucciones.path
#         imagenes = convert_from_path(ruta_pdf, first_page=0, last_page=1)
#         ruta_imagen_temporal = "almacen/static/files/miniatura.png"
#         imagenes[0].save(ruta_pdf, "png")
        
#         return render(request, 'paginas/productos/mostrarProducto.html', {'producto': producto, 
#                                                                           'ruta_imagen': ruta_imagen_temporal, 
#                                                                           'ruta_miniatura': ruta_pdf })
    
#     return render(request, 'paginas/productos/mostrarProducto.html', {'producto': producto})


# def mostrarProducto(request, id):
#     producto = Producto.objects.get(id=id)

#     if producto.manualInstrucciones:
#         ruta_miniatura = "static/files/miniaturaPDF.png"
#         return render(request, 'paginas/productos/mostrarProducto.html', {'producto': producto, 'ruta_miniatura': ruta_miniatura})
    
#     return render(request, 'paginas/productos/mostrarProducto.html', {'producto': producto})
