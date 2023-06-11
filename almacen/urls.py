from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('listaProductos/', views.listaProductos, name='listaProductos'),
    path('nuevoProducto/', views.nuevoProducto, name='nuevoProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/', views.eliminarProducto, name='eliminarProducto'),
]
