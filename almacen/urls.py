from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('listaProductos/', views.listaProductos, name='listaProductos'),
    path('nuevoProducto/', views.nuevoProducto, name='nuevoProducto'),
    path('editarProducto/', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/', views.eliminarProducto, name='eliminarProducto'),
    path('producto/', views.producto, name='producto'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

